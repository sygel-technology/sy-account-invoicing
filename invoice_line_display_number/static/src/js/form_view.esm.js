/* Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
 *  * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

import {FormController} from "@web/views/form/form_controller";
import {patch} from "@web/core/utils/patch";
import {session} from "@web/session";

patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
        this._setSubViewLimitInvoice();
    },

    async _setSubViewLimitInvoice() {
        if (this.props.resModel === "account.move") {
            const value = session.invoice_line_display_number || 10000;
            const limit = parseInt(value, 10);
            for (const fieldName of ["invoice_line_ids", "line_ids"]) {
                var field = Object.values(this.archInfo.fieldNodes).find(
                    (node) => node.name === fieldName
                );
                if (field?.views && field.views.list && limit) {
                    field.views.list.limit = limit;
                }
            }
        }
    },
});
