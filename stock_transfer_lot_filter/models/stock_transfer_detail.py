# -*- coding: utf-8 -*-
# Copyright 2015-2017 Rooms For (Hong Kong) Limited T/A OSCG
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, _


class stock_transfer_details(models.TransientModel):
    _inherit = 'stock.transfer_details'

    @api.multi
    def wizard_view(self):
        picking_id = self.env.context.get('active_id')
        code = self.env['stock.picking'].browse(picking_id).picking_type_id.\
            code
        if not code:
            dest_loc_id = self.env.context.get('default_destinationloc_id',
                                               False)
            src_loc_id = self.env.context.get('default_sourceloc_id', False)
            dest_loc = self.env['stock.location'].browse(dest_loc_id)
            src_loc = self.env['stock.location'].browse(src_loc_id)
            if dest_loc.usage == 'internal' and src_loc.usage == 'supplier':
                code = 'incoming'
        if code == 'incoming':
            ext_id = 'stock.view_stock_enter_transfer_details'
        else:
            ext_id = 'stock_transfer_lot_filter.view_stock_enter_transfer_details_z1'
        view = self.env.ref(ext_id)

        return {
            'name': _('Enter transfer details'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'stock.transfer_details',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.ids[0],
            'context': self.env.context,
        }
