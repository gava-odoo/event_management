#-*- coding: utf-8 -*-

from odoo import models,fields

class EventTemplate(models.Model):
    _name = 'event.template'
    _description = 'All type of Events we organise'
    _order = 'sequence'

    name = fields.Char(string='Name', required=True)
    event_expenses_ids = fields.One2many('event.expenses','event_type_id')
    sequence = fields.Integer(string='Sequence', default=1)