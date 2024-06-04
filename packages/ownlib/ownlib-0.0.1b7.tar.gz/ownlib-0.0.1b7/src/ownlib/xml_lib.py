
# TODO Though about -> class style code refactoring

from pprint import pprint
from settings.xml_settings import *
#
#
# def get_names(attr_list: list) -> list:
#     return [TagInfo(note.tag).name for note in attr_list]
#
#
# def get_attributes(element):
#     attributes = [_ for _ in element]
#     return attributes


def xml_element_parsed(record: ElementTree.Element,
                       schema_pattern: str = REGISTRY_SCHEMA['XML_SCHEMA']) -> tuple[Record, ...]:
    """
    Gets parsed ElementTree.Element attributes as tuple[NamedTuple, ...]

    :param record: ElementTree.Element: transfer data according to the XML schema of "SberBank" (Russia) standard.
    :param schema_pattern: str: XML schema`s URL
    :return tuple[Record, ...] - transfer data
    """
    _result_list = []
    for attrib in record:
        label = attrib.tag.removeprefix(schema_pattern)
        value = attrib.text
        _result_list.append(Record(label, value))

    return tuple(_result_list)


def get_xml_root(xml_filename: str) -> ElementTree.Element:
    tree = ElementTree.parse(xml_filename)
    xml_data_root = tree.getroot()

    return xml_data_root


def get_registry_data(xml_root: ElementTree.Element) -> RegistryData:
    """
    Get XML.Element attributes
    :param xml_root: Element.Element - XML records root
    :return: RegistryData - Registry data fields
    """
    # Fill RegistryData class object via XML attributes and were field names
    _registry = RegistryData(registry_type=xml_root.get(REGISTRY_SCHEMA['TYPE'], ''),
                             source_date=xml_root.get(REGISTRY_SCHEMA['SOURCE_DATE'], ''),
                             contract_id=xml_root.get(REGISTRY_SCHEMA['CONTRACT_ID'], ''),
                             contract_date=xml_root.get(REGISTRY_SCHEMA['CONTRACT_DATE'], ''),
                             company_name=xml_root.get(COMPANY_SCHEMA['FULLNAME'], ''),
                             company_fee_id=xml_root.get(COMPANY_SCHEMA['FEE_ID'], ''),
                             company_account=xml_root.get(COMPANY_SCHEMA['ACCOUNT_ID'], ''),
                             company_bank_id=xml_root.get(COMPANY_SCHEMA['BANK_ID'], ''),
                             registry_source_id=xml_root.get(REGISTRY_SCHEMA['SOURCE_ID'], ''),
                             registry_id=xml_root.get(REGISTRY_SCHEMA['ID'], ''),
                             registry_date=xml_root.get(REGISTRY_SCHEMA['DATE'], '')
                             )
    return _registry


def xml_registry_file_as_tuple(xml_file: str) -> tuple[RegistryData, tuple[tuple[Record, ...], ...]]:
    """
    Get parsed SBRF personal card payment transfers data from XML file
    :param xml_file: str - XML registry data file path
    :return: tuple - (RegistryData, ((Record, ...), ...)) - Registry and transfers data
    """

    _root = get_xml_root(xml_file)
    _root_elements = _root.findall('./')
    _registry = get_registry_data(_root)

    # TODO descript all XML Elements group processing
    _registry_transfers = _root_elements[0]

    _transfers = []
    for xml_transfer_elements in _registry_transfers:
        _transfer_data = xml_element_parsed(xml_transfer_elements)
        _transfers.append(_transfer_data)

    return _registry, tuple(_transfers)


if __name__ == '__main__':
    xml_data_source = input('Enter XML file path:>')
    parsed_xml_registry = xml_registry_file_as_tuple(xml_data_source)
    ...
    pprint(parsed_xml_registry)
