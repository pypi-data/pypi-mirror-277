{
    'name': 'Bike Shop',
    'version': '0.0.1',
    'category': 'Services/Bike Shop',
    'license': 'GPL-3',
    'summary': 'Basic functionality for managing a bicycle shop',
    'description': """
        A work order management solution for bicycle repair shops.
        """,
    'depends': [
            'base',
            'mail',
            'product',
            'sale',
            'stock',
    ],
    'author': 'Sam Whited',
    'website': 'https://blog.samwhited.com',
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',

        'data/bikeshop_delay_reason_data.xml',
        'data/mail_activity_type_data.xml',

        'views/bikeshop_bicycle_views.xml',
        'views/bikeshop_delay_reason_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/product_product_views.xml',
        'views/bikeshop_menus.xml',
    ],
    'demo': [
        'data/sale_demo.xml',
    ],
    'application': True,
    'installable': True,
    'price': 300.00,
    'currency': 'USD',
    'support': 'odoo@atlbikeshed.com',
}
