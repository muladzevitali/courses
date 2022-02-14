import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    def __init__(self, file_path):
        self.data = dict()
        with open(file_path, mode='r', encoding='utf-8') as input_stream:
            self.data = json.load(input_stream)

        @property
        def parsed_data():
            return self.data


class XMLDataExtractor:
    def __init__(self, file_path):
        self.tree = etree.parse(file_path)

    @property
    def parsed_data(self):
        return self.tree


def data_extraction_factory(file_path):
    if file_path.endswith("json"):
        extractor = JSONDataExtractor
    elif file_path.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(file_path))
    return extractor(file_path)


def extract_data_from(file_path):
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(file_path)
    except ValueError:
        print('File not supported')

    return factory_obj
