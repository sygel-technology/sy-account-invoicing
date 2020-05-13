.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

====================
Bank Accounts Report
====================

Choose which bank accounts will be displayed on invoice and sale order reports.


Installation
============

Just install.


Configuration
=============

Go to Accounting -> Configuration -> Payment Modes and configure the "Bank Account on Reports" section for every payment mode. "Account Source" is "No" by default, which means no account will be displayed on reports. By choosing "Company" and "Use Invoice Account" it will display the account set on the invoice. Unchecking "Use Invoice Account", you can manually set as many accounts from your company as you want to appear on the invoice. By choosing  "Partner", it will take the partner account from the mandate on the invoice if it is required. Additionally, choose "Mandate" or "Bank Account", so if the mandate is not required, it will look for the account on the last active mandate for the partner or on its last bank account. Choose "Apply to Sale Orders" if you want it to work for sale orders too.


Usage
=====

Make an invoice or a sale report and choose a payment mode that has been previously configured. The correspondent accounts will be displayed at the end of the report.


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
* Valentín Vinagre <valentin.vinagre@qubiq.es>
* Valentín Vinagre <valentin.vinagre@sygel.es>


Maintainer
~~~~~~~~~~

This module is part of the `sygel/qu-account-invoicing <https://github.com/sygel-technology/sy-account-invoicing>`_.

To contribute to this module, please visit https://github.com/sygel-technology.
