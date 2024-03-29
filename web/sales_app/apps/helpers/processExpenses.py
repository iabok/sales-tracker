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
        self.fields = None
        self.ExpenseRecord = namedtuple('Expenses', 'name, amount, \
             station_id, sales_date, sales')

    def mapFields(self):
        """
         process the fields
        """
        if not isinstance(self.name, list) \
           or not isinstance(self.amount, list):

            return False

        self.fields = zip(self.name, self.amount)

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
        if self.getMapFields() is not None:
            upackedFields = list(map(list, self.getMapFields()))
            return map(lambda field: field + missingFields, upackedFields)

    def getExpenseInsertData(self, missingFields, model):
        """
         returns a namedtuple for database insertion
        """
        listOfFields = []
        fields = self.getExpenseInsertFields(missingFields)
        for expense in map(self.ExpenseRecord._make, list(fields)):
            listOfFields.append(model['expenses'](name=expense.name,
                                amount=expense.amount,
                                station_id=expense.station_id,
                                sales_date=expense.sales_date,
                                sales=expense.sales))

        return listOfFields
