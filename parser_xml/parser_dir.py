from .parser_xml import ParserXml
import os
# from parser_xlsx_kart import Excel2json
# from parser_osv_xlsx import ParserOsv


class ParserDir:
    def __init__(self, folder_name):
        self.xml_files = []
        self.folder_name = folder_name

    def find_process_xml(self):
        for file in os.listdir(self.folder_name):
            test = ParserXml(file)
            test.process_xml()
        return