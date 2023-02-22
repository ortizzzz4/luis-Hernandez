# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string="Title",required=True)
    
    description = fields.Text(string="Description")
    
    level = fields.Selection(string="Level", selection=[('beginner','Beginner'),
                                                        ('intermediate','Intermediate'),
                                                        ('advanced','Advanced')],
                             copy=False)
    
    active = fields.Boolean(string="Active", default=True)
    
    base_price = fields.Float(string="Base Price", default=0.00)
    
    additional_free = fields.Float(string="Additional Fee", default=10.00)
    
    total_price = fields.Float(string="Total Price", readonly=True)
    
    sessions_ids = fields.One2many(comodel_name="academy.session",
                                   inverse_name="course_id", string="Sessions")
     
     
    @api.onchange('base_price','additional_free')
    def _onchannge_total_price(self):
        if self.base_price < 0.0:
            raise UserError("Base Price cannot be set a Negative")
        
        self.total_price = self.base_price + self.additional_free
        
    @api.constrains('additional_free')
    def _check_additional_free(self):
        for record in self:
            if record.additional_free < 10.00:
                raise ValidationError(f"Additional free cannto be less than 10.00 U$S {record.additional_free}")
    