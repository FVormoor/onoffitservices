# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models


class MailFollowers(models.Model):
    _inherit = "mail.followers"

    # Restrict To Add Followers from Send / Receive Mail
    def _insert_followers(
        self,
        res_model,
        res_ids,
        partner_ids,
        subtypes=None,
        customer_ids=None,
        check_existing=True,
        existing_policy="skip",
    ):
        if self.env.company.sh_disable_follower_email:
            if (res_model in [
                    "sale.order",
                    "purchase.order",
                    "account.move",
                    "stock.picking",
                    "crm.lead",]
                and not self.env.context.get("sh_follow_button_clicked")
                and not self.env.context.get(
                    "sh_follow_button_clicked_message_subscribe"
                )
                and self.env.context.get("sh_follow_button_clicked_inserted")
                and not self.env.context.get("allow_manual_create")
                and not self.env.context.get("manually_added_follower") or self.env.context.get("fetchmail_cron_running") or self.env.context.get("sh_is_compose_message")
            ):
                return False
            else:
                return super(MailFollowers, self)._insert_followers(
                    res_model,
                    res_ids,
                    partner_ids,
                    subtypes=None,
                    customer_ids=None,
                    check_existing=True,
                    existing_policy="skip",
                )

        elif (
            self.env.context.get("sh_follow_button_clicked")
            and self.env.context.get("sh_follow_button_clicked_message_subscribe")
            and not self.env.context.get("sh_follow_button_clicked_inserted")
        ):
            return (
                super(MailFollowers, self)
                .with_context(sh_follow_button_clicked_inserted=True)
                ._insert_followers(
                    res_model,
                    res_ids,
                    partner_ids,
                    subtypes=None,
                    customer_ids=self.env.user.partner_id.id,
                    check_existing=True,
                    existing_policy="skip",
                )
            )
        else:
            return super(MailFollowers, self)._insert_followers(
                res_model,
                res_ids,
                partner_ids,
                subtypes=None,
                customer_ids=None,
                check_existing=True,
                existing_policy="skip",
            )
