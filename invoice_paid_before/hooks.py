# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def post_init_hook(cr, registry):
    
    cr.execute(
        """
        UPDATE account_move am SET invoice_paid_before = true
        WHERE am.move_type in ('out_invoice', 'out_refund', 'in_invoice', 'in_refund') AND
        am.amount_total != 0.0 AND
        am.invoice_paid_before is null AND
        am.amount_residual = 0.0
    """
    )
