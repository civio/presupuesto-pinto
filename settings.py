# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

MAIN_ENTITY_LEVEL = 'municipio'
MAIN_ENTITY_NAME = 'Pinto'

BUDGET_LOADER = 'PintoBudgetLoader'
PAYMENTS_LOADER = 'PintoPaymentsLoader'

FEATURED_PROGRAMMES = ['9240', '4910', '4930']

OVERVIEW_INCOME_NODES = [
                          {
                            'nodes': [['11', '113']],
                            'label': 'Sobre bienes inmuebles de naturaleza urbana'
                          },
                          '13', '42', '45',
                          {
                            'nodes': [['11', '115']],
                            'label': 'Impuesto sobre vehículos de tracción mecánica'
                          },
                          {
                            'nodes': [['11', '116']],
                            'label': 'Impuesto sobre incremento del valor de los terrenos de naturaleza urbana'
                          },
                        ]
OVERVIEW_EXPENSE_NODES = ['45', '13', '92', '32', '23', '34', '33', '17']

# How aggresive should the Sankey diagram reorder the nodes. Default: 0.79 (Optional)
# Note: 0.5 usually leaves nodes ordered as defined. 0.95 sorts by size (decreasing).
OVERVIEW_RELAX_FACTOR = 0.5

# Show Payments section in menu & home options. Default: False.
SHOW_PAYMENTS           = True

# Show Tax Receipt section in menu & home options. Default: False.
SHOW_TAX_RECEIPT        = True

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
SHOW_COUNTIES_AND_TOWNS = False

# Show an extra tab with institutional breakdown. Default: True.
SHOW_INSTITUTIONAL_TAB  = False

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = False

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
#SHOW_ACTUAL = True

# Include financial income/expenditures in overview and global policy breakdowns. Default: False.
INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = False

# Search in entity names. Default: True.
SEARCH_ENTITIES = False

# Supported languages. Default: ('es', 'Castellano')
LANGUAGES = (
  ('es', 'Castellano'),
)

# Setup Data Source Budget link
DATA_SOURCE_BUDGET      = 'http://www.ayto-pinto.es/presupuestos-municipales-2015'

# Setup Data Source Population link
DATA_SOURCE_POPULATION  = 'http://www.ine.es/jaxiT3/Tabla.htm?t=2861'

# Setup Data Source Inflation link
DATA_SOURCE_INFLATION   = 'http://www.ine.es/jaxiT3/Tabla.htm?t=10019&L=0'

# Setup Main Entity Web Url
MAIN_ENTITY_WEB_URL     = 'http://www.ayto-pinto.es/'

# Setup Main Entity Legal Url (if empty we hide the link)
MAIN_ENTITY_LEGAL_URL   = 'http://www.ayto-pinto.es/web/ayuntamiento-de-pinto/aviso-legal'

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
COOKIES_URL             = 'http://www.ayto-pinto.es/web/ayuntamiento-de-pinto/aviso-legal'

# Allow overriding of default treemap color scheme
COLOR_SCALE = [ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf' ]
