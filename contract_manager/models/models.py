# -*- coding: utf-8 -*-

from odoo import models, fields, api


class contract_manager(models.Model):
    _name = 'contract.manager'
    _description = 'Contract Manager'

    name = fields.Char(string='Title',required=True)
    start_date = fields.Date(string='Start Date',required=True)
    client = fields.Many2one('res.partner',string='Client',required=True)
    note = fields.Text(string='Additional Note')
    status = fields.Selection([("running","Running"),("completed","Completed"),("paused","Paused")], default="running", )
    amount = fields.Monetary(string='Amount',currency_field="currency_id",required=True)
    supporting_document = fields.Many2many("ir.attachment",string="Supporting Documents",)
    end_date = fields.Date(string='End Date',required=True)
    duration = fields.Integer(string='Duration', readonly=True, compute='_compute_duration')
    currency_id = fields.Many2one('res.currency',string='Currency',required=True)
    contract_id = fields.Char(string="Contract Ref", readonly=True, compute='_compute_contract_ref' )
       
    
    @api.depends('start_date','end_date')
    def _compute_duration (self):
        for record in self:
            record.duration = (record.end_date - record.start_date).days if record.start_date and record.end_date else 0
    
    
    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     res = super(contract_manager, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
    #     if view_type == 'form':
    #         for field in res['fields']:
    #             if field == 'end_date':
    #                 min_date = self.env.context.get('default_start_date', fields.Date.today())
    #                 res['fields'][field]['options'] = {'min_date': str(min_date)}
    #     return res

     def send_notification_email(self):
        template = self.env.ref('contract.email_template_leave')
        for record in self:
            # Check if the template exists
            const today = date.today()
            if template:
                template.send_mail(record.id, force_send=True)