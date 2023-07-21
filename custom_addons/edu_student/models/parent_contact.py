from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from datetime import date, datetime, timedelta

class Parent_Contact(models.Model):
    _name = 'edu_student.parent_contact'
    _description = 'edu_student parent_contact'

    fname = fields.Char(string="First Name", required=True)
    lname = fields.Char(string="Last Name", required=True)
    name = fields.Char(string="Full Name", compute="_set_name")
    r_type = fields.Selection([
        ('ma','Mother'),
        ('fa','Father'),
        ('br', 'Brother'),
        ('si', 'Sister'),
        ('o', 'other'),
    ], required=True)
    p_number = fields.Char(string="Phone Number")
    email = fields.Char(string="E-mail")
    student_id = fields.Many2one("edu_student.student")
    parent_id = fields.Many2one("edu_student.parent")

    @api.onchange('fname', 'lname')
    def _set_name(self):
        for record in self:
            if record.fname and record.lname:
                record.name = f"{record.fname} {record.lname}"