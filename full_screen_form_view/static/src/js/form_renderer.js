/** @odoo-module **/


const { onMounted, useRef } = owl;
import { browser } from "@web/core/browser/browser";

import { patch } from "@web/core/utils/patch";
import { FormRenderer } from "@web/views/form/form_renderer";
patch(FormRenderer.prototype, {
    setup() {
        super.setup();
        if (browser.localStorage.getItem("full_screen") === 'true') {
            this.hideChatter = true;
        }
        else {
            this.hideChatter = false;
        }
        onMounted(() => {
            if (this.rootRef.el && this.rootRef.el.querySelectorAll('div.o-mail-Form-chatter').length === 1) {
                this._ShowHideRightPanel();
            }
        });

        this.rootRef = useRef("compiled_view_root");
    },

    _onHideRightPanel() {
        this.hideChatter = true;
        browser.localStorage.setItem("full_screen", true);
        this._ShowHideRightPanel();
    },

    _onShowRightPanel() {
        this.hideChatter = false;
        browser.localStorage.setItem("full_screen", false);
        this._ShowHideRightPanel();
    },


    _ShowHideRightPanel() {
        var listRendererDiv = document.querySelector('div.o_list_renderer');
        if (listRendererDiv) {
            listRendererDiv.style.width = '';
        }

        if (this.hideChatter) {
            document.querySelector('button.button-hide-right-panel').classList.add('d-none');
            document.querySelector('button.button-show-right-panel').classList.remove('d-none');

            var formSheetDiv = document.querySelector('div.o_form_sheet');
            if (formSheetDiv) {
                formSheetDiv.classList.add('full-screen-form');
            }

            var formSheetBgDiv = document.querySelector('div.o_form_sheet_bg');
            if (formSheetBgDiv) {
                var nextElement = formSheetBgDiv.nextElementSibling;
                if (nextElement) {
                    nextElement.classList.add('d-none');
                }
            }
        } else {
            document.querySelector('button.button-show-right-panel').classList.add('d-none');
            document.querySelector('button.button-hide-right-panel').classList.remove('d-none');

            var formSheetDiv = document.querySelector('div.o_form_sheet');
            if (formSheetDiv) {
                formSheetDiv.classList.remove('full-screen-form');
            }

            var formSheetBgDiv = document.querySelector('div.o_form_sheet_bg');
            if (formSheetBgDiv) {
                var nextElement = formSheetBgDiv.nextElementSibling;
                if (nextElement) {
                    nextElement.classList.remove('d-none');
                }
            }
        }
    },
});