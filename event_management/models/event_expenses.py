#-*- coding: utf-8 -*-

from odoo import models, fields, api

class EventExpenses(models.Model):
    _name = 'event.expenses'
    _description = 'Event Expenses'

    name = fields.Char(string='Name')
    amount = fields.Float(string='Amount', required=True)
    event_id = fields.Many2one('event.event', string="Event")
    event_type_id = fields.Many2one(related='event_id.template_id', store=True)
    member_id = fields.Many2one('team.members')
    description = fields.Text()
    status = fields.Selection(selection=[('accepted', 'Accepted'), ('refused', 'Refused')])

    @api.model
    def create(self, vals):
        self.env['event.event'].browse(vals['event_id']).state = 'started'
        return super().create(vals)

    def action_confirm(self):
        self.status = 'accepted'
        self.event_id.amount_spent+= self.amount

    def action_refused(self):
        self.status = 'refused'

