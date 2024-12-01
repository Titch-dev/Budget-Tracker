import sqlite3
from unittest import TestCase

from models.user import User
from models.category import Category
from models.goal import Goal
from models.income import Income
from models.expense import Expense

from db_access import get_income_by_id, get_goal_by_id, \
    get_category_by_id, get_expense_by_id, get_user_by_username, \
    get_user_categories, get_user_expenses, get_user_goals, get_user_income, \
    delete_category, delete_expense, delete_income, \
    update_category, update_expense, update_income, \
    create_user, create_goal, create_category, create_expense, create_income, \
    get_expenses_by_category, get_income_by_category, get_expenses_by_month, get_user_categories_by_type, \
    update_income_category_to_null, update_expenses_category_to_null, get_sum_of_user_incomes, \
    get_income_by_month, get_expenses_by_goal, get_sum_of_user_expenses_to_date

from db_build import CREATE_USER_TABLE, CREATE_CATEGORY_TABLE, CREATE_GOAL_TABLE, \
    CREATE_INCOME_TABLE, CREATE_EXPENSE_TABLE, INSERT_USER, INSERT_CATEGORIES, \
    INSERT_GOAL, INSERT_INCOMES, INSERT_EXPENSES, INITIAL_USER, INITIAL_CATEGORIES, \
    INITIAL_GOAL, INITIAL_INCOME, INITIAL_EXPENSES


class TestDBAccess(TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('budget_tracker.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS user")
        self.cursor.execute(CREATE_USER_TABLE)
        self.cursor.execute("DROP TABLE IF EXISTS category")
        self.cursor.execute(CREATE_CATEGORY_TABLE)
        self.cursor.execute("DROP TABLE IF EXISTS goal")
        self.cursor.execute(CREATE_GOAL_TABLE)
        self.cursor.execute("DROP TABLE IF EXISTS expense")
        self.cursor.execute(CREATE_EXPENSE_TABLE)
        self.cursor.execute("DROP TABLE IF EXISTS income")
        self.cursor.execute(CREATE_INCOME_TABLE)
        self.cursor.execute(INSERT_USER, INITIAL_USER)
        self.cursor.executemany(INSERT_CATEGORIES, INITIAL_CATEGORIES)
        self.cursor.execute(INSERT_GOAL, INITIAL_GOAL)
        self.cursor.executemany(INSERT_EXPENSES, INITIAL_EXPENSES)
        self.cursor.executemany(INSERT_INCOMES, INITIAL_INCOME)
        self.conn.commit()

    def tearDown(self):
        self.conn.commit()
        self.conn.close()

    ### User queries ###
    def test_get_user_by_username(self):
        expected_username = 'McFly'
        expected_password = 'delorean'
        actual = get_user_by_username('McFly')

        self.assertEqual(expected_username, actual.username)
        self.assertEqual(expected_password, actual.password)

    def test_create_user(self):
        user = User.create(username='Biff', password='almanac')
        create_user(user)
        actual = get_user_by_username('Biff')

        self.assertTrue(actual)
        self.assertEqual(user.username, actual.username)
        self.assertEqual(user.password, actual.password)

    ### Category queries ###
    def test_get_category_by_id(self):
        expected_name = 'Salary'
        actual = get_category_by_id(1)

        self.assertEqual(expected_name, actual.name)

    def test_create_category(self):
        expected = Category.create(name='test',
                                   desc='test desc',
                                   budget=0.00,
                                   cat_type='income',
                                   user_id=1)
        new_id = create_category(expected)
        actual = get_category_by_id(new_id)

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.budget, actual.budget)
        self.assertEqual(expected.cat_type, actual.cat_type)
        self.assertEqual(expected.user_id, actual.user_id)

    def test_get_user_categories(self):
        expected_categories = [Category(id=1,
                                         name='Salary',
                                         desc='Monthly salary payment.',
                                         budget=0.0,
                                         cat_type='income',
                                         created_at=None,
                                         user_id=1),
                                Category(id=2,
                                         name='Rent',
                                         desc='Monthly rental payment.',
                                         budget=0.0,
                                         cat_type='expense',
                                         created_at=None,
                                         user_id=1),
                                Category(id=3,
                                         name='Utilities',
                                         desc='Electricity, water, and gas bills.',
                                         budget=0.0,
                                         cat_type='expense',
                                         created_at=None,
                                         user_id=1),
                                Category(id=4,
                                         name='Dining Out',
                                         desc='Eating out at restaurants and cafes.',
                                         budget=150.0,
                                         cat_type='expense',
                                         created_at=None,
                                         user_id=1),
                                Category(id=5,
                                         name='Health & Fitness',
                                         desc='Gym membership and health-related expenses.',
                                         budget=0.0,
                                         cat_type='expense',
                                         created_at=None,
                                         user_id=1),
                                Category(id=6,
                                         name='Goals',
                                         desc='Working towards financial goals.',
                                         budget=0.0,
                                         cat_type='expense',
                                         created_at=None,
                                         user_id=1)]

        actual_categories = get_user_categories(1)

        self.assertEqual(len(expected_categories), len(actual_categories), "The list lengths do not match")

        for expected, actual in zip(expected_categories, actual_categories):
            self.assertEqual(expected.name, actual.name)
            self.assertEqual(expected.desc, actual.desc)
            self.assertEqual(expected.budget, actual.budget)
            self.assertEqual(expected.cat_type, actual.cat_type)
            self.assertEqual(expected.user_id, actual.user_id)

    def test_update_category(self):
        expected = get_category_by_id(1)
        expected.name = 'test'
        expected.budget = 100
        update_category(expected)
        actual = get_category_by_id(1)

        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.budget, expected.budget)

        pass

    def test_delete_category(self):
        category_id = 1
        delete_category(category_id)
        actual = get_category_by_id(category_id)

        self.assertFalse(actual)

    def test_get_user_categories_by_type(self):
        expected = [Category(id=1,
                             name='Salary',
                             desc='Monthly salary payment.',
                             budget=0.0,
                             cat_type='income',
                             created_at=None,
                             user_id=1)]
        actual = get_user_categories_by_type(1, 'income')

        self.assertEqual(len(expected), len(actual), "The list lengths do not match")

        for actual, expected in zip(expected, actual):
            self.assertEqual(expected.name, actual.name)
            self.assertEqual(expected.desc, actual.desc)
            self.assertEqual(expected.budget, actual.budget)
            self.assertEqual(expected.cat_type, actual.cat_type)
            self.assertEqual(expected.user_id, actual.user_id)

    ##### Goals queries #####
    def test_get_goal_by_id(self):
        goal_id = 1
        expected_name = 'Vacation Fund'
        expected_target = 5000.00
        actual = get_goal_by_id(goal_id)

        self.assertEqual(actual.id, goal_id)
        self.assertEqual(actual.name, expected_name)
        self.assertEqual(actual.target, expected_target)

    def test_create_goal(self):
        expected = Goal.create(name='test',
                               desc='test desc',
                               target=100.00,
                               end_date=None,
                               user_id=1)
        new_id = create_goal(expected)
        actual = get_goal_by_id(new_id)

        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.desc, expected.desc)
        self.assertEqual(actual.target, expected.target)
        self.assertEqual(actual.user_id, expected.user_id)

    def test_get_user_goals(self):
        expected_goals = [Goal(id=1,
                         name='Vacation Fund',
                         desc='Saving for a vacation trip to Hawaii.',
                         target=5000.0,
                         end_date="2025-06-01 00:00:00",
                         created_at="2024-10-31 17:40:26",
                         user_id=1)]
        actual_goals = get_user_goals(1)

        self.assertEqual(len(actual_goals), len(expected_goals), "The list lengths do not match")

        for actual, expected in zip(actual_goals, expected_goals):
            self.assertEqual(actual.name, expected.name)
            self.assertEqual(actual.desc, expected.desc)
            self.assertEqual(actual.target, expected.target)
            self.assertEqual(actual.user_id, expected.user_id)

    ##### Income queries #####
    def test_get_income_by_id(self):
        expected = Income(id=1,
                          name='Work Salary',
                          amount=2000.0,
                          effect_date='2024-06-25',
                          created_at=None,
                          user_id=1,
                          cat_id=1,
                          cat_name='Salary')
        actual = get_income_by_id(1)

        self.assertEqual(actual.id, expected.id)
        self.assertEqual(actual.amount, expected.amount)
        self.assertEqual(actual.user_id, expected.user_id)
        self.assertEqual(actual.cat_name, expected.cat_name)

    def test_create_income(self):
        expected = Income.create(name='test',
                                 amount=10.00,
                                 effect_date="2025-09-09",
                                 user_id=1)
        new_id = create_income(expected)
        actual = get_income_by_id(new_id)

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.amount, actual.amount)
        self.assertEqual(expected.user_id, actual.user_id)

    def test_get_user_income(self):
        expected = Income(id=1,
                          name='Work Salary',
                          amount=2000.0,
                          user_id=1,
                          effect_date='2024-06-25',
                          created_at=None,
                          cat_id=1,
                          cat_name='Salary')
        actual = get_user_income(1)

        self.assertEqual(expected.id, actual[0].id)
        self.assertEqual(expected.user_id, actual[0].user_id)
        self.assertEqual(expected.cat_id, actual[0].cat_id)

    def test_get_income_by_category(self):
        expected = Income(id=1,
                          name='Work Salary',
                          amount=2000.0,
                          effect_date='2024-06-25',
                          created_at=None,
                          user_id=1,
                          cat_id=1,
                          cat_name='Salary')
        actual = get_income_by_category(1)

        self.assertEqual(expected.id, actual[0].id)
        self.assertEqual(expected.user_id, actual[0].user_id)
        self.assertEqual(expected.cat_id, actual[0].cat_id)

    def test_update_income(self):
        expected = get_income_by_id(1)
        expected.name = 'test'
        expected.amount = 1200.00
        expected.cat_id = 6
        expected.cat_name = 'Goals'

        update_income(expected)
        actual = get_income_by_id(1)

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.amount, actual.amount)
        self.assertEqual(expected.cat_name, actual.cat_name)

    def test_update_income_category_to_null(self):
        expected = Income(id=1,
                          name="Work Salary",
                          amount=2000.00,
                          effect_date="2024-06-25",
                          created_at=None,
                          user_id=1,
                          cat_id=None,
                          cat_name=None)

        update_income_category_to_null(cat_id=1)
        actual = get_income_by_id(income_id=1)

        self.assertEqual(expected.id, actual.id)
        self.assertEqual(expected.cat_id, actual.cat_id)
        self.assertEqual(expected.cat_name, actual.cat_name)

    def test_delete_income(self):
        income_id = 1
        delete_income(income_id)
        actual = get_income_by_id(income_id)

        self.assertFalse(actual)

    def test_get_income_by_month(self):
        month = '2024-10'
        expected = [Income(id=5,
                           name='Work Salary',
                           amount=2000.0,
                           effect_date='2024-10-25',
                           created_at=None,
                           user_id=1,
                           cat_id=1,
                           cat_name='Salary')]
        actual = get_income_by_month(1, month)

        self.assertEqual(len(expected), len(actual))

        for expected, actual in zip(expected, actual):
            self.assertEqual(expected.id, actual.id)
            self.assertEqual(expected.name, actual.name)
            self.assertEqual(expected.id, actual.id)

    def test_get_sum_of_user_incomes(self):
        expected = 10000
        actual = get_sum_of_user_incomes(1)

        self.assertEqual(expected, actual)

    ##### Expense queries #####
    def test_get_expense_by_id(self):
        expense_id = 1
        expected = Expense.create(name='Rent',
                                  amount=1200.0,
                                  effect_date='2024-07-01',
                                  user_id=1)
        actual = get_expense_by_id(expense_id)

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.amount, actual.amount)
        self.assertEqual(expected.effect_date, actual.effect_date)
        self.assertEqual(expected.user_id, actual.user_id)

    def test_create_expense(self):
        expected = Expense.create(name='test',
                                  amount=100.00,
                                  effect_date='2025-09-09',
                                  user_id=1)
        expense_id = create_expense(expected)
        actual = get_expense_by_id(expense_id)

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.amount, actual.amount)
        self.assertEqual(expected.effect_date, actual.effect_date)
        self.assertEqual(expected.user_id, actual.user_id)

    def test_get_user_expenses(self):
        expected = Expense(id=1,
                           name='Rent',
                           amount=1200.0,
                           effect_date='2024-07-01',
                           created_at=None,
                           user_id=1,
                           cat_id=2,
                           cat_name='Rent',
                           goal_id=None,
                           goal_name=None)
        actual = get_user_expenses(1)

        self.assertEqual(expected.id, actual[0].id)
        self.assertEqual(expected.name, actual[0].name)
        self.assertEqual(expected.amount, actual[0].amount)
        self.assertEqual(expected.effect_date, actual[0].effect_date)
        self.assertEqual(expected.user_id, actual[0].user_id)
        self.assertEqual(expected.cat_name, actual[0].cat_name)
        self.assertEqual(expected.goal_name, actual[0].goal_name)

    def test_get_expenses_by_category(self):
        expected_expenses = [
            Expense(id=15,
                    name='Gym',
                    amount=75.0,
                    effect_date='2024-10-02',
                    created_at=None,
                    user_id=1,
                    cat_id=5,
                    cat_name='Health & Fitness',
                    goal_id=None,
                    goal_name=None)
        ]
        actual_expenses = get_expenses_by_category(5)

        self.assertEqual(len(expected_expenses), len(actual_expenses), 'The lists lengths dont match')

        for expected, actual in zip(expected_expenses, actual_expenses):
            self.assertEqual(expected.id, actual.id)
            self.assertEqual(expected.name, actual.name)
            self.assertEqual(expected.amount, actual.amount)
            self.assertEqual(expected.effect_date, actual.effect_date)
            self.assertEqual(expected.user_id, actual.user_id)
            self.assertEqual(expected.cat_name, actual.cat_name)
            self.assertEqual(expected.goal_name, actual.goal_name)

    def test_update_expense(self):
        expected = get_expense_by_id(1)
        expected.name = 'test'
        expected.amount = 100.00
        expected.effect_date = '2021-09-09 20:00:00'
        expected.cat_id = 1
        expected.goal_id = 1
        update_expense(expected)
        actual = get_expense_by_id(1)

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.amount, actual.amount)
        self.assertEqual(expected.effect_date, actual.effect_date)

    def test_update_expenses_category_to_null(self):
        expected = Expense(id=15,
                           name="Gym",
                           amount=75.00,
                           effect_date="2024-10-02",
                           created_at=None,
                           user_id=1,
                           cat_id=None,
                           cat_name=None,
                           goal_id=None,
                           goal_name=None)

        update_expenses_category_to_null(cat_id=5)
        actual = get_expense_by_id(15)

        self.assertEqual(expected.id, actual.id)
        self.assertEqual(expected.cat_id, actual.cat_id)
        self.assertEqual(expected.cat_name, actual.cat_name)

    def test_delete_expense(self):
        expense_id = 1
        delete_expense(expense_id)
        actual = get_expense_by_id(expense_id)

        self.assertFalse(actual)

    def test_get_expense_by_month(self):
        expected = Expense(id=6,
                            name='Rent',
                            amount=1200.0,
                            effect_date='2024-08-01',
                            created_at=None,
                            user_id=1,
                            cat_id=2,
                            cat_name='Rent',
                            goal_id=None,
                            goal_name=None)

        actual = get_expenses_by_month(1, '2024-08')
        self.assertEqual(expected.id, actual[0].id)
        self.assertEqual(expected.name, actual[0].name)
        self.assertEqual(expected.amount, actual[0].amount)
        self.assertEqual(expected.user_id, actual[0].user_id)

    def test_get_expenses_by_goal(self):
        expected = Expense(id=9,
                           name='Vacation Saving',
                           amount=20.0,
                           effect_date='2024-08-25',
                           created_at=None,
                           user_id=1,
                           cat_id=6,
                           cat_name='Goals',
                           goal_id=1,
                           goal_name='Vacation Fund')

        actual = get_expenses_by_goal(1)

        self.assertEqual(expected.id, actual[0].id)
        self.assertEqual(expected.goal_name, actual[0].goal_name)
        self.assertEqual(expected.goal_id, actual[0].goal_id)

    def test_get_sum_of_user_expenses_to_date(self):
        expected = 5415.0
        actual = get_sum_of_user_expenses_to_date(1)

        self.assertEqual(expected, actual)
