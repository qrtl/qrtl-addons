# -*- coding: utf-8 -*-
# Copyright 2015-2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class stock_production_lot(models.Model):
    _inherit = 'stock.production.lot'

    @api.one
    @api.depends('product_id', 'ref', 'quant_ids.qty', 'quant_ids.location_id')
    def _compute_balance(self):
        int_loc_ids = self.env['stock.location'].search(
            [('usage', '=', 'internal')])
        location_ids = [loc.id for loc in int_loc_ids]
        quant_ids = self.env['stock.quant'].search(
            [('lot_id', '=', self.id),
             ('product_id', '=', self.product_id.id),
             ('location_id', 'in', location_ids)])
        for quant in quant_ids:
            self.lot_balance += quant.qty

    lot_balance = fields.Float(string='Lot Qty on Hand', store=True,
                               readonly=True, compute='_compute_balance')

    def init(self, cr):
        # update lot_balance field when installing
        cr.execute("""
            update stock_production_lot lot
            set lot_balance =
                (select sum(qty)
                from stock_quant
                where lot_id = lot.id
                and product_id = lot.product_id
                and location_id in
                    (select id
                    from stock_location
                    where usage = 'internal'
                    )
                )
        """)
