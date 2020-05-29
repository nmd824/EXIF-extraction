from PIL import Image
from PIL.ExifTags import TAGS
import os

directory = ""

entries = os.scandir("")

for entry in entries:
    if "mp4" in entry.name:
        os.remove(directory+entry.name)
    elif entry.name.startswith("."):
        continue
    else:
        image = Image.open(directory+entry.name)
        exifdata = image.getexif()

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            if tag is not "DateTimeOriginal":
                continue
            else:
                data = exifdata.get(tag_id)
                if isinstance(data, bytes):
                    data = data.decode()
                year = int(data[0:4])
                if year < 2015:
                    os.remove(directory+entry.name)
