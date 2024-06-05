import json
import random
import os
import uuid
import re
import copy
import xml.etree.ElementTree as ET
from PIL import Image
from typing import Dict, Union

from .utility import *
from .storyprofiles import CHARACTER_FIGURE_ACCESSORY_KEYS, STORY_SCENARIO_STYLES
from .characterpostures import CHARACTER_FIGURES

RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RESET  = "\033[0m"

DEFAULT_LANGUAGE="zh-CN"
LANGUAGE_ENG="en-US"
DEFAULT_NARRATOR="M"
VISIBLE_ACTORS=("boy", "girl", "eily")
INVISIBLE_ACTORS=("", "M", "F")
SCENARIO_ACTORS=("ending", "exam", "concentrak", "notes")
LOCAL_DEFAULT_ROOT="./test"

##### experimental code
class MText:
    def __init__(self, text, language:str=None):
        if isinstance(text, str):
            if language == None:
                self.text = text
            else:
                self.text = {language: text}
        elif isinstance(text, dict) and all(isinstance(v, str) for v in text.values()):
            self.text = text
        else:
            raise ValueError("Invalid text format")
#### end of experimental code

class Script:
    def __init__(self, subscript=None, sound=None, narrator=None, alternative=None, languages=None):
        self.subscript = subscript
        self.sound = sound
        self.narrator = narrator
        self.alternative = alternative
        self._languages = []
        if isinstance(languages, list) or isinstance(languages, tuple):
            for language in languages:
                if isinstance(language, str) and len(language) > 0:
                    self._languages.append(language)
        elif isinstance(languages, str) and len(languages) > 0:
            self._languages = [languages]
        
    def copy(self):
        return copy.deepcopy(self)

    def reset2test(self, newNarrator=None):
        assert (newNarrator in VISIBLE_ACTORS or newNarrator in INVISIBLE_ACTORS) \
            or newNarrator == None
        if self.sound != None and isinstance(self.sound, str) and len(self.sound) > 0:
            self.sound = switch_to_test_path(self.sound)
            self.narrator = newNarrator if newNarrator != None else self.narrator
            self.languages = None                

    def export(self):
        data = {}
        if self.sound != None:
            data["sound"] = self.sound
        if self.subscript != None:
            data["subscript"] = self.subscript
        if self.narrator != None:
            data["narrator"] = self.narrator
        if self.alternative != None:
            data["alternative"] = self.alternative
        if self._languages != None and isinstance(self._languages, list) and len(self._languages) > 0:
            data["languages"] = self._languages

        if (isinstance(self.subscript, str) and len(self.subscript) > 0) \
            or (isinstance(self.subscript, dict) and any((isinstance(v, str) and len(v) > 0) for v in self.subscript.values())):
            return data
        else:
            return None


class Interaction:
    def __init__(self, actorId=None, text=None, figure=None, position=None, transform=None, \
                 popup=None, onResult=None, onPoster=None, voice=None, type=None, start="", duration=""):
        self.start = start
        self.duration = duration
        self.onResult = onResult
        self.onPoster = onPoster
        self.actorId = actorId
        self.figure = figure
        self.position = position
        self.transform = transform
        self.popup = popup
        self.text = text
        self.voice = voice
        self.type = type

    def copy(self):
        return copy.deepcopy(self)
    
    def merge(self, interaction):
        updated = self.copy()
        updated.start = interaction.start if interaction.start != "" else updated.start
        updated.duration = interaction.duration if interaction.duration != "" else updated.duration
        updated.onResult = interaction.onResult if interaction.onResult != None else updated.onResult
        updated.onPoster = interaction.onPoster if interaction.onPoster != None else updated.onPoster
        updated.actorId = interaction.actorId if interaction.actorId != None else updated.actorId
        updated.figure = interaction.figure if interaction.figure != None else updated.figure
        updated.position = interaction.position if interaction.position != None else updated.position
        updated.transform = interaction.transform if interaction.transform != None else updated.transform
        updated.popup = interaction.popup if interaction.popup != None else updated.popup
        updated.text = interaction.text if interaction.text != None else updated.text
        updated.voice = interaction.voice if interaction.voice != None else updated.voice
        updated.type = interaction.type if interaction.type != None else updated.type

        return updated
    
    def export(self):
        data = {}
        data["start"] = self.start
        data["duration"] = self.duration
        if self.popup!=None or self.text!=None or self.voice!=None:
            data["content"] = {}
            if self.popup != None:
                data["content"]["popup"] = self.popup
            if self.text != None:
                data["content"]["text"] = self.text
            if self.voice != None:
                data["content"]["voice"] = self.voice
        if self.onResult != None:
            data["onResult"] = self.onResult
        if self.onPoster != None:
            data["onPoster"] = self.onPoster
        if self.position != None and isinstance(self.position, list):
            data["position"] = self.position
        if self.transform != None and isinstance(self.transform, str) \
            and len(self.transform) > 0:
            data["transform"] = self.transform
        if self.figure != None:
            data["figure"] = self.figure
        if self.actorId != None:
            data["actor"] = self.actorId
        if self.type != None:
            data["type"] = self.type

        if len(data) > 2:
            return data
        else:
            return None

# default interaction with actor posture
class PostureInteraction(Interaction):
    def __init__(self, actorId=-1, figure=None, position=None, transform=None):
        super().__init__(type="motion", actorId=actorId, figure=figure, \
                            position=position, transform=transform)
        
class Event:
    def __init__(self, id=None, scene=None, board=None, objects=None, interactions=None):
        self.id = id
        self.scene = copy.deepcopy(scene) if isinstance(scene, dict) else scene
        self.board = copy.deepcopy(board) if isinstance(board, dict) else board
        self.objects = copy.deepcopy(objects) if isinstance(objects, list) else objects
        self.interactions = copy.deepcopy(interactions) if isinstance(interactions, list) else interactions
    
    def export(self):
        data = {}
        if self.id != None:
            data["id"] = self.id
        if self.scene != None:
            data["scene"] = copy.deepcopy(self.scene) if isinstance(self.scene, dict) else self.scene
        if self.board != None:
            data["board"] = copy.deepcopy(self.board) if isinstance(self.board, dict) else self.board
        if self.objects != None:
            data["objects"] = copy.deepcopy(self.objects) if isinstance(self.objects, list) else self.objects
        if self.interactions != None:
            data["interactions"] = copy.deepcopy(self.interactions) if isinstance(self.interactions, list) else self.interactions
        
        if len(data) > 0:
            return data
        else:
            None

class Story:

    def test(self, fileName="testStory.json", localOutputPath=LOCAL_DEFAULT_ROOT, language=DEFAULT_LANGUAGE):
        directory = os.path.join(localOutputPath, self.storyId)
        if not os.path.exists(directory):
            os.makedirs(directory)

        language = DEFAULT_LANGUAGE if language == None else language
        scripts = self.exportScripts()
        if self._synthesizer != None:
            try:
                for script in scripts:
                    for voice in script["voices"]:
                        soundFileName = voice.get("sound", None)
                        if isinstance(soundFileName, str) and len(soundFileName) > 0:
                            text = voice["subscript"][language] if isinstance(voice["subscript"], dict) else voice["subscript"]
                            alternativeText = None if "alternative" not in voice \
                                else (voice["alternative"][DEFAULT_LANGUAGE] \
                                    if isinstance(voice["alternative"], dict) \
                                    else voice["alternative"])
                            narrator = voice["narrator"]
                            text = text if alternativeText == None else alternativeText
                            self._synthesizer.synthesizeFile(
                                    narrator, remove_emojis(text), language, directory, os.path.basename(soundFileName)
                                )
                            localOutputFileName = os.path.join(directory, os.path.basename(soundFileName))
                            if self._cosUploader != None:
                                self._cosUploader.local2cos(localOutputFileName, self.storyId, self.audioPath)   
            except Exception as e:
                print(f"Story.test failed for {script}\n", e)

        with open(os.path.join(localOutputPath, fileName), "w") as file:
            json.dump(
                self.export(), file, ensure_ascii=False, indent=4, sort_keys=False
            )
        print(f"Story.test exported to {os.path.join(localOutputPath, fileName)}")
    
    def export(self, debug=False):
        voices = [{"sound": "/story/audios/OurMusicBox - 24 Hour Coverage - intro.mp3"}]
        events = []
        for i, page in enumerate(self._pages):
            if debug:
                print(f"{YELLOW}Story.export(), page{i} type {page.type}{RESET}")
            pageObject = page.export(voiceOffset=len(voices), pageId=float(len(events)))
            if pageObject != None and isinstance(pageObject, dict) \
                and "voices" in pageObject and "events" in pageObject:
                for entry in pageObject["voices"]:
                    entryObject = {}
                    for key in set(entry.keys()) & {"sound", "languages"}:
                        if entry[key] != None:
                            entryObject[key] = entry[key]
                    if len(entryObject) > 0:
                        voices.append(entryObject)
                events = events + pageObject["events"]

        return {"voices": voices, "events": events}

    def exportScripts(self):
        voices = []
        for i, page in enumerate(self._pages):
            pageObject = page.export(voiceOffset=len(voices))
            pageVoices = []
            for voice in pageObject["voices"]:
                if (isinstance(voice.get("subscript", None), str) or isinstance(voice.get("subscript", None), dict)) and len(voice["subscript"]) > 0:
                    pageVoices.append(voice)
            if len(pageVoices) > 0:
                voices = voices + [{"page": i, "voices": pageVoices}]

        return voices

    def exportAudios(self, localOutputPath=LOCAL_DEFAULT_ROOT, uploadToCos=True):
        directory = os.path.join(localOutputPath, self.storyId)
        if not os.path.exists(directory):
            os.makedirs(directory)

        if self._synthesizer:
            voices = self.exportScripts()
            for page in voices:
                for i, voice in enumerate(page["voices"]):
                    if not isinstance(voice.get("sound", None), str) or voice["sound"].startswith("/story/"): # Ignore if production audio
                        continue
                    try:
                        fileName = os.path.basename(voice["sound"])
                        character = voice["narrator"]
                        for language in voice["subscript"]:
                                subscript = (
                                    voice["alternative"][language]
                                    if ("alternative" in voice) and (language in voice["alternative"]) and (voice["alternative"][language] != None)
                                    else voice["subscript"][language]
                                )
                                print(f'Page {page["page"]}/Script {i}')
                                self._synthesizer.synthesizeFile(
                                    character, remove_emojis(subscript), language, directory, fileName
                                )
                                localOutputFileName = os.path.join(directory, fileName)

                                if self._cosUploader != None and uploadToCos:
                                    self._cosUploader.local2cos(localOutputFileName, self.storyId, self.audioPath)
                    except Exception as e:
                        print(f"Synthesize & upload script failed for <{voice['subscript']}><{subscript}>\n", e)
                        continue

    def exportProduct(self, fileName=None, localOutputPath='./prod'):
        if self._cosUploader == None:
            print("Cos uploader is not available, exit.")
            return

        if not os.path.exists(localOutputPath):
            os.makedirs(localOutputPath)

        storyObject = self.export()
        
        # Copy audios to product path
        for i, voice in enumerate(storyObject["voices"]):
            storyObject["voices"][i]["sound"] = self._cosUploader.test2product(voice["sound"])

        # Copy images to product path
        for j, event in enumerate(storyObject["events"]):
            if "board" in event and isinstance(event["board"], dict):
                board = event["board"]
                if "content" in board and isinstance(board["content"], dict) \
                    and "image" in board["content"] and isinstance(board["content"]["image"], str) \
                    and len(board["content"]["image"]) > 0:
                    storyObject["events"][j]["board"]["content"]["image"] = self._cosUploader.test2product(board["content"]["image"])
                if "contentList" in board and isinstance(board["contentList"], list) \
                    and len(board["contentList"]) > 0:
                    for k, contentEntry in enumerate(board["contentList"]):
                        if "image" in contentEntry and isinstance(contentEntry["image"], str) \
                            and len(contentEntry["image"]) > 0:
                            storyObject["events"][j]["board"]["contentList"][k]["image"] = self._cosUploader.test2product(contentEntry["image"])

        productFileName = fileName if fileName != None else os.path.join(localOutputPath, self.title + ".product.json")
        with open(productFileName, "w") as file:
            json.dump(
                storyObject, file, ensure_ascii=False, indent=4, sort_keys=False
            )
        print(f"Story resource copied from test to production, product story generated as {productFileName}.")

    @staticmethod
    def buildStoryCollection(outputName, storyList):
        storyCollection = {"collection": []}
        for story in storyList:
            storyTitle = story[:len(story)-5] if story.endswith(".json") else story
            storyCollection["collection"].append(storyTitle)
        with open(outputName, "w") as file:
            json.dump(
                storyCollection, file, ensure_ascii=False, indent=4, sort_keys=False
            )

    @staticmethod
    def retrieveSvgSize(image_path):
        # Load the SVG file
        tree = ET.parse(image_path)
        root = tree.getroot()

        # Extract attributes from the <svg> tag
        width = root.get("width", 0)  # Get the width attribute
        height = root.get("height", 0)  # Get the height attribute
        viewBox = root.get("viewBox", "0, 0, 0, 0")  # Get the viewBox attribute

        split_pattern = r"[ ,]+"

        return [int(width), int(height)], [
            int(float(num)) for num in re.split(split_pattern, viewBox)
        ]

    @staticmethod
    def retrievePixelSize(image_path):
        # Open the image using the Python Imaging Library (PIL)
        image = Image.open(image_path)

        # Get the width and height of the image in pixels
        width, height = image.size

        # Return the width and height as a tuple
        return width, height

    @staticmethod
    def getImageSize(file_path):
        width = height = 0
        try:
            if ".svg" in file_path[-4:]:
                dim2, dim4 = Story.retrieveSvgSize(file_path)
                if dim2 == [0, 0]:
                    width = dim4[2]
                    height = dim4[3]
                else:
                    width = dim2[0]
                    height = dim2[1]
            elif (
                ".jpg" in file_path[-4:]
                or ".jpeg" in file_path[-5:]
                or ".png" in file_path[-4:]
                or ".gif" in file_path[-4:]
            ):
                width, height = Story.retrievePixelSize(file_path)
        except:
            print("Retrieve image size error for", file_path)
        return width, height
    
    @staticmethod
    def loadFromFile(fileName, locale=DEFAULT_LANGUAGE, **kwargs):
        story = None
        storyId = None
        try:
            with open(fileName, 'r') as f:
                object = json.load(f)
            voices = object["voices"]
            events = object["events"]
            storyId = kwargs["storyId"] if "storyId" in kwargs else storyId
            if len(voices) > 1:
                for i in range(1, len(voices)):
                    folder = voices[i].get("sound", "//").split("/")[-2]
                    if len(folder) == 36: # length of uuid.uuid4()
                        storyId = folder
            storyStyle = None
            validScene = None
            for i in range(len(events)):
                if events[i].get("scene", None) != None and len(events[i]["scene"]) > 0:
                    validScene = events[i]["scene"]
                    break
            for styleKey in STORY_SCENARIO_STYLES.keys():
                for key, value in STORY_SCENARIO_STYLES[styleKey]["scenarios"].items():
                    if value == validScene \
                        or (key == "notes" and value["scene"] == validScene):
                        storyStyle = styleKey
                        break
            defaultNarrator = None
            for event in events:
                if defaultNarrator != None:
                    break
                if "objects" in event and isinstance(event["objects"], list):
                    _, _, defaultNarrator, _, _, _ = get_actors(event["objects"])
            kwargs["narrator"] = defaultNarrator if defaultNarrator != None else DEFAULT_NARRATOR
            story = Story(title=os.path.basename(fileName).replace(".json", ""), 
                        storyId=storyId, 
                        style=storyStyle, 
                        locale=locale, 
                        **kwargs)

            pageScenario = "cover"      # 没有样式匹配，设为CoverPage
            for event in events:
                # 获取页面类型
                if "board" in event \
                    and ((event["board"].get("type", None) != None and len(event["board"]["type"]) > 0) \
                         or (isinstance(event["board"].get("content", None), dict) \
                             and event["board"]["content"].get("type", None) != None)):
                    pageScenario = event["board"]["type"] if event["board"].get("type", None) != None else event["board"]["content"]["type"]
                elif "board" in event \
                    and isinstance(event["board"].get("content", None), dict) \
                    and event["board"]["content"].get("magnify", None) != None:
                    pageScenario = "classroom"
                else:
                    sceneObject = event.get("scene", None)
                    if "index" in sceneObject and sceneObject["index"] == STORY_SCENARIO_STYLES[storyStyle]["scenarios"]["concentrak"]["index"]:
                        pageScenario = "concentrak"
                    elif isinstance(sceneObject, str) and len(sceneObject) > 0:
                        for key, value in STORY_SCENARIO_STYLES[storyStyle]["scenarios"].items():
                            if isinstance(value, str) and value == sceneObject:
                                pageScenario = key
                    elif "bgColor" in sceneObject and len(sceneObject["bgColor"]) > 0:
                        pageScenario = "blackboard"

                # 创建对应页面
                print(f"Loading page as {pageScenario}")
                # CoverPage
                if pageScenario == "cover":
                    story.createPage(
                        sceneType = pageScenario,
                        source = "",
                        voices = voices,
                        board = event.get("board", None),
                        objects = event.get("objects", None),
                        interactions = event.get("interactions", None)
                        )
                # ClassroomPage
                elif pageScenario == "classroom":
                    story.createPage(
                        sceneType = pageScenario,
                        voices = copy.deepcopy(voices),
                        board = event.get("board", None),
                        objects = event.get("objects", None),
                        interactions = event.get("interactions", None)
                        )
                # BlackboardPage
                elif pageScenario == "blackboard":
                    story.createPage(
                        sceneType = pageScenario,
                        source = "",
                        voices = copy.deepcopy(voices),
                        board = event.get("board", None),
                        objects = event.get("objects", None),
                        interactions = event.get("interactions", None)
                        )

                # ConcentrakPage
                elif pageScenario == "concentrak":
                    story.createPage(
                        sceneType = pageScenario,
                        text = "",
                        voices = copy.deepcopy(voices),
                        board = event.get("board", None),
                        objects = event.get("objects", None),
                        interactions = event.get("interactions", None)
                        )
                # ExamPage
                elif pageScenario == "exam":
                    story.createPage(
                        sceneType = pageScenario,
                        actor = "", 
                        voices = copy.deepcopy(voices),
                        board = event.get("board", None),
                        objects = event.get("objects", None),
                        interactions = event.get("interactions", None)
                    )

                # NotesPage
                elif pageScenario == "notes":
                    story.createPage(
                        sceneType = pageScenario,
                        actor = "", 
                        voices = copy.deepcopy(voices),
                        board = event.get("board", None),
                        objects = event.get("objects", None),
                        interactions = event.get("interactions", None)
                    )

                else:
                    pass            
            
        except Exception as e:
            print("Load story from file exception:\n", e)
            return None
            
        return story

    def __init__(self, title, storyId=None, style="shinkai_makoto", **kwargs):
        self.title = title
        self.storyId = storyId if storyId != None else uuid.uuid4()
        self.styles = STORY_SCENARIO_STYLES[style]
        self.locale = kwargs["locale"] if "locale" in kwargs else DEFAULT_LANGUAGE
        self.narrator = kwargs["narrator"] if "narrator" in kwargs else DEFAULT_NARRATOR
        self._pages = []
        self.posterPath = 'test/posters/'
        self.audioPath = 'test/audios/'

        self._cosUploader = kwargs["uploader"] if "uploader" in kwargs else None
        self._synthesizer = kwargs["synthesizer"] if "synthesizer" in kwargs else None

        self._defaultCharacters = CHARACTER_FIGURES

        print(f"Create a new story title: {title}, Id:", self.storyId)

    def getAudioPath(self, fileName):
        return os.path.join("/", self.audioPath, self.storyId, fileName)

    def _getPosturePosition(self, actor, id):
        figureName = self._defaultCharacters[actor][id]
        if "boy" in figureName:
            if "half" in figureName:
                return self.styles["positions"]["right-bottom"]
            elif "standright" in figureName:
                return self.styles["positions"]["right"]
            elif "-stand-" in figureName:
                return self.styles["positions"]["left"]
            else: # head
                return [0, 0]
        elif "girl" in figureName:
            if "half" in figureName:
                return self.styles["positions"]["right-bottom"]
            elif "-stand-" in figureName:
                return self.styles["positions"]["right"]
            else: # head
                return [0, 0]
        else:
            return [0, 0]

        return [0, 0]
    def getUserPostureIdAndPosition(
        self, actor, postures, keyScenario="stand", excludeAccessories=True
    ):
        id = -1
        if type(postures) is int:
            id = postures
        elif type(postures) is list and type(postures[0]) is int:
            id = postures[0]
        elif self._defaultCharacters == None:
            id = 0
        else:
            currentActorFigures = self._defaultCharacters[actor]
            availableFigures = []
            for j, figure in enumerate(currentActorFigures):
                skip = False
                if excludeAccessories:
                    for accessory in CHARACTER_FIGURE_ACCESSORY_KEYS:
                        if accessory in figure:
                            skip = True
                if skip:
                    continue
                if keyScenario in figure and all(keyWord in figure for keyWord in postures):
                    availableFigures.append({"index": j, "figure": figure})
            id = random.choice(availableFigures)["index"] if len(availableFigures) > 0 else 0
        return id, self._getPosturePosition(actor, id)

    def _NewPage(self, sceneType, **kwargs):
        try:
            scene = sceneType.lower()
        except Exception as e:
            print(f"problematic sceneType in type {type(sceneType)}: {sceneType}")
        newPage = None
        if scene == "classroom":
            newPage = ClassroomPage(self, **kwargs)
        elif scene == "blackboard":
            newPage = BlackboardPage(self, **kwargs)
        elif scene == "cover":
            newPage = CoverPage(self, **kwargs)
        elif scene == "exam":
            if "actor" not in kwargs:
                raise Exception(f'argument "actor" is required')
            newPage = ExamPage(self, **kwargs)
        elif scene == "concentrak":
            if "text" not in kwargs:
                raise Exception(f'argument "text" is required')
            newPage = ConcentrakPage(self, **kwargs)
        elif scene == "notes":
            if "actor" not in kwargs:
                raise Exception(f'argument "actor" is required')
            newPage = NotesPage(self, **kwargs)
        else:
            print(f"Invalid scenario type {sceneType}, must be one of ('exam', 'notes', 'cover', 'blackboard', 'concentrak', 'classroom')")

        return newPage        

    def createPage(self, sceneType, **kwargs):
        newPage = self._NewPage(sceneType, **kwargs)

        if newPage != None:
            self._pages.append(newPage)

        return newPage

    def createPageAtPos(self, pos, sceneType, **kwargs):
        if pos >= 0 and pos < len(self._pages):
            newPage = self._NewPage(sceneType, **kwargs)
            if newPage != None:
                self._pages.insert(pos, newPage)
        else:
            print("Input pos is out of boundary.")
            newPage = None

        return newPage
    
    def removePageAtPos(self, pos):
        if pos >= 0  and pos < len(self._pages):
            self._pages.pop(pos)

    def getPage(self, pos):
        return self._pages[pos] if (pos >= 0  and pos < len(self._pages)) else None

    def uploadImageToCos(self, source):
        if self._cosUploader != None:
            if isinstance(source, dict):
                for key in source:
                    source[key] = self._cosUploader.local2cos(source[key], self.storyId, self.posterPath)
            else:
                source = self._cosUploader.local2cos(source, self.storyId, self.posterPath)
        return source


class Page:
    def __init__(self, type, storyInstance):
        self.story = storyInstance
        self.narrator = storyInstance.narrator
        self.locale = storyInstance.locale
        self.type = type
        self.scene = {}
        self.board = {}
        self.objects = []
        self.subscripts = []
        self.mutescripts = []
        self.interactions = []
        self.defaultInteractions = []
        self.actor = None

    def _getUserId(self, actor):
        userId = -1
        for i, object in enumerate(self.objects):
            if object["name"].lower() == actor.lower():
                userId = i

        if userId == -1:
            self.objects.append({"name": actor})
            userId = len(self.objects) - 1
        return userId
    
    @staticmethod
    def fit_image_rect(rect, width, height, screenWidth=960.0, screenHeight=540.0):
        # image is wider in ratio
        if width / height > (rect[2] if rect[2] > 1.0 else rect[2]*screenWidth) / (rect[3] if rect[3] > 1.0 else rect[3]*screenHeight):
            height = round((rect[2] if rect[2] > 1.0 else rect[2]*screenWidth) * height / width / (1.0 if rect[3] > 1.0 else screenHeight), 3)
            width = rect[2] * 1.0
        # vice versa, rect is wider in ratio
        else:
            width = round((rect[3] if rect[3] > 1.0 else rect[3]*screenHeight) * width / height / (1.0 if rect[2] > 1.0 else screenWidth), 3)
            height = rect[3] * 1.0
        rect[2] = width
        rect[3] = height
        
        return rect


    def test(self, fileName="testPage.json", localOutputPath=LOCAL_DEFAULT_ROOT, language=DEFAULT_LANGUAGE):
        directory = os.path.join(localOutputPath, self.story.storyId)
        if not os.path.exists(directory):
            os.makedirs(directory)

        language = DEFAULT_LANGUAGE if language == None else language
        scripts = self.exportScripts()
        if self.story._synthesizer != None:
            try:
                for script in scripts:
                    soundFileName = script["sound"]
                    if isinstance(soundFileName, str) and len(soundFileName) > 0:
                        text = script["subscript"][language] if isinstance(script["subscript"], dict) else script["subscript"]
                        alternativeText = None if "alternative" not in script else \
                            (script["alternative"][language] \
                                if isinstance(script["alternative"], dict) \
                                else script["alternative"])
                        narrator = script["narrator"]
                        text = alternativeText if isinstance(alternativeText, str) else text
                        self.story._synthesizer.synthesizeFile(
                                narrator, remove_emojis(text), language, directory, os.path.basename(soundFileName)
                            )
                        localOutputFileName = os.path.join(directory, os.path.basename(soundFileName))

                        if self.story._cosUploader != None:
                            self.story._cosUploader.local2cos(localOutputFileName, self.story.storyId, self.story.audioPath)
            except Exception as e:
                print(f"Page.test failed for {script}\n", e)

        with open(os.path.join(localOutputPath, fileName), "w") as file:
            json.dump(
                self.export(), file, ensure_ascii=False, indent=4, sort_keys=False
            )
        print(f"Page.test exported to {os.path.join(localOutputPath, fileName)}")

    def export(self, voiceOffset, pageId):
        raise NotImplementedError("Subclasses must implement export()")

    def exportScripts(self):
        return self.export()["voices"]

##### 问答页面 #####
class ExamPage(Page):
    # onResult: -2
    class InitInteraction(Interaction):
        ON_RESULT = -2
        POPUP = 4
        def __init__(self, actorId=None, text=None, voice=None):
            super().__init__(onResult=self.ON_RESULT, actorId=actorId, text=text, \
                             voice=voice, type="talk", popup=self.POPUP)

    # onResult: -1
    class ErrorInteraction(Interaction):
        ON_RESULT = -1
        POPUP = 4
        def __init__(self, actorId=None, text=None, voice=None):
            super().__init__(onResult=self.ON_RESULT, actorId=actorId, text=text, \
                             voice=voice, type="talk", popup=self.POPUP)

    # popup = 2, onResult: self.correctAnswerId
    class SuccessInteraction(Interaction):
        POPUP = 2
        def __init__(self, actorId=None, onResult=None, text=None, voice=None):
            super().__init__(onResult=onResult, actorId=actorId, text=text, \
                             voice=voice, type="talk", popup=self.POPUP)
    
    def __init__(self, storyInstance, actor, postures=["smilesay"], audio=None, **kwargs):
        super().__init__("exam", storyInstance)
        self.scene = self.story.styles["scenarios"]["exam"]
        self.defaultObject = "exam"
        self.questionSubscript = None
        self.questionInteractions = []
        self.boardContentListScripts = []

        if all(key in kwargs for key in ("voices", "board", "objects", "interactions")):
            voices = kwargs["voices"]
            self.board = kwargs["board"]
            if "content" in self.board and isinstance(self.board["content"], dict):
                boardContent = self.board["content"]
                if "options" in boardContent:
                    options = boardContent["options"]
                    for i, option in enumerate(options if isinstance(options, list) else options[DEFAULT_LANGUAGE]):
                        if isinstance(options, dict):
                            oneOptionDict = {}
                            for key in options.keys():
                                oneOptionDict[key] = options[key][i]
                            self.mutescripts.append(Script(subscript=oneOptionDict))
                        elif isinstance(options, list):
                            self.mutescripts.append(Script(subscript=option))

            self.objects = kwargs["objects"]
            self.actor, actorId, _, _, _, _ = get_actors(self.objects)
            for interaction in kwargs["interactions"]:
                if isinstance(interaction, dict):
                    if ("figure" in interaction and interaction.get("figure", -1) > -1) and "position" in interaction:
                        self.defaultInteractions.append(PostureInteraction(
                            actorId = interaction["actor"] if interaction.get("actor", -1) > -1 else actorId,
                            position = interaction["position"],
                            figure = interaction["figure"],
                            transform = interaction["transform"] \
                                if (isinstance(interaction.get("transform", None), str) \
                                    and len(interaction["transform"]) > 0) \
                                else None
                        ))

                    # onResult = -2 | 0, initInteraction
                    if "content" in interaction and \
                        "onResult" in interaction and (interaction["onResult"][0] if isinstance(interaction["onResult"], list) else interaction["onResult"]) in (-2, 0):
                        content = interaction["content"]
                        if isinstance(content, dict) and "voice" in content:
                            voiceId = content["voice"]
                            self.soundFile = voices[voiceId]["sound"]
                            text = self.board["content"]["question"] \
                                if ("content" in self.board and isinstance(self.board["content"], dict) and "question" in self.board["content"]) else ""
                            self.questionSubscript = Script(
                                sound = self.soundFile,
                                subscript = text,
                                narrator = self.actor,
                                languages = voices[voiceId]["languages"] if "languages" in voices[voiceId] else None)
                            self.defaultInteractions.append(ExamPage.InitInteraction(
                                actorId = self._getUserId(self.defaultObject),
                                text = text,
                                voice = 0
                            ))
                    elif "onResult" in interaction:
                        onResultValue = (interaction["onResult"][0] if isinstance(interaction["onResult"], list) else interaction["onResult"])
                        textValue = interaction["content"].get("text", "") \
                            if ("content" in interaction and isinstance(interaction["content"], dict)) \
                            else ""
                        
                        # onResultValue > 0, successInteraction
                        if onResultValue > 0:
                            self.correctAnswerId = onResultValue
                            if "content" in interaction and isinstance(interaction["content"].get("popup", None), int):
                                popup = interaction["content"]["popup"]
                                if popup == 2:
                                    self.defaultInteractions.append(ExamPage.SuccessInteraction(
                                        actorId = self._getUserId(self.defaultObject),
                                        onResult = onResultValue,
                                        text = textValue
                                    ))
                                if popup == 4:
                                    self.defaultInteractions.append(Interaction(
                                        actorId = self._getUserId(self.defaultObject),
                                        onResult = onResultValue,
                                        text = textValue,
                                        popup = popup,
                                        type = "talk"
                                    ))
                        # onResultValue == -1, errorInteraction
                        elif onResultValue == -1:
                            self.defaultInteractions.append(ExamPage.ErrorInteraction(
                                actorId = self._getUserId(self.defaultObject),
                                text = textValue,
                                voice = -1
                            ))
                        if len(textValue) > 0:
                            self.mutescripts.append(Script(subscript=textValue))
                    elif "type" in interaction and interaction["type"] in ("motion", "talk") and "figure" in interaction:
                        postures = interaction["figure"]
                        if "content" in interaction and isinstance(interaction["content"], dict) and "voice" in interaction["content"]:
                            content = interaction["content"]
                            voiceId = content["voice"]
                            contentText = content["text"] if "text" in content else ""
                            questionText = self.board["content"]["question"] if ("content" in self.board and isinstance(self.board["content"], dict) and "question" in self.board["content"]) else ""
                            if contentText == questionText and voiceId > 0:
                                self.soundFile = voices[voiceId]["sound"]
                                self.questionSubscript = Script(
                                    sound = self.soundFile,
                                    subscript = questionText,
                                    narrator = self.actor,
                                    languages = voices[voiceId]["languages"] if "languages" in voices[voiceId] else None)
                                                                
                                self.questionInteractions.append(ExamPage.InitInteraction(
                                    actorId=self._getUserId(self.defaultObject),
                                    voice=voiceId
                                ))
        else:
            self.actor = actor
            self.soundFile = self.story.getAudioPath(f"voice-{uuid.uuid4()}.mp3" if audio == None else audio)
            posture_list = (
                [postures]
                if (isinstance(postures, str) or isinstance(postures, int))
                else postures
            )
            figure, position = self.story.getUserPostureIdAndPosition(actor, posture_list, keyScenario="half")

            scale = None
            if (isinstance(kwargs.get("scale", None), int) or isinstance(kwargs.get("scale", None), float)) and kwargs["scale"] > 0:
                scale = f"scale({kwargs['scale']})"
            self.defaultInteractions.append(PostureInteraction(
                actorId = self._getUserId(self.actor),
                position = position,
                transform = scale if scale != None else "scale(1.5)",
                figure = figure
            ))
            

    def setQuestion(self, question, options, answers=None, **kwargs):
        assert isinstance(question, str) or isinstance(question, dict) or question == None
        if options != None:
            assert isinstance(options, list) or isinstance(options, dict)
        newQuestion = None if question == None else (question if isinstance(question, dict) else {self.locale: question})

        hasChinese = False
        optionList = options if isinstance(options, list) else options[DEFAULT_LANGUAGE]
        for i, option in enumerate(optionList):
            if has_chinese_char(option):
                hasChinese = True
            if isinstance(options, dict):
                oneOptionDict = {}
                for key in options.keys():
                    oneOptionDict[key] = options[key][i]
                self.mutescripts.append(Script(subscript=oneOptionDict))
            elif isinstance(options, list):
                self.mutescripts.append(Script(subscript=option))

        answer_list = None
        if hasChinese:
            if isinstance(answers, dict):
                answer_list = {}
                for locale in answers.keys():
                    answer_list[locale] = [answers[locale]] if not isinstance(answers[locale], list) else answers[locale]
            else:
                answer_list = [] if answers == None else ({DEFAULT_LANGUAGE: [answers] if not isinstance(answers, list) else answers})
            options = options if isinstance(options, dict) else {DEFAULT_LANGUAGE: options}
        else:
            answer_list = [] if answers == None else ([answers] if not isinstance(answers, list) else answers)
            options = options if isinstance(options, list) else options[DEFAULT_LANGUAGE]

        fontSize = kwargs["fontSize"] if "fontSize" in kwargs else "20px"
        if isinstance(fontSize, int):
            fontSize = str(fontSize) + "px"
        self.board = {
            "content": {
                "fontSize": fontSize,
                "fontColor": kwargs["fontColor"] if "fontColor" in kwargs else "white",
                "question": newQuestion if newQuestion != None else (self.board["content"]["question"] if self.board["content"]["question"] else ""),
                "options": options,
                "answer": answer_list,
                "colsPerRow": kwargs["colsPerRow"] if "colsPerRow" in kwargs else 1,
            },
            "type": "exam",
            "rect": kwargs["rect"] if "rect" in kwargs else [0, 0, 1, 1],
        }

        self.correctAnswerId = 0
        language = next(iter(options), None) if isinstance(options, dict) else None
        if (isinstance(answer_list, list) and len(answer_list) > 0) or (isinstance(answer_list, dict) and len(answer_list[language]) > 0):
            for i, option in enumerate(options[language] if isinstance(options, dict) else options):
                for entry in (answer_list[language] if (isinstance(options, dict) and isinstance(answer_list, dict)) else answer_list):
                    if entry == option:
                        self.correctAnswerId += 2**i

        # 如果新内容与原内容不同。则需先生成test内容，下一步再更新production上内容
        if newQuestion != None:
            if self.questionSubscript == None:
                self.questionSubscript = Script(
                    sound = self.story.getAudioPath(f"voice-{uuid.uuid4()}.mp3"),
                    subscript = newQuestion,
                    narrator = self.actor
                )
            elif self.questionSubscript.subscript != newQuestion:
                self.questionSubscript.subscript = newQuestion
                self.questionSubscript.sound = self.story.getAudioPath(f"voice-{uuid.uuid4()}.mp3") \
                    if self.questionSubscript.sound == None or len(self.questionSubscript.sound) == 0 \
                    else self.questionSubscript.sound
                self.questionSubscript.reset2test(self.actor)

        self.questionInteractions = []

        # 初始化页面行为 onResult: -2
        self.questionInteractions.append(ExamPage.InitInteraction(
            actorId = self._getUserId(self.defaultObject),
            voice = 0
            ))

        # 错误答案提示行为 onResult: -1
        self.questionInteractions.append(ExamPage.ErrorInteraction(
            actorId = self._getUserId(self.defaultObject),
            text = kwargs["onErrorPrompt"] \
                if "onErrorPrompt" in kwargs and kwargs["onErrorPrompt"] != 0 and len(kwargs["onErrorPrompt"]) > 0 \
                else ("再想想" \
                      if "alwaysTruePrompt" not in kwargs \
                      else (kwargs["alwaysTruePrompt"] \
                            if isinstance(kwargs["alwaysTruePrompt"], dict) \
                            else {self.locale: kwargs["alwaysTruePrompt"]}))
            ))

        # 正确答案行为 onResult: 由所有正确答案id计算所得
        if self.correctAnswerId > 0:
            self.questionInteractions.append(ExamPage.SuccessInteraction(
                onResult=self.correctAnswerId,
                actorId=self._getUserId(self.defaultObject)
                ))
            if "onSuccessPrompt" in kwargs and kwargs["onSuccessPrompt"] != 0 and len(kwargs["onSuccessPrompt"]) > 0:
                self.defaultInteractions.append(Interaction(
                                        actorId = self._getUserId(self.defaultObject),
                                        onResult = self.correctAnswerId,
                                        text = kwargs["onSuccessPrompt"],
                                        popup = 4,
                                        type = "talk"
                                    ))
                self.mutescripts.append(Script(subscript=kwargs["onSuccessPrompt"]))

    def setFontSize(self, size):
        if "content" in self.board and isinstance(self.board["content"], dict):
            self.board["content"]["fontSize"] = str(size)+"px" if isinstance(size, int) else size

    def setColsPerRow(self, colsPerRow):
        if "content" in self.board and isinstance(self.board["content"], dict):
            self.board["content"]["colsPerRow"] = colsPerRow

    def setRect(self, rect):
        if isinstance(self.board, dict):
            self.board["rect"] = rect

    def setFontColor(self, color):
        if "content" in self.board and isinstance(self.board["content"], dict):
            self.board["content"]["fontColor"] = color

    def addImage(self, source, rect=[0, 0, 1, 1], autoFit=True, uploadToCos=True, caption=None):
        assert isinstance(rect, list) and len(rect) >= 4 and rect[2] > 0 and rect[3] > 0
        width, height = Story.getImageSize(next(iter(source.values()), None) if isinstance(source, dict) else source)
        assert width > 0 and height > 0

        if autoFit:
            rect = Page.fit_image_rect(rect, width, height)

        if "contentList" not in self.board:
            self.board["contentList"] = []
        if  uploadToCos:
            source = self.story.uploadImageToCos(source)

        self.board["contentList"].append(
            {
                "image": source,
                "rect": rect,
                "caption": ""
            }
        )
        newCaption = ""
        if caption != None and (isinstance(caption, dict) or isinstance(caption, str)) and len(caption) > 0:
            newCaption = caption if isinstance(caption, dict) else {self.locale: caption}
        self.board["contentList"][-1]["caption"] = newCaption
        self.boardContentListScripts.append(Script(subscript=newCaption))

    def updateImage(self, pos, source, rect=[0, 0, 1, 1], autoFit=True, uploadToCos=True, caption=None):
        if pos < len(self.board["contentList"]) and pos >= 0:
            assert isinstance(rect, list) and len(rect) >= 4 and rect[2] > 0 and rect[3] > 0
            width, height = Story.getImageSize(next(iter(source.values()), None) if isinstance(source, dict) else source)
            assert width > 0 and height > 0

            if autoFit:
                rect = Page.fit_image_rect(rect, width, height)

            if uploadToCos:
                source = self.story.uploadImageToCos(source)

            self.board["contentList"][pos] = {
                    "image": update_object(self.board["contentList"][pos]["image"], source, self.locale),
                    "rect": rect,
                    "caption": ""
                }
            
            newCaption = ""
            if caption != None and (isinstance(caption, dict) or isinstance(caption, str)) and len(caption) > 0:
                newCaption = caption if isinstance(caption, dict) else {self.locale: caption}
            self.board["contentList"][pos]["caption"] = newCaption
            self.boardContentListScripts[pos] = Script(subscript=newCaption)

    def removeImage(self, pos):
        if pos < len(self.board["contentList"]) and pos >= 0:
            self.board["contentList"].pop(pos)
            self.boardContentListScripts.pop(pos)

    def export(self, voiceOffset=0, pageId=0.0):
        outSubscripts = [subscript.export() for subscript in ([self.questionSubscript] + self.boardContentListScripts + self.mutescripts) \
                         if subscript is not None and subscript.export() is not None]

        outInteractions = []
        for interaction in self.defaultInteractions + self.questionInteractions:
            newInteration = None
            if interaction.voice != None and interaction.voice > -1:
                newInteration = interaction.copy()
                newInteration.voice += voiceOffset
            exported = newInteration.export() if newInteration != None else interaction.export() 
            if exported != None:
                outInteractions.append(exported)

        return {
            "voices": outSubscripts,
            "events": [
                {
                    "id": pageId,
                    "scene": self.scene if isinstance(self.scene, str) else copy.deepcopy(self.scene),
                    "board": copy.deepcopy(self.board),
                    "objects": copy.deepcopy(self.objects),
                    "interactions": outInteractions,
                }
            ],
        }

##### 总结页面 #####
class NotesPage(Page):
    def __init__(self, storyInstance, actor, postures=["smilesay"], endingEffect=True, audio=None, **kwargs):
        super().__init__("notes", storyInstance)
        self.scene = self.story.styles["scenarios"]["notes"]["scene"]
        self.board = self.story.styles["scenarios"]["notes"]["board"]
        self.bullets = []
        self.defaultObject = "notes"

        if all(key in kwargs for key in ("voices", "board", "objects", "interactions")):
            voices = kwargs["voices"]
            self.board = kwargs["board"]
            self.objects = kwargs["objects"]
            self.actor, actorId, self.narrator, _, defaultObject, _ = get_actors(self.objects)
            self.defaultObject = defaultObject if defaultObject != None else self.narrator if self.narrator != None else self.defaultObject
            html = self.board["content"].get("html", None)
            self.soundFile = self.story.getAudioPath(f"voice-{uuid.uuid4()}.mp3" if audio == None else audio)
            self.soundFileLanguages = None
            self.endingEffect = False
            postures = 0
            transform = None
            if isinstance(html, dict):
                bullets = {}
                for key in html.keys():
                    bullets[key] = get_bullets_from_html(html[key])
                for i in range(len(bullets[DEFAULT_LANGUAGE])):
                    self.bullets.append({key: bullets[key][i] for key in bullets.keys()})
            elif isinstance(html, str):
                self.bullets = get_bullets_from_html(html)
            for interaction in kwargs["interactions"]:
                if isinstance(interaction, dict):
                    if "content" in interaction:
                        content = interaction["content"]
                        if isinstance(content, dict) and "voice" in content:
                            value = content["voice"]
                            if value == 0:
                                self.endingEffect = True
                            elif value > 0:
                                self.soundFile = voices[value]["sound"]
                                self.soundFileLanguages = voices[value]["languages"] if "languages" in voices[value] else None
                    elif "type" in interaction and "figure" in interaction:
                        if "transform" in interaction:
                            transform = interaction["transform"]
                        value = interaction["figure"]
                        if interaction["type"] == "motion":
                            postures = value
                        elif interaction["type"] == "talk":
                            if interaction["actor"] == actorId and value > -1: 
                                postures = value
            figure, position = self.story.getUserPostureIdAndPosition(self.actor, postures, keyScenario="half")
            self.defaultInteractions.append(
                PostureInteraction(
                    position = position,
                    transform = transform if transform != None else "scale(1.5)",
                    figure = figure,
                    actorId = actorId
                ))
            # Remove content from board, leave template only
            if isinstance(self.board["content"]["html"], dict):
                key = next(iter(self.board["content"]["html"].keys()), None)
                if key != None:
                    self.board["content"]["html"] = self.board["content"]["html"][key]
                    pattern = r"<ul>(.*?)</ul>"
                    text = self.board["content"]["html"]\
                        .replace("</ul><ul>", "")\
                        .replace("</li><li>", "")\
                        .replace("<li>", "")\
                        .replace("</li>", "")
                    matches = re.findall(pattern, text, flags=re.DOTALL)
                    for match in matches:
                        text = text.replace(match, "{}")
                    self.board["content"]["html"] = text
            if isinstance(self.bullets, dict):
                for key in self.bullets.keys():
                    print("language:", key, "bullets:", self.bullets[key])
            elif isinstance(self.bullets, list):
                print("bullets:", self.bullets)
        else:
            self.actor = actor
            self.soundFile = self.story.getAudioPath(f"voice-{uuid.uuid4()}.mp3" if audio == None else audio)
            self.endingEffect = endingEffect
            self.soundFileLanguages = kwargs["languages"] if ("languages" in kwargs and isinstance(kwargs["languages"], list)) else None

            posture_list = (
                [postures]
                if (isinstance(postures, str) or isinstance(postures, int))
                else postures
            )
            figure, position = self.story.getUserPostureIdAndPosition(actor, posture_list, keyScenario="half")
            scale = None
            if (isinstance(kwargs.get("scale", None), int) or isinstance(kwargs.get("scale", None), float)) and kwargs["scale"] > 0:
                scale = f"scale({kwargs['scale']})"
            self.defaultInteractions.append(
                PostureInteraction(
                    position = position,
                    transform = scale if scale != None else "scale(1.5)",
                    figure = figure,
                    actorId = self._getUserId(actor)
                ))

        self.endingInteraction = Interaction(
                duration = "auto",
                voice = 0,
                text = "",
                actorId = self._getUserId(self.defaultObject),
                type = "talk"
            )

    def addBullet(self, text):
        self.bullets.append(text if isinstance(text, dict) else {self.locale: text})
        self.soundFileLanguages = None
        if isinstance(self.soundFile, str):
            self.soundFile = switch_to_test_path(self.soundFile)

    def updateBullet(self, pos, text):
        if pos < len(self.bullets) and pos >= 0:
            self.bullets[pos] = update_object(self.bullets[pos], text, self.locale)
        self.soundFileLanguages = None
        if isinstance(self.soundFile, str):
            self.soundFile = switch_to_test_path(self.soundFile)

    def removeBullet(self, pos):
        if pos < len(self.bullets) and pos >= 0:
            self.bullets.pop(pos)
        self.soundFileLanguages = None
        if isinstance(self.soundFile, str):
            self.soundFile = switch_to_test_path(self.soundFile)

    def setEndingEffect(self, on: bool):
        self.endingEffect = on

    def export(self, voiceOffset=0, pageId=0.0):
        bullets_strings = {}
        bullets_subscripts = {}
        for bullet in self.bullets:
            if isinstance(bullet, dict):
                for key in bullet.keys():
                    bullets_strings[key] = f"<li>{bullet[key]}</li>" \
                        if (key not in bullets_strings or bullets_strings[key] == None) \
                        else bullets_strings[key] + f"<li>{bullet[key]}</li>"
                    bullets_subscripts[key] = bullet[key] \
                        if (key not in bullets_subscripts or bullets_subscripts[key] == None) \
                        else bullets_subscripts[key] + "<break time=\"1500ms\"/>" + bullet[key]
            else:
                if self.locale not in bullets_strings:
                    bullets_strings[self.locale] = ""
                if self.locale not in bullets_subscripts:
                    bullets_subscripts[self.locale] = ""
                bullets_strings[self.locale] = f"<li>{bullet}</li>" \
                    if bullets_strings[self.locale] in (None, "") \
                    else bullets_strings[self.locale] + f"<li>{bullet}</li>"
                bullets_subscripts[self.locale] = bullet \
                    if bullets_subscripts[self.locale] in (None, "") \
                    else bullets_subscripts[self.locale] + "<break time=\"1500ms\"/>" + bullet

        outBoard = copy.deepcopy(self.board)
        formatString = outBoard["content"]["html"]
        outBoard["content"]["html"] = {}
        for key in bullets_strings:
            outBoard["content"]["html"][key] = formatString.format(bullets_strings[key])
                
        noteScript = Script(
            sound=self.soundFile,
            subscript=bullets_subscripts,
            narrator=self.actor,
            languages = self.soundFileLanguages if isinstance(self.soundFileLanguages, list) else None
            )
        outSubscripts = [noteScript.export()]

        notesInteraction = Interaction(
                voice = 0 + voiceOffset,
                type = "talk",
                actorId = self._getUserId(self.defaultObject)
            )
        outInteractions = [interaction.export() for interaction in (self.defaultInteractions + [notesInteraction] + ([self.endingInteraction] if self.endingEffect else []))]

        return {
            "voices": outSubscripts,
            "events": [
                {
                    "id": pageId,
                    "scene": self.scene if isinstance(self.scene, str) else copy.deepcopy(self.scene),
                    "board": outBoard,
                    "objects": copy.deepcopy(self.objects),
                    "interactions": outInteractions
                }
            ],
        }


##### 概念页面 #####
class ConcentrakPage(Page):
    class ConcentrakInteraction(Interaction):
        def __init__(self, actorId=-1, text=None):
            super().__init__(popup=6, actorId=actorId, text=text)

    def __init__(self, storyInstance, text, **kwargs):
        super().__init__("concentrak", storyInstance)
        self.scene = self.story.styles["scenarios"]["concentrak"]
        self.defaultObject = "concentrak"

        if all(key in kwargs for key in ("voices", "board", "objects", "interactions")):
            voices = kwargs["voices"]
            self.objects = kwargs["objects"]
            self.board = kwargs["board"]
            for interaction in kwargs["interactions"]:
                if isinstance(interaction, dict):
                    if "content" in interaction:
                        content = interaction["content"]
                        if isinstance(content, dict):
                            if "popup" in content and "text" in content:
                                text = content["text"]
                                if content["popup"] == 6:
                                    self.mutescripts.append(Script(subscript=text))
                                    self.defaultInteractions.append(ConcentrakPage.ConcentrakInteraction(
                                        actorId = interaction["actor"],
                                        text = text
                                        ))
                                elif content["popup"] == 4 and "voice" in content and content["voice"] > 0:
                                    voiceId = content["voice"]
                                    if "actor" in interaction:
                                        actorId = interaction["actor"]
                                        self.subscripts.append(Script(
                                            sound = voices[voiceId]["sound"],
                                            subscript = text,
                                            narrator = self.objects[actorId]["name"],
                                            languages = voices[voiceId]["languages"] \
                                                if isinstance(voices[voiceId].get("languages", None), list) \
                                                else None 
                                            ))
                                        self.interactions.append(Interaction(
                                            duration = "auto",
                                            popup = 4,
                                            text = text,
                                            voice = len(self.subscripts) - 1,
                                            actorId = actorId,
                                            type = "talk"))
        else:
            self.mutescripts.append(Script(subscript=text))
            self.defaultInteractions.append(ConcentrakPage.ConcentrakInteraction(
                    actorId = self._getUserId(self.defaultObject),
                    text = text if isinstance(text, dict) else {self.locale: text}
                    ))

    def addNarration(self, text, narrator=None, alternativeText=None, audio=None, **kwargs):
        narrator = narrator if narrator != None else self.narrator if self.narrator != None else self.actor
        self.subscripts.append(Script(
            sound = self.story.getAudioPath(f"voice-{uuid.uuid4()}.mp3" if audio == None else audio),
            subscript = text if isinstance(text, dict) else {self.locale: text},
            narrator = narrator,
            alternative = {self.locale: alternativeText} if alternativeText != None else None,
            languages = kwargs["languages"] if isinstance(kwargs.get("languages", None), list) else None
            ))          
        
        self.interactions.append(Interaction(
            duration = "auto",
            popup = 4,
            voice = len(self.subscripts) - 1,
            text = text if isinstance(text, dict) else {self.locale: text},
            figure = -1 if narrator in VISIBLE_ACTORS else None,
            actorId = self._getUserId(narrator),
            type = "talk"
        ))

    def updateNarration(self, pos, text=None, narrator=None, alternativeText=None):
        subscript = text if isinstance(text, dict) else ({self.locale: text} if text != None else None)
        alternative = alternativeText if isinstance(alternativeText, dict) else ({self.locale: alternativeText} if alternativeText != None else None)
        if pos < len(self.subscripts) and pos >= 0 and (subscript!=None or narrator!=None or alternative!=None):
            self.subscripts[pos].reset2test()
            if subscript != None:
                self.subscripts[pos].subscript = update_object(self.subscripts[pos].subscript, subscript, self.locale)
                self.interactions[pos].text = update_object(self.interactions[pos].text, subscript, self.locale)
            if alternative != None:
                self.subscripts[pos].alternative = update_object(self.subscripts[pos].alternative, alternative, self.locale)
            if narrator != None:
                self.subscripts[pos].reset2test(narrator)
                self.interactions[pos].actorId = self._getUserId(narrator)
                self.interactions[pos].figure = -1 if narrator in VISIBLE_ACTORS else None

    def removeNarration(self, pos):
        if pos < len(self.subscripts) and pos >= 0:
            self.subscripts.pop(pos)
            self.interactions.pop(pos)
            if pos < len(self.interactions):
                for i, interaction in enumerate(self.interactions[pos:]):
                    self.interactions[i].voice = interaction.voice - 1

    def export(self, voiceOffset=0, pageId=0.0):
        outSubscripts = [subscript.export() \
                            for subscript in self.subscripts + self.mutescripts \
                            if subscript is not None and subscript.export() is not None]
        
        outInteractions = []
        for interaction in (self.defaultInteractions + self.interactions):
            newInteration = None
            if interaction.voice != None and interaction.voice > -1:
                newInteration = interaction.copy()
                newInteration.voice += voiceOffset
            exported = newInteration.export() if newInteration != None else interaction.export() 
            if exported != None:
                outInteractions.append(exported)

        return {
            "voices": outSubscripts,
            "events": [
                {
                    "id": pageId,
                    "scene": "" if self.scene == None else (self.scene if isinstance(self.scene, str) else copy.deepcopy(self.scene)),
                    "board": copy.deepcopy(self.board),
                    "objects": copy.deepcopy(self.objects),
                    "interactions": outInteractions,
                }
            ],
        }


##### 黑板页面 #####
class BoardPage(Page):
    def __init__(self, pageType, storyInstance, **kwargs):
        assert pageType in ("cover", "blackboard", "classroom")
        super().__init__(pageType, storyInstance)
        self.scene = self.story.styles["scenarios"][pageType]
        self.narrations = {"subscripts": [], "interactions": []}
        self.narrator = self.story.narrator
        self.narratorId = -1
        self.hasImage = False
        self.enableImageMagnify = True if pageType == "classroom" else False
        self.boardContentScript = None
        self.boardContentListScripts = []
        self.defaultInteraction = None

        if all(key in kwargs for key in ("voices", "board", "objects", "interactions")):
            voices = kwargs.get("voices", None)
            self.objects = kwargs.get("objects", None)
            self.board = kwargs.get("board", None)
            if self.board != None and "content" in self.board:
                boardContent = self.board["content"]
                if isinstance(boardContent, dict) and "caption" in boardContent:
                    self.boardContentScript = Script(subscript=boardContent["caption"])
            if self.board != None and "rect" in self.board and isinstance(self.board["rect"], list):
                self.hasImage = True
            if self.objects != None:
                self.actor, self.actorId, self.narrator, self.narratorId, _, _ = get_actors(self.objects)

            if kwargs.get("interactions", None) != None:
                for interaction in kwargs["interactions"]:
                    if isinstance(interaction, dict):
                        # interactions that involves posters, or non visible-actor-involved
                        if "actor" in interaction and "content" in interaction \
                            and (("onResult" in interaction and (interaction["onResult"][0] if isinstance(interaction["onResult"], list) else interaction["onResult"]) > 0) \
                            or ("onPoster" in interaction and (interaction["onPoster"][0] if isinstance(interaction["onPoster"], list) else interaction["onPoster"]) > 0) \
                            or (self.objects[interaction["actor"]]["name"] not in VISIBLE_ACTORS)):
                            actorId = interaction["actor"]
                            content = interaction["content"]
                            if isinstance(content, dict) and "text" in content and "voice" in content and content["voice"] > 0:
                                text = content["text"]
                                voiceId = content["voice"]
                                self.narrations["subscripts"].append(Script(
                                    sound = voices[voiceId]["sound"],
                                    subscript = text,
                                    narrator = self.objects[actorId]["name"],
                                    languages = voices[voiceId]["languages"] if "languages" in voices[voiceId] and isinstance(voices[voiceId]["languages"], list) else None
                                ))
                                self.narrations["interactions"].append(Interaction(
                                    duration = interaction.get("duration", ""),
                                    actorId = actorId,
                                    figure = interaction.get("figure", None),
                                    text = text,
                                    popup = 4,
                                    onPoster = interaction.get("onResult", None) or interaction.get("onPoster", None),
                                    voice = len(self.narrations["subscripts"]) - 1,
                                    type = interaction.get("type", None)
                                ))
                        # visible-actor-involved interactions
                        elif "actor" in interaction:
                            actorId = interaction["actor"]
                            if "content" in interaction:
                                content = interaction["content"]
                                if isinstance(content, dict) and "text" in content and "voice" in content and content["voice"] > 0:
                                    text = content["text"]
                                    voiceId = content["voice"]   
                                    self.subscripts.append(Script(
                                        sound=voices[voiceId]["sound"],
                                        subscript=text,
                                        narrator=self.objects[actorId]["name"],
                                        languages=voices[voiceId]["languages"] if isinstance(voices[voiceId].get("languages", None), list) else None
                                    ))
                                    self.interactions.append(Interaction(
                                        duration = interaction.get("duration", ""),
                                        popup = content.get("popup", None),
                                        text = text,
                                        voice = len(self.subscripts) - 1,
                                        actorId = actorId,
                                        type = interaction.get("type", None)
                                    ))
                            if ("figure" in interaction and interaction.get("figure", -1) > -1) and "position" in interaction:
                                self.defaultInteraction = Interaction(
                                    figure = interaction["figure"],
                                    position = interaction["position"],
                                    transform = interaction.get("transform", None),
                                    actorId = actorId,
                                    type = "talk"
                                )

    def setActor(self, actor, postures=["smilesay", "-stand-"], **kwargs):
        if actor in VISIBLE_ACTORS:
            if self.actor != actor:
                update_visible_actor(self.objects, actor)
                [script.reset2test(self.actor, actor) for script in self.subscripts]
                self.actor = actor

            posture_list = (
                [postures]
                if (isinstance(postures, str) or isinstance(postures, int))
                else [postures[0]] \
                    if (isinstance(postures, list) and isinstance(postures[0], int))
                    else postures
            )
            figure, position = self.story.getUserPostureIdAndPosition(actor, posture_list, keyScenario="")
            if isinstance(kwargs.get("position", None), list) and len(kwargs["position"]) == 2:
                position = kwargs["position"]
            scale = None
            if (isinstance(kwargs.get("scale", None), int) or isinstance(kwargs.get("scale", None), float)) and kwargs["scale"] > 0:
                scale = f"scale({kwargs['scale']})"
            self.defaultInteraction = Interaction(
                                figure = figure,
                                position = position,
                                transform = scale if scale != None else self.story.styles["transform"],
                                type = "talk",
                                actorId = self._getUserId(actor)
                            )
        elif actor == None:
            self.defaultInteraction = None

    def setDialog(self, text, alternativeText=None, **kwargs):
        newSubscript = Script(
            sound = switch_to_test_path(self.subscripts[0]["sound"]) \
                if (len(self.subscripts) > 0 and isinstance(self.subscripts[0], dict) \
                    and self.subscripts[0].sound != None and len(self.subscripts[0].sound) > 0) \
                else self.story.getAudioPath(f"voice-{uuid.uuid4()}.mp3"),
            subscript = text if isinstance(text, dict) else {self.locale: text},
            narrator = self.actor,
            languages = kwargs["languages"] if isinstance(kwargs.get("languages", None), list) else None,
            alternative = (alternativeText if isinstance(alternativeText, dict) else {self.locale: alternativeText}) \
                if alternativeText != None else None
        )
            
        newInteraction = Interaction(
            duration = "auto",
            popup = kwargs["popup"] if "popup" in kwargs else self.story.styles["popup"],
            voice = 0,
            text = text if isinstance(text, dict) else {self.locale: text},
            type = "talk",
            figure = -1, 
            actorId = self._getUserId(self.actor)
        )
        self.subscripts = [newSubscript] + self.subscripts[1:] if self.subscripts else [newSubscript]
        self.interactions = [newInteraction] + self.interactions[1:] if self.interactions else [newInteraction]

    def addDialog(self, text, alternativeText=None, **kwargs):
        self.subscripts.append(Script(
            sound = self.story.getAudioPath(f"voice-{uuid.uuid4()}.mp3"),
            subscript = text if isinstance(text, dict) else {self.locale: text},
            narrator = self.actor,
            languages = kwargs["languages"] if isinstance(kwargs.get("languages", None), list) else None,
            alternative = (alternativeText if isinstance(alternativeText, dict) else {self.locale: alternativeText}) \
                if alternativeText != None else None
        ))

        self.interactions.append(Interaction(
            duration="auto",
            voice=len(self.subscripts) - 1,
            popup=kwargs["popup"] if "popup" in kwargs else self.story.styles["popup"],
            text=text if isinstance(text, dict) else {self.locale: text},
            figure=-1,
            actorId=self._getUserId(self.actor),
            type="talk"))

    def updateDialog(self, pos, text=None, alternativeText=None, popup=None):
        if pos < len(self.subscripts) and pos >= 0:
            self.subscripts[pos].subscript = update_object(self.subscripts[pos].subscript, text, self.locale)
            self.subscripts[pos].alternative = update_object(self.subscripts[pos].alternative, alternativeText, self.locale)
            self.subscripts[pos].reset2test()

            self.interactions[pos].text = update_object(self.interactions[pos].text, text, self.locale)
            if popup != None:
                self.interactions[pos].popup = popup

    def removeDialog(self, pos):
        if pos < len(self.subscripts) and pos >= 0:
            self.subscripts.pop(pos)
            self.interactions.pop(pos)
            if pos < len(self.interactions):
                for i, interaction in enumerate(self.interactions[pos:]):
                    self.interactions[i].voice = interaction.voice - 1

    def addNarration(self, text, narrator=None, alternativeText=None, audio=None, **kwargs):
        narrator = narrator if narrator != None else self.narrator if self.narrator != None else self.actor
        subscript = text if isinstance(text, dict) else {self.locale: text}
        self.narrations["subscripts"].append(Script(
            sound = self.story.getAudioPath(f"voice-{uuid.uuid4()}.mp3" if audio == None else audio),
            subscript = subscript,
            narrator = narrator,
            alternative = {self.locale: alternativeText} if alternativeText != None else None,
            languages = kwargs["languages"] if isinstance(kwargs.get("languages", None), list) else None
        ))

        self.narrations["interactions"].append(Interaction(
            duration="auto",
            popup = 4,
            voice = len(self.narrations["subscripts"]) - 1,
            text = subscript,
            figure = -1 if narrator in VISIBLE_ACTORS else None,
            actorId = self._getUserId(narrator),
            type = "talk"))

    def updateNarration(self, pos, text=None, narrator=None, alternativeText=None):
        subscript = text if isinstance(text, dict) else ({self.locale: text} if text != None else None)
        alternative = alternativeText if isinstance(alternativeText, dict) else ({self.locale: alternativeText} if alternativeText != None else None)
        if pos < len(self.narrations["subscripts"]) and pos >= 0 and (subscript!=None or narrator!=None or alternative!=None):
            self.narrations["subscripts"][pos].reset2test()
            if subscript != None:
                self.narrations["subscripts"][pos].subscript = update_object(self.narrations["subscripts"][pos].subscript, subscript, self.locale)
                self.narrations["interactions"][pos].text = update_object(self.narrations["interactions"][pos].text, subscript, self.locale)
            if alternative != None:
                self.narrations["subscripts"][pos].alternative = update_object(self.narrations["subscripts"][pos].alternative, alternative, self.locale)
            if narrator != None:
                self.narrations["subscripts"][pos].reset2test(narrator)
                self.narrations["interactions"][pos].actorId = self._getUserId(narrator)
                self.narrations["interactions"][pos].figure = -1 if narrator in VISIBLE_ACTORS else None

    def removeNarration(self, pos):
        if pos < len(self.narrations["subscripts"]) and pos >= 0:
            self.narrations["subscripts"].pop(pos)
            self.narrations["interactions"].pop(pos)
            if pos < len(self.narrations["interactions"]):
                for i, interaction in enumerate(self.narrations["interactions"][pos:]):
                    self.narrations["interactions"][i].voice = interaction.voice - 1

    def setImage(self, source, rect=[0.2, 0.2, 400, 400], autoFit=True, uploadToCos=True, **kwargs):
        assert type(rect) is list and len(rect) >= 4 and rect[2] > 0 and rect[3] > 0
        width, height = Story.getImageSize(next(iter(source.values()), None) if isinstance(source, dict) else source)
        assert width > 0 and height > 0

        if autoFit:
            rect = Page.fit_image_rect(rect, width, height)

            if self.actor == "boy":
                if rect[2] > 1.0:
                    rect[0] = round(((1 - rect[0]) if rect[0] <= 1.0 else rect[0]/960.0) - rect[2]/960.0, 3)
                elif rect[2] < 1.0:
                    rect[0] = ((1 - rect[0]) if rect[0] <= 1.0 else rect[0]/960.0) - rect[2]

        if uploadToCos:
            source = self.story.uploadImageToCos(source)

        caption = kwargs["caption"] if "caption" in kwargs else ""
        self.board = {
            "content": {
                "caption": caption,
                "image": source
            },
            "rect": rect,
        }
        if (isinstance("caption", str) and len(caption) > 0) or (isinstance(caption, dict) and len(next(iter(caption.values()), "") > 0)):
            fontSize = kwargs["fontSize"] if "fontSize" in kwargs else "24px"
            if isinstance(fontSize, int):
                fontSize = str(fontSize) + "px"
            self.board["content"]["fontSize"] = fontSize
            self.board["content"]["fontColor"] = kwargs["fontColor"] if "fontColor" in kwargs else "white"

        self.boardContentScript = Script(subscript=caption)

        if kwargs["magnify"] if "magnify" in kwargs else self.enableImageMagnify:
            self.board["content"]["magnify"] = True

        border = kwargs["border"] if "border" in kwargs else self.enableImageMagnify
        if border:
            self.board["content"]["border"] = kwargs["borderStyle"] if "borderStyle" in kwargs else self.story.styles["frame"]
        if not border:
            self.board["content"].pop("border", None)

        self.hasImage = True

    def addImage(self, source, rect=[0, 0, 1, 1], autoFit=True, uploadToCos=True, caption=None, **kwargs):
        assert isinstance(rect, list) and len(rect) >= 4 and rect[2] > 0 and rect[3] > 0
        width, height = Story.getImageSize(next(iter(source.values()), None) if isinstance(source, dict) else source)
        assert width > 0 and height > 0

        if autoFit:
            rect = Page.fit_image_rect(rect, width, height)

        if uploadToCos:
            source = self.story.uploadImageToCos(source)

        if "contentList" not in self.board:
            self.board["contentList"] = []

        self.board["contentList"].append(
            {
                "image": source,
                "rect": rect,
                "caption": ""
            }
        )

        newCaption = ""
        if caption != None and (isinstance(caption, dict) or isinstance(caption, str)) and len(caption) > 0:
            newCaption = caption if isinstance(caption, dict) else {self.locale: caption}
        self.board["contentList"][-1]["caption"] = newCaption
        self.boardContentListScripts.append(Script(subscript=newCaption))

        if kwargs["magnify"] if "magnify" in kwargs else self.enableImageMagnify:
            self.board["contentList"][-1]["magnify"] = True

        border = kwargs["border"] if "border" in kwargs else self.enableImageMagnify
        if border:
            self.board["contentList"][-1]["border"] = kwargs["borderStyle"] if "borderStyle" in kwargs else self.story.styles["frame"]
        if not border:
            self.board["contentList"][-1].pop("border", None)

    def updateImage(self, pos, source, rect=[0, 0, 1, 1], autoFit=True, uploadToCos=True, caption=None, **kwargs):
        if pos < len(self.board["contentList"]) and pos >= 0:
            assert isinstance(rect, list) and len(rect) >= 4 and rect[2] > 0 and rect[3] > 0
            width, height = Story.getImageSize(next(iter(source.values()), None) if isinstance(source, dict) else source)
            assert width > 0 and height > 0

            if autoFit:
                rect = Page.fit_image_rect(rect, width, height)

            if uploadToCos:
                source = self.story.uploadImageToCos(source)

            self.board["contentList"][pos] = {
                    "image": update_object(self.board["contentList"][pos]["image"], source, self.locale),
                    "rect": rect,
                    "caption": ""
                }
            
            newCaption = ""
            if caption != None and (isinstance(caption, dict) or isinstance(caption, str)) and len(caption) > 0:
                newCaption = caption if isinstance(caption, dict) else {self.locale: caption}
            self.board["contentList"][pos]["caption"] = newCaption
            self.boardContentListScripts[pos].subscript = newCaption

            if kwargs["magnify"] if "magnify" in kwargs else self.enableImageMagnify:
                self.board["contentList"][pos]["magnify"] = True

            border = kwargs["border"] if "border" in kwargs else self.enableImageMagnify
            if border:
                self.board["contentList"][pos]["border"] = kwargs["borderStyle"] if "borderStyle" in kwargs else self.story.styles["frame"]
            if not border:
                self.board["contentList"][pos].pop("border", None)

    def removeImage(self, pos):
        if pos < len(self.board["contentList"]) and pos >= 0:
            self.board["contentList"].pop(pos)
            self.boardContentListScripts.pop(pos)

    def setVideo(self, source, autoFit=True, rect=[0.1, 0.1, 640, 360], **kwargs):
        assert len(rect) >= 4 and type(rect) is list

        if autoFit and self.actor == "boy":
            if rect[2] > 1.0:
                rect[0] = round(0.9 - rect[2]/0.9, 3)
            elif rect[2] < 1.0:
                rect[0] = 0.9 - rect[2]

        fontSize = kwargs["fontSize"] if "fontSize" in kwargs else "24px"
        if isinstance(fontSize, int):
            fontSize = str(fontSize) + "px"
        caption = kwargs["caption"] if "caption" in kwargs else ""
        self.board = {
            "content": {
                "caption": caption,
                "src": source
            },
            "rect": rect,
        }
        border = kwargs["border"] if "border" in kwargs else self.enableImageMagnify
        if border:
            self.board["content"]["border"] = kwargs["borderStyle"] if "borderStyle" in kwargs else self.story.styles["frame"]
        if "videoType" in kwargs:
            self.board["content"]["videoType"] = kwargs["videoType"].lower()

        if (isinstance("caption", str) and len(caption) > 0) or (isinstance(caption, dict) and len(next(iter(caption.values()), "") > 0)):
            fontSize = kwargs["fontSize"] if "fontSize" in kwargs else "24px"
            if isinstance(fontSize, int):
                fontSize = str(fontSize) + "px"
            self.board["content"]["fontSize"] = fontSize
            self.board["content"]["fontColor"] = kwargs["fontColor"] if "fontColor" in kwargs else "white"

        self.boardContentScript = Script(subscript=caption)

        self.hasImage = True

    def export(self, voiceOffset=0, pageId=0.0):
        outSubscripts = [subscript.export() for subscript in self.subscripts \
                         if subscript is not None and subscript.export() is not None]
        # only count those subscript-with-voice
        narrationOffset = len(outSubscripts)
        outSubscripts += [subscript.export() for subscript in (self.narrations["subscripts"] + [self.boardContentScript] + self.boardContentListScripts) \
                         if subscript is not None and subscript.export() is not None]

        tempInteractions = []
        if len(self.interactions) > 0:
            for interaction in self.interactions:
                updatedInteraction = interaction.merge(self.defaultInteraction) if self.defaultInteraction != None else interaction.copy()
                if self.hasImage:
                    updatedInteraction.popup = 4
                tempInteractions.append(updatedInteraction)
        elif self.defaultInteraction != None:
            defaultInteraction = self.defaultInteraction.merge(Interaction(type="motion"))
            tempInteractions.append(defaultInteraction)


        for interaction in self.narrations["interactions"]:
            tempNarration = interaction.copy()
            tempNarration.voice += narrationOffset
            tempInteractions.append(tempNarration)

        outInteractions = []
        for interaction in tempInteractions:
            if interaction.voice != None and interaction.voice > -1:
                interaction.voice += voiceOffset
            exported = interaction.export()
            if exported != None:
                outInteractions.append(exported)

        return {
            "voices": outSubscripts,
            "events": [Event(
                id=pageId, 
                scene=self.scene,
                board=self.board,
                objects=self.objects,
                interactions=outInteractions
                ).export()
            ],
        }


##### 黑板页面 #####
class BlackboardPage(BoardPage):
    def __init__(self, storyInstance, **kwargs):
        pageType = "blackboard"
        super().__init__(pageType, storyInstance, **kwargs)

        if "source" in kwargs and len(kwargs["source"]) > 0:
            self.setImage(**kwargs)

        if "actor" in kwargs and kwargs["actor"] in VISIBLE_ACTORS:
            self.setActor(**kwargs)

    def addNarration(self, text, narrator=None, alternativeText=None, audio=None, **kwargs):
        super().addNarration(text, narrator, alternativeText, audio, **kwargs)
        if kwargs.get("onPoster", None) != None or kwargs.get("onResult", None) != None:
            onPosterId = kwargs.get("onPoster", None) or kwargs.get("onResult", None)
            if onPosterId > len(self.board.get("contentList", [])) + (1): # onResult=1 is always reserved for board image
                print(f"{YELLOW}Warning{RESET}: onPoster/onResult is greater than available image count and is ignored.")
            else:
                self.narrations["interactions"][-1].onPoster = onPosterId

    def updateNarration(self, pos, text=None, narrator=None, alternativeText=None, **kwargs):
        super().updateNarration(pos, text, narrator, alternativeText)
        if kwargs.get("onPoster", None) != None or kwargs.get("onResult", None) != None:
            onPosterId = kwargs.get("onPoster", None) or kwargs.get("onResult", None)
            if onPosterId > len(self.board.get("contentList", [])) + (1): # onResult=1 is always reserved for board image
                print(f"{YELLOW}Warning{RESET}: onPoster/onResult is greater than available image count and is ignored.")
            self.narrations["interactions"][pos].onResult = None
            self.narrations["interactions"][pos].onPoster = onPosterId
        elif "onPoster" in kwargs or "onResult" in kwargs:
            self.narrations["interactions"][pos].onPoster = None
            self.narrations["interactions"][pos].onResult = None


##### 封面页面 #####
class CoverPage(BoardPage):
    def __init__(self, storyInstance, **kwargs):
        pageType = "cover"
        super().__init__(pageType, storyInstance, **kwargs)

        if kwargs.get("source", None) != None and len(kwargs["source"]) > 0:
            self.setImage(**kwargs)

    def setActor(self, **kwargs):
        pass
    
    def addDialog(self, **kwargs):
        pass

    def updateDialog(self, **kwargs):
        pass
    
    def removeDialog(self, **kwargs):
        pass


##### 教室页面 #####
class ClassroomPage(BoardPage):
    def __init__(self, storyInstance, **kwargs):
        pageType = "classroom"
        super().__init__(pageType, storyInstance, **kwargs)

        if "actor" in kwargs and kwargs["actor"] in VISIBLE_ACTORS:
            self.setActor(**kwargs)
    
    def addNarration(self, text, narrator=None, alternativeText=None, audio=None, **kwargs):
        super().addNarration(text, narrator, alternativeText, audio, **kwargs)
        if kwargs.get("onPoster", None) != None or kwargs.get("onResult", None) != None:
            onPosterId = kwargs.get("onPoster", None) or kwargs.get("onResult", None)
            if onPosterId > len(self.board.get("contentList", [])) + (1): # onResult=1 is always reserved for board image
                print(f"{YELLOW}Warning{RESET}: onPoster/onResult is greater than available image count and is ignored.")
            else:
                self.narrations["interactions"][-1].onPoster = onPosterId

    def updateNarration(self, pos, text=None, narrator=None, alternativeText=None, **kwargs):
        super().updateNarration(pos, text, narrator, alternativeText)
        if kwargs.get("onPoster", None) != None or kwargs.get("onResult", None) != None:
            onPosterId = kwargs.get("onPoster", None) or kwargs.get("onResult", None)
            if onPosterId > len(self.board.get("contentList", [])) + (1): # onResult=1 is always reserved for board image
                print(f"{YELLOW}Warning{RESET}: onPoster/onResult is greater than available image count and is ignored.")
            self.narrations["interactions"][pos].onResult = None
            self.narrations["interactions"][pos].onPoster = onPosterId
        elif "onPoster" in kwargs or "onResult" in kwargs:
            self.narrations["interactions"][pos].onPoster = None
            self.narrations["interactions"][pos].onResult = None
