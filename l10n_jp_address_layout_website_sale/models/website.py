# -*- coding: utf-8 -*-
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class Website(models.Model):
    _inherit = 'website'
    
    def get_default_country_id(self):
        country_id = self.env["ir.config_parameter"].sudo().get_param(
            'l10n_jp_address_layout_website_sale.default_country_id')
        return country_id
