# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Project(models.Model):
    _inherit = 'project.project'

    deadline_date = fields.Datetime(string='Deadline Date')
    budget = fields.Float(string='Budget')
    project_size = fields.Selection([('small', 'Small'), ('medium', 'Medium'),  ('large', 'Large')],
                                     string='Number of Months in a Period', default='small')
