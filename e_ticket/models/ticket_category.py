from odoo import api, fields, models, _
from datetime import datetime


class TicketCategory(models.Model):
    _name = "ticket.category"
    _description = "E-Ticket Category"

    name = fields.Char(string="Category Name")
    code = fields.Char(string='Category ID', readonly=True, copy=False, default=lambda self: _('New'))
    # active = fields.Boolean(string='Active', default=True)

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('ticket.category') or _('New')

        res = super(TicketCategory, self).create(vals)
        return res
