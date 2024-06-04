"""
Project data struct holder
"""
from datetime import datetime

from ownlib.class_person import Person

from loguru import logger

DATE_FIELD_SIZE: int = 15
AFTER_DATE_FIELD_PATTERN: str = ' - '
MESSAGE_OFFSET: int = 20


class WhatsAppMessage:
    """
    WhatsApp message data struct definition and methods holder
    """
    def __init__(self, _foreign_string: str = ''):
        """
        Init class WhatsAppMessage environment
        :param _foreign_string: Source string from WhatsApp export file
        """
        _default_sender: Person = Person('')

        self.sender_found: bool = False
        self.source = _foreign_string
        self.sender_field, self.sender_border = self.get_sender(self,
                                                                self.source)
        if self.sender_found:
            self.sender = Person(self.sender_field, names_order='fml')
            logger.debug("\n\t" + f"Set {self.sender=}")
        else:
            self.sender = _default_sender
            logger.debug("\n\t" + f"Sender data not found in {self.source=}")

        self.get_message_info(self)

        logger.debug(f"Sender fields: {self.sender.lastname} /\\"
                     f" {self.sender.firstname} /\\"
                     f" {self.sender.middlename}")
        logger.debug(f"Sender start position: {self.sender_border[0]}")
        logger.debug(f"Sender end position: {self.sender_border[1]}")

    @staticmethod
    def get_sender(self, buff: str):
        """
        Return name and position message author`s nickname in whole message string
        :param self:
        :param buff:    Message string
        :return:        Message`s author (str),
                        start:  first author`s field position
                        end:    last author`s field position
        """
        _start_shift = 3
        _end_shift = -1
        start = buff.find(' - ')
        end = buff.find(': ')
        if start > 0 and end > 0:
            start += _start_shift
            end += _end_shift
            self.sender_found = True
            _sender = buff[start: end + 1]
        # return _sender, [start, end]
        else:
            self.sender_found = False
            _sender = ''
        return _sender, [start, end]

    @staticmethod
    # TODO Изучить статические методы и корретное использование self ниже
    def get_message_info(self):
        """
        Parse message datetime and set status flag ['system', \
        'master', 'continuation']
        """
        self.master = False

        last_date_field_index = self.source.find(AFTER_DATE_FIELD_PATTERN) - 1
        datetime_field = self.source[:last_date_field_index]
        logger.debug(f"{datetime_field=}")

        try:
            self.message_datetime = datetime.strptime(datetime_field,
                                                      '%d.%m.%Y, %H:%M')
            logger.debug(f"{type(self.message_datetime)=}")
            logger.debug("%Y, '2020' year in date string format")
            self.master = True
        except ValueError:
            try:
                self.message_datetime = datetime.strptime(datetime_field,
                                                          '%d.%m.%y, %H:%M')
                logger.debug(f"{type(self.message_datetime)=}")
                logger.debug("%y, '20' year in date string format")
                self.master = True
            except ValueError:
                logger.debug("No datetime found in message string.")
                self.master = False

            except Exception as func_exc:
                logger.warning(f"[!] Second layer. Unusual exception:"
                               f"{func_exc.__class__}")
                raise

        except Exception as func_exc:
            logger.warning(f"[!] First layer. Unusual exception:"
                           f"{func_exc.__class__}")
            raise

        finally:
            if self.master:
                if len(self.sender.name):
                    self.status = 'message'
                    self.msg_start = self.sender_border[1] + 3
                else:
                    self.status = 'system'
                    self.msg_start = len(datetime_field) + len(AFTER_DATE_FIELD_PATTERN) + 1
            else:
                self.status = 'continuation'
                self.msg_start = 0

        self.message = self.source[self.msg_start:]
        logger.debug(f"{self.status=}")
