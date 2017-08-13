import unittest
import processProductSales


class TestProcessingProductSalesMethods(unittest.TestCase):

    testData = {'product_name': ['1', '4'],
                'quantity': ['4', '2'], 'price': ['3', '3']}

    product = processProductSales.ProductSales(
        testData['product_name'],
        testData['quantity'],
        testData['price'])

    def test_map_fields_method(self):
        expectData = [['1', '4', '3'], ['4', '2', '3']]
        self.product.mapFields()
        products = self.product.getMapFields()
        actual = list(map(list, products))

        self.assertEqual(expectData, actual)
        self.assertIsInstance(products, Iterable)

    def test_map_fields_method_fails_if_not_list(self):
        """
         Test mapping fields
        """
        product = processProductSales.ProductSales(1, 2, 3)
        self.assertFalse(product.mapFields())

    def test_total_Product_Sales_method(self):
        """
         Test get total sales
        """
        expectTotal = 18
        total = self.product.totalProductSales()

        self.assertEqual(expectTotal, total)
        self.assertIsInstance(total, int)

    def test_get_Product_Insert_Fields_method(self):
        """
         Test inserting missing data
        """
        expectData = [['1', '4', '3', 'a', 'b', 'c'],
                      ['4', '2', '3', 'a', 'b', 'c']]

        missingFields = ['a', 'b', 'c']
        actual = self.product.getProductInsertFields(missingFields)
        self.assertEqual(expectData, list(actual))

    def test_get_product_insert_data_method(self):
        """
         Test get insert Data
        """
        names = ('name', 'quantity', 'unit_price',
                 'sales_id', 'station_id', 'sales_date')

        missingFields = ['a', 'b', 'c']
        actual = self.product.getProudctInsertData(missingFields)
        actual = [x._fields for x in actual]
        self.assertEqual(names, actual.pop())


if __name__ == '__main__':
    unittest.main()
