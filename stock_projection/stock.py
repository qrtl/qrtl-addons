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

import openerp.addons.decimal_precision as dp
from osv import osv, fields
from tools.translate import _


class stock_move(osv.osv):
    _inherit = 'stock.move'
    
    def _get_prod_loc_qoh(self, cr, uid, ids, product, location, context=None):
        res = 0
        
        results = []
        results2 = []

        states = ('done',)
        what = ('in','out',)
        where = [(location,), (location,), (product,), tuple(states)]

        if 'in' in what:
            cr.execute(
                "select sum(r.product_qty / u.factor), r.product_id "
                "from stock_move r left join product_uom u on (r.product_uom=u.id) "
                "where location_id NOT IN %s"
                "and location_dest_id IN %s"
                "and product_id IN %s"
                "and state IN %s"
                "group by product_id",tuple(where))
            results = cr.dictfetchone()
            if results:
                res = results['sum']
        if 'out' in what:
            cr.execute(
                "select sum(r.product_qty / u.factor), r.product_id "
                "from stock_move r left join product_uom u on (r.product_uom=u.id) "
                "where location_id IN %s"
                "and location_dest_id NOT IN %s"
                "and product_id IN %s"
                "and state IN %s"
                "group by product_id",tuple(where))
            results2 = cr.dictfetchone()
            if results2:
                res -= results2['sum']
          
        return res


    def _projected_qty(self, cr, uid, ids, field_names, args, context=None):
        res = {}

        # show error message in case the browser is refreshed (because the correct result cannot show in this case)
        location = context.get('location_id')        
        if not location:
            raise osv.except_osv(_('Error!'),_("Please run a query through the menu item again."))

        neg_true = []
        neg_false = []

        first_line = True
        begin_qty = 0
        
        # the purpose of this line is to re-sort the ids by 'date_expected' (otherwise, default _order setting of the object is applied and the result becomes incorrect)
        move_ids = self.search(cr, uid, [('is_stock_projection','=',True)], order='date_expected, id', context=context)

        for move in self.browse(cr, uid, move_ids, context=context):
            res[move.id] = {
                'begin_qty': 0.0,
                'move_qty': 0.0,
                'projected_qty': 0.0,
                'ref2': '',
                'origin2': '',
                'is_out': False,
                'is_neg_bal': False,
            }

            if first_line == True:
                product = move.product_id.id
                begin_qty = self._get_prod_loc_qoh(cr, uid, ids, product, location, context=context)
                first_line = False               

            if move.location_id.id == location:
                move_qty = move.product_qty / move.product_uom.factor * -1
                res[move.id]['is_out'] = True
            else:
                move_qty = move.product_qty / move.product_uom.factor

            res[move.id]['begin_qty'] = begin_qty
            res[move.id]['move_qty'] = move_qty
            end_qty = begin_qty + move_qty
            res[move.id]['projected_qty'] = end_qty

            # if the projected balance is negative, make the line bold (see the view definition)
            if end_qty < 0:
                res[move.id]['is_neg_bal'] = True

            # begin_qty of the next line should be the same as the end_qty of the current line
            begin_qty = end_qty

            # update 'Reference'.
            ref2 = ''
            if move.picking_id:
                ref2 = move.picking_id.name
            else:
                ref2 = move.name
            res[move.id]['ref2'] = ref2

            # update 'Source'
            origin2 = ''
            if not move.origin:
                loc_obj = self.pool.get('stock.location')
                usage = loc_obj.read(cr, uid, [move.location_id.id, move.location_dest_id.id], ['usage'])
                if usage and usage[0]['usage'] == 'production' or usage[1]['usage'] == 'production':
                    origin2 = self.pool.get('mrp.production').read_group(cr, uid, [('name','=',move.name)], ['origin'], ['origin'], limit=1)[0]['origin']
            else:
                origin2 = move.origin
            res[move.id]['origin2'] = origin2
            
        return res

    # override the output sorting only for Stock Projection report 
    def _generate_order_by(self, order_spec, query):
        order_by = super(stock_move, self)._generate_order_by(order_spec, query)
        if any('is_stock_projection' in s for s in query.where_clause):
            order_by = order_by.replace('"date_expected" desc', '"date_expected"')  # remove 'desc' instruction for date_expected
        return order_by


    _columns = {
        'is_stock_projection': fields.boolean('Is Stock Projection'),
        'qty_available': fields.related('product_id', 'qty_available', type="float", relation="product.product", string=u"Total QOH"),
        'begin_qty': fields.function(_projected_qty, type='float', digits_compute=dp.get_precision('Product Unit of Measure'), string=u'Begin Qty', multi="move"),
        'move_qty': fields.function(_projected_qty, type='float', digits_compute=dp.get_precision('Product Unit of Measure'), string=u'Move Qty', multi="move"),
        'projected_qty': fields.function(_projected_qty, type='float', digits_compute=dp.get_precision('Product Unit of Measure'), string=u'Projected Qty', multi="move"),
        'ref2': fields.function(_projected_qty, type='char', string=u'Reference', multi='move'),
        'origin2': fields.function(_projected_qty, type='char', string=u'Source', multi="move"),
        'is_neg_bal': fields.function(_projected_qty, type='boolean', string=u'Is Negative Balance', multi='move'),
        'is_out': fields.function(_projected_qty, type='boolean', string=u'Is Outgoing', multi='move'),
    }
    _defaults = {
    }
    
stock_move()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
