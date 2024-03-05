from odoo import models, fields, api
import xlrd


class ImportSOLinesWizard(models.TransientModel):
    _name = 'import.so.lines.wizard'
    _description = 'Import Sale Order Lines Wizard'

    file = fields.Binary(string="Excel File", required=True)
    file_path = fields.Char()

    def import_so_lines(self, file_path):
        # Membuka file Excel
        workbook = xlrd.open_workbook(file_path)
        worksheet = workbook.sheet_by_index(0)

        # Loop melalui setiap baris pada file Excel
        for row_index in range(1, worksheet.nrows):  # Mulai dari indeks 1 untuk melewati baris header
            row = worksheet.row(row_index)

            # Mendapatkan nilai dari setiap sel pada baris
            product_name = row[0].value
            quantity = row[1].value
            unit_price = row[2].value
            
        self.file_path = file_path

    def import_so(self):
        # Pastikan untuk mengganti folder_path dengan path yang sesuai
        folder_path = "/home/sekar/Documents"
        file_name = "Book1.xlsx"

        # Memanggil metode import_so_lines() dengan menyertakan file_path yang benar
        file_path = folder_path + "/" + file_name
        self.import_so_lines(file_path)
