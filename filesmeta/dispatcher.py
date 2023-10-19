from filesmeta import worker_all, worker_images, worker_pdf, worker_ms_office


class Dispatcher:

    worker_all = worker_all.WorkerAll()
    worker_images = worker_images.WorkerImages()
    worker_pdf = worker_pdf.WorkerPDF()
    worker_ms_office = worker_ms_office.WorkerMsOffice()
