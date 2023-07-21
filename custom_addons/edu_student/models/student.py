from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from datetime import date, datetime, timedelta

class Student(models.Model):
    _name = 'edu_student.student'
    _description = 'edu_student student'
    fname = fields.Char(string="First Name", required=True)
    lname = fields.Char(string="Last Name", required=True)
    name = fields.Char(string="Full Name", compute="_set_name")
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female'),
    ], required=True, default='male')
    dob = fields.Date('Date of Birth', required=True)
    age = fields.Char(string="Age",readonly=True)
    vaccine_id = fields.Many2many("edu_student.vaccine")
    parent_id = fields.Many2one("edu_student.parent")
    parent_contact_id = fields.One2many("edu_student.parent_contact","student_id","parent contact")
    class_name_id = fields.Many2many("edu_student.class_name")
    class_name = fields.Char(string="Class Name")

    @api.onchange('dob')
    def _set_age(self):
        for record in self:
            if record.dob:
                current_date = date.today()
                dob_f = record.dob
                age = current_date.year - dob_f.year
                if age <= 0:
                    raise ValidationError("Invalid Date of Birth")
                elif age == 1:
                    record.age = f'{age} year old'
                elif age > 1:
                    record.age = f'{age} years old'

    @api.onchange('fname', 'lname')
    def _set_name(self):
        for record in self:
            if record.fname and record.lname:
                record.name = f"{record.fname} {record.lname}"

    def generate(self):
        return {
            'res_model': 'edu_student.generate_class_name',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref("edu_student.generate_form").id,
            'target': 'new'
        }
    def gen_class(self):
        self.class_name_id