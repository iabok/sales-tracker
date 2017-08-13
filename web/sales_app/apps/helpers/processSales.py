'''
 Process the sales
'''
import operator

from helpers import processExpenses
from helpers import processFuelSales
from helpers import processProductSales


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
            'petrol_open': self.sales['petrol_open'],
            'petrol_close': self.sales['petrol_close'],
            'petrol_price': self.sales['petrol_price']
        }

        desiel = {
            'desiel_open': self.sales['desiel_open'],
            'desiel_close': self.sales['desiel_close'],
            'desiel_price': self.sales['desiel_price']
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
