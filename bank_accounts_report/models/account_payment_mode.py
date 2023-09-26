# Copyright 2018 Xavier Piernas <xavier.piernas@qubiq.es>
# Copyright 2020-2022 Valentin Vinagre <valentin.vinagre@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class AccountPaymentMode(models.Model):
    _inherit = 'account.payment.mode'

    account_source = fields.Selection([
        ('company', _('Company')),
        ('partner', _('Partner')),
        ('no', _('No'))],
        default='no',
        string=_('Account Source')
    )
    report_text = fields.Char(
        string=_('Text on report'),
        help=_('This text will be displayed on the report with the accounts'),
        translate=True
    )
    invoice_account = fields.Boolean(
        default=True,
        string=_('Use Invoice Account'),
        help=_('Use the bank account set on the invoice')
    )
    res_partner_bank_ids = fields.Many2many(
        comodel_name='res.partner.bank',
        string=_('Bank Accounts')
    )
    partner_account_source = fields.Selection([
        ('mandate', _('Mandate')),
        ('bank', _('Bank Account'))],
        default='bank',
        string=_('Partner Account Source')
    )
    apply_sale_order = fields.Boolean(
        default=False,
        string=_('Apply to Sale Orders')
    )
    show_part_bank_account = fields.Selection(
        selection=[
            ("full", "Full"),
            ("first", "First n chars"),
            ("last", "Last n chars"),
        ],
        string="How show bank account",
        default="full",
        help="Show in invoices partial or full bank account number",
    )
    show_part_bank_account_chars = fields.Integer(
        string="# of digits"
    )
    show_payment_message_sale = fields.Boolean(
        default=False,
        string='Show Payment Message in Sales'
    )
    show_payment_message_invoice = fields.Boolean(
        default=False,
        string='Show Payment Message on Invoices'
    )
    payment_message = fields.Char(
        string='Payment Message',
        help="This text will appear in the sales reports and Invoice reports "
        "that are so configured followed by the name of the Invoice/Sale. "
        "e.g. if the message is 'Indicate in the transfer the concept:' in "
        "the invoice and/or sales reports it will appear: "
        "'Indicate in the transfer the concept:'+ Invoice/Sale name.",
        translate=True
    )
