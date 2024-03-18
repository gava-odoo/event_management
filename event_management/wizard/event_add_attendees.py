# -*- coding: utf-8 -*-

from odoo import fields, models


class EventAddAttendees(models.TransientModel):
    _name = 'event.add.attendees'
    _description = 'Add Attendees to all available events'

    event_id = fields.Many2one('event.event', string="Events")
    member_id = fields.Many2one('team.members', string='Team Member')
    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone No.', required=True)
    email = fields.Char(string='Email-id', required=True, default='alex@odoo.com')

    def action_add_attendee(self):
        active_ids = self.env.context.get('active_ids')
        events = self.env['event.event'].browse(active_ids)
        for event in events:
            event.event_attendees_ids.create(
                {
                    'name': self.name,
                    'phone': self.phone,
                    'email' : self.email,
                    'member_id': self.member_id.id,
                    'events_ids': event.id,
                }
            )