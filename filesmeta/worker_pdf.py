import pikepdf
import pandas as pd

class WorkerPDF:
    pdf_paths = list()

    def get_pdf_meta_data(self):
        perm = pd.DataFrame()
        if self.pdf_paths:
            for pdf_path in self.pdf_paths:
                try:
                    pdf = pikepdf.Pdf.open(pdf_path)
                    pdf_docinfo = pdf.docinfo
                    _dict = dict()
                    for key, value in pdf_docinfo.items():
                        _dict[key] = str(value)
                    temp = pd.DataFrame(_dict, index=[0])
                except:
                    temp = pd.DataFrame()
                temp["pdf_path"] = pdf_path
                perm = pd.concat([perm, temp])
                return perm
