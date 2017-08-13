'''
 Process the Expenses fields
'''
from collections import namedtuple


class Expenses:
    """
     Expenses process class
    """

    def __init__(self, name, amount):
        '''
         constructor
        '''
        self.name = name
        self.amount = amount
        self.fields = []
        self.ExpenseRecord = namedtuple('Expenses', 'name, amount, \
            sales_id, station_id, sales_date')

    def mapFields(self):
        """
         process the fields
        """
        if not isinstance(self.name, list) \
           or not isinstance(self.amount, list):

            return False

        self.fields.append(
            zip(self.name, self.amount))

    def getMapFields(self):
        """
         get the fields
        """
        return self.fields

    def totalExpenses(self):
        """
         Returns the total of all expenses
        """
        if not isinstance(self.amount, list):

            return False

        return sum(map(int, self.amount))

    def getExpenseInsertFields(self, missingFields):
        """
         Inserts the missing fields and cleans up the Expenses \
         ready for insertion

         missingFields = [sales_id, station_id, sales_date]
         returns a namedtuple
        """

        if not isinstance(missingFields, list):

            return False

        self.mapFields()
        upackedFields = [i for i in map(list, *self.fields)]
        allFields = map(lambda field: field + missingFields, upackedFields)

        return list(map(self.ExpenseRecord._make, allFields))
