#-*- coding: utf-8 -*-

from odoo import fields, models

class TeamsMembers(models.Model):
    _name = 'team.members'
    _description = 'The different teams which will work for events'

    name = fields.Char('Name', required=True)
    contact_no = fields.Char('Contact Number')
    managed_by = fields.Many2one('res.group', string='Managed_by')
    email = fields.Char('Email ID', required=True)
    dob = fields.Date(string='Date of Birth')
    employement_type = fields.Selection([('intern','Internship'), ('employee','Full Time Employee')])
    department = fields.Many2one('departments', string='Department', ondelete='set null')
    head_of_department = fields.Char(related='department.head', store=True)

    # add 2-3 more models and more fields

    