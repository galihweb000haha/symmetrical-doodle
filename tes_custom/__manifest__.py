{
    'name': 'Tes Custom',
    'summary': "Tes Custom ",
    'description': """
        v1.0.0
        By: Me
    """,
    'author': "Galih Fikran ",
    'website': "www.galihfikran.com",
    'version': '16.0.1.0.0', 
    'data': [
        #security
        'security/ir.model.access.csv',

        #data
        'data/sequences.xml',

        #views
        'views/room_order_views.xml',
        'views/room_views.xml',
        'views/menu_views.xml',
    ],
    'depends': ['base'],
    'auto_install': False,
    'installable': True,
    'application': False,
    'license': 'OEEL-1'
}