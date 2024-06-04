"""Objects for parsing 1C XML files"""

# TODO FIX - can`t to find source from business import Company
# TODO Fix wrong ACCOUNT_ID in COMPANY_INFO

from typing import (NamedTuple, Union)
import re

from dataclasses import dataclass
from datetime import date

from xml.etree import ElementTree

from ownlib.class_person import (PersonNames, Person)

from loguru import logger


DATA_PATH = 'outside_data/'
CARDS_PAYMENT_DATAFILE = 'Логистика.xml'
# CARDS_PAYMENT_DATAFILE = 'Экспотрейд.xml'
PAYLOAD_SOURCE = DATA_PATH + CARDS_PAYMENT_DATAFILE

PAYLOAD_GROUP = dict(PAYLOAD='ЗачислениеЗарплаты',
                     PAYLOAD_KIND='ВидЗачисления',
                     INCOME_KIND='КодВидаДохода',
                     CONTROL='КонтрольныеСуммы')

REGISTRY_SCHEMA = dict(XML_SCHEMA='{http://v8.1c.ru/edi/edi_stnd/109}',
                       TYPE='{http://www.w3.org/2001/XMLSchema-instance}type',
                       SOURCE_DATE='ДатаФормирования',
                       CONTRACT_ID='НомерДоговора',
                       CONTRACT_DATE='ДатаДоговора',
                       SOURCE_ID='ИдПервичногоДокумента',
                       ID='НомерРеестра',
                       DATE='ДатаРеестра')

COMPANY_SCHEMA = dict(FULLNAME='НаименованиеОрганизации',
                      FEE_ID='ИНН',
                      ACCOUNT_ID='РасчетныйСчетОрганизации',
                      BANK_ID='БИК')

EMPLOYEE_TRANSACTION = dict(LASTNAME='Фамилия',
                            FIRSTNAME='Имя',
                            SURNAME='Отчество',
                            BANK='ОтделениеБанка',
                            ACCOUNT='ЛицевойСчет',
                            AMOUNT='Сумма',
                            CURRENCY_ID='КодВалюты')

# TMP - humanizing transfer record indexes.
REGISTRY = 0
PERSONA = 1
AMOUNT = 2


@dataclass
class TagInfo:
    """XML tag string mining class

    Attributes:
        tag: str - original XML element.tag
        name: str - tag name
        path: str - tag path

    Examples:
        TagInfo('{your_element_path}your_element_name')"""
    def __init__(self, tag):
        self.tag: str = tag
        # TODO Have 2 drop slash before "s" at the line below?
        self.name: str = re.findall(r'[^{/D/s?}]\w+', tag)[-1]
        self.path: str = self.tag.rsplit(self.name)[0]


class EmployeePayload(NamedTuple):
    lastname: str
    firstname: str
    middlename: str
    bank_office_id: str
    account_id: str
    amount: float
    currency_id: str


class Record(NamedTuple):
    """
    Data record struct:

    Attributes:
        label: str - record label
        value: str - record value
    """
    label: str
    value: Union[str, int, float]


class RegistryData(NamedTuple):
    """
    Transfer registry data

    Attributes:
        registry_type: str - Registry type code
        source_date: str -Registry primary making date
        contract_id: str - Contract ID
        contract_date: str - Contract start date
        company_name: str - Full company name
        company_fee_id: str - Company fee ID
        company_account: str - Account ID (number)
        company_bank_id: str - Bank ID
        registry_source_id: str - Parent document ID
        registry_id: str - Transfer registry ID
        registry_date: str - Registry complete state date
    """
    registry_type: str
    source_date: str
    contract_id: str
    contract_date: str
    company_name: str
    company_fee_id: str
    company_account: str
    company_bank_id: str
    registry_source_id: str
    registry_id: str
    registry_date: str


# TODO Thought about the function placing. Have I define it here?
def unknown_element_found(elements, current: dict) -> Union[list, None]:
    """
    Try to found xml elements not in current
    :param elements: list - elements checking list
    :param current: dict - known for current project element list
    :return: founded element list or None in another case
    """
    _new_elements = []
    _current_data = current.values()
    for element in elements:
        try:
            _tag_name = TagInfo(element.tag).name
            if _tag_name not in _current_data:
                logger.warning(f"[!] Find new element: <{element}>")
                _new_elements.append(element)
        except Exception as ex:
            logger.error(f"[!!!] Unknown exception in checking <{elements=}>")
            raise ex
    return _new_elements if _new_elements else None
