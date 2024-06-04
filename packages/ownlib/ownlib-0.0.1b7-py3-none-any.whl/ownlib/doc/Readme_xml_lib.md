### XML lib library usage

`
if __name__ == '__main__':
    from xml_parse import xml_registry_file_as_tuple

    FILENAME = 2
    DATA_SOURCE_DIR = 'outside_data'
    PATH_PATTERN = '*.xml'
    FULL_DATA_PATH_PATTERN = '/'.join((DATA_SOURCE_DIR, PATH_PATTERN))

    while True:
        data_filename = chosen_filename(FULL_DATA_PATH_PATTERN)
        if data_filename is not None:
            parsed_transfers = xml_registry_file_as_tuple('/'.join((DATA_SOURCE_DIR, data_filename)))
            pprint(parsed_transfers, compact=True)
        else:
            logger.info(f"Parsing exit.")
            break
`
