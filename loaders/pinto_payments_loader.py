# -*- coding: UTF-8 -*-
from budget_app.loaders import PaymentsLoader
from budget_app.models import Budget

payments_mapping = {
    'default': {'fc_code': 3, 'date': 0, 'payee': 6, 'description': 7, 'amount': 1},
    '2018': {'fc_code': 2, 'date': 0, 'payee': 6, 'description': 7, 'amount': 1},
}


class PaymentsCsvMapper:
    def __init__(self, year):
        mapping = payments_mapping.get(str(year))

        if not mapping:
            mapping = payments_mapping.get('default')

        self.fc_code = mapping.get('fc_code')
        self.date = mapping.get('date')
        self.payee = mapping.get('payee')
        self.description = mapping.get('description')
        self.amount = mapping.get('amount')


class PintoPaymentsLoader(PaymentsLoader):
    # Parse an input line into fields
    def parse_item(self, budget, line):
        # Mapper
        mapper = PaymentsCsvMapper(budget.year)

        # We got the functional codes
        fc_code = line[mapper.fc_code].strip()

        # In 2018 we don't get the functional code in all the data, so we use
        # the full budget heading
        if budget.year == 2018:
            fc_code = fc_code[7:10]

        # We got some 2- digit codes or even empty ones, so we normalize them
        fc_code = fc_code.rjust(3, '0')

        # First two digits of the programme make the policy id
        policy_id = fc_code[:2]

        # What we want as area is the policy description
        if policy_id == '00':
            policy = 'Otros'
        else:
            policy = Budget.objects.get_all_descriptions(budget.entity)['functional'][policy_id]

        # We got an iso date or nothing
        date = line[mapper.date] if mapper.date else None

        # Payee data
        payee = line[mapper.payee].strip()

        # We got some anonymized entries
        anonymized = False
        anonymized = (True if payee == 'Protegido(*)' else anonymized)

        # Description
        description = line[mapper.description].strip()

        # Amount
        amount = line[mapper.amount]
        amount = self._read_english_number(amount)

        return {
            'area': policy,
            'programme': None,
            'ic_code': None,
            'fc_code': None,
            'ec_code': None,
            'date': date,
            'payee': payee,
            'anonymized': anonymized,
            'description': description,
            'amount': amount
        }
