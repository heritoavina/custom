# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Project(models.Model):
    _inherit = 'project.project'

    requirement_id = fields.Many2one('dynamic.requirement.field', string='Requirement')

    # @api.depends('stage_id')
    # def compute_mandatory_field(self):
