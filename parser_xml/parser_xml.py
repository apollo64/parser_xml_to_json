import xmltodict
import json
import os


class ParserXml:
    def __init__(self, file_name):
        self.file_name = file_name
        self.full_path = None
        self.my_xml_data = None

    def taking_out(self):
        self.full_path = os.path.abspath(os.path.join("input", self.file_name))
        with open(self.full_path) as xml_file:
            mxd = xmltodict.parse(xml_file.read())
            xml_file.close()
        self.my_xml_data = mxd
        return

    def convert_save(self):
        name, ext = os.path.splitext(self.file_name)
        mxd = self.my_xml_data
        json_data = json.dumps(mxd, indent=4, sort_keys=False,
                               ensure_ascii=False)
        f = open(f'output/{name}.json', 'w')
        f.write(json_data)
        f.close()
        return

    def process_xml(self):
        try:
            self.taking_out()
            self.convert_save()
        except Exception as e:
            print(f'Error of {e}')

        return

#
# file_name = 'ОСВ ТД Лакомка с 01.01.2017 по 31.01.2017.xml'
# name, ext = os.path.splitext(file_name)
#
# full_file = os.path.abspath(os.path.join("xml", file_name))
#
# with open(full_file) as xml_file:
#     my_dict = xmltodict.parse(xml_file.read())
#
# xml_file.close()
# # json_data = json.dumps(my_dict, indent=4, sort_keys=True) # original
# json_data = json.dumps(my_dict, indent=4, sort_keys=False,
#                        ensure_ascii=False)  # best. sort_keys False always
#
# f = open(f'output/{name}.json', 'w')
# f.write(json_data)
# f.close()
