# -*- coding: utf-8 -*-
{
    'name': "cdn_om_hospital",

    'summary': """
        There's a app i build with following Odoo Mates on Youtube""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dapow",
    'website': "https://dapow.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/patient_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'wizard/cancel_appointment.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/female_patient.xml',
        'views/appointment.xml',
        'views/res_config_settings.xml',
        'views/patient_tag.xml',
        'views/odoo_playground.xml',
        'views/operation.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
