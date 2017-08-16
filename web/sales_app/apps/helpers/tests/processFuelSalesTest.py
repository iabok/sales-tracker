import unittest
import processFuelSales

class Fuel(object):
    pass

class TestProcessingFuelSalesMethods(unittest.TestCase):
    """
     Expenses test class
    """
    petrol = {'petrol_open': 2, 'petrol_close': 4, 'petrol_price': 2}
    desiel = {'desiel_open': 2, 'desiel_close': 4, 'desiel_price': 3}
    sales = processFuelSales.FuelSales(petrol, desiel)
    # Fuel = {}
    models = {
      'sales': 'Sales',
      'fuel': Fuel,
      'productSales': 'ProductSales',
      'expenses': 'Expenses'
    }

    def test_getting_litresSold(self):
        """
         Test getting litres sold per fuel type
        """

        expected = {'petrol': 2, 'desiel': 2}
        actual = self.sales.computeLitresSold()

        self.assertEqual(expected, actual)

    def test_getting_fuel_sales(self):
        """
         Test getting fuel sales sold per fuel type
        """

        expected = {'petrol': 4, 'desiel': 6}
        actual = self.sales.computeFuelSales()

        self.assertEqual(expected, actual)

    def test_getting_totalFuelSales(self):
        """
         Test getting total Fuel sales of all types
        """

        expected = 10
        actual = self.sales.totalFuelSales()

        self.assertEqual(expected, actual)

    def test_map_fields_method(self):
        expected = [[2, 4, 2, '2', '1', '2017-12-12'],
                    [2, 4, 3, '2', '1', '2017-12-12']]
        missingFields = ['2', '1', '2017-12-12']
        actual = self.sales.insertMissingFields(missingFields)

        self.assertEqual(expected, list(actual))

    def test_get_fuel_insert_data_method(self):
        """
         Test get insert Data
        """
        names = ('opening_meter', 'closing_meter',
                 'unit_price', 'sales_id', 'station_id', 'sales_date')

        missingFields = ['2', '1', '2017-12-12']
        actual = self.sales.getFuelInsertData(missingFields, self.models, 2)
        print(actual)
        #actual = [x._fields for x in actual]

        #self.assertEqual(names, actual.pop())


if __name__ == '__main__':
    unittest.main()
