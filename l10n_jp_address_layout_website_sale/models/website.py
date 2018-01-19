# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.http import request
from odoo import models


class Website(models.Model):
    _inherit = 'website'
    
    def get_default_country_id(self):
        country_id = self.env["ir.config_parameter"].sudo().get_param(
            'l10n_jp_address_layout_website_sale.default_country_id')
        if not country_id:
            country_code = request.session['geoip'].get('country_code')
            if country_code:
                country_id = request.env['res.country'].search(
                    [('code', '=', country_code)], limit=1)
        return country_id
