#-*- coding: utf-8 -*-

from odoo import models,fields

class EventRegistration(models.Model):
    _name = 'event.registration'
    _description = 'Event Registration'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email-id', required=True)
    address = fields.Text(string='Address', required=True)
    phone = fields.Char(string='Phone No.', required=True)
    details = fields.Text(string='What are you looking for')
