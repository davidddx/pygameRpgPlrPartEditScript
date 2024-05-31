from PIL import Image
import os

DIRECTION_IDS = {
        "Back": 0,
        "BackRight": 1,
        "BackLeft": 2,
        "Front": 3,
        "FrontLeft": 4,
        "FrontRight": 5,
        "Left": 6,
        "Right": 7,
        }

def getImageFacingPath() -> list:
    validDirectionNames = ["Back", "BackRight", "BackLeft", "Front", "FrontLeft", "FrontRight", "Left", "Right"]
    partsDir = os.path.join(os.getcwd(), "Parts")
    directionDirs = []
    for folderName in os.listdir(partsDir):
        if folderName == "__pycache__":
            continue
        if not folderName in validDirectionNames:
            continue
        directionDirs.append(os.path.join(partsDir, folderName))

    return directionDirs

def getPartsPath(direction_path: str) -> list:
    validPartNames = ["Hair"]
    partPaths = []
    for folderName in os.listdir(direction_path):
        if folderName == "__pycache__" or folderName not in validPartNames:
            continue
        partPaths.append(os.path.join(direction_path, folderName, "0"))
    return partPaths

def makeNewColorDirectories(direction_paths : list[str]):
    armsColorIDs = [
            (238, 195, 154, 255),
            (217, 160, 102, 255),
            (143, 86, 59, 255),
            (75, 46, 33, 255),
            (178, 94, 54, 255),
            ]
    headColorIDs = armsColorIDs
    shirtColorIDs = [
            (172, 50, 50, 255),
            (0, 0, 0, 255),
            (99, 155, 255, 255),
            (47, 155, 53, 255),
            (167, 173, 20, 255),
            (100, 20, 173, 255),
            (226, 157, 187, 255),
            (255, 255, 255, 255),
            (202, 133, 26, 255),
            ]
    pantsColorIDs = [
            (99, 155, 255, 255),
            (172, 50, 50, 255),
            (0, 0, 0, 255),
            (47, 155, 53, 255),
            (167, 173, 20, 255),
            (100, 20, 173, 255),
            (226, 157, 187, 255),
            (255, 255, 255, 255),
            (202, 133, 26, 255),
            ]
    feetColorIDs = shirtColorIDs
    eyesColorIDs = [
            (102, 57, 49, 255),
            (0, 0, 0, 255),
            (135, 29, 29, 255),
            (94, 91, 195, 255),
            (55, 109, 82, 255),
            (128, 125, 69, 255),
            (118, 66, 138, 255),
            (210, 215, 211, 255),
            ]
    eyebrowsColorIDs = eyesColorIDs
    validPartNames = ["Arms", "Feet", "Pants", "Head", "Eyes", "Eyebrows", "Shirt"]

    for direction in direction_paths:
        print(os.listdir(direction))
        for partName in os.listdir(direction):
            print(f"{partName=}")
            if partName == "__pycache__" or partName not in validPartNames:
                continue
            partDirs = []
            currentPath = os.path.join(direction, partName)
            colorIDs = None
            match partName:
                case "Arms":
                    colorIDs = armsColorIDs
                case "Feet":
                    colorIDs = feetColorIDs
                case "Pants":
                    colorIDs = pantsColorIDs
                case "Head":
                    colorIDs = headColorIDs
                case "Eyes":
                    colorIDs = eyesColorIDs
                case "Eyebrows":
                    colorIDs = eyebrowsColorIDs
                case "Shirt":
                    colorIDs = shirtColorIDs

                    
            for i in range(len(colorIDs)):
                newPath = os.path.join(currentPath, f"{i}")
                if not os.path.exists(newPath):
                    print(f"path {newPath=} does not exist. creating this directory...")
                    os.mkdir(path= newPath)
                baseDir = os.path.join(currentPath, f"{0}")
                targetDir = os.path.join(currentPath, f"{i}")
                baseColor = colorIDs[0]
                convertImagesToColor(base_dir= baseDir, rgb_color_final= colorIDs[i], id_current=i, base_color=baseColor, target_dir = targetDir)

def makeHairColorDirectories(direction_paths : list[str]):
    eyesColorIDs = [
            (0, 0, 0, 255),
            (102, 57, 49, 255),
            (135, 29, 29, 255),
            (94, 91, 195, 255),
            (55, 109, 82, 255),
            (128, 125, 69, 255),
            (118, 66, 138, 255),
            (210, 215, 211, 255),
            ]
    styleIDs = [0, 1, 2, 3, 4, 5, 6]
    eyebrowsColorIDs = eyesColorIDs
    hairColorIDs = eyesColorIDs
    validPartNames = ["Hair"]
    for direction in direction_paths:
        print(os.listdir(direction))
        for partName in os.listdir(direction):
            print(f"{partName=}")
            if partName == "__pycache__" or partName not in validPartNames:
                continue
            partDirs = []
            currentPath = os.path.join(direction, partName)
            colorIDs = None
            match partName:
                case "Hair":
                    colorIDs = hairColorIDs
            for styleIdx in range(len(styleIDs)):
                for colorIdx in range(len(colorIDs)):
                    newPath = os.path.join(currentPath, f"{colorIdx}")
                    if not os.path.exists(newPath):
                        print(f"path {newPath=} does not exist. creating this directory...")
                        os.mkdir(path= newPath)
                    baseDir = os.path.join(currentPath, f"{styleIdx}", f"{0}")
                    targetDir = os.path.join(currentPath, f"{styleIdx}", f"{colorIdx}")
                    baseColor = colorIDs[0]
                    #print(f"{baseDir=}")
                    #print(f"{targetDir=}")

                    convertImagesToColor(base_dir= baseDir, rgb_color_final= colorIDs[colorIdx], id_current=colorIdx, base_color=baseColor, target_dir = targetDir)
    
def convertImagesToColor(base_dir: str, rgb_color_final: tuple[int, int, int], id_current: int, base_color: tuple[int, int, int], target_dir: str): 
    
    if id_current == 0:
        return None
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"dir {target_dir} created")
        #return None 
    try:
        #print(f"{base_dir=}")
        #print(f"{target_dir=}")
        #print(f"{os.listdir(base_dir)=}")
        animationFrameModel = ["0.png", "1.png", "2.png", "3.png"]
        checkTargetDirFrames = []
        for fileName in os.listdir(target_dir):
            if fileName == "__pycache__":
                continue
            checkTargetDirFrames = []
        if checkTargetDirFrames.sort() == animationFrameModel:
            return None
        for fileName in os.listdir(base_dir):
            if fileName == "__pycache__":
                continue
            if fileName not in animationFrameModel:
                continue
            # print(fileName)
            convertImageToColor(image_path = os.path.join(base_dir, fileName), rgb_color_original= base_color, rgb_color_final = rgb_color_final, save_path
                                = os.path.join(target_dir, fileName))


    except Exception as e:
        print(f"Could not convert images to specified color for dir: \n{base_dir},\n {e}")
        print("exiting...")
        return None

def convertImageToColor(image_path: str, rgb_color_original: tuple[int, int, int], rgb_color_final: tuple[int, int, int], save_path: str):
    image = Image.open(image_path)
    pixelData = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            #print(pixelData[i,j])
            if rgb_color_original != pixelData[i, j]:
                continue
            pixelData[i, j] = rgb_color_final
    image.save(fp= save_path)

if __name__ == "__main__":
    print("running main...")

    imageFacingPath = getImageFacingPath()
    print(f"{imageFacingPath=}")
    makeHairColorDirectories(direction_paths= imageFacingPath)
    makeNewColorDirectories(direction_paths= imageFacingPath)
