# -*- coding: utf-8 -*-
{
    'name': "Sincsol_LMS_Course",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sincsol__lms__base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/Course.xml',
        'views/MainPage.xml',
        'views/UserCourses.xml',
        'views/Ustadam_app_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

