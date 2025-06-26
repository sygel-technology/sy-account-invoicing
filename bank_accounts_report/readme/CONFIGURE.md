1. **Access Payment Modes**
   To configure the payment modes that will influence how bank accounts and payment messages are displayed:

   - Navigate to ``Accounting > Configuration > Payment Modes``.

2. **Configure Each Payment Mode**
   For each payment mode, adjust the following options according to your needs on Bank Account on Reports section:

   - **Account Source:**

     - Choose **Company** to display bank accounts associated with the company on reports.
     - Choose **Partner** to display bank accounts from the partner based on mandates or direct bank accounts.

       - If **Company** is selected, you can opt to **Use Invoice Account**, which will display the account set on the invoice. If this option is unchecked, you can manually select multiple accounts from your company to appear. If both options are left empty (no invoice account and no manually selected accounts), no bank account or payment message will appear on the report, to avoid displaying empty or incorrect information.

       - If **Partner** is selected, decide whether the account will be taken from an existing mandate or simply from the last active bank account of the partner.
   - **Apply to Sale Orders:** Check this option if you want the settings to apply to sales orders as well.
   - **Report Text:** Enter a custom message that will appear on sales and invoice reports.
   - **Payment Message:** If you want a payment message displayed on invoices or sales orders, check the 'Show Payment Message in Invoices' and/or 'Show Payment Message in Sales' checkbox and complete the 'Payment Message' field. Invoices or Sales Orders will show 'Payment Message' + Invoice/Sales name.

3. **Visibility of the Bank Account Number**
   Configure how you would like bank account numbers to be displayed on reports:

   - **How Show Bank Account:**

     - **Full:** The entire bank account number is displayed.

     - **First n chars:** Only the first specified number of characters of the bank account number will be shown, with the rest being masked.

     - **Last n chars:** Only the last specified number of characters of the bank account number will be shown, with the beginning of the number being masked.
