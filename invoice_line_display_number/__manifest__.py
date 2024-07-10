# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Invoice Line Display Number",
    "summary": "Configure number of invoice lines to be shown",
    "version": "15.0.1.0.0",
    "category": "Invoicing",
    "website": "https://github.com/sygel-technology/sy-account-invoicing",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
    ],
    "data": ["data/invoice_line_display_number_data.xml"],
    "assets": {
        "web.assets_backend": [
            "invoice_line_display_number/static/src/js/form_view.js",
        ]
    },
}
