import pandas as pd
from PIL import Image
from PIL.ExifTags import TAGS


class WorkerImages:
    image_paths = list()

    def get_exif_data(self):
        perm = pd.DataFrame()
        if self.image_paths:
            for image_path in self.image_paths:
                try:
                    image = Image.open(image_path)
                    exif_data = image.getexif()
                    _dict = dict()
                    for tag_id in exif_data:
                        # Gets the tag name, instead of human unreadable tag id
                        _dict[TAGS.get(tag_id, tag_id)] = exif_data.get(tag_id)
                    temp = pd.DataFrame(_dict, index=[0])
                except:
                    temp = pd.DataFrame()
                temp["image_path"] = image_path
                perm = pd.concat([perm, temp])
                return perm
