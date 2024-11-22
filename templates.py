### Menus
WELCOME_MENU = '''
************************************************************************
        Please input a number corresponding to the options below:

                            1. Login
                            2. Register

************************************************************************
                            Option: '''

DASHBOARD_MENU = '''
************************************************************************
        Please input a number corresponding to the options below:

                1. Add expense          
                2. View expenses
                3. View expenses by category
                4. Add income
                5. View income
                6. View income by category
                7. Set budget for a category
                8. View budget for a category
                9. Set financial goals
                10. View progress towards financial goals
                11. Quit
************************************************************************
                            Option: '''

### General
ERROR_MESSAGE = '''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    {}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''

CONFIRM_MESSAGE = '''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    {}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'''

LOGOUT_MESSAGE = '''
************************************************************************
    Thanks for using the budget tracker,
        {}, you are now logged out
************************************************************************
'''
### Users


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
                    
                            Option: '''

SELECT_CATEGORY = '''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    Select a category from the above
                Enter the reference or one of the below:
                        
                        {}. Create a new category
                   Any Key. Do not assign a category
                        
                            Option: '''

CATEGORY_BUDGET = '''
------------------------------------------------------------------------
Category name:          {}
Current Month:          {}
Budget spent:          R{}
Budget remaining:      R{}
Monthly budget set at: R{}
------------------------------------------------------------------------
'''

### Goals
ADD_GOAL = '''
************************************************************************
                        ADD A FINANCIAL GOAL:
'''

SELECT_GOAL = '''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        Please enter one of the above references, or enter one of
                        the below options:

                        {}. Create a new goal
                   Any Key. Do not assign a goal
                        
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
    
    Advise saving an average of R{} per week to achieve your goal 
------------------------------------------------------------------------
                    Press return key to continue'''

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
              Any key. Cancel
                    
'''

INCOME_SUMMARY = '''
------------------------------------------------------------------------
                          INCOME SUMMARY:
'''

INCOME_SELECT = '''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        Please enter one of the above references to view an
            income or enter any other key to cancel
                        
                        Option: '''

INCOME_OPTION = '''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        1. Delete Income
                        Any Key. Cancel
                        
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

'''

EXPENSE_SUMMARY = '''
------------------------------------------------------------------------
                        {} EXPENSE SUMMARY:
                           
                           Spent
    Total amount:          R{}
    Categories'''

SELECT_EXPENSE = '''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        Please enter one of the above references to view an
            expense or enter any other key to cancel

                        Option: '''

EXPENSE_OPTION = '''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    1. Update expense amount
                    2. Delete expense
                    Any other key. Cancel
                        
                        Option: '''
