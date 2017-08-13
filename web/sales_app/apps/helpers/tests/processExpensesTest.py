import unittest
import processExpenses


class TestProcessingExpensesMethods(unittest.TestCase):

    testData = {'credit_name': ['power', 'water'], 'amount': ['3', '4']}

    expenses = processExpenses.Expenses(
        testData['credit_name'],
        testData['amount'])

    def test_getting_mapped_fields(self):
        expectData = [['power', '3'], ['water', '4']]
        self.expenses.mapFields()
        expenses = self.expenses.getMapFields()
        actual = list(map(list, expenses))

        self.assertEqual(expectData, actual)

    def test_map_fields_method_fails_if_not_list(self):
        """
         Test mapping fields
        """
        expenses = processExpenses.Expenses(1, 2)
        self.assertFalse(expenses.mapFields())

    def test_total_expenses(self):
        """
         Test get total sales
        """
        expectTotal = 7
        total = self.expenses.totalExpenses()

        self.assertEqual(expectTotal, total)

    def test_get_expense_Insert_Fields(self):
        """
         Test inserting missing data
        """
        expectData = [['power', '3', '2', '1', '2017-12-12'],
                      ['water', '4', '2', '1', '2017-12-12']]

        missingFields = ['2', '1', '2017-12-12']
        actual = self.expenses.getExpenseInsertFields(missingFields)
        self.assertEqual(expectData, list(actual))

    def test_get_expense_insert_data(self):
        """
         Test get insert Data
        """
        names = ('name', 'amount', 'sales_id', 'station_id', 'sales_date')

        missingFields = ['2', '1', '2017-12-12']
        actual = self.expenses.getExpenseInsertData(missingFields)
        actual = [x._fields for x in actual]
        self.assertEqual(names, actual.pop())


if __name__ == '__main__':
    unittest.main()
