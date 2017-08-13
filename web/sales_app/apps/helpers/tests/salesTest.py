import unittest
import processSales


class TestSalesMethods(unittest.TestCase):

    testData = {'petrol_open': ['2'], 'petrol_close': ['4'],
                'petrol_price': ['2'], 'desiel_open': ['2'],
                'desiel_close': ['4'], 'desiel_price': ['3'],
                'product_name': ['1', '4'], 'quantity': ['4', '2'],
                'price': ['3', '3'], 'credit_name': ['a', 'a'],
                'amount': ['3', '4']}
    sales = processSales.Sales(testData)

    def test_getting_total_revenue(self):
        """
         Testing geting total revenue.
        """
        expected = 28
        actual = self.sales.totalRevenue()

        self.assertEqual(expected, actual)

    def test_getting_total_expenses(self):
        """
         Testing geting total revenue.
        """
        expected = 7
        actual = self.sales.totalExpenses()
        self.assertEqual(expected, actual)

    def test_getting_total_sales(self):
        """
         Testing geting total revenue.
        """
        expected = 21
        actual = self.sales.totalSales()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
