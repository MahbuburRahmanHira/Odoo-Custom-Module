from odoo import api, fields, models, _
from datetime import datetime


class TicketManagement(models.Model):
    _name = "ticket.management"
    _description = "E-Ticket Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "code"

    code = fields.Char(string='Ticket No', readonly=True, copy=False, default=lambda self: _('New'))
    member_id = fields.Char(string='Member ID', required=True)
    branch_name = fields.Many2one('res.branch', string='Branch Name')
    category_name = fields.Many2one("ticket.category", string="Category Name", tracking=True)
    description = fields.Text(string="Description", tracking=True)
    time = fields.Datetime(string="Time", default=fields.Datetime.now, readonly=True)
    deadline = fields.Datetime(string="Deadline", readonly=False, states={'draft': [('readonly', True)]},
                               tracking=True)
    assign_to = fields.Many2one("hr.employee", string="Assign To", domain="[('department_id', 'in', ['ICT', 'IT Filed Support', 'IT Infrastructure & Office support', 'Software Development & Innovation', 'System Administration & Analysis'])]", readonly=True,
                                states={'submit': [('required', True)]}, tracking=True)
    # reject = fields.Char(string="Rejection Cause")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submit'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft', tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('ticket.management') or _('New')
        res = super(TicketManagement, self).create(vals)
        return res

    def action_draft(self):
        self.state = 'draft'

    def action_submit(self):
        self.state = 'submit'

    def action_back_to_assign(self):
        self.state = 'submit'
        self.deadline = False

    def action_progress(self):
        self.state = 'in_progress'

    def action_done(self):
        self.state = 'done'
