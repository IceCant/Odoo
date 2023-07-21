from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from datetime import date, datetime, timedelta

class Vaccine_Type(models.Model):
    _name = 'edu_student.vaccine'
    _description = 'edu_student vaccine'

    name = fields.Char(string="Name")
    idate = fields.Date('Date of Injection')
    rmark = fields.Text("Remark")
    vaccine_type_id = fields.Many2one("edu_student.vaccine_type")