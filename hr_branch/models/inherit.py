from odoo import models, fields, api, _


class HrDepartment(models.Model):
    _inherit = 'hr.department'

    branch_id = fields.Many2one('res.branch', string='Branch Name')


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    branch_id = fields.Many2one('res.branch', string='Branch Name')


class HrPublic(models.Model):
    _inherit = 'hr.employee.public'

    branch_id = fields.Many2one('res.branch', string='Branch Name')
