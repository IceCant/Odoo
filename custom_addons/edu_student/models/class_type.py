from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from datetime import date, datetime, timedelta

class Class_Type(models.Model):
    _name = 'edu_student.class_type'
    _description = 'edu_student class_type'

    name = fields.Char(string="Name")
    rmark = fields.Text("Remark")