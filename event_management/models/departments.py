#-*- coding: utf-8 -*-

from odoo import fields, models

class Departments(models.Model):
    _name = 'departments'
    _description = 'All the departments in the company'

    name = fields.Char('Name', required=True)
    contact_no = fields.Char('Contact Number')
    head = fields.Many2one('team.members', string='Head')
    email_id = fields.Char('Email ID', required=True)
    employees_ids = fields.One2many('team.members', string='Employee\'s', inverse_name='department_id')

