# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DynamicRequirement(models.Model):
    _name = 'dynamic.requirement.field'

    name = fields.Char(string='Name', default="New", required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    type = fields.Selection([('site', 'Site'), ('milestone', 'Milestone')],
                                     string='Type', default='site', required=True)
    active = fields.Boolean('Active', default=True)
    line_ids = fields.One2many('dynamic.requirement.field.line', 'dynamic_requirement_id',
                               string="Mandatory Project Line")
    company_id = fields.Many2one('res.company', string='Company')

