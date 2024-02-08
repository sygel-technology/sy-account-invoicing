# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move"

    invoice_paid_before = fields.Boolean(
        string="Paid Before",
        readonly=True,
        default=False,
        copy=False
    )

    def _compute_amount(self):
        ret_vals = super()._compute_amount()
        self.filtered(
            lambda a: a.is_invoice() and
            a.amount_total != 0.0 and
            not a.invoice_paid_before and
            a.amount_residual == 0.0
        ).write({
            "invoice_paid_before": True
        })
        return ret_vals
