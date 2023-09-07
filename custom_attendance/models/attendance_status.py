from datetime import date, time, datetime, timedelta
from odoo import models, fields, api


class AttendanceStatus(models.Model):
    _inherit = "hr.attendance"
    _description = "Attendance Status"

    attendance_status = fields.Selection([
        ('in_time', 'In Time'),
        ('late', 'Late'),
        ('leave', 'Leave'),
        ('absent', 'Absent'),
    ], string='Status', index=True, readonly=True, copy=False, tracking=True, compute='_compute_attendance_status_2')
    leave_request_id = fields.Many2one('hr.leave', string='Leave Request', readonly=True)

    @api.depends('check_in')
    def _compute_attendance_status_2(self):
        for rec in self:
            check_in = rec.check_in + timedelta(hours=6, minutes=0)
            today = datetime.today()
            today1 = date.today()
            initial_time = today.replace(hour=0, minute=0, second=0, microsecond=0)
            time = initial_time + timedelta(hours=9, minutes=0)
            absent = initial_time + timedelta(hours=6, minutes=0)
            if check_in < absent:
                # rec.attendance_status = 'absent'
                # print(f"Check-in: {check_in}, Absent: {absent}")
                leave_request = self.env['hr.leave'].search([
                    ('employee_id', '=', rec.employee_id.id),
                    ('request_date_from', '<=', today1),
                    ('request_date_to', '>=', today1),
                    ('state', '=', 'validate'),
                ])

                if leave_request:
                    # print(f"Leave request found: {leave_request}")
                    rec.attendance_status = 'leave'
                else:
                    rec.attendance_status = 'absent'

            elif absent <= check_in <= time:
                rec.attendance_status = 'in_time'
            elif check_in > time:
                rec.attendance_status = 'late'


