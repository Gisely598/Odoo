from odoo import _, api, fields, models, tools

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    delivered_id = fields.Many2one('res.users', string="Entregar a:")

    def get_picking_lots(self, product_id):
            pickings = self.env['stock.picking'].search([('origin', '=', self.name)])
            lot_names = []
            for picking in pickings:
                picking_lines = picking.move_line_ids.filtered(lambda l: l.product_id.id == product_id)
                if picking_lines:
                    lot_names += picking_lines.mapped('lot_id.name')
            return ' '.join(lot_names)


