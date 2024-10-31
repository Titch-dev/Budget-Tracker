import sqlite3
from unittest import TestCase

from models.user import User
from models.category import Category
from models.goal import Goal
from models.income import Income
from models.expense import Expense

from db_access import get_income_by_id, get_user_by_id, get_goal_by_id, \
    get_category_by_id, get_expense_by_id, get_user_by_email, \
    get_user_categories, get_user_expenses, get_user_goals, get_user_income, \
    delete_category, delete_expense, delete_goal, delete_income, delete_user, \
    update_category, update_expense, update_goal, update_income, update_user, \
    create_user, create_goal, create_category, create_expense, create_income

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

    def tearDown(self) -> None:
        self.cursor.close()
        self.conn.close()

    ### User queries ###
    def test_get_user_by_email(self):
        expected_email = 'test@test.com'
        expected_password = 'password'
        actual = get_user_by_email('test@test.com')

        self.assertEqual(expected_email, actual.email)
        self.assertEqual(expected_password, actual.password)

    def test_get_user_by_id(self):
        expected_email = 'test@test.com'
        expected_password = 'password'
        actual = get_user_by_id(1)

        self.assertEqual(expected_email, actual.email)
        self.assertEqual(expected_password, actual.password)

    def test_create_user(self):
        user = User.create(email='user@test.com', password='password')
        create_user(user)
        actual = get_user_by_email('user@test.com')

        self.assertTrue(actual)
        self.assertEqual(user.email, actual.email)
        self.assertEqual(user.password, actual.password)

    def test_update_user(self):
        user = get_user_by_email('test@test.com')
        print(f"user email = {user.email}, user id = {user.id}")
        user.password = 'test'
        update_user(user)
        expected = user
        actual = get_user_by_email('test@test.com')

        self.assertEqual(expected.password, actual.password)

    def test_delete_user(self):
        user_id = 1
        delete_user(user_id)
        actual = get_user_by_id(user_id)
        print(actual)

        self.assertFalse(actual)

    ### Category queries ###
    def test_get_category_by_id(self):
        cat_id = 1
        expected_name = 'Salary'
        actual = get_category_by_id(cat_id)

        self.assertEqual(cat_id, actual.id)
        self.assertEqual(expected_name, actual.name)

    def test_create_category(self):
        category = Category.create('test', 'test desc', 0.00, 1)
        create_category(category)
        self.cursor.execute('SELECT * FROM category WHERE name = "test"')
        data = self.cursor.fetchone()
        actual = Category(data[0], data[1], data[2], data[3], data[4], data[5])

        self.assertEqual(category.name, actual.name)
        self.assertEqual(category.desc, actual.desc)
        self.assertEqual(category.budget, actual.budget)
        self.assertEqual(category.user_id, actual.user_id)

    def test_get_user_categories(self):
        expected_categories = [Category(id=1,
                                         name='Salary',
                                         desc='Monthly salary payment',
                                         budget=0.0,
                                         created_at='2024-10-31 15:09:30',
                                         user_id=1),
                                Category(id=2,
                                         name='Rent',
                                         desc='Monthly rent payment.',
                                         budget=0.0,
                                         created_at='2024-10-31 15:09:30',
                                         user_id=1),
                                Category(id=3,
                                         name='Utilities',
                                         desc='Electricity, water, and gas bills.',
                                         budget=0.0,
                                         created_at='2024-10-31 15:09:30',
                                         user_id=1),
                                Category(id=4,
                                         name='Dining Out',
                                         desc='Eating out at restaurants and cafes.',
                                         budget=150.0,
                                         created_at='2024-10-31 15:09:30',
                                         user_id=1),
                                Category(id=5,
                                         name='Health & Fitness',
                                         desc='Gym membership and health-related expenses.',
                                         budget=0.0,
                                         created_at='2024-10-31 15:09:30',
                                         user_id=1),
                                Category(id=6,
                                         name='Goals',
                                         desc='Working towards financial goals.',
                                         budget=0.0,
                                         created_at='2024-10-31 15:09:30',
                                         user_id=1)]

        actual_categories = get_user_categories(1)

        self.assertEqual(len(actual_categories), len(expected_categories), "The list lengths do not match")

        for actual, expected in zip(actual_categories, expected_categories):
            self.assertEqual(actual.name, expected.name)
            self.assertEqual(actual.desc, expected.desc)
            self.assertEqual(actual.budget, expected.budget)
            self.assertEqual(actual.user_id, expected.user_id)

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

    ### Goals queries ###
    def test_get_goal_by_id(self):
        goal_id = 1
        expected_name = 'Vacation Fund'
        expected_target = 5000.00
        actual = get_goal_by_id(goal_id)
        print(actual)

        self.assertEqual(actual.id, goal_id)
        self.assertEqual(actual.name, expected_name)
        self.assertEqual(actual.target, expected_target)

    def test_create_goal(self):
        expected = Goal.create(name='test',
                               desc='test desc',
                               target=100.00,
                               end_date=None,
                               user_id=1)
        create_goal(expected)
        self.cursor.execute('SELECT * FROM goal WHERE name = "test"')
        data = self.cursor.fetchone()
        actual = Goal(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

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

    def test_update_goal(self):
        expected = get_goal_by_id(1)
        expected.name = 'test'
        expected.target = 1000.00
        update_goal(expected)
        actual = get_goal_by_id(1)

        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.target, expected.target)

    def test_delete_goal(self):
        goal_id = 1
        delete_goal(goal_id)
        actual = get_goal_by_id(goal_id)

        self.assertFalse(actual)

    ### Income queries ###
    def test_get_income_by_id(self):
        expected = Income(id=1,
                          name='Work Salary',
                          amount=2000.0,
                          effect_date='2024-06-25 00:00:00',
                          created_at='2024-10-31 18:02:25',
                          user_id=1,
                          category_name='Salary')
        actual = get_income_by_id(1)

        self.assertEqual(actual.id, expected.id)
        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.amount, expected.amount)
        self.assertEqual(actual.user_id, expected.user_id)
        self.assertEqual(actual.category_name, expected.category_name)

    def test_create_income(self):
        expected = Income.create(name='test',
                                 amount=10.00,
                                 effect_date="2025-09-09 20:00:00",
                                 user_id=1)
        create_income(expected, 1)
        self.cursor.execute('SELECT * FROM income WHERE name = "test"')
        data = self.cursor.fetchone()
        actual = Income(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.amount, expected.amount)
        self.assertEqual(actual.effect_date, expected.effect_date)
        self.assertEqual(actual.user_id, expected.user_id)

    def test_get_user_income(self):
        expected_income = [Income(id=1,
                                  name='Work Salary',
                                  amount=2000.0,
                                  user_id=1,
                                  effect_date=None,
                                  created_at=None,
                                  category_name='Salary'),
                           Income(id=2,
                                  name='Work Salary',
                                  amount=2000.0,
                                  user_id=1,
                                  effect_date=None,
                                  created_at=None,
                                  category_name='Salary'),
                           Income(id=3,
                                  name='Work Salary',
                                  amount=2000.0,
                                  user_id=1,
                                  effect_date=None,
                                  created_at=None,
                                  category_name='Salary'),
                           Income(id=4,
                                  name='Work Salary',
                                  amount=2000.0,
                                  user_id=1,
                                  effect_date=None,
                                  created_at=None,
                                  category_name='Salary'),
                           Income(id=5,
                                  name='Work Salary',
                                  amount=2000.0,
                                  user_id=1,
                                  effect_date=None,
                                  created_at=None,
                                  category_name='Salary')]
        actual_income = get_user_income(1)

        self.assertEqual(len(actual_income), len(expected_income))

        for actual, expected in zip(actual_income, expected_income):
            self.assertEqual(actual.id, expected.id)
            self.assertEqual(actual.name, expected.name)
            self.assertEqual(actual.amount, expected.amount)
            self.assertEqual(actual.user_id, expected.user_id)
            self.assertEqual(actual.category_name, expected.category_name)

    def test_update_income(self):
        expected = get_income_by_id(1)
        expected.name = 'test'
        expected.amount = 1200.00
        expected.category_name = 'Goals'
        update_income(income=expected, cat_id=6)
        actual = get_income_by_id(1)

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.amount, actual.amount)
        self.assertEqual(expected.category_name, actual.category_name)

    def test_delete_income(self):
        income_id = 1
        delete_income(income_id)
        actual = get_income_by_id(income_id)

        self.assertFalse(actual)

    ### Expense queries ###
    def test_get_expense_by_id(self):
        expense_id = 1
        expected = Expense.create(name='Rent',
                                  amount=1200.0,
                                  effect_date='2024-07-01 00:00:00',
                                  user_id=1)
        actual = get_expense_by_id(expense_id)

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.amount, actual.amount)
        self.assertEqual(expected.effect_date, actual.effect_date)
        self.assertEqual(expected.user_id, actual.user_id)

    def test_create_expense(self):
        expected = Expense.create(name='test',
                                  amount=100.00,
                                  effect_date='2025-09-09 20:00:00',
                                  user_id=1)
        create_expense(expected, 6, 1)
        self.cursor.execute('SELECT * FROM expense WHERE name = "test"')
        data = self.cursor.fetchone()
        actual = Expense(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.amount, actual.amount)
        self.assertEqual(expected.effect_date, actual.effect_date)
        self.assertEqual(expected.user_id, actual.user_id)

    def test_get_user_expenses(self):
        expected_expenses = [
            Expense(id=1,
                    name='Rent',
                    amount=1200.0,
                    effect_date='2024-07-01 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Rent',
                    goal_name=None),
            Expense(id=2,
                    name='Electricity Bill',
                    amount=60.0,
                    effect_date='2024-07-03 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Utilities',
                    goal_name=None),
            Expense(id=3,
                    name='Ask Italian',
                    amount=40.0,
                    effect_date='2024-07-05 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Dining Out',
                    goal_name=None),
            Expense(id=4,
                    name='Gas Bill',
                    amount=30.0,
                    effect_date='2024-07-06 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Utilities',
                    goal_name=None),
            Expense(id=5,
                    name='Burger King',
                    amount=15.0,
                    effect_date='2024-07-20 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Dining Out',
                    goal_name=None),
            Expense(id=6,
                    name='Rent',
                    amount=1200.0,
                    effect_date='2024-08-01 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Rent',
                    goal_name=None),
            Expense(id=7,
                    name='Electricity Bill',
                    amount=60.0,
                    effect_date='2024-08-03 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Utilities',
                    goal_name=None),
            Expense(id=8,
                    name='Gas Bill',
                    amount=30.0,
                    effect_date='2024-08-06 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Utilities',
                    goal_name=None),
            Expense(id=9,
                    name='Vacation Saving',
                    amount=20.0,
                    effect_date='2024-08-25 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Goals',
                    goal_name='Vacation Fund'),
            Expense(id=10,
                    name='Rent',
                    amount=1200.0,
                    effect_date='2024-09-01 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Rent',
                    goal_name=None),
            Expense(id=11,
                    name='Electricity Bill',
                    amount=60.0,
                    effect_date='2024-09-03 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Utilities',
                    goal_name=None),
            Expense(id=12,
                    name='Gas Bill',
                    amount=30.0,
                    effect_date='2024-09-06 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Utilities',
                    goal_name=None),
            Expense(id=13,
                    name='Vacation Saving',
                    amount=30.0,
                    effect_date='2024-09-25 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Goals',
                    goal_name='Vacation Fund'),
            Expense(id=14,
                    name='Rent',
                    amount=1200.0,
                    effect_date='2024-10-01 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Rent',
                    goal_name=None),
            Expense(id=15,
                    name='Gym',
                    amount=75.0,
                    effect_date='2024-10-02 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Health & Fitness',
                    goal_name=None),
            Expense(id=16,
                    name='Electricity Bill',
                    amount=60.0,
                    effect_date='2024-10-03 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Utilities',
                    goal_name=None),
            Expense(id=17,
                    name='Gas Bill',
                    amount=30.0,
                    effect_date='2024-10-06 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Utilities',
                    goal_name=None),
            Expense(id=18,
                    name='Yo Sushi',
                    amount=45.0,
                    effect_date='2024-10-10 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Dining Out',
                    goal_name=None),
            Expense(id=19,
                    name='Vacation Saving',
                    amount=30.0,
                    effect_date='2024-10-25 00:00:00',
                    created_at='2024-10-31 20:10:48',
                    user_id=1,
                    category_name='Goals',
                    goal_name='Vacation Fund'),
        ]
        actual_expenses = get_user_expenses(1)

        self.assertEqual(len(expected_expenses), len(actual_expenses), 'The lists lengths dont match')

        for expected, actual in zip(expected_expenses, actual_expenses):
            self.assertEqual(expected.id, actual.id)
            self.assertEqual(expected.name, actual.name)
            self.assertEqual(expected.amount, actual.amount)
            self.assertEqual(expected.effect_date, actual.effect_date)
            self.assertEqual(expected.user_id, actual.user_id)
            self.assertEqual(expected.category_name, actual.category_name)
            self.assertEqual(expected.goal_name, actual.goal_name)

    def test_update_expense(self):
        expected = get_expense_by_id(1)
        expected.name = 'test'
        expected.amount = 100.00
        expected.effect_date = '2021-09-09 20:00:00'
        update_expense(expected, 1, 1)
        actual = get_expense_by_id(1)

        self.assertEqual(expected.name, actual.name)
        self.assertEqual(expected.amount, actual.amount)
        self.assertEqual(expected.effect_date, actual.effect_date)

    def test_delete_expense(self):
        expense_id = 1
        delete_expense(expense_id)
        actual = get_expense_by_id(expense_id)

        self.assertFalse(actual)