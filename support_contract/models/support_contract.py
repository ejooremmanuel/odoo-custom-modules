from odoo import models, fields, api

class support_contract(models.Model):
    _name = 'support.contract'
    _description = 'Support Contract'
    _inherit = 'contract.manager'

    contract_type = fields.Selection([('o','On Premise'),('c','Call Out')])
    callout_type = fields.Selection([('p','Pay as You Go'),('c','Contractual')])
    invoice = fields.Binary(string='Invoice')
