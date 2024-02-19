#-*- coding: utf-8 -*-

from odoo import models,fields

class Events(models.Model):
    _name = 'event.event'
    _description = 'Event details'

    name = fields.Char(string='Event Type', required=True)
    budget = fields.Float(string='Budget')
    limited_seats_available = fields.Boolean(string='Limited Seats')
    total_seats_available = fields.Integer(string='Total no. of Seats')
    managed_by_id = fields.Many2one('team.members', string='Managed By')
    teams_involved_ids = fields.Many2many('departments', string='Teams')
    tag_ids = fields.Many2many('event.tags',string='Tags')
    customer_id = fields.Many2one('res.partner', string='Client', copy=False)
    salesman_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)