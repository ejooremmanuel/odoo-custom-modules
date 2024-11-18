from odoo import models, fields, api
from datetime import date, datetime

class hr_contracts(models.Model):
    _name = 'hr.contracts'
    _description = 'HR Contract'
    _inherit = 'contract.manager'


    #contract_type = fields.Selection([('o','On Premise'),('c','Call Out')])
    #callout_type = fields.Selection([('p','Pay as You Go'),('c','Contractual')])
    # invoice_filename = fields.Char(string="File Name")
    # invoice_filename
    invoice = fields.Binary(string='Invoice', attachment=True)

    @api.depends()
    def _compute_contract_ref(self):
        for record in self:
            contract_number = record.id
            if contract_number < 10:
                record.contract_id = 'LBA/HRC/000{}'.format(contract_number)
            elif 10 == contract_number < 100:
                record.contract_id = 'LBA/HRC/00{}'.format(contract_number)
            else:
                record.contract_id = 'LBA/HRC/0{}'.format(contract_number)
    

    @api.model
    def send_notification_email(self):
        template = self.env.ref('hr_contracts.email_template_hr_contracts')
        contracts = self.env['hr.contracts'].search([('status', '=', 'running')])
        for record in contracts:
            email = record.client.email
            start_date = record.start_date 
            duration = record.duration
            today = date.today()
            is_seventy_five_due = (today - start_date).days == int(duration * 0.75)  
            is_last_day = (today - start_date).days == int(duration)  
            if template and (is_seventy_five_due or is_last_day):
                template.send_mail(res_id=record.id, email_values={'email_to': f'{email,email}'}, force_send=True)
        return True