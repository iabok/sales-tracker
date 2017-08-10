'''
 Process the Fuel sales
'''
# import operator


class Sales:
    """
     Fuel process class
    """

    def __init__(self, sales):
        """
         constructor
        """
        self.sales = sales

    def totalSales(self):
        """
         processes the litres sold for each fuel type

         returnType: Dictionary
        """
        if not isinstance(self.sales, dict):

            return False

        return self.sales
