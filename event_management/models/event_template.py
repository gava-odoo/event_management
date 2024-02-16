#-*- coding: utf-8 -*-

from odoo import models,fields

class EventTemplate(models.Model):
    _name = "event.template"
    _description = "All type of Evnets we organise"

    name = fields.Selection(selection=[('wedding','Wedding'), ('garba','Garba'), ('music concert','Music Concert'), ('comedy show','Comedy Show'), ('tournament','Tournament')])