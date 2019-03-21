# -*- coding: UTF-8 -*-
from budget_app.loaders import PaymentsLoader
from budget_app.models import Budget

import re

payments_mapping = {
    'default': {'fc_code': 3, 'date': 0, 'payee': 6, 'description': 7, 'amount': 1},
    '2018': {'fc_code': 3, 'date': 1, 'payee': 6, 'description': 7, 'amount': 4},
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

        # In 2018 we don't get the functional code separately, so we use
        # the full budget heading
        if budget.year == 2018 and fc_code:
            fc_code = fc_code.split()[2]

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

        # we need to ensure we're using an Unicode string so it handles
        # the accented characters correctly
        payee = unicode(payee, encoding='utf8')

        # ensure consistent values
        payee = 'ANONIMIZADO' if (payee == 'Protegido(*)' or payee == '*Protegido*') else payee
        payee = 'ACREEDORES VARIOS' if payee == '' else payee

        # normalize data
        payee = payee.replace(', ', ' ').replace(',', ' ')
        payee = payee.replace('  ', ' ').replace(',', ' ')
        payee = re.sub(r'\s\s+', ' ', payee)
        payee = re.sub(r' SL$', ' S.L.', payee)
        payee = re.sub(r' S L$', ' S.L.', payee)
        payee = re.sub(r' S\.L$', ' S.L.', payee)
        payee = re.sub(r' SLL$', ' S.L.L.', payee)
        payee = re.sub(r' SLU$', ' S.L.U.', payee)
        payee = re.sub(r' SA$', ' S.A.', payee)
        payee = re.sub(r' S\.A$', ' S.A.', payee)
        payee = re.sub(r' S A$', ' S.A.', payee)
        payee = re.sub(r' SAU$', ' S.A.U.', payee)
        payee = re.sub(r' S\.A\.U$', ' S.A.U.', payee)
        payee = re.sub('ASOCICION', 'ASOCIACION', payee)
        payee = re.sub('ASSOCIACION', 'ASOCIACION', payee)
        payee = re.sub(u'ASOCIACIÓN', 'ASOCIACION', payee)
        payee = re.sub(r'^ALMENDRO MARTINEZ ANGEL LUIS$', 'ALMENDRO MARTINEZ ANGEL LUIS - ESCUELA AKIRE', payee)
        payee = re.sub(r'^AMANTARA SDAD.COOP.MAD$', 'AMANTARA S.COOP.MAD.', payee)
        payee = re.sub(ur'^AMANTARA SDAD.COOP.MADRILEÑA$', 'AMANTARA S.COOP.MAD.', payee)
        payee = re.sub(r'^ARCONTE ARQUITECTURA Y CONSULTORIA TECNICA S R L$', 'ARCONTE ARQUITECTURA Y CONSULTORIA TECNICA S.L.P.', payee)
        payee = re.sub(r'^ASAC COMUNICACIONES$', 'ASAC COMUNICACIONES S.L.', payee)
        payee = re.sub(r'^AUTOCARES JULIA$', 'AUTOCARES JULIA S.A.', payee)
        payee = re.sub(r'^ARJE FORMACION S\.L\.$', 'ARJE FORMACION S.L.U.', payee)
        payee = re.sub(r'^ASERPINTO S\.A\.$', 'ASERPINTO S.A.U.', payee)
        payee = re.sub(r'^ASOCIACION CASA CASTILLA LA MANCHA$', 'ASOCIACION CASA REGIONAL CASTILLA LA MANCHA', payee)
        payee = re.sub(r'^ASOCIACION THE CROSS BORDER PROJECT S\.L\.$', 'ASOCIACION THE CROSS BORDER PROJECT', payee)
        payee = re.sub(r'^AUTOSAE S A RENAULT$', 'AUTOSAE S.A.U. --RENAULT--', payee)
        payee = re.sub(r'^BALERDI TORRES IMANOL$', 'ABALERDI TORRES IMANOL - ARAP', payee)
        payee = re.sub(r'^BENORT SOCIAL SL PROYECTOS SOCIALES$', 'BENORT SOCIAL S.L. PROYECTOS SOCIALES', payee)
        payee = re.sub(r'^BENORT SOCIAL S\.L\.PROYECTOS SOCIALES$', 'BENORT SOCIAL S.L. PROYECTOS SOCIALES', payee)
        payee = re.sub(r'^CAMACHO VELAYOS MARIA JESUS$', 'CAMACHO VELAYOS MARIA JESUS - SURBIKE', payee)
        payee = re.sub(r'^CANAL DE ISABEL II$', 'CANAL DE ISABEL II S.A.', payee)
        payee = re.sub(r'^CLUB DEPORTIVO ELEMENTAL FUTSAL PINTO$', 'CLUB DEPORTIVO ELEMENTAL FUTSALA PINTO', payee)
        payee = re.sub(r'^COMUNIDAD DE MADRID-CONSEJ\. PRESIDENCIA- PUBL\.OFICIALES$', 'COMUNIDAD DE MADRID-CONSEJ. PRESIDENCIA-PUBLICACION OFICIAL EN BOCM', payee)
        payee = re.sub(r'^DUAL IBERICA S\.A\.U\.$', 'DUAL IBERICA RIESGOS PROFESIONALES S.A.U.', payee)
        payee = re.sub(r'^EDUCASERVI SL - ESCUELA INFANTIL PIMPOLLITOS$', 'EDUCASERVI S.L. - ESCUELA INFANTIL PIMPOLLITOS', payee)
        payee = re.sub(r'^EL CORTES INGLES S\.A\.$', 'EL CORTE INGLES S.A.', payee)
        payee = re.sub(r'^EMERGALIA S\.L\.$', 'EMERGALIA S.L.U.', payee)
        payee = re.sub(r'^EMERGENCIAS Y FORMACION SANITARIA S\.L\. -EMERFOR--$', 'EMERGENCIAS Y FORMACION SANITARIA S.L.U. --EMERFOR--', payee)
        payee = re.sub(r'^FERNANDEZ SANCHEZ MONTSERRAT$', u'FERNANDEZ SANCHEZ MONTSERRAT - AGRUPACIÓN VECINAL', payee)
        payee = re.sub(r'^FORUM CONSULTING ASSOCIATES S\.L\.$', 'FORUM CONSULTING ASSOCIATES 2014 S.L.(VILCHES ABOGADOS)', payee)
        payee = re.sub(r'^FOUR WINDS S\.L\.$', 'FOURWINDS S.L.', payee)
        payee = re.sub(r'^FUNDACION EUROPEA PARA LA SOCIEDAD DE LA INFORMACION$', 'FUNDACION EUROPEA PARA LA SOCIEDAD DE LA INFORMACION Y LA ADM.ELECTRONICA', payee)
        payee = re.sub(r'^GASCON TEJADO PATROCINIO$', 'GASCON TEJADO PATROCINIO - CASA CASTILLA LA MANCHA', payee)
        payee = re.sub(r'^GOMEZ ARELLANO M\. TERESA$', 'GOMEZ ARELLANO M. TERESA - ESCUELA DANZA TERE', payee)
        payee = re.sub(r'^GOMEZ CRUZ JOSE MANUEL$', 'GOMEZ CRUZ JOSE MANUEL--PRODUCCION DE VIDEO---', payee)
        payee = re.sub(r'^GRAFICAS ARIES$', 'GRAFICAS ARIES S.A.', payee)
        payee = re.sub(r'^GRANDES ALMACENES FNACESPAÑA S\.A\.U\.$', 'GRANDES ALMACENES FNAC ESPAÑA S.A.U.', payee)
        payee = re.sub(r'^LOPEZ BARROSO CESAR - ALMAVIVA TEATRO$', 'LOPEZ BARROSO CESAR - ALMA VIVA TEATRO', payee)
        payee = re.sub(r'^MAESTRE AZURMENDI NICOLAS$', 'MAESTRE AZURMENDI NICOLAS(PROCURADOR)', payee)
        payee = re.sub(r'^MINUZ DE MINETTI ZULMA MONICA$', 'MINUZ DE MINETTI ZULMA MONICA - ASOCIACION ARTE SANO', payee)
        payee = re.sub(r'^MOLERO PATENTES & MARCAS S\.L\.$', 'MOLERO PATENTES Y MARCAS S.L.', payee)
        payee = re.sub(r'^MORALES LOPEZ MIGUEL ANGEL$', 'MORALES LOPEZ MIGUEL ANGEL - RUNNING PINTO', payee)
        payee = re.sub(r'^MUSICOS UNIDOS SIGLO XXI S\. COOP\.MAD\.$', 'MUSICOS UNIDOS SIGLO XXI S.COOP.MAD.', payee)
        payee = re.sub(r'^PASAJES LIBRERIA INTERNACIONAL$', 'PASAJES LIBRERIA S.L.U.', payee)
        payee = re.sub(r'^SANCHEZ ARENAS MONTSERRAT$', 'SANCHEZ ARENAS MONTSERRAT - ESCUELA DANZA MONTSE', payee)
        payee = re.sub(r'^SELOGAS S\.L\.$', 'SELOGAS S.L. SERVICIOS Y LOGISTICA DE AREAS DE SERVICIO', payee)
        payee = re.sub(r'^SERVICIOS DE ALQUILER Y FERRETERIA S\.A\. SERALFE S\.A\.$', 'SERVICIOS DE ALQUILER Y FERRETERIA S.A. --SERALFE S.A.--', payee)
        payee = re.sub(r'^SOPEÑA GOMEZ JUAN MANUEL$', 'SOPEÑA GOMEZ JUAN MANUEL - SURBIKE', payee)
        payee = re.sub(r'^TORRES ALONSO EMILIA$', 'TORRES ALONSO EMILIA - PINTO BASKET', payee)
        payee = re.sub(r'^URKEL MULTIMEDIA S\.L\.$', 'URKEL MULTIMEDIA S.L.-CINEPROYECTOS-', payee)
        payee = re.sub(r'^VILLALBA YEPES JESSICA$', 'VILLALBA YEPES JESSICA - CASA ANDALUCIA', payee)

        # We got some anonymized entries
        anonymized = (payee == 'ANONIMIZADO')

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
