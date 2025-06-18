from odoo.tests.common import TransactionCase


class TestSaleOrderBankAccounts(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Test Partner",
            }
        )

        cls.bank_account = cls.env["res.partner.bank"].create(
            {
                "acc_number": "ES9820385778983000760236",
                "partner_id": cls.partner.id,
            }
        )

        cls.payment_method = cls.env["account.payment.method"].create(
            {
                "name": "Test Method",
                "payment_type": "outbound",
                "code": "test_method",
            }
        )

        cls.journal = cls.env["account.journal"].create(
            {
                "name": "Test Bank Journal",
                "type": "bank",
                "code": "TBNK",
            }
        )

        cls.payment_mode = cls.env["account.payment.mode"].create(
            {
                "name": "Company Bank Mode",
                "account_source": "company",
                "invoice_account": False,
                "apply_sale_order": True,
                "res_partner_bank_ids": [(6, 0, [cls.bank_account.id])],
                "payment_method_id": cls.payment_method.id,
                "bank_account_link": "fixed",
                "fixed_journal_id": cls.journal.id,
            }
        )

        cls.sale_order = cls.env["sale.order"].create(
            {
                "partner_id": cls.partner.id,
                "payment_mode_id": cls.payment_mode.id,
            }
        )

        cls.account_move = cls.env["account.move"].create(
            {
                "partner_id": cls.partner.id,
                "payment_mode_id": cls.payment_mode.id,
            }
        )

    def test_bank_accounts_company_mode_sale_order(self):
        accounts = self.sale_order.bank_accounts_report()
        self.assertEqual(len(accounts), 1)
        self.assertIn(self.bank_account, accounts)

    def test_bank_accounts_company_mode_account_move(self):
        accounts = self.account_move.bank_accounts_report()
        self.assertEqual(len(accounts), 1)
        self.assertIn(self.bank_account, accounts)
