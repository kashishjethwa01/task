from odoo import models,fields, api
import base64
import csv
import io


class Emprec(models.TransientModel):
    _name = 'emp.master.wizard'

    file = fields.Binary(string="Upload CSV File", required=True)
    filename = fields.Char(string="Filename")

    name = fields.Char("Name")
    department = fields.Char("Department")
    join_date = fields.Date("Joining Date")
    gross_sal = fields.Float("Gross Salary")
    allowance = fields.Float("Allowance")
    deduction = fields.Float("Deduction")

    emp_data_file = fields.Binary("Employee Data file")

    def action_import_employees(self):
        data = base64.b64decode(self.file)
        file_input = io.StringIO(data.decode("utf-8"))
        reader = csv.DictReader(file_input)

        for row in reader:
            name = row.get('Name')
            department = row.get('Department')
            joining_date = row.get('Joining Date')
            gross_sal = float(row.get('Gross Salary', 0))
            allowance = float(row.get('Allowance', 0))
            deduction = float(row.get('Deduction', 0))


            self.env['emp.master'].create({
                    'name': name,
                    'department_id': self.env['emp.department'].search([('name', '=', department)], limit=1).id,
                    'joining_date': joining_date,
                    'gross_sal': gross_sal,
                    'allowance': allowance,
                    'deduction': deduction,
                })

            emp_master_pool = self.env['emp.master']
            emp_master_pool.create(
                {'name': row['Name'], 'department': row['Department'], 'joining_date': row['Joining Date'],
                 'gross_sal': float(row['Gross_Salary']), 'allowance': float(row['Allowance']),
                 'deduction': float(row['Deduction']), })




