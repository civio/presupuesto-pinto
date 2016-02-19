# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

MAIN_ENTITY_LEVEL = 'municipio'
MAIN_ENTITY_NAME = 'Pinto'

BUDGET_LOADER = 'PintoBudgetLoader'
PAYMENTS_LOADER = 'PintoPaymentsLoader'

FEATURED_PROGRAMMES = ['3340', '4910', '9120']

OVERVIEW_INCOME_NODES = [
                          { 'label': 'Impost sobre béns immobles (IBI)', 'nodes': [['11', '113'], ['11', '114']] },
                          { 'label': 'Resta d\'impostos locals propis (plusvàlua, IAE, circulació y ICIO)', 'nodes': [['11', '115'], ['11', '116'], '13', '29'] },
                          { 'label': 'Impostos cedits (IRPF, IVA i especials)', 'nodes': ['10', '21', '22'] },
                          { 'label': 'Taxes, preus públics i altres', 'nodes': ['30', '32', '33', '34', '35', '36', '38', '39'] },
                          { 'label': 'Transferències corrents de l\'estat', 'nodes': '42' },
                          { 'label': 'Transferències corrents de comunitats autònomes, ens locals i altres', 'nodes': ['41', '44', '45', '46', '47', '48', '49'] },
                          { 'label': 'Rendiments patrimonials', 'nodes': ['50', '52', '53', '54', '55'] },
                          { 'label': 'Ingressos de capital', 'nodes': ['60', '61', '68', '75', '79'] },
                          { 'label': 'Ingressos financers', 'nodes': ['84', '90', '94'] }
                        ]
OVERVIEW_EXPENSE_NODES =  [
                            { 'label': 'Deute', 'nodes': '01' },
                            { 'label': 'Seguretat i mobilitat ciutadana', 'nodes': '13' },
                            { 'label': 'Habitatge i urbanisme', 'nodes': ['15', '45'] },
                            { 'label': 'Serveis urbans i medi ambient', 'nodes': ['16', '17'] },
                            { 'label': 'Serveis socials i salut', 'nodes': ['23', '31'] },
                            { 'label': 'Educació', 'nodes': '32' },
                            { 'label': 'Cultura', 'nodes': '33' },
                            { 'label': 'Esports', 'nodes': '34' },
                            { 'label': 'Promoció econòmica i ocupació', 'nodes': ['43', ['49', '4931']] },
                            { 'label': 'Transport públic', 'nodes': '44' },
                            { 'label': 'Òrgans de govern', 'nodes': '91' },
                            { 'label': 'Transferències a altres administracions', 'nodes': '94' },
                            { 'label': 'Serveis de caràcter general i administració', 'nodes': ['21', '92', '93', ['49', '4911']] }
                          ]

# How aggresive should the Sankey diagram reorder the nodes. Default: 0.79 (Optional)
# Note: 0.5 usually leaves nodes ordered as defined. 0.95 sorts by size (decreasing).
OVERVIEW_RELAX_FACTOR = 0.5

# Show Payments section in menu & home options. Default: False.
SHOW_PAYMENTS           = False

# Show Tax Receipt section in menu & home options. Default: False.
SHOW_TAX_RECEIPT        = False

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
SHOW_COUNTIES_AND_TOWNS = False

# Show an extra tab with institutional breakdown. Default: True.
SHOW_INSTITUTIONAL_TAB  = True

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
MAIN_ENTITY_LEGAL_URL   = 'http://ajuntament.barcelona.cat/es/aviso-legal'

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
COOKIES_URL             = 'http://ajuntament.barcelona.cat/es/aviso-legal'

# Allow overriding of default treemap color scheme
COLOR_SCALE = [ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf' ]
