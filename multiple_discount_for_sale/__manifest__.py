# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': ' Multiple Discount For Sale',
    "version": "15.0.1.0.0",
    'category': 'Sales/Sales',
    'description': """
Multiple Discounts For Sale 
=============================================

 This module shows a 2 other level of discount in the <i>sale order</i>.
    """,
    'license': 'AGPL-3',
    'images': ['static/description/icon.png'],
    "development_status": "Beta",
    "category": "Sale",
    'author': 'Odoo Consultant medconsultantweb@gmail.com',
    'website': 'http://www.weblemon.org',
    'price': '10.0',
    'currency': 'USD',

    'depends': ['sale_management', 'sale_margin','account'],
    'demo': [],
    'data': [
        'reports/inherit_sale_report_template.xml'
    ],
}
