from odoo import models, fields, api

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