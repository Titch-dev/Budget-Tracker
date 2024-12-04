### Menus
WELCOME_MENU = '''
************************************************************************
        Please input a number corresponding to the options below:

                            1. Login
                            2. Register
                          ____________
                            Option: '''

DASHBOARD_MENU = '''
************************************************************************
                                             ___________________________
        1.  Add expense                     | {}
        2.  View expenses                   | 
        3.  View expenses by category       | Acc Balance:  R{}
        4.  Add income                      | Date:         {}
        5.  View income                     |___________________________
        6.  View income by category                 
        7.  Set budget for a category              
        8.  View budget for a category             
        9.  Set financial goals                    
        10. View progress towards financial goals 
        11. Quit
'''

### General
ERROR_MESSAGE = '''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    {}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

LOGOUT_MESSAGE = '''
************************************************************************
                Thanks for using the budget tracker,
                    {}, you are now logged out
************************************************************************
'''
### Users
ADD_USER = '''
************************************************************************
                            REGISTRATION:
'''


### Categories
ADD_CATEGORY = '''
************************************************************************
                            ADD A CATEGORY:
'''

CATEGORY_OPTION = '''
************************************************************************
        What would you like to do with category: {}
    
                        1. Update Budget
                        2. Delete Category
            Any other key. Cancel
                          ____________
                            Option: '''

SELECT_CATEGORY = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 
            Enter a 'ref' number to select a category above
                        or choose from below:
                        
                        {}. Create a new {} category
             Any other key. Cancel
                          ____________
                            Option: '''

CATEGORY_BUDGET = '''
------------------------------------------------------------------------
Category name:          {}
Month:                  {} {}
Spent:                  R{}
Budget remaining:       {}
Monthly budget set at:  R{}
------------------------------------------------------------------------
'''

### Goals
ADD_GOAL = '''
************************************************************************
                        ADD A FINANCIAL GOAL:
'''

GOAL_LIST = '''
************************************************************************
                            FINANCIAL GOALS:
'''

SELECT_GOAL = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 
        Please enter one of the above references, or enter one of
                        the below options:

                        {}. Create a new goal
             Any other key. Cancel
                          ____________
                            Option: '''

GOAL_SUMMARY = '''
------------------------------------------------------------------------
                            GOAL SUMMARY:
    
    Goal Name:          {}
    Goal Description:
        {}
        
    Goal Balance:      R{}
    Goal Target:       R{}      Remaining Target:  R{}
    Goal End:       {}      Remaining Time:     {}days
    
    {} 
------------------------------------------------------------------------'''

### Income
INCOME_ADD = '''
************************************************************************
                             ADD AN INCOME:
'''

INCOME_VIEW = '''
************************************************************************
            Please select from one of the following options:
            
                    1. Retrieve all incomes
                    2. Retrieve income by month
        Any other key. Cancel
                          ____________
                            Option: '''

INCOME_SUMMARY = '''
------------------------------------------------------------------------
                          {} INCOME SUMMARY:
                           
                           Spent
    Total amount:          R{}
    Categories'''

SELECT_INCOME = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 
        Enter one of the above 'ref' for further info on an income
                    or enter any other key to cancel
                          ____________
                            Option: '''

INCOME_OPTION = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 
                    1. Update income amount
                    2. Delete income
        Any other key. Cancel
                          ____________
                            Option: '''

### Expense
ADD_EXPENSE = '''
************************************************************************
                             ADD AN EXPENSE:
'''

EXPENSE_VIEW = '''
************************************************************************
            Please select from one of the following options:

                    1. Retrieve all expenses
                    2. Retrieve expenses by month
        Any other key. Cancel
                          ____________
                            Option: '''

EXPENSE_CATEGORY = '''
------------------------------------------------------------------------
                       VIEW EXPENSES BY CATEGORY
'''

EXPENSE_SUMMARY = '''
------------------------------------------------------------------------
                        {} EXPENSE SUMMARY:
                           
                           Spent
    Total amount:          R{}
    Categories'''

SELECT_EXPENSE = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 
    Enter one of the above 'ref' for further info on an expense
                    or enter any other key to cancel
                          ____________
                            Option: '''

EXPENSE_LIST = '''
------------------------------------------------------------------------
                        EXPENSE LIST DETAIL:
'''

EXPENSE_OPTION = '''
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 
                    1. Update expense amount
                    2. Delete expense
        Any other key. Cancel
                          ____________
                            Option: '''
