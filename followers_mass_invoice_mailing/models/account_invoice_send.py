# Copyright 2020 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountInvoiceSend(models.TransientModel):
    _inherit = "account.invoice.send"

    def _send_email(self):
        if self.is_email:
            ctx = self._context
            if len(ctx.get('active_ids')) == 1:
                super()._send_email()
            else:
                for active_id in ctx.get('active_ids'):
                    invoice = self.env["account.move"].browse([active_id])
                    new_ctx = dict(
                        lang=ctx.get('lang'),
                        tz=ctx.get('lang'),
                        uid=ctx.get('uid'), 
                        allowed_company_ids=ctx.get('allowed_company_ids'), 
                        active_model=ctx.get('active_model'), 
                        active_id=active_id, 
                        active_ids=[active_id], 
                        default_model='account.move', 
                        default_res_id=active_id, 
                        default_res_model='account.move', 
                        default_use_template=True, 
                        default_template_id=ctx.get('default_template_id'), 
                        default_composition_mode='comment', 
                        mark_invoice_as_sent=ctx.get('mark_invoice_as_sent'),
                        custom_layout=ctx.get('custom_layout'), 
                        model_description='Invoice', 
                        force_email=True, 
                        no_new_invoice=ctx.get('no_new_invoice'), 
                        mail_notify_author=ctx.get('mail_notify_author')
                    )
                    values = {
                        'model': 'account.move',
                        'res_id': invoice.id,
                        'template_id': self.template_id.id,
                        'composition_mode': 'comment',
                    }
                    wizard = self.env['account.invoice.send'].with_context(
                            new_ctx).create(values)
                    wizard._compute_composition_mode()
                    wizard.onchange_template_id()
                    wizard.onchange_is_email()  
                    wizard._send_email()
