# -*- coding: utf-8 -*-
{
    'name': 'HR Branch',
    'author': 'GUK',
    'website': 'http://www.guk.com',
    'sequence': 11,
    'depends': [
        'base',
        'web',
        'hr'

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/branch_views.xml',
        'views/region_views.xml',
        'views/zone_views.xml',
        'views/area_views.xml',
        #'views/inherit_views.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'BDT',
    'license': 'OPL-1',

}
