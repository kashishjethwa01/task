from odoo import models, fields


class Skill(models.Model):
    _name = 'emp.skill'

    name = fields.Char("Name")
    emp_id = fields.Many2many('emp.master', 'emp_skill_rel', 'skill_id', 'emp_id', string=" Employees")