# -*- coding: utf-8 -*-
{
    'name': "Odoo Academy dos",

    'summary': """Academy app to manage Training""",

    'description': """
        Academy Module to manage Training:
        - Courses
        -Sessions
        -Attendees
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",

    'license':'LGPL-3',
    'category': 'Training',
    'version': '0.1',

    
    'depends': ['base','sale','website'],

   
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/product_views_inherit.xml',
        'views/sale_views_inherit.xml',
        'views/session_views.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_templates.xml',
        'views/academy_web_templates.xml',
     
    ],
  
    'demo': [
        'demo/academy_demo.xml'
    ],
}
