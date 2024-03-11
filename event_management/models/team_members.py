#-*- coding: utf-8 -*-

from odoo import api, fields, models

class TeamsMembers(models.Model):
    _name = 'team.members'
    _description = 'The different teams which will work for events'
    _order = 'id'

    name = fields.Char('Name', required=True)
    contact_no = fields.Char('Contact Number')
    managed_by = fields.Many2one('team.members', string='Managed By')
    email = fields.Char('Email ID', required=True)
    dob = fields.Date(string='Date of Birth')
    employement_type = fields.Selection([('intern', 'Internship'), ('employee', 'Full Time Employee')])
    department_id = fields.Many2one('departments', string='Department', ondelete='set null')
    head_of_department = fields.Char(compute='_compute_hod', store=True)

    @api.depends('department_id')
    def _compute_hod(self):
        for record in self:
            record.head_of_department = record.department_id.head.name if record.department_id.head else ''
   