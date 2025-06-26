.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

====================
Bank Accounts Report
====================

Choose which bank accounts will be displayed and payment message on invoice and sale
order reports.


Installation
============

Just install.


Configuration
=============

1. **Access Payment Modes**
   To configure the payment modes that will influence how bank accounts and payment messages are displayed:

   - Navigate to ``Accounting > Configuration > Payment Modes``.

2. **Configure Each Payment Mode**
   For each payment mode, adjust the following options according to your needs on Bank Account on Reports section:

   - **Account Source:** 
   
     - Choose **Company** to display bank accounts associated with the company on reports.
     - Choose **Partner** to display bank accounts from the partner based on mandates or direct bank accounts.
       
       - If **Company** is selected, you can opt to **Use Invoice Account**, which will display the account set on the invoice. If this option is unchecked, you can manually select multiple accounts from your company to appear.
         If both options are left empty (no invoice account and no manually selected accounts), no bank account or payment message will appear on the report, to avoid displaying empty or incorrect information.
       
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

Usage
=====

**Creating Invoices or Sales Orders**
Once the payment modes are configured, you can proceed to create invoices or sales orders that use these payment modes.

**Verification in Reports**

- **Create an Invoice/Sales Order:** Ensure to select the previously configured payment mode.
- **Review the Generated Report:** When generating the report for the invoice or sales order, check the end of the document to see the bank accounts listed as per your configuration. Additionally, any configured payment message should appear as set.


Bug Tracker
===========

Bugs and errors are managed in `issues of GitHub <https://github.com/sygel-technology/sy-account-invoicing/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/sygel-technology/sy-account-invoicing/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* QubiQ, Odoo Community Association (OCA)


Contributors
~~~~~~~~~~~~

* Xavier Piernas <xavier.piernas@qubiq.es>
* Valentín Vinagre <valentin.vinagre@sygel.es>
* Manuel Regidor <manuel.regidor@sygel.es>


Maintainer
~~~~~~~~~~

This module is part of the `sygel/qu-account-invoicing <https://github.com/sygel-technology/sy-account-invoicing>`_.

To contribute to this module, please visit https://github.com/sygel-technology.
