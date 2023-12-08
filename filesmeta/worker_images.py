# import pandas as pd
from PIL import Image
from PIL.ExifTags import TAGS


class WorkerImages:
    filepath = str()
    extensions = ["png", "jpg", "JPG", "PNG"]

    def get(self):
        # perm = pd.DataFrame()
        if self.filepath:
            # for image_path in self.filepath:
            _dict = dict()
            try:
                image = Image.open(self.filepath)
                exif_data = image.getexif()
                # _dict = dict()
                for tag_id in exif_data:
                    # Gets the tag name, instead of human unreadable tag id
                    _dict[TAGS.get(tag_id, tag_id)] = exif_data.get(tag_id)
                # temp = pd.DataFrame(_dict, index=[0])
            except:
                pass
                # _dict = dict()
                # temp = pd.DataFrame()
            # _dict["image_path"] = image_path
            # perm = pd.concat([perm, temp])
            return _dict
