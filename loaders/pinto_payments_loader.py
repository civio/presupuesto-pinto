# -*- coding: UTF-8 -*-
from budget_app.loaders import PaymentsLoader

class PintoPaymentsLoader(PaymentsLoader):

    # Parse an input line into fields
    def parse_item(self, budget, line):
        return {
            'area': line[3].strip(),
            'programme': line[2].strip(),
            'fc_code': None,  # We don't try (yet) to have foreign keys to existing records
            'ec_code': None,
            'date': line[0].strip(),
            'contract_type': None,
            'payee': self._titlecase(line[6].strip()),
            'description': self._spanish_titlecase(line[7].strip()),
            'amount': self._read_english_number(line[1])
        }
