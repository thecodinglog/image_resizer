import PIL.Image
import json

with open("settings.json") as f:
    jsonData = json.load(f)

    im = PIL.Image.open(jsonData["input"])

    for item in jsonData["output"]:
        lSize = (item["size"][0], item["size"][1])
        lFilename = (item["filename"].replace("{x}", str(item["size"][0])).replace("{y}", str(item["size"][1])))

        im2 = im.resize(lSize, PIL.Image.ANTIALIAS)
        im2.save("result/" + lFilename, quality=100)
