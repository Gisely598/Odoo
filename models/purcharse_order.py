# -*- coding: utf-8 -*-
from odoo import models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_report_custom_purchaseorder(self):
        """ Este método genera y retorna el reporte PDF personalizado. """
        if not self:
            # Si no hay registros, lanzar un error o manejar la situación
            raise ValueError("No se seleccionó ninguna orden de compra para generar el reporte.")
        
        return self.env.ref('rs_custom_report_print.action_report_custom_purchaseorder').report_action(self)
