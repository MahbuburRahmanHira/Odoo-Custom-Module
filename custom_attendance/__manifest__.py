# -*- coding: utf-8 -*-
{
    'name': 'Custom Attendance Management',
    'author': 'Hira',
    'website': 'http://www.hira.com',
    'sequence': 1,
    'depends': [
        'base',
        'web',
        'hr',
        'hr_attendance',
        'hr_holidays',

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_attendance_views.xml',
        'views/attendance_status_views.xml',
        'views/menus.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 99,
    'currency': 'USD',
    'license': 'OPL-1',

}
