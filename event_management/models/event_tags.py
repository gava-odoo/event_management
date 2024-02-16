#-*- coding: utf-8 -*-

from odoo import models,fields

class EventTags(models.Model):
    _name = "event.tags"
    _description = "Tags for different events"

    name = fields.Char(string='Event Type', required=True)