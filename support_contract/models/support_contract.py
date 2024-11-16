from odoo import models, fields, api
from datetime import date, datetime

class support_contract(models.Model):
    _name = 'support.contract'
    _description = 'Support Contract'
    _inherit = 'contract.manager'


    contract_type = fields.Selection([('o','On Premise'),('c','Call Out')])
    callout_type = fields.Selection([('p','Pay as You Go'),('c','Contractual')])
    # invoice_filename = fields.Char(string="File Name")
    # invoice_filename
    invoice = fields.Binary(string='Invoice', attachment=True)

    @api.depends()
    def _compute_contract_ref(self):
        for record in self:
            contract_number = record.id
            if contract_number < 10:
                record.contract_id = 'LBA/SUPPORT/CONTRACT/00{}'.format(contract_number)
            elif 10 == contract_number < 100:
                record.contract_id = 'LBA/SUPPORT/CONTRACT/0{}'.format(contract_number)
            else:
                record.contract_id = 'LBA/SUPPORT/CONTRACT/{}'.format(contract_number)
    

    @api.model
    def send_notification_email(self):
        template = self.env.ref('contract_manager.email_template_contract')
        # contracts = self.search_read([('status', '=', 'running')])
        # print (self.env['mail.mail'].search_read([]))
        print (self.env['support.contract'].search_read([]))
        print(contracts)
        for record in contracts:
            print(record,template,"jrertt")
            today = date.today()
            is_seventy_five_due = (today - record.start_date).days == int(record.duration * 0.75)  
            is_last_day = (today - record.start_date).days == int(record.duration)  
            is_check = record.end_date == today 
            if template and is_check:
                template.send_mail(record.id, force_send=True)
                print('here??')
        return True