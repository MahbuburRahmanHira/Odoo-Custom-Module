from odoo import api, fields, models, _
from datetime import datetime


class HrBranch(models.Model):
    _name = "res.branch"
    _description = "HR Branch"

    name = fields.Char(string="Branch Name", required=True)
    region_id = fields.Many2one('region', string="Region")
    zone_id = fields.Many2one('zone', string="Zone")
    area_id = fields.Many2one('area', string="Area")
    program_type = fields.Selection([
        ('pksf', 'PKSF'),
        ('smap', 'SMAP')], required=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency", related="company_id.currency_id",
                                  stored=True)
    active = fields.Boolean(string="Active", default=True)
    image = fields.Image(string="Image")
    mobile = fields.Integer(string="Phone")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address")
    code = fields.Char(string='Sequence', readonly=True, copy=False, default=lambda self: _('New'))

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Name already exists!'),
        ('code_unique', 'unique(code)', 'Code already exists!'),
    ]

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('res.branch') or _('New')
        res = super(HrBranch, self).create(vals)
        return res
