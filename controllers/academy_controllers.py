# -*- coding: utf-8 -*-
from odoo import http

class ACademy(http.Controller):
    @http.route('/academy', auth='public', website=True)
    def index(self, **kw):
        return "hello"
    
    @http.route('/academy/courses/', auth='public', website=True)
    def courses(self, **kw):
        courses = http.request.env['academy.course'].search([])
        return http.request.render('odoo_acade.course_website',{
            'courses':courses,
        })

    @http.route('/academy/<model("academy.session"):session>/', auth='public', website=True)
    def session(self, session):
        return http.request.render('odoo_acade.session_website',{
            'session':session,
        })