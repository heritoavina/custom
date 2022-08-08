# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SiteStage(models.Model):
    _name = 'site.stage'

    name = fields.Char(string='Stage Name', required=True)
    folded_kanban = fields.Boolean('Folded in Kanban', default=False)
    sequence = fields.Integer('Sequence')
