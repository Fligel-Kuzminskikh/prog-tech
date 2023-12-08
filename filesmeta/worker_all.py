from os.path import getsize, getctime, getmtime
from numpy import nan


class WorkerAll:
    filepath = str()

    def get(self):
        _dict = dict()
        if self.filepath:
            try:
                _dict["size_in_bytes"] = getsize(filename=self.filepath)
            except:
                _dict["size_in_gigabytes"] = nan
            try:
                _dict["date_created"] = getctime(filename=self.filepath)
            except:
                _dict["date_created"] = nan
            try:
                _dict["date_last_changed"] = getmtime(filename=self.filepath)
            except:
                _dict["date_last_changed"] = nan
        return _dict
