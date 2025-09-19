/** @odoo-module **/

import {
    createElement,
    setAttributes,
} from "@web/core/utils/xml";

import { patch } from "@web/core/utils/patch";
import { FormCompiler } from "@web/views/form/form_compiler";

patch(FormCompiler.prototype, {

    compile(node, params) {
        const res = super.compile(...arguments);
        const chatterContainerHookXml = res.querySelector(".o-mail-Form-chatter");
        const sheet = res.querySelector("div.o_form_sheet_bg");
        if (sheet && chatterContainerHookXml) {
            const form_statusbar = sheet.querySelector("div.o_form_statusbar");

            const $div = createElement('div');
            const $hide_button = createElement('button');
            $hide_button.classList.add("btn", "btn-outline-primary", "button-hide-right-panel", "o_form_button_create");
            $hide_button.setAttribute("t-on-click", `() => __comp__._onHideRightPanel()`);
            $hide_button.setAttribute("t-if", "!__comp__.env.inDialog");
            $hide_button.setAttribute("title", 'Hide Chatter');
            $hide_button.setAttribute("t-out", '"Hide Chatter"');

            const $show_button = createElement('button');
            $show_button.classList.add("btn", "btn-outline-primary", "button-show-right-panel", "o_form_button_create", "d-none");
            $show_button.setAttribute("t-on-click", `() => __comp__._onShowRightPanel()`);
            $show_button.setAttribute("t-if", "!__comp__.env.inDialog");
            $show_button.setAttribute("title", 'Show Chatter');
            $show_button.setAttribute("t-out", '"Show Chatter"');

            $div.append($hide_button);
            $div.append($show_button);

            if (form_statusbar) {
                $div.classList.add("div-hide-show-right-panel");
                form_statusbar.append($div);
            }
            else {
                $div.classList.add("d-flex", "justify-content-end", "mb-1");
                sheet.prepend($div);
            }
        }

        return res;
    },

});

