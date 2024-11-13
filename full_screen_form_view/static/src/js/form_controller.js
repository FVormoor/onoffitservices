/** @odoo-module **/


const { onMounted } = owl;
var localStorage = require('web.local_storage');

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
patch(FormController.prototype, "full_screen_form_view.FormController", {

    setup() {
        this._super();

        if($(this.props.archInfo.xmlDoc).find('div.oe_chatter').length == 1) {
            this.state.isChatter = true;

            if (localStorage.getItem("full_screen") === 'true') {
                this.state.hideChatter = true;
            }
            else {
                this.state.hideChatter = false;
            }

            onMounted(() => {
                this._ShowHideRightPanel();
            });
        }
        else {
            this.state.isChatter = false;
        }
    },
    _onHideRightPanel(ev) {
        ev.preventDefault();
        this.state.hideChatter = true;
        localStorage.setItem("full_screen", true);
        this._ShowHideRightPanel();
    },

    _onShowRightPanel(ev) {
        ev.preventDefault();
        this.state.hideChatter = false;
        localStorage.setItem("full_screen", false);
        this._ShowHideRightPanel();
    },

    async _ShowHideRightPanel() {
        $('div.o_list_renderer').css('width', '');

        if(this.state.hideChatter) {
            if ($('div.o_form_sheet').length) {
                $('div.o_form_sheet').addClass('full-screen-form');
            }
            if ($('div.o_form_view_container').length) {
                $('div.o_form_view_container').next().addClass('d-none');
            }
        }
        else {
            if ($('div.o_form_sheet').length) {
                $('div.o_form_sheet').removeClass('full-screen-form');
            }
            if ($('div.o_form_view_container').length) {
                $('div.o_form_view_container').next().removeClass('d-none');
            }
        }
    }
});