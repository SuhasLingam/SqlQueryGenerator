import time


print('*********************************************')
print('\n')
print('\tWelcome To SQL Query Generator')
print('\n')
print('*********************************************')
time.sleep(2)
print('\n')
print('Select a Option')
Selectquery = int(input('\n 1) SELECT \n 2) INSERT IN \n 3) DELETE \n 4) UPDATE \n 5) ORDER BY \n\n SelectedQuery = '))


def GlobalTableName():
    global tableName
    tableName = str(input('\nEnter Table Name : '))
    
            
def proceedQuery(Selectquery):
    if (Selectquery == 1):
        GlobalTableName()
        print(' \nSelect Option \n')
        option = int(input('1) Specify Column \n2) From All\n\n SelectedOption = '))
        if(option == 1):
            ColumnName = str(input('\nEnter the Column Name : '))
            print('\nYour Final Query is \n')
            print(f'SELECT {ColumnName} FROM {tableName}; \n')
                
            
            
proceedQuery(Selectquery)