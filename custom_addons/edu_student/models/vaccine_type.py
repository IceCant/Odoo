from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from datetime import date, datetime, timedelta

class Vaccine(models.Model):
    _name = 'edu_student.vaccine_type'
    _description = 'edu_student vaccine_type'

    name = fields.Char(string="Name")
    rmark = fields.Text("Remark")