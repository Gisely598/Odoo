# -*- coding: utf-8 -*-
{
    'name': 'Custom Report Print',
    'version': '3.1',
    'description': 'Reportes PDF personalizados',
    'summary': 'Personalización Reporte PDF de impresión, mejoras en las margenes superiores, en la recepcion solo muestra productos recibidos y mejoras de formatos',
    'author': 'Retail & IT Solutions ft JhonConnor',
    'website': 'https://retailsolutions-bo.com/',
    'category': 'Purchases', 
    'depends': ['base', 'purchase', 'stock','mail', 'uom'],
    'data': [
        'report/report.xml',
        'report/purchase_order_custom_report.xml',
        'views/purchase_order_view.xml',
        'views/stock_picking_view.xml',
        'report/report_template_guia_remision.xml',
        'report/report_template_recepcion.xml',
        'report/report_template_guia_remision.xml',
    ],
    'installable': True,
    'application': False,
}