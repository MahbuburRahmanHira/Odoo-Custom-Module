from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
from odoo import http
from odoo.http import request
from datetime import datetime
import calendar, math, re, io, base64, os, json, werkzeug

import logging
# logger = logging.getLogger(name_)


class Zone(models.Model):
    _name = "zone"
    _description = "Zone"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", readonly=True)
    region_id = fields.Many2one('region', string="Region")
    company_id = fields.Many2one(comodel_name="res.company", string="Company", default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", related="company_id.currency_id",
                                  stored=True)
    active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Name already exists!'),
        ('code_unique', 'unique(code)', 'Code already exists!'),
    ]

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('zone.name')
        res = super(Zone, self).create(vals)
        return res