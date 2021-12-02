# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright (C) 2014 - hiro TAKADA. All Rights Reserved
#    @author hiro TAKADA <hiro@thdo.biz>
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

import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

from odoo.osv import osv
import calendar
from odoo import _, api, exceptions, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'
    
    monthly_cutoff = fields.Boolean(
        string='Monthly Cutoff',
    )
    month_end_cutoff = fields.Boolean(
        string='Cutoff at Month-End',
    )
    cutoff_date = fields.Integer(
        string='Cutoff Date',
        default=1,
    )


    @api.one
    def compute(self, value, date_ref=False):
        date_ref = date_ref or fields.Date.today()
        #pt = self.browse(id, context=context)
        amount = value
        sign = value < 0 and -1 or 1
        result = []
        if self.env.context.get('currency_id'):
            currency = self.env['res.currency'].browse(self.env.context['currency_id'])
        else:
            currency = self.env.user.company_id.currency_id
        for line in self.line_ids:
            if line.value == 'fixed':
                amt = sign * currency.round(line.value_amount)
            elif line.value == 'percent':
                amt = currency.round(value * (line.value_amount / 100.0))
            elif line.value == 'balance':
                amt = currency.round(amount)
            if amt:
                if not self.monthly_cutoff:  # added
                    next_date = fields.Date.from_string(date_ref)
                    if line.option == 'day_after_invoice_date':
                        next_date += relativedelta(days=line.days)
                        if line.day_of_the_month > 0:
                            months_delta = (line.day_of_the_month < next_date.day) and 1 or 0
                            next_date += relativedelta(day=line.day_of_the_month, months=months_delta)
                    elif line.option == 'after_invoice_month':
                        next_first_date = next_date + relativedelta(day=1, months=1)  # Getting 1st of next month
                        next_date = next_first_date + relativedelta(days=line.days - 1)
                    elif line.option == 'day_following_month':
                        next_date += relativedelta(day=line.days, months=1)
                    elif line.option == 'day_current_month':
                        next_date += relativedelta(day=line.days, months=0)

                # additional code is here
                else:
                    ref_date = datetime.strptime(str(date_ref), '%Y-%m-%d')

                    # identify number of months to add
                    months_to_add = line.months_added
                    if not self.month_end_cutoff:
                        if ref_date.day > self.cutoff_date:
                            months_to_add += 1
                    next_date = ref_date + relativedelta(months=months_to_add)
                    # identify date of the month
                    if line.month_end_pay:
                        date = calendar.monthrange(
                            next_date.year,
                            next_date.month)[1]
                    else:
                        date = line.payment_date
                    next_date = next_date + relativedelta(day=date)
                # up to here

                result.append((fields.Date.to_string(next_date), amt))
                amount -= amt
        amount = sum(amt for _, amt in result)
        dist = currency.round(value - amount)
        if dist:
            last_date = result and result[-1][0] or fields.Date.today()
            result.append((last_date, dist))
        return result

    @api.constrains('cutoff_date')
    def _check_cutoff_date(self):
        if self.monthly_cutoff and not self.month_end_cutoff and \
                (self.cutoff_date < 1 or self.cutoff_date > 30):
            raise ValidationError(_("Cutoff Date must be in the range between 1 and 30.  %s") % (
                self.cutoff_date))
    
    @api.onchange('monthly_cutoff')
    def _onchange_monthly_cutoff(self):
        self.line_ids.monthly_cutoff = self.monthly_cutoff
        if self.monthly_cutoff:
            self.line_ids.option = ""
        elif not self.line_ids.option:
            self.line_ids.option = 'day_after_invoice_date'


class AccountPaymentTermLine(models.Model):
    _inherit = 'account.payment.term.line'

    monthly_cutoff = fields.Boolean(
        related='payment_id.monthly_cutoff',
        string='Monthly Cutoff',
    )
    months_added = fields.Integer(
        string='Months to Add', default=1,
    )
    month_end_pay = fields.Boolean(
        string='Payment at Month End',
    )
    payment_date = fields.Integer(
        string='Payment Date', default=1,
    )

    option = fields.Selection([
            ('day_after_invoice_date', "day(s) after the invoice date"),
            ('after_invoice_month', "day(s) after the end of the invoice month"),
            ('day_following_month', "of the following month"),
            ('day_current_month', "of the current month"),
        ],
        default='day_after_invoice_date', required=False, string='Options'
        )

    @api.constrains('payment_date')
    def _check_payment_date(self):
        if self.monthly_cutoff and not self.month_end_pay and \
                (self.payment_date < 1 or self.payment_date > 30):
            raise ValidationError(_("Payment Date must be in the range between 1 and 30.  %s") % (
                self.payment_date))
