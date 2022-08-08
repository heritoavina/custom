# -*- coding: utf-8 -*-
{
    'name': "Port cities project module",

    'summary': """
        Module for managing the customer project
        """,

    'description': """
        * Module for managing the project *
    """,

    'author': "Toavina",
    'category': 'project',
    'version': '15.0.0.0',

    'depends': ['base', 'project'],

    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/site_stage_view.xml',
    ],
}
