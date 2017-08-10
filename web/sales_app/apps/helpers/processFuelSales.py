'''
 Process the Fuel sales
'''
import operator


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

    def computeLitresSold(self):
        """
         processes the litres sold for each fuel type

         returnType: Dictionary
        """
        if not isinstance(self.petrol, dict) \
           or not isinstance(self.desiel, dict):

            return False

        return {
            'petrol': operator.sub(self.petrol['petrol_close'],
                                   self.petrol['petrol_open']),
            'desiel': operator.sub(self.desiel['desiel_close'],
                                   self.desiel['desiel_open'])
        }

    def computeFuelSales(self):
        """
         Computes sales for each fuel type

         returnType: Dictionary
        """

        litresSold = self.computeLitresSold()

        return {
            'petrol': operator.mul(litresSold['petrol'],
                                   self.petrol['petrol_price']),
            'desiel': operator.mul(litresSold['desiel'],
                                   self.desiel['desiel_price'])
        }

    def totalFuelSales(self):
        """
         Computes the total fuel sales

         returnType: Interger
        """

        return sum(self.computeFuelSales().values())
