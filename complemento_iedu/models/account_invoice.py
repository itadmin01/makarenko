# -*- coding: utf-8 -*-
from odoo import fields, models, api,_ 

class AccountMove(models.Model):
    _inherit = 'account.move'

    iedu_habilitar = fields.Boolean(string="IEDU")
    nombre_alumno = fields.Char(string="Nombre")
    apellido_alumno = fields.Char(string="Apellidos")
    curp_alumno = fields.Char(string="CURP")
    nivelEducativo = fields.Char(string="Nivel educativo")
    autRVOE = fields.Char(string="RVOE")

    @api.model
    def to_json(self):
        res = super(AccountMove,self).to_json()
        if self.iedu_habilitar:
            res.update({
                'iedu10': {
                    'nombreAlumno': self.nombre_alumno + ' '+ self.apellido_alumno,
                    'CURP': self.curp_alumno,
                    'rfcPago': self.partner_id.vat,
                    'nivelEducativo': self.nivelEducativo,
                    'autRVOE': self.autRVOE,
                 },
             })
        return res

