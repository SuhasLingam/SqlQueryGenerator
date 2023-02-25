import time


global SelectWhereClause
print('*********************************************')
print('\n')
print('\tWelcome To SQL Query Generator')
print('\n')
print('*********************************************')
time.sleep(0)
print('\n')
print('Select a Option')
Selectquery = int(input(
    '\n 1) SELECT \n 2) INSERT IN \n 3) DELETE \n 4) UPDATE \n 5) ORDER BY \n\n SelectedQuery = '))


def GlobalTableName():
    global tableName
    tableName = str(input('\nEnter Table Name : '))

def addWhereClause():
    global whereClause
    print("\nEnter the Condition\nExample: name = 'John' \n")
    whereClause = str(input("Condition = "))

def SelectQueryFunct():
    print(' \nSelect Option \n')
    option = int(input('1) Specify Column \n2) From All\n\n SelectedOption = '))
    if (option == 1):
        ColumnName = str(input('\nEnter the Column Name : '))
        SelectWhereClause = int(input("\nDo You Want To Include Where Clause ? \n 1) YES 2) NO \n Selected Option : "))
        
        if(SelectWhereClause == 1):
            addWhereClause()
            print('\nYour Final Query is \n')
            print(f'SELECT {ColumnName} FROM {tableName} WHERE {whereClause}; \n')
        
        
    else:
        SelectWhereClause = int(input("\nDo You Want To Include Where Clause ? \n 1) YES 2) NO \n Selected Option : "))
        if(SelectWhereClause == 1):
            addWhereClause()
            print('\nYour Final Query is \n')
            print(f'SELECT * FROM {tableName} WHERE {whereClause}; \n')
        else:    
            print('\nYour Final Query is \n')
            print(f'SELECT * FROM {tableName}; \n')

def proceedQuery(Selectquery):
    if (Selectquery == 1):
        GlobalTableName()
        SelectQueryFunct()


proceedQuery(Selectquery)
