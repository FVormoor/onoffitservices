# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models

class MailComposer(models.TransientModel):
    """ Wizard to invite partners (or channels) and make them followers. """
    _inherit = 'mail.compose.message'

    def _action_send_mail(self, auto_commit=False):
        
        
        if self.env.company.sh_disable_follower_email :
            if not self.env.context.get("sh_is_compose_message"):
                additionnal_context = {'sh_is_compose_message': True}
                return super(MailComposer, self).with_context(**additionnal_context)._action_send_mail(auto_commit=auto_commit)
            else:
                return super(MailComposer, self)._action_send_mail(auto_commit=auto_commit)
        else:    
            return super(MailComposer, self)._action_send_mail(auto_commit=auto_commit)
