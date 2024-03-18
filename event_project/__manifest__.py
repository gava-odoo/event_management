#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Event-Project',
    'category': 'Management/Event Project',
    'sequence' : -98,
    'description': 'A Management Module for Creating Project for Events',
    'summary': 'Event project creation',
    'depends' : ['event_management', 'project'],
    'data': [
        'report/event_project_reports.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
    'version': '1.0',
}