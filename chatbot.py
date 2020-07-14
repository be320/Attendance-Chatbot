from rivescript import RiveScript
import gspread 
from oauth2client.service_account import ServiceAccountCredentials
import pprint

pp = pprint.PrettyPrinter()
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Chatbot-Attendance-aeb274912a52.json', scope)

client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Attendance").sheet1

# Extract and print all of the values
attendance = sheet.get_all_records()
pp.pprint(attendance)

bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()
id = "undefined"
name = "undefined"


while True:
    msg = str(input('You> '))
    print('Bot>'+bot.reply('localuser', msg))
    id = bot.get_uservar('localuser', 'id')
    name = bot.get_uservar('localuser', 'name')
    if (id != "undefined" and name != "undefined"):
        row = [id,name]
        index = len(attendance)+2
        sheet.insert_row(row, index) 
        break



