import imaplib
import HTML_PARSER
import re
import boto3

number ='+13216840161'
print type(number)
client = boto3.client('sns', 'us-east-1')
client.publish(PhoneNumber='+13216840161', Message='Good-bye')
# #
#
#
#
#
# parser = HTML_PARSER.MyHTMLParser()
# mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
# usn = 'unflacrosserecruitment'
# pas = 'Magicman123456!'
# mail.login(usn, pas)
# # # This will display the list of inboxes
# # # for i in mail.list()[1]:
# # #     l = i.decode().split(' "/" ')
# # #     print(l[0] + " = " + l[1])
# # # #
# mail.select('Recruitment')
# result, data = mail.uid('search',None,"ALL")
# # print  data[0]
# inbox_items = data[0].split()
# print  inbox_items
# # for email in inbox_items:
# fetchResult, fetchData = mail.uid("fetch",inbox_items[14], '(RFC822)')
# message = re.sub("\s+", " ",fetchData[0][1].replace('=\r\n', "").replace('=0D', "").replace('=E2=80=99', "")).decode("utf-8")
# parser.feed(message)