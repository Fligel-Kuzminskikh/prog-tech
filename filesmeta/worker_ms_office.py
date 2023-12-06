import pandas as pd
from docx import Document
from pptx import Presentation
from openpyxl import load_workbook


class WorkerMsOffice:
    docx_paths = list()
    xl_paths = list()
    pptx_paths = list()

    def get_metadata_docx(self):
        perm = pd.DataFrame()
        for docx_path in self.docx_paths:
            try:
                docx = Document(docx=docx_path)
                properties = docx.core_properties
                metadata = {}
                for directory in dir(properties):
                    if not directory.startswith('_'):
                        metadata[directory] = str(getattr(properties, directory))
                temp = pd.DataFrame(metadata, index=[0])
            except:
                temp = pd.DataFrame()
            temp["filepath"] = docx_path
            perm = pd.concat([perm, temp])
            return perm

    def get_metadata_xl(self):
        perm = pd.DataFrame()
        for xl_path in self.xl_paths:
            try:
                workbook = load_workbook(xl_path)
                metadata = {}
                for directory in dir(workbook.properties):
                    if not directory.startswith('_') and directory not in ["to_tree", "from_tree"]:
                        metadata[directory] = str(getattr(workbook.properties, directory))
                temp = pd.DataFrame(metadata, index=[0])
            except:
                temp = pd.DataFrame()
            temp["filepath"] = xl_path
            perm = pd.concat([perm, temp])
            return perm

    def get_metadata_pptx(self):
        perm = pd.DataFrame()
        for pptx_path in self.pptx_paths:
            try:
                pptx = Presentation(pptx=pptx_path)
                properties = pptx.core_properties
                metadata = {}
                for directory in dir(properties):
                    if not directory.startswith('_'):
                        metadata[directory] = str(getattr(properties, directory))
                temp = pd.DataFrame(metadata, index=[0])
            except:
                temp = pd.DataFrame()
            temp["filepath"] = pptx_path
            perm = pd.concat([perm, temp])
            return perm

    def get_metadata_ms_office(self):
        return pd.concat([self.get_metadata_xl(), self.get_metadata_docx(), self.get_metadata_pptx()])
