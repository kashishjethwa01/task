from odoo import models,fields, api
from odoo.exceptions import UserError


class Department(models.Model):
    _name = 'emp.department'
    emp_id = fields.One2many('emp.master', 'department_id', string=" Employee")

    name = fields.Char("Name")



    """def unlink(self):
        for department in self:
            if department.emp_id:
                raise UserError("Error: Employee exist")
        return super(Department, self).unlink()"""

    def unlink(self):
        for department in self:
            if department.emp_id:
                department.emp_id.unlink()
        rtn = super(Department, self).unlink()
        return rtn

