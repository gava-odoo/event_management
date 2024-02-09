from odoo import fields, models

class TeamsMembers(models.Model):
    _name = 'team.members'
    _description = 'The different teams which will work for events'

    name = fields.Char('Name', required=True)
    contact_no = fields.Char('Contact Number')
    managed_by = fields.Char('Managed By',required=True)
    email_id = fields.Char('Email ID', required=True)
    dob = fields.date('Date of Birth')
    employement_type = fields.selection([('intern' , 'Internship') , ('employee' , 'Full Time Employee')])
    department = fields.many2one('departments',string='Department',ondelete='set null')
    