import pikepdf
# import pandas as pd


class WorkerPDF:
    filepath = str()
    extensions = ["pdf"]

    def get(self):
        # perm = pd.DataFrame()
        if self.filepath:
            # for pdf_path in self.pdf_paths:
            _dict = dict()
            try:
                pdf = pikepdf.Pdf.open(self.filepath)
                pdf_docinfo = pdf.docinfo
                for key, value in pdf_docinfo.items():
                    _dict[key] = str(value)
                # temp = pd.DataFrame(_dict, index=[0])
            except:
                pass
                # temp = pd.DataFrame()
            # temp["pdf_path"] = pdf_path
            # _dict["pdf_path"] = pdf_path
            # perm = pd.concat([perm, temp])
            return _dict
