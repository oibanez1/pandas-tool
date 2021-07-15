import gspread
import os
import pandas as pd

DIRNAME = os.path.dirname(__file__)
path = os.path.join(DIRNAME, 'credentials.json')

def upload_to_google_sheets(output_csv, google_sheet_name, user_gmail):
    #authorization
    client = gspread.service_account(path)
    #create,share,open spreadsheet. import final data to spreadsheet
    sh = client.create(google_sheet_name)
    sh.share(user_gmail, perm_type='user', role='writer')
    spreadsheet = client.open(google_sheet_name)
    content = open(output_csv, 'r').read()
    client.import_csv(spreadsheet.id, content)

raw_data_csv = input('Enter name of raw data csv: ')
output_csv = input('Enter name of output csv: ')
gmail_user = input('Enter your email address: ')
google_sheet_name = input('Enter name of google sheet name: ')

bank_data = pd.read_csv(raw_data_csv)
#get index of purchase date  and index of fees because that is where the last transaction is posted. This will give all transactions
date_index = bank_data.index[bank_data['www.citicards.com'] == 'date']
fee_index = bank_data.index[bank_data['www.citicards.com'] == 'Fees charged']
transactions = bank_data.iloc[date_index[0]:fee_index[0], 0:6]

#drop columns with no useful data, dropped duplicate row, rennamed col to reflect data within it
transactions = transactions\
    .drop(columns=['Unnamed: 1', 'Unnamed: 3', 'Unnamed: 4'])\
    .drop(4)\
    .rename(columns={'www.citicards.com':'Date', 'Unnamed: 2':'Description', 'Customer Service 1-855-473-4583':'Amount'})

transactions.to_csv(output_csv, index=False)

upload_to_google_sheets(output_csv, google_sheet_name, gmail_user)
