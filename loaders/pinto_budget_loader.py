# -*- coding: UTF-8 -*-
from budget_app.models import *
from budget_app.loaders import SimpleBudgetLoader
from decimal import *
import csv
import os
import re

class PintoBudgetLoader(SimpleBudgetLoader):

    # An artifact of the in2csv conversion of the original XLS files is a trailing '.0', which we remove here
    def clean(self, s):
        return s.split('.')[0]

    def parse_item(self, filename, line):
        # Programme codes have changed in 2015, due to new laws. Since the application expects a code-programme
        # mapping to be constant over time, we are forced to amend budget data prior to 2015.
        # See https://github.com/dcabo/presupuestos-aragon/wiki/La-clasificaci%C3%B3n-funcional-en-las-Entidades-Locales
        programme_mapping = {
            '1340': '1350',
            '2300': '2311',
            '3240': '3204',
        }
        # Data is confusing post-2015, so we clean it up also
        programme_mapping_post_2015 = {
            '3201': '3200',
            '3202': '3200',
            '3203': '3200',
            '3205': '3200',
            '3207': '3200',
            '3343': '4930',
            '2313': '9240',
        }

        is_expense = (filename.find('gastos.csv')!=-1)
        is_actual = (filename.find('/ejecucion_')!=-1)
        if is_expense:
            # We got 3-digit functional codes as input (mostly), so we make them all
            # into 4-digit ones by adding an extra zero, i.e. left-justify them adding a 0.
            fc_code = line[1].rjust(3, '0').ljust(4, '0')

            print fc_code

            # For years before 2015 we check whether we need to amend the programme code
            year = re.search('municipio/(\d+)/', filename).group(1)
            if int(year) < 2015:
                fc_code = programme_mapping.get(fc_code, fc_code)
            else:
                fc_code = programme_mapping_post_2015.get(fc_code, fc_code)

            return {
                'is_expense': True,
                'is_actual': is_actual,
                'fc_code': fc_code,
                'ec_code': line[2][:-2],        # First three digits (everything but last two)
                'ic_code': '100',
                'item_number': line[2][-2:],    # Last two digits
                'description': self._spanish_titlecase(line[3].strip()),
                'amount': self._parse_amount(line[7 if is_actual else 4])
            }

        else:
            return {
                'is_expense': False,
                'is_actual': is_actual,
                'ec_code': line[0][:-2],        # First three digits (everything but last two)
                'ic_code': '100',               # All income goes to the root node
                'item_number': line[0][-2:],    # Last two digits
                'description': self._spanish_titlecase(line[1].strip()),
                'amount': self._parse_amount(line[5 if is_actual else 2])
            }

    # We don't have an institutional breakdown in Torrelodones, so we create just a catch-all organism.
    # (We then configure the theme so we don't show an institutional breakdown anywhere.)
    def load_institutional_classification(self, path, budget):
        InstitutionalCategory(  institution='1',
                                section='10',
                                department='100',
                                description='Ayuntamiento de Pinto',
                                budget=budget).save()
