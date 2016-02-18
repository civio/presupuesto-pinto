# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

MAIN_ENTITY_LEVEL = 'municipio'
MAIN_ENTITY_NAME = 'Pinto'

BUDGET_LOADER = 'PintoBudgetLoader'
PAYMENTS_LOADER = 'PintoPaymentsLoader'

FEATURED_PROGRAMMES = ['1710', '3321', '3261', '1630', '2410', '3263', '3340', '3370', '3410', '4411', '9242']

OVERVIEW_INCOME_NODES = [['11', '113'], ['11', '114'], ['11', '115'], ['11', '116'], ['13', '130'], ['29', '290'], ['10', '100'], ['21', '210'], ['22', '220'], '42', '41', '44', '45', '46', '47', '48', '49']
OVERVIEW_EXPENSE_NODES = ['01', '13', '15', '45', '16', '17', '23', '31', '32', '33', '34', '43', ['49', '493'], '44', '91', '94', '21', '92', '93', ['49', '491']]

# Show an extra tab with institutional breakdown. Default: True.
SHOW_INSTITUTIONAL_TAB = True

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = False

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
#SHOW_ACTUAL = True

# Include financial income/expenditures in overview and global policy breakdowns. Default: False.
INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = True

# Search in entity names. Default: True.
SEARCH_ENTITIES = False

# Supported languages. Default: ('ca', 'Catal&agrave;')
LANGUAGES = (
  ('es-es', 'Castellano'),
)

# Allow overriding of default treemap color scheme
COLOR_SCALE = [ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf' ]

# Set the custom cookies url or leave it as empty string if default url is to be used
CUSTOM_COOKIES = ''
