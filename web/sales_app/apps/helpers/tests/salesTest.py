import unittest
import processFuelSales


class TestSalesMethods(unittest.TestCase):

    testData = {'csrfmiddlewaretoken': ['T3BaBX4dqizLBovTC51LvE5q0ji90R42HSNMe0IgusSnMe1ixMKzgzWcBLPDUJSk'], 'petrol_open': ['2'], 'petrol_close': ['4'], 'petrol_price':
     ['2'], 'desiel_open': ['2'], 'desiel_close': ['4'], 'desiel_price': ['3'], 'product_name': ['1', '4'], 'quantity': ['4', '2'], 'price': ['3', '3'], 'credit_name': ['a', 'a'], 'amount': ['3', '4']}

    def test_method(self):
        petrol = {'petrol_open': 2, 'petrol_close': 4, 'petrol_price': 2}
        desiel = {'desiel_open': 2, 'desiel_close': 4, 'desiel_price': 3}
        Sales = processFuelSales.FuelSales(petrol, desiel)
        # Expense.mapFields()
        print(Sales.computeLitresSold())
        print(Sales.computeFuelSales())
        print(Sales.totalFuelSales())
        # print(Expense.getExpenseInsertFields(['a', 'b', 'c']))


if __name__ == '__main__':
    unittest.main()
