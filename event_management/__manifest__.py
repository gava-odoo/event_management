#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Event-Management',
    'category': 'Management/Event Management',
    'sequence' : -100,
    'description': 'A Management Module for managing and handling events',
    'summary': 'Event management system',
    'depends' : ['base', 'website'],
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
        'views/event_templates.xml',
        'views/event_menus.xml',
        'report/event_event_reports.xml',
        'report/event_event_views.xml',
        'wizard/event_add_attendees.xml',
        'data/event_template_data.xml',
        'data/event_event_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
    'version': '1.0',
}