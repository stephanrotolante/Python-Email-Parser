import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


class connect():

    def __init__(self, sheetName):
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("lacrosse-email-data-a3cd09b85cf8.json", scope)

        self.sheetName = sheetName

        self.client = gspread.authorize(creds)

        self.sheet = self.client.open(sheetName).sheet1

        self.currentRow= self.nextRow()

    def printAllRecords(self):
        records = self.sheet.get_all_records()

        pprint(records)

    def updateCell(self,row,col,data):

        self.sheet.update_cell(row,col,data)

    def nextRow(self):
        str_list = filter(None,self.sheet.col_values(1))
        return int(len(str_list)+1)

    def nextCol(self):
        str_list = filter(None, self.sheet.row_values(self.currentRow))
        col_num = int(len(str_list) + 1)

        if  col_num == 12:
            self.currentRow = self.nextRow()
            return 1
        else:
            return col_num
