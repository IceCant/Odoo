from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from datetime import date, datetime, timedelta

class Class_Name(models.Model):
    _name = 'edu_student.class_name'
    _description = 'edu_student class_name'

    name = fields.Char(string="Name")
    rmark = fields.Text("Remark")
