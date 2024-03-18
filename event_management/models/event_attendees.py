#-*- coding: utf-8 -*-

from odoo import models,fields

class EventAttendees(models.Model):
    _name = 'event.attendees'
    _description = 'Attendees of an event'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email-id', required=True, default='alex@odoo.com')
    phone = fields.Char(string='Phone No.', required=True)
    details = fields.Text(string='What are you looking for')
    events_ids = fields.Many2many('event.event',string='Event')
    member_id = fields.Many2one('team.members', string='Team Member')
    