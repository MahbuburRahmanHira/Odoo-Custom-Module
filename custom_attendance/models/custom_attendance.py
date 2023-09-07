from datetime import date, timedelta

from odoo import models, fields
from odoo.exceptions import ValidationError


class CustomAttendance(models.Model):
    _name = "custom.attendance"
    _description = "Custom Attendance Management"
    _rec_name = "employee_id"

    employee_id = fields.Many2one('hr.employee', string="Employee Name")
    barcode = fields.Char(string="Employee ID", related='employee_id.barcode')
    date = fields.Date(string="Date",default=fields.Date.context_today)
    att_type = fields.Selection([
        ('check_in', 'Check In'),
        ('check_out', 'Check Out'),], string='Type', required=True)
    check_in = fields.Datetime(string="Check In")
    check_out = fields.Datetime(string="Check Out")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('request', 'Requested'),
        ('approve', 'Approve'),
        ('reject', 'Reject'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft', tracking=True)

    def action_draft(self):
        self.state = 'draft'

    def action_request(self):
        self.state = 'request'

    def action_validity(self):
        for rec in self:
            today = date.today()
            attendance = self.env['hr.attendance'].search([('employee_id', '=', rec.employee_id.id), ('check_in', '>=', today)])
            if attendance:
                check_in = attendance.check_in + timedelta(hours=6, minutes=0)
                raise ValidationError("Employee Attendance Entry Time %s" % check_in)
            else:
                raise ValidationError("Employee Today Attendance Not Entry !")

    def action_approve(self):
        self.state = 'approve'
        for rec in self:
            today = date.today()
            attendance = self.env['hr.attendance'].search(
                [('employee_id', '=', rec.employee_id.id), ('check_in', '>=', today)])
            if attendance:
                if rec.check_in:
                    attendance_chech_in = self.env['hr.attendance'].search([('id', '=', attendance.id), ('check_in', '>=', rec.check_in)])
                    attendance.write({
                        'check_in': rec.check_in,
                    })
                elif rec.check_out:
                    attendance_check_out = self.env['hr.attendance'].search([('employee_id', '=', rec.employee_id.id), ('check_in', '>=', rec.check_in)])
                    # print(attendance_check_out)
                    attendance.write({
                        'check_out': rec.check_out,
                    })
                    print(attendance.check_out)
            else:
                new_attendance = self.env['hr.attendance'].create({
                    'employee_id': rec.employee_id.id,
                    'check_in': rec.check_in,
                })


    def action_reject(self):
        self.state = 'reject'
