import time



print('*********************************************')
print('\n')
print('\tWelcome To SQL Query Generator')
print('\n')
print('*********************************************')
time.sleep(2)
print('\n')


print('Select a Option')
Selectquery = int(input('\n 1) SELECT \n 2) INSERT IN \n 3) DELETE \n 4) UPDATE \n 5) ORDER BY \n'))


def proceedQuery(Selectquery):
    if (Selectquery == 1):
        option = int(input('Select an Option : \n 1) Specify a Table Name \n 2) Select from all Tables'))
        tableName = str(input('Enter Table Name :'))


proceedQuery(Selectquery)