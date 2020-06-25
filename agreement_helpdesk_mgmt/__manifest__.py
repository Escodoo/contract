# Copyright 2020 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Agreement Helpdesk Mgmt',
    'summary': """
        This module allows you to link a helpdesk ticket to an agreement and adds a smart button on the agreement to look at the list of related helpdesk tickets.""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Open Source Integrators,Odoo Community Association (OCA)',
    'website': 'https://github.com/oca/contract',
    'depends': [
        "helpdesk_mgmt",
        "agreement_serviceprofile",
    ],
    'data': [
        'views/helpdesk_ticket.xml',
        'views/agreement.xml',
    ],
    'demo': [
    ],
}
