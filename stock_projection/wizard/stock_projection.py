# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright (C) 2014 Rooms For (Hong Kong) Limited T/A OSCG
#    <https://www.odoo-asia.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp.osv import fields, osv


class stock_projection(osv.osv_memory):
    _name = "stock.projection"
    _description = "Stock Projection"
    _columns = {
        'product_id': fields.many2one('product.product', 'Product', required=True),
        'location_id': fields.many2one('stock.location', 'Location', required=True),
    }
        
    def stock_projection_open_window(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        act_obj = self.pool.get('ir.actions.act_window')

        if context is None:
            context = {}
        data = self.read(cr, uid, ids, [], context=context)[0]

        result = mod_obj.get_object_reference(cr, uid, 'stock_projection', 'action_stock_projection1')
        id = result and result[1] or False
        result = act_obj.read(cr, uid, [id], context=context)[0]
        product_id = data.get('product_id', False) and data['product_id'][0] or False
        location_id = data.get('location_id', False) and data['location_id'][0] or False
        result['context'] = str({'product_id': product_id, 'location_id': location_id})

        move_obj = self.pool.get('stock.move')
        
        # set is_stock_projection to False for all records
        move_ids = move_obj.search(cr, uid, [('is_stock_projection','!=',False)], context=context)
        self.pool.get('stock.move').write(cr, uid, move_ids, {'is_stock_projection': False}, context=context)		

        # set is_stock_projection to True for records meeting the condition 
        move_ids = move_obj.search(cr, uid, [('state','not in',['done', 'cancel']),('product_id','=',product_id),'|',('location_id','=',location_id),('location_dest_id','=',location_id)], context=context)
        # if location_id and location_dest_id are the same (e.g. internal move record generated for MO), exclude the record from output
        # we need to have this since adding "('location_id','!=','location_dest_id')" in the domain of above line did not work
        for move in move_obj.browse(cr, uid, move_ids, context=context):
            locations = move_obj.read(cr, uid, move.id, ['location_id', 'location_dest_id'])
            if locations['location_id'] == locations['location_dest_id']:
                move_ids.remove(move.id)
        self.pool.get('stock.move').write(cr, uid, move_ids, {'is_stock_projection': True}, context=context)
        
        return result

    _defaults = {
#        'location_id': 12,
    }

stock_projection()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
