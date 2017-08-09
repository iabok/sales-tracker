'''
 Process the product sales fields
'''
from collections import namedtuple


class ProductSales:
    """
     Product process class
    """

    def __init__(self, product_name, quantity, price):
        '''
         constructor
        '''
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.fields = []
        self.productRecord = namedtuple('Product', 'name, quantity, \
            unit_price, sales_id, station_id, sales_date')

    def mapFields(self):
        """
         process the fields
        """
        if not isinstance(self.product_name, list) \
           or not isinstance(self.quantity, list) \
           or not isinstance(self.price, list):

            return False

        self.fields.append(
            zip(self.product_name, self.quantity, self.price))

    def getMapFields(self):
        """
         get the fields
        """
        return self.fields

    def totalProductSales(self):
        """
         Returns the total of all product sales
         Returns an integer
        """
        if not isinstance(self.product_name, list) \
           or not isinstance(self.quantity, list) \
           or not isinstance(self.price, list):

            return False

        return sum(map(lambda x: x[0] * x[1], zip(self.quantity, self.price)))

    def getProductInsertFields(self, sales_id, station_id, sales_date):
        """
         Inserts the missing fields and cleans up the product sales \
         ready for insertion
        """

        missingFields = [sales_id, station_id, sales_date]
        upackedFields = [i for i in map(list, *self.fields)]
        allFields = map(lambda field: field + missingFields, upackedFields)

        return list(map(self.productRecord._make, allFields))
