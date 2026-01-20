# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Management',
    'summary': 'Manages employee management system',
    'description': 'Manages employee management system',
    'depends': ['base','mail'],
    'data': [
        'wizard/emp_rec.xml',
        'views/view.xml'
        ],
    'installable': True,
}
