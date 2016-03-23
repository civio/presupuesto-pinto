# -*- coding: UTF-8 -*-
from budget_app.loaders import PaymentsLoader
from budget_app.models import Budget

class PintoPaymentsLoader(PaymentsLoader):

    # Parse an input line into fields
    def parse_item(self, budget, line):

        programme_id = line[3].strip()[:2]

        # Convert 11 to 01 for Deuda Pública
        if programme_id == '11':
            programme_id = '01'

        # But what we want as area is the programme description
        programme = Budget.objects.get_all_descriptions(budget.entity)['functional'][programme_id]

        return {
            'area': programme,
            'programme': None,
            'fc_code': None,  # We don't try (yet) to have foreign keys to existing records
            'ec_code': None,
            'date': line[0].strip(),
            'contract_type': None,
            'payee': self._titlecase(line[6].strip()),
            'description': self._spanish_titlecase(line[7].strip()),
            'amount': self._read_english_number(line[1])
        }
