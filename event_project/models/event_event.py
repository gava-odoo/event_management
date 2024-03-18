#-*- coding: utf-8 -*-

from odoo import api, fields, models, Command


class AccountEstateProperty(models.Model):
    _inherit = 'event.event'
    
    def action_start(self):
        self.ensure_one()
        values = {
            'name': self.name,
        }
        self.env['project.project'].create(values)
        return super().action_start()