# -*- coding: UTF-8 -*-
from budget_app.loaders import SimpleBudgetLoader
from budget_app.models import InstitutionalCategory


expenses_mapping = {
    'default': {'fc_code': 1, 'full_ec_code': 2, 'description': 3, 'forecast_amount': 4, 'actual_amount': 7},
    '2018': {'fc_code': 2, 'full_ec_code': 3, 'description': 4, 'forecast_amount': 8, 'actual_amount': 11},
    '2019': {'fc_code': 2, 'full_ec_code': 3, 'description': 4, 'forecast_amount': 8, 'actual_amount': 11},
    '2020': {'fc_code': 2, 'full_ec_code': 3, 'description': 4, 'forecast_amount': 8, 'actual_amount': 11},
    '2022': {'fc_code': 1, 'full_ec_code': 2, 'description': 3, 'forecast_amount': 4, 'actual_amount': 7},
}

income_mapping = {
    'default': {'full_ec_code': 0, 'description': 1, 'forecast_amount': 2, 'actual_amount': 5},
}

programme_mapping = {
    '1340': '1350',
    '2300': '2311',
    '3240': '3204',
}

programme_mapping_post_2015 = {
    '3201': '3200',
    '3202': '3200',
    '3203': '3200',
    '3205': '3200',
    '3207': '3200',
    '3343': '4930',
    '2313': '9240',
}


class BudgetCsvMapper:
    def __init__(self, year, is_expense):
        column_mapping = income_mapping

        if is_expense:
            column_mapping = expenses_mapping

        mapping = column_mapping.get(str(year))

        if not mapping:
            mapping = column_mapping.get('default')

        self.ic_code = mapping.get('ic_code')
        self.fc_code = mapping.get('fc_code')
        self.full_ec_code = mapping.get('full_ec_code')
        self.description = mapping.get('description')
        self.forecast_amount = mapping.get('forecast_amount')
        self.actual_amount = mapping.get('actual_amount')


class PintoBudgetLoader(SimpleBudgetLoader):

    # An artifact of the in2csv conversion of the original XLS files is a trailing '.0', which we remove here
    def clean(self, s):
        return s.split('.')[0]

    # Make year data available in the class and call super
    def load(self, entity, year, path, status):
        self.year = year
        SimpleBudgetLoader.load(self, entity, year, path, status)

    # Parse an input line into fields
    def parse_item(self, filename, line):
        # Type of data
        is_expense = (filename.find('gastos.csv') != -1)
        is_actual = (filename.find('/ejecucion_') != -1)

        # Mapper
        mapper = BudgetCsvMapper(self.year, is_expense)

        # Institutional code
        # All expenses go to the root node
        ic_code = '100'

        # Economic code
        # The economic codes sometimes miss the last two digits
        full_ec_code = line[mapper.full_ec_code].strip()
        full_ec_code = full_ec_code.ljust(5, '0')

        # Concepts are the firts three digits from the economic codes
        ec_code = full_ec_code[:3]

        # Item numbers are the last two digits from the economic codes (fourth and fifth digits)
        item_number = full_ec_code[-2:]

        # Description
        description = line[mapper.description].strip()
        description = self._spanish_titlecase(description)

        # Parse amount
        amount = line[mapper.actual_amount if is_actual else mapper.forecast_amount]
        amount = self._parse_amount(amount)

        if is_expense:
            # Functional code
            # We got 3-digit functional codes as input (mostly), so we make them all
            # into 4-digit ones by normalizing with extra zeroes
            fc_code = line[mapper.fc_code].strip()
            fc_code = self.clean(fc_code).rjust(3, '0').ljust(4, '0')

            # Programme codes have changed in 2015, due to new laws. Since the application expects a code-programme
            # mapping to be constant over time, we are forced to amend budget data prior to 2015.
            # See https://github.com/civio/presupuesto/wiki/La-clasificaci%C3%B3n-funcional-en-las-Entidades-Locales
            # For years before 2015 we check whether we need to amend the programme code
            # But data is confusing post-2015, so we clean it up also
            if int(self.year) < 2015:
                fc_code = programme_mapping.get(fc_code, fc_code)
            else:
                fc_code = programme_mapping_post_2015.get(fc_code, fc_code)

        # Income
        else:
            # Functional code
            # We don't have a functional code in income
            fc_code = None

        return {
            'is_expense': is_expense,
            'is_actual': is_actual,
            'fc_code': fc_code,
            'ec_code': ec_code,
            'ic_code': ic_code,
            'item_number': item_number,
            'description': description,
            'amount': amount
        }

    # We don't have an institutional breakdown, so we create just a catch-all organism.
    # (We then configure the theme so we don't show an institutional breakdown anywhere.)
    def load_institutional_classification(self, path, budget):
        InstitutionalCategory(institution='1',
                              section='10',
                              department='100',
                              description='Ayuntamiento de Pinto',
                              budget=budget).save()
