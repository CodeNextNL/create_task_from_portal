# Copyright (C) codeNext
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Portal create task as customer',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'codeNext',
    'website': 'https://www.codenext.nl',
    'category': 'Hidden',
    'depends': [
        'portal',
        'website_form_builder'
    ],
    'data': [
        'views/templates.xml',
        'views/assets.xml'
    ],
    'installable': True,
    'auto_install': True,
    'post_init_hook': 'post_init_hook',
}
