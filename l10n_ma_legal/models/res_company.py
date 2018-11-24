# -*- coding: utf-8 -*-
from odoo import models, fields
    
class ResCompany(models.Model):
    _inherit = 'res.company'
    
    tp = fields.Char(string='TP')
    ice = fields.Char(string='ICE')
    cnss = fields.Char(string='CNSS')

