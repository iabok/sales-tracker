'''
 Process the product sales fields
'''
from collections import namedtuple


class ProductSales:
    '''
     Product process class
    '''
    ProductRecord = namedtuple('Product', 'name, quantity, \
        unit_price, sales_id, station_id, sales_date')

    def __init__(self, product_name, quantity, price):
        '''
         constructor
        '''
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.fields = []

    def mapFields(self):
        '''
         process the fields
        '''
        if not isinstance(self.product_name, list) \
           or not isinstance(self.quantity, list) \
           or not isinstance(self.price, list):

            return False

        return zip(self.product_name, self.quantity, self.price)

    def getMapFields(self):
        '''
         get the fields
        '''
        return self.fields

    def totalProductSales(self):
        """
         Returns the total of all product sales
        """
        if not isinstance(self.product_name, list) \
           or not isinstance(self.quantity, list) \
           or not isinstance(self.price, list):

            return False

        return sum(map(lambda x: x[0] * [1], zip(self.quantity, self.price)))
