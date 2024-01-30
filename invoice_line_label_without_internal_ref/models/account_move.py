# Copyright 2024 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def _get_computed_name(self):
        res = super()._get_computed_name()
        if self.move_id.move_type in ['out_invoice', 'out_refund'] and\
                self.product_id.default_code:
            res = res.replace("[{}] ".format(self.product_id.default_code), '')
        return res
