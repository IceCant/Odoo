from odoo import api, fields, models
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from datetime import date, datetime, timedelta

class Generate_Class_Name(models.TransientModel):
    _name = 'edu_student.generate_class_name'
    _description = 'edu_student generate_class_name'

    grade_id = fields.Many2many("edu_student.grade")
    grade_group_id = fields.Many2many("edu_student.grade_group")
    class_type_id = fields.Many2one("edu_student.class_type")

    def generate_class(self):
        current_student = self.env['edu_student.student'].browse(self.env.context.get('active_id'))
        for gid in self.grade_id:
            for ggid in self.grade_group_id:
                vals = {
                    'name' :f"{gid.name} {ggid.name} {self.class_type_id[0].name}"
                }
                current_student.write({'class_name_id':[(0, 0, vals)]})

