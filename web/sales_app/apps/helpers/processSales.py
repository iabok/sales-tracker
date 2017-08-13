'''
 Process the sales
'''
import operator
import processExpenses
import processFuelSales
import processProductSales


class Sales:
    """
     Fuel process class
    """

    def __init__(self, formData):
        """
         constructor
        """
        self.sales = formData

    def totalRevenue(self):
        """
         Calculates the total revenue
         totalRevenue = fuelSales + productSales

         return type = int
        """
        if not isinstance(self.sales, dict):

            return False

        products = processProductSales.ProductSales(
            self.sales['product_name'],
            self.sales['quantity'],
            self.sales['price'])

        petrol = {
            'petrol_open': self.sales['petrol_open'][0],
            'petrol_close': self.sales['petrol_close'][0],
            'petrol_price': self.sales['petrol_price'][0]
        }

        desiel = {
            'desiel_open': self.sales['desiel_open'][0],
            'desiel_close': self.sales['desiel_close'][0],
            'desiel_price': self.sales['desiel_price'][0]
        }

        fuel = processFuelSales.FuelSales(petrol, desiel)
        totalProductSales = products.totalProductSales()
        fuelSales = fuel.totalFuelSales()

        return operator.add(fuelSales, totalProductSales)

    def totalExpenses(self):
        """
         Calculates the total expenses

         return type = int
        """
        if not isinstance(self.sales, dict):

            return False

        expenses = processExpenses.Expenses(
            self.sales['credit_name'],
            self.sales['amount'])

        return expenses.totalExpenses()

    def totalSales(self):
        totalRevenue = self.totalRevenue()
        totalExpenses = self.totalExpenses()

        return operator.sub(totalRevenue, totalExpenses)
