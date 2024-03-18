#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta

class Events(models.Model):
    _name = 'event.event'
    _description = 'Event details'
    _order = 'start_date, end_date'

    name = fields.Char(string='Event Type', required=True)
    description = fields.Text(string='Description', compute='_compute_description')
    template_id = fields.Many2one('event.template', string='Event Type')
    budget = fields.Float(string='Budget')
    limited_seats_available = fields.Boolean(string='Limited Seats', default=False)
    total_seats_available = fields.Integer(string='Total no. of Seats', required=True)
    start_date = fields.Date(string='Start Date', default=datetime.today().date())
    end_date = fields.Date(string='End Date', compute='_compute_end_date', inverse='_inverse_end_date', store=True)
    duration = fields.Integer(string='Duration', default=3)
    managed_by_id = fields.Many2one('team.members', string='Managed By')
    teams_involved_ids = fields.Many2many('departments', string='Teams')
    tag_ids = fields.Many2many('event.tags',string='Tags')
    customer_id = fields.Many2one('res.partner', string='Client', copy=False)
    salesman_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    expense_ids = fields.One2many('event.expenses', 'event_id')
    amount_spent = fields.Float(string='Amount Spent')
    image = fields.Image(string='Image')
    location = fields.Text('Location')
    event_attendees_ids = fields.Many2many('event.attendees',relation='attendees')
    state = fields.Selection(selection = [
        ('scheduled', 'Scheduled'),
        ('registered', 'Registered'),
        ('started', 'Started'),
        ('finished', 'Finished'),
        ('cancelled', 'Cancelled'),
    ], string='Status')

    _sql_constraints = [
        ('total_seats_available', 'CHECK(NOT limited_seats_available OR total_seats_available > 0)',
         'Please Enter the Total No. of seats Available'),
         ('budget', 'CHECK(budget > 0)',
         'Please Enter the positive value of Budget'),
         ('AmountSpent', 'CHECK(amount_spent < Budget)',
         'Budget Exceeded'),
    ]

    @api.depends('name', 'duration', 'budget', 'customer_id')
    def _compute_description(self):
        self.ensure_one()
        self.description = 'Organize a {} for {} days in the budget of {} for {}'.format(self.name, self.duration, self.budget, self.customer_id.name)

    @api.depends('duration')
    def _compute_end_date(self):
        self.ensure_one()
        self.end_date = self.start_date + timedelta(days=self.duration)
    
    def _inverse_end_date(self):
        self.ensure_one()
        if self.end_date:
            self.duration = (self.end_date - self.start_date).days
        else:
            self.duration = 3

    @api.constrains('start_date', 'end_date')
    def check_duration(self):
        if (self.end_date < self.start_date):
            raise UserError('End date cannot be before start date')

    @api.ondelete(at_uninstall=False)
    def _unlink_cannot_delete_event(self):
        for record in self:
            if record.state not in ['scheduled', 'registered']:
                raise UserError('Cannot delete a event with state other than Scheduled or Registered.')
    
    def action_start(self):
        if self.state == 'cancelled':
            raise UserError('Cannot start a cancelled event')
        else:
            self.state = 'started'

    def action_cancel(self):
        if self.state == 'started':
            raise UserError('Cannot cancel an event once already started')
        else:
            self.state = 'cancelled'

