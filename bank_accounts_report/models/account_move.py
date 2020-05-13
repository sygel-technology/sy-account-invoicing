# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# Copyright 2020 Valentin Vinagre <valentin.vinagre@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def bank_accounts_report(self):
        bank_accounts = []
        if self.payment_mode_id:
            if self.payment_mode_id.account_source == 'company':
                if self.payment_mode_id.invoice_account and\
                        self.invoice_partner_bank_id:
                    bank_accounts.append(self.invoice_partner_bank_id)
                elif self.payment_mode_id.res_partner_bank_ids:
                    for account in self.payment_mode_id.res_partner_bank_ids:
                        bank_accounts.append(account)
            if self.payment_mode_id.account_source == 'partner':
                if self.mandate_required and self.mandate_id and\
                        self.mandate_id.partner_bank_id:
                    bank_accounts.append(self.mandate_id.partner_bank_id)
                else:
                    if self.payment_mode_id.\
                            partner_account_source == 'mandate':
                        mandates = self.partner_id.commercial_partner_id.\
                            valid_mandate_id
                        if mandates:
                            bank_accounts.append(mandates.partner_bank_id)
                    else:
                        accounts = self.partner_id.commercial_partner_id.\
                            bank_ids
                        if accounts:
                            bank_accounts.append(accounts[-1])
        return bank_accounts
