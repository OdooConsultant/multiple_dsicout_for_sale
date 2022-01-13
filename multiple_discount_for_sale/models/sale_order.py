# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    discount2 = fields.Float(
        string='Disc2.%',
        default=0.0
    )

    discount3 = fields.Float(
        string='Disc3.%',
        default=0.0
    )

    @api.depends('product_uom_qty', 'discount', 'discount2', 'discount3', 'price_unit',
                 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            price2 = price * (1 - (line.discount2 or 0.0) / 100.0)
            price3 = price2 * (1 - (line.discount3 or 0.0) / 100.0)

            taxes = line.tax_id.compute_all(price3,
                                            line.order_id.currency_id,
                                            line.product_uom_qty,
                                            product=line.product_id,
                                            partner=line.order_id.partner_shipping_id
                                            )
            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups('account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])


