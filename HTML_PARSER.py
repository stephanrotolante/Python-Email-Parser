from HTMLParser import HTMLParser
import google_sheets_api
from time import sleep
import boto3
import re


class MyHTMLParser(HTMLParser):

    def __init__(self):

        HTMLParser.__init__(self)

        client = boto3.client('sns', 'us-east-1')

        self.spreadSheet = google_sheets_api.connect("email-data")

        self.client = client

        self.lastEntry = ""



    def handle_data(self, data):


        list_Of_Tokens = ["Name:","Email:","Address:","State:","High School:","High School graduation Year:","Have you applied to UNF:","Cell Phone:","Position:","Tell us about your lacrosse career (i.e. years of experience, stats, accomplishments):","Link to Highlight Tape (If you do not have one insert N/A):"]
        if self.lastEntry in list_Of_Tokens:
            if self.lastEntry == "Name:":
                self.name = data
            elif self.lastEntry == "Email:":
                self.email = data
            elif self.lastEntry == "High School:":
                self.hs = data
            elif self.lastEntry == 'Cell Phone:':

                # self.cell = '+1'+re.sub("\s+", "", data.replace("-","")).encode('utf-8')
                self.cell = '+13216840161'
                print boto3.client('sns', 'us-east-1').publish(PhoneNumber='+13216840161', Message='Hey')
                # print self.cell
                # print type(self.cell)
                # print self.client.publish(PhoneNumber='+13216840161', Message='Hey ')
                sleep(2)
            elif self.lastEntry == 'High School graduation Year:':
                self.hgyr = data
            elif self.lastEntry == 'State:':
                self.state = data
            elif self.lastEntry == "Position:":
                self.pos = data
            elif self.lastEntry == "Have you applied to UNF:":
                self.applied = data
            elif self.lastEntry == "Link to Highlight Tape (If you do not have one insert N/A):":
                print 1
                # print self.client.publish(PhoneNumber='+19046145732',
                #                      Message='Name:\n'+self.name
                #                           +'\nEmail:\n'+self.email
                #                           +'\nHigh School:\n'+self.hs
                #                           +'\nCell:\n'+self.cell
                #                           +'\nGraduation Year:\n'+self.hgyr
                #                           +'\nState:\n'+self.state
                #                           +'\nPosition:\n'+self.pos
                #                           +'\nHave You Applied to UNF:\n'+self.applied)

            col = self.spreadSheet.nextCol()
            row = self.spreadSheet.currentRow
            self.spreadSheet.updateCell(row, col, data)
            sleep(2)

        self.lastEntry = data

