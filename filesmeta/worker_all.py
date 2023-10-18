from os.path import getsize, getctime, getmtime


class WorkerAll:
    filepath = None

    def get_size(self):
        return getsize(filename=self.filepath)/1000000000

    def get_time_creation(self):
        return getctime(filename=self.filepath)

    def get_time_modification(self):
        return getmtime(filename=self.filepath)
