# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = "academy.course"
    _description = "Course Info "
    
    name = fields.Char(string = 'Title', required=True)
    description = fields.Text(string= 'Description')
    
    level = fields.Selection(string='Level',
                            selection =[('beginner', 'Beginner'),
                                        ('intermediate','Intermediate'),
                                       ('advance','Advance')],   
                            copy=False)
    active = fields.Boolean(string='Active', default=True)
    
    country = fields.Selectio=(string='Level',selection =[('El Salvador', 'San Salvador'),
                                        ('Guatemala','Guatemala'),
                                       ('Mexico','Mexico DF')],   )