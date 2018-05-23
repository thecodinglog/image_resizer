import PIL.Image
import json

im = PIL.Image.open('blog_icon.png')
print(im.size)

with open("asset_info.json") as f:
    jsonData = json.load(f)
    for item in jsonData["list"]:
        lSize = (item["size"][0], item["size"][1])
        lFilename = (item["filename"].replace("{x}", str(item["size"][0])).replace("{y}", str(item["size"][1])))

        im2 = im.resize(lSize, PIL.Image.ANTIALIAS)
        im2.save("result/" + lFilename, quality=100)
