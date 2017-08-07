'''
 Process the product sales fields
'''


class ProductSales:
    '''
     Product process class
    '''
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

        for i in enumerate(self.product_name):
            self.fields.append([
                self.product_name[i],
                self.quantity[i],
                self.price[i]
            ])

    def getMapFields(self):
        '''
         get the fields
        '''
        return self.fields
