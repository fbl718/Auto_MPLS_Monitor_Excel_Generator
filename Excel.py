import xlsxwriter


class Excel(object):
    # Initialization of column sizes, fonts and image properties, which are all set manually.
    def __init__(self, name):
        self.book = xlsxwriter.Workbook(name)
        self.sheet = self.book.add_worksheet()
        self.sheet.set_column("A:A", 26.25)
        self.sheet.set_column("B:C", 4.63)
        self.sheet.set_column("D:D", 6.88)
        self.sheet.set_column("E:F", 19)
        self.sheet.set_column("G:H", 26.88)
        self.sheet.set_column("I:J", 25.63)
        self.sheet.set_column("K:K", 9.88)
        self.sheet.set_column("L:L", 23.88)
        self.property = {
            'font_size': 12,
            'bold': False,
            'align': 'center',
            'valign': 'vcenter',
            'font_name': '宋体',
            'text_wrap': False,
        }
        self.cell_format = self.book.add_format(self.property)
        self.img_format = {
            'x_offset': 15,
            'y_offset': 0,
            'x_scale': 0.15,
            'y_scale': 0.15,
            'url': None,
            'tip': None,
            'image_data': None,
            'positioning': None
        }

    # Write column names.
    def write_column_name(self, colums_name):
        for i in range(0, len(colums_name)):
            self.sheet.write(0, i, colums_name[i], self.cell_format)

    # Write data.
    def write_content(self, row_num, data):
        for i in range(0, len(data)):
            self.sheet.write(row_num, i, data[i], self.cell_format)

    # Insert images.
    def insert_image(self, row_num, col_num, image):
        self.sheet.insert_image(row_num, col_num, image, self.img_format)

    # Close file.
    def close(self):
        self.book.close()
