# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DynamicRequirementLine(models.Model):
    _name = 'dynamic.requirement.field.line'

    sequence = fields.Integer(string='Sequence', default=10)
    dynamic_requirement_id = fields.Many2one('dynamic.requirement.field',
                                             string="Requirement Mandatory Project")
    stage_id = fields.Many2one('site.stage', 'Site Stage')
    mandatory_fields_ids = fields.Many2many('ir.model.fields', string='Mandatory fields')
    custom_warning = fields.Char(string='Custom Warning Message ', required=True)
    company_id = fields.Many2one('res.company', string='Company')