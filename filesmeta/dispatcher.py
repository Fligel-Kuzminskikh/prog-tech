from filesmeta import worker_all, worker_images, worker_pdf, worker_ms_office
from re import findall
from os.path import join
from numpy import nan


class Dispatcher:

    special_workers = dict()
    path = str()
    name = str()

    def add_special_worker(self, special_worker):
        special_worker_extensions = special_worker.extensions
        for special_worker_extension in special_worker_extensions:
            self.special_workers[special_worker_extension] = special_worker

    worker_all = worker_all.WorkerAll()
    worker_images = worker_images.WorkerImages()
    worker_pdf = worker_pdf.WorkerPDF()
    worker_ms_office = worker_ms_office.WorkerMsOffice()

    def get_metadata_file(self):
        _dict = dict()
        _dict["name"] = self.name
        _dict["path"] = self.path
        if findall(string=self.name, pattern=r"((?<=\.)[A-Za-z]+$)"):
            _dict["extension"] = findall(string=self.name, pattern=r"((?<=\.)[A-Za-z]+$)")[0]
        else:
            _dict["extension"] = nan
        self.worker_all.filepath = join(self.path, self.name)
        self.add_special_worker(special_worker=self.worker_images)
        self.add_special_worker(special_worker=self.worker_pdf)
        self.add_special_worker(special_worker=self.worker_ms_office)
        general_metadata = self.worker_all.get()
        if _dict["extension"] in self.special_workers.keys():
            self.special_workers[_dict["extension"]].filepath = join(self.path, self.name)
            special_metadata = self.special_workers[_dict["extension"]].get()
            if special_metadata:
                general_metadata.update(special_metadata)
        _dict.update(general_metadata)
        return _dict
