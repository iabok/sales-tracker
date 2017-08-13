'''
 Process the Fuel sales
'''
import operator
from collections import namedtuple


class FuelSales:
    """
     Fuel process class
    """

    def __init__(self, petrol, desiel):
        """
         constructor
        """
        self.petrol = petrol
        self.desiel = desiel
        self.fuelRecord = namedtuple('Fuel', 'opening_meter, \
            closing_meter, unit_price, sales_id, station_id, sales_date')

    def computeLitresSold(self):
        """
         processes the litres sold for each fuel type

         returnType: Dictionary
        """
        if not isinstance(self.petrol, dict) \
           or not isinstance(self.desiel, dict):

            return False

        return {
            'petrol': operator.sub(int(self.petrol['petrol_close']),
                                   int(self.petrol['petrol_open'])),
            'desiel': operator.sub(int(self.desiel['desiel_close']),
                                   int(self.desiel['desiel_open']))
        }

    def computeFuelSales(self):
        """
         Computes sales for each fuel type

         returnType: Dictionary
        """

        litresSold = self.computeLitresSold()

        return {
            'petrol': operator.mul(litresSold['petrol'],
                                   int(self.petrol['petrol_price'])),
            'desiel': operator.mul(litresSold['desiel'],
                                   int(self.desiel['desiel_price']))
        }

    def totalFuelSales(self):
        """
         Computes the total fuel sales

         returnType: Interger
        """

        return sum(self.computeFuelSales().values())

    def insertMissingFields(self, missingFields):
        fields = [[self.petrol['petrol_open'],
                   self.petrol['petrol_close'],
                   self.petrol['petrol_price']],
                  [self.desiel['desiel_open'],
                   self.desiel['desiel_close'],
                   self.desiel['desiel_price']]]

        return map(lambda field: field + missingFields, fields)

    def getFuelInsertData(self, missingFields):
        """
         returns a namedtuple for database insertion
        """
        fields = self.insertMissingFields(missingFields)
        return list(map(self.fuelRecord._make, list(fields)))
