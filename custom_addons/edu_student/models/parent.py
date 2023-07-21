from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from datetime import date, datetime, timedelta

class Parent(models.Model):
    _name = 'edu_student.parent'
    _description = 'edu_student parent'

    name = fields.Char(string="Full Name", copy=False)
    parent_contact_id = fields.One2many("edu_student.parent_contact","parent_id","parent contact")
    rmark = fields.Text("Remark")

    _sql_constraints = [
        ('name_unique', 'unique (name)', 'The name must be unique !')
    ]
