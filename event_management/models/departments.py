#-*- coding: utf-8 -*-

from odoo import fields, models

class Departments(models.Model):
    _name = 'departments'
    _description = 'All the departments in the company'

    name = fields.Char('Name', required=True)
    contact_no = fields.Char('Contact Number')
    head = fields.Char('Head of Department',required=True)
    email_id = fields.Char('Email ID', required=True)
    employees = fields.One2many('team.members', string='Employee\'s', inverse_name='department')

