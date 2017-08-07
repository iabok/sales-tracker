'use strict';
/**
 * Computes Sales, expenses
 * @type Object
 */
 var SALES = SALES || {};

/**
 * Initialising the compute constructor
 * @method Compute
 */
 SALES.Compute = function () {
   this.soldLitres = 0;
   this.totalSalesLitres = 0;
   this.productSalesSold = 0;
   this.totalProductSales = 0;
   this.totalCreditExpense = 0;
   this.total = 0;
 };

 /**
  * Calculates the number of litres sold
  * @method litres
  * @param  int opening opening meter reading
  * @param  int closing closing meter reading
  * @return void
  */
 SALES.Compute.prototype.litres = function(opening, closing) {
   this.soldLitres = closing - opening;
 };

 /**
  * Calculates the amount made from the litres sold
  * @method price
  * @param  int price price of the fuel
  * @return void
  */
 SALES.Compute.prototype.price = function(price) {
   this.totalSalesLitres = this.soldLitres * price;
 };

 /**
  * Calculates amount collected from product Sales e.g oils etc.
  * @method productSales
  * @param  Object productDetails Object containing quantity and price for the \n
  * product sold
  * @return int amount collected from the sale
  */
 SALES.Compute.prototype.productSales = function(productDetails) {
       if (productDetails instanceof Object) {
         this.otherSalesSold = productDetails.id_quantity * productDetails.id_price;
       }

       return this.otherSalesSold;

 };

 /**
  * Calculates the total of all product sales
  * @method totalOfProductSales
  * @param  Object productDetails details of the each product sale
  * @return int total collected for all the product sold
  */
 SALES.Compute.prototype.totalOfProductSales = function(productDetails) {
   var totalOfEachSale = [];
   var total = 0;
   if (productDetails instanceof Object) {
     for (var key in productDetails) {
         if (productDetails.hasOwnProperty(key)) {
                if (productDetails[key]['total'] && !isNaN(productDetails[key]['total'])) {
                    totalOfEachSale.push(productDetails[key]['total']);
                }
         }
     }
   }
   if(totalOfEachSale.length > 0) {
      totalOfEachSale.forEach(function (value) {
         total += parseInt(value);
     });
   }
   this.totalProductSales = total;
   return total;
 };

 /**
  * Calculates the total of sales made including product sales and fuel \n
  * sales
  * @method calcauteTotal
  * @param  Object petrol total sales of petrol
  * @param  Object desiel total sales of desiel
  * @param  Object productSalesTotal total of product sales
  * @param  Object creditExpenses total of expenses inccured
  * @return int total cash
  */
 SALES.Compute.prototype.calcauteTotal = function(petrol, desiel, productSalesTotal, creditExpenses) {
     var sales = petrol.totalPrice() + desiel.totalPrice() + productSalesTotal.total;
     this.total = sales - creditExpenses.totalCreditExpense;

     return this.total;
 };

 /**
  * Calculates the total of all expenses including credits inccured
  * @method creditExpenses
  * @param  Object creditDetails expenses and credit details
  * @return int total of expenses and credit
  */
 SALES.Compute.prototype.creditExpenses = function(creditDetails) {
     var totalOfEachCreditExpense = [];
     var total = 0;
     if (creditDetails instanceof Object) {
       for (var key in creditDetails) {
           if (creditDetails.hasOwnProperty(key)) {
               if(creditDetails[key]['id_amount']) {
                 totalOfEachCreditExpense.push(creditDetails[key]['id_amount']);
               }
           }
       }
     }
     if(totalOfEachCreditExpense.length > 0) {
        totalOfEachCreditExpense.forEach(function (value) {
           total += parseInt(value);
       });
     }
     this.totalCreditExpense = total;

     return total;
 };

 /**
  * return the litres of fuel sold
  * @method litresSold
  * @return void
  */
 SALES.Compute.prototype.litresSold = function() {

   return this.soldLitres;
 };

 /**
  * returns the total sales for the litres sold
  * @method totalPrice
  * @return void
  */
 SALES.Compute.prototype.totalPrice = function() {

   return this.totalSalesLitres;
 };

 /**
  * returns the total of all sales including product sales
  * @method totalSales
  * @return void
  */
 SALES.Compute.prototype.totalSales = function() {

   return this.total;
 };
