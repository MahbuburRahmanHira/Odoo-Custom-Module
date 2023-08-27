# -*- coding: utf-8 -*-
{
    'name': 'E-Ticket Management',
    'author': 'Hira',
    'website': 'http://www.hira.com',
    'sequence': 1,
    'depends': [
        'base',
        'web',
        'hr',
        'hr_branch',
        'mail',

    ],
    'data': [
        'security/security_group.xml',
        'security/ir.model.access.csv',
        'views/ticket_views.xml',
        'views/category_views.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 100,
    'currency': 'BDT',
    'license': 'OPL-1',

}
