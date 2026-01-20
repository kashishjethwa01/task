from odoo import models,fields, api
from datetime import date

class EmpManagement(models.Model):
    _name = 'emp.master'
    _inherit = _inherit = ['mail.thread', 'mail.activity.mixin'] #chatter

    name = fields.Char("Name")
    phone_no = fields.Char("Phone No")
    birth_date = fields.Date("Birth Date")
    age = fields.Integer('Age', compute='compute_age')
    joining_date = fields.Date("Joining Date")
    department = fields.Char("Department")
    gross_sal = fields.Float("Gross Salary")
    allowance = fields.Float("Allowance")
    deduction = fields.Float("Deduction")
    net_salary = fields.Float("Net Salary")
    net_salary_compute = fields.Float(compute='compute_net_salary', string="Net Salary Compute", store=True,tracking=True)


    department_id = fields.Many2one('emp.department', string=" Department")
    skill_id = fields.Many2many('emp.skill', 'emp_skill_rel', 'emp_id', 'skill_id', string=" Skill")
    active = fields.Boolean('Active', default=True)
    days_in_company = fields.Integer(string="Days in Company", compute="_compute_days_in_company", store=True)


    @api.onchange('gross_sal', 'allowance', 'deduction')
    def _onchange_net_salary(self):
        self.net_salary = self.gross_sal + self.allowance - self.deduction

    @api.depends('gross_sal', 'allowance', 'deduction')
    def compute_net_salary(self):
        for rec in self:
            rec.net_salary_compute = rec.gross_sal + rec.allowance - rec.deduction

    def compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = 0


    @api.depends('joining_date')
    def _compute_days_in_company(self):
        for rec in self:
            if rec.joining_date:
                rec.days_in_company = (date.today() - rec.joining_date).days
        else:
            rec.days_in_company = 0

    def action_show_days(self):
        for rec in self:
            return
            {'type': 'ir.actions.act_window',
             'name': 'Days in Company',
             'view_mode': 'form',
             'res_model': 'emp.master',
            'res_id': rec.id,
             'target': 'current', }

