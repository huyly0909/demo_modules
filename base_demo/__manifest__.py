{
    'name': 'BASE DEMO',
    'summary': '',
    'version': '11.0.1.0.0',
    'category': 'Tools',
    'author':
        'Huy Ly',
    'website': 'https://2wa.vn',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'mail_bot',
    ],
    'data': [
        'data/mailbot_data.xml',
        'data/res_users_demo.xml',
        'data/res_partner_demo.xml',
        # Views
        'views/webclient_templates.xml',
    ],
    'qweb': ['static/src/xml/base.xml'],
    'application': False,
}
