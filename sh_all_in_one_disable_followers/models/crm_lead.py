# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        res = super(CrmLead, self).create(vals)
        if res.user_id and self.env.company.sh_disable_follower_lead:
            res.message_unsubscribe(
                [res.user_id.partner_id.id, self.env.user.partner_id.id])
        return res

    def write(self, vals):
        if vals.get('user_id', False):
            user_id = self.env['res.users'].sudo().search(
                [('id', '=', vals.get('user_id', False))], limit=1)
            if user_id and self.env.company.sh_disable_follower_lead:
                res = super(CrmLead, self).write(vals)
                if self:
                    for rec in self:
                        rec.message_unsubscribe(
                            [user_id.partner_id.id, self.env.user.partner_id.id])
                return res
        return super(CrmLead, self).write(vals)

    def message_subscribe(
        self,
        partner_ids=None,
        subtype_ids=None
    ):
        if self.env.company.sh_disable_follower_lead and self.env.context.get('mail_post_autofollow') and not self.env.context.get('sh_follow_button_clicked') and not self.env.context.get('allow_manual_create') and not self.env.context.get('manually_added_follower'):
            if partner_ids and len(partner_ids) == 1 and self.env.user.partner_id.id == partner_ids[0]:
                return super(CrmLead, self).message_subscribe(
                    partner_ids, subtype_ids
                )
            else:
                return False
        if self.env.context.get('sh_follow_button_clicked') and not self.env.context.get('sh_follow_button_clicked_message_subscribe'):
            if not subtype_ids:
                self.env['mail.followers'].with_context(sh_follow_button_clicked=True)._insert_followers(
                    self._name, self.ids,
                    partner_ids, subtypes=None,
                    customer_ids=partner_ids, check_existing=True, existing_policy='skip')
            else:
                self.env['mail.followers'].with_context(sh_follow_button_clicked=True)._insert_followers(
                    self._name, self.ids,
                    partner_ids, subtypes=dict((pid, subtype_ids)
                                            for pid in partner_ids),
                    customer_ids=partner_ids, check_existing=True, existing_policy='replace')

            res = super(CrmLead, self).with_context(sh_follow_button_clicked_message_subscribe=True).message_subscribe(
                partner_ids=partner_ids, subtype_ids=subtype_ids)
            return res
        elif self.env.context.get('allow_manual_create') and self.env.context.get('manually_added_follower'):
            return super(CrmLead, self).message_subscribe(
                partner_ids, subtype_ids
            )
        else:
            return super(CrmLead, self).message_subscribe(
                partner_ids, subtype_ids
            )
