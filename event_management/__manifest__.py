#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Event-Management',
    'category': 'Management/Event Management',
    'sequence' : -100,
    'description': 'A Management Module for managing and handling events',
    'summary': 'Event management system',
    'data': [
        'security/ir.model.access.csv',
        'views/clients.xml',
        'views/departments_views.xml',
        'views/team_members_views.xml',
        'views/event_event_views.xml',
        'views/event_expenses_views.xml',
        'views/event_template_views.xml',
        'views/event_tags_views.xml',
        'views/event_res_partner.xml',
        'views/event_menus.xml',
        'data/event_template_data.xml',
        'data/event_event_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
    'version': '1.0',
}