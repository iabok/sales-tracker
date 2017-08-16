'''
 Process the sales
'''
import operator
from collections import namedtuple
from helpers import processExpenses
from helpers import processFuelSales
from helpers import processProductSales


class Sale:
    """
     Fuel process class
    """

    def __init__(self, formData, model):
        """
         constructor
        """
        self.models = model
        self.data = None
        self.sales = {
            'station_id': formData['station_id'],
            'sales_date': formData['date'],
            'petrol_open': formData['petrol_open'],
            'petrol_close': formData['petrol_close'],
            'petrol_price': formData['petrol_price'],
            'desiel_open': formData['desiel_open'],
            'desiel_close': formData['desiel_close'],
            'desiel_price': formData['desiel_price'],
            'product_name': formData.getlist('product_name'),
            'quantity': formData.getlist('quantity'),
            'price': formData.getlist('price'),
            'credit_name': formData.getlist('credit_name'),
            'amount': formData.getlist('amount')
        }

        self.products = processProductSales.ProductSales(
            self.sales['product_name'],
            self.sales['quantity'],
            self.sales['price'])

        self.expenses = processExpenses.Expenses(
            self.sales['credit_name'],
            self.sales['amount'])

        self.petrol = {
            'petrol_open': self.sales['petrol_open'],
            'petrol_close': self.sales['petrol_close'],
            'petrol_price': self.sales['petrol_price']
        }

        self.desiel = {
            'desiel_open': self.sales['desiel_open'],
            'desiel_close': self.sales['desiel_close'],
            'desiel_price': self.sales['desiel_price']
        }

        self.missingFields = [self.sales['station_id'],
                              self.sales['sales_date']]

    def totalRevenue(self):
        """
         Calculates the total revenue
         totalRevenue = fuelSales + productSales

         return type = int
        """
        if not isinstance(self.sales, dict):

            return False

        fuel = processFuelSales.FuelSales(self.petrol, self.desiel)
        totalProductSales = self.products.totalProductSales()
        fuelSales = fuel.totalFuelSales()

        if fuelSales is not False and totalProductSales is not False:

            return operator.add(fuelSales, totalProductSales)

    def totalExpenses(self):
        """
         Calculates the total expenses

         return type = int
        """
        if not isinstance(self.sales, dict):

            return False

        if self.expenses.totalExpenses() is not False:

            return self.expenses.totalExpenses()

    def totalSales(self):
        """
         Computes total Sales
        """

        totalRevenue = self.totalRevenue()
        totalExpenses = self.totalExpenses()

        return operator.sub(totalRevenue, totalExpenses)

    def saveData(self):
        """
         Save data
        """

        sales = self.models['sales'](station_id=self.sales['station_id'],
                                     sales_date=self.sales['sales_date'],
                                     total_sales=self.totalSales(),
                                     total_expenses=self.totalExpenses(),
                                     total_revenue=self.totalRevenue())
        sales.save()
        self.missingFields.extend([sales])
        self.saveFuel()
        self.saveProductSales()
        self.saveExpenses()

        return True

    def saveFuel(self):
        """
         Save Fuel sales
        """
        fuel = processFuelSales.FuelSales(self.petrol, self.desiel)
        fuelSales = fuel.getFuelInsertData(self.missingFields, self.models)
        for fuel in fuelSales:
            fuel.save()

        return True

    def saveProductSales(self):
        """
         Saves Product Sales
        """

        items = self.products.getProudctInsertData(self.missingFields,
                                                   self.models)

        for product in items:
            product.save()

        return True

    def saveExpenses(self):
        """
         Saves Expenses
        """

        items = self.expenses.getExpenseInsertData(self.missingFields,
                                                   self.models)
        for expense in items:
            expense.save()

        return True
