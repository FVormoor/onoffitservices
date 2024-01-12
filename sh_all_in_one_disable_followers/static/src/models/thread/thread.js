/** @odoo-module **/

import { FollowButton } from "@mail/components/follow_button/follow_button";
import { patch } from "web.utils";
var rpc = require("web.rpc");

patch(FollowButton.prototype, "follow_unfollow", {
    /**
     * @override
     */

    // Pass context on Follow Button Click
    _onClickFollow(ev) {
        this._super();
        rpc.query({
            model: this.thread.model,
            method: "message_subscribe",
            args: [[this.thread.id]],
            context: { sh_follow_button_clicked: true },
        });
    },
});