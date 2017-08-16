'''
 Process the product sales fields
'''
from collections import namedtuple
import operator


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
        self.fields = None
        self.productRecord = namedtuple('Product', 'name, quantity, \
            unit_price, station_id, sales_date, sales')

    def mapFields(self):
        """
         process the fields
        """
        if not isinstance(self.product_name, list) \
           or not isinstance(self.quantity, list) \
           or not isinstance(self.price, list):

            return False

        self.fields = zip(self.product_name, self.quantity, self.price)

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
        if not isinstance(self.quantity, list) \
           or not isinstance(self.price, list):

            return False

        quantity = list(map(int, self.quantity))
        price = list(map(int, self.price))

        return sum(map(lambda x: operator.mul(*x), zip(quantity, price)))

    def getProductInsertFields(self, missingFields):
        """
         Inserts the missing fields and cleans up the product sales \
         ready for insertion

         missingFields = [sales_id, station_id, sales_date]
        """

        if not isinstance(missingFields, list):

            return False

        self.mapFields()
        if self.getMapFields() is not None:
            upackedFields = list(map(list, self.getMapFields()))

            return map(lambda field: field + missingFields, upackedFields)

        return False

    def getProudctInsertData(self, missingFields, model):
        """
         returns a namedtuple for database insertion
        """
        listOfFields = []
        fields = self.getProductInsertFields(missingFields)
        for product in map(self.productRecord._make, list(fields)):
            listOfFields.append(model['productSales'](
                                name=product.name,
                                quantity=product.quantity,
                                unit_price=product.unit_price,
                                station_id=product.station_id,
                                sales_date=product.sales_date,
                                sales=product.sales))
        return listOfFields
