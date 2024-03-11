#-*- coding: utf-8 -*-

from odoo import fields, models, api

class EstatePropertyUsers(models.Model):
    _inherit = 'res.partner'

    event_ids = fields.One2many('event.event', 'customer_id', string='Events', domain="[('customer_id', '=', id)]")