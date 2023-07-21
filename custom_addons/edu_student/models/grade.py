from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from datetime import date, datetime, timedelta

class Grade(models.Model):
    _name = 'edu_student.grade'
    _description = 'edu_student grade'

    name = fields.Char(string="Name")
    rmark = fields.Text("Remark")
