import re

REGEX_PARTTERN_ONLY_NUMBERS = "[^0-9]+"
NO_FRIST_AREA_CODE_NUMBER = ['0', '1']
NO_FRIST_EXCHANGE_CODE_NUMBER = ['0', '1']


class PhoneNumber:

    def __init__(self, number):
        number_clear = re.sub(REGEX_PARTTERN_ONLY_NUMBERS, "", number)

        if len(number_clear) == 11 and number_clear[0] == '1':
            number_clear = number_clear[1:]

        if len(number_clear) != 10:
            raise ValueError("Wrong length.")

        if number_clear[0] in NO_FRIST_AREA_CODE_NUMBER or number_clear[3] in NO_FRIST_EXCHANGE_CODE_NUMBER:
            raise ValueError("Wrong numbers")

        self.number = number_clear

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        exchange_code = self.number[3:6]
        subscriber_number = self.number[6:]

        pretty_number = "({area_code}) {exchange_code}-{subscriber_number}".format(
            area_code=self.area_code, exchange_code=exchange_code, subscriber_number=subscriber_number)
        return pretty_number
