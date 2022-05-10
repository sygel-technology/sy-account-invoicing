# Copyright 2021 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    def _get_invoice_line_name_from_product(self):
        name = super(AccountInvoiceLine, self)._get_invoice_line_name_from_product()
        if self.product_id and self.invoice_id.type in ('out_invoice', 'out_refund'):
            name = self.product_id.with_context(display_default_code=True).display_name
        return name
