import pandas as pd
import numpy as np
'''
Purchase Date,   Description(company bought from),  Category?,  Amount($),  
01/12/2021       State Farm                         Insurance   -123.40
'''
bank_data = pd.read_csv('example_statement.csv')
#get index of purchase date  and index of fees because that is where the last transaction is posted. This will give all transactions
date_index = bank_data.index[bank_data['www.citicards.com'] == 'date']
fee_index = bank_data.index[bank_data['www.citicards.com'] == 'Fees charged']
transactions = bank_data.iloc[date_index[0]:fee_index[0], 0:6]

#drop columns with no useful data, dropped duplicate row, rennamed col to reflect data within it
transactions = transactions.drop(columns=['Unnamed: 1', 'Unnamed: 3', 'Unnamed: 4'])\
    .rename(columns={'www.citicards.com':'Date', 'Unnamed: 2':'Description', 'Customer Service 1-855-473-4583':'Amount'})\
    .drop(4)

print(transactions)





# transactions = transactions.drop(columns=['Unnamed: 1', 'Unnamed: 3', 'Unnamed: 4'])
# transactions = transactions.rename(columns={'www.citicards.com':'Date', 'Unnamed: 2':'Description', 'Customer Service 1-855-473-4583':'Amount'})
# transactions = transactions.drop(4)
