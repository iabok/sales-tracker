/**
 * Variables
 * @type Objects, array
 */
var template = $('.product-sales-form > .row:first').clone(true);
var creditExpenseTemplate = $('.credit-expense-form > .row:first').clone(true);
var otherSalesTemplate = template.clone(true);
var formCount = 1;
var creditFormCount = 1;
var productSalesIds = [];
var creditExpenseIds = [];
var trackProductSales = {};
var allProductSales = {};
var trackCreditExpenses = {};
var allCreditExpenses = {};
var petrol = {
  opening : 0,
  closing : 0
};
var desiel = {
  opening : 0,
  closing : 0
};

var productSalesTotal = {
  total : 0
};

var salesSummary = {
  total : 0
};
var petrolSales = new SALES.Compute();
var desielSales = new SALES.Compute();
var product = new SALES.Compute();
var creditExpenses = new SALES.Compute();
var totalSales = new SALES.Compute();

/**
 * [computeFuelSales description]
 * @method computeFuelSales
 * @param  {[type]}         fuelType     [description]
 * @param  {[type]}         openingMeter [description]
 * @param  {[type]}         closingMeter [description]
 * @param  {[type]}         unitPrice    [description]
 * @param  {[type]}         sales        [description]
 * @return {[type]}                      [description]
 */
function computeFuelSales(fuelType, openingMeter, closingMeter, unitPrice, sales) {
  if(fuelType instanceof Object) {
    if(!isNaN(openingMeter)) {
      fuelType.opening = openingMeter;
    }

    if(!isNaN(closingMeter)) {
      fuelType.closing = closingMeter;
    }
  }

  if(sales instanceof Object) {
    sales.litres(fuelType.opening, fuelType.closing);
    sales.price(unitPrice);

    return {
      litresSold : sales.litresSold() > 0 ? sales.litresSold() : 0,
      totalSales : sales.totalPrice()
    };
  }

  return {};

}

/**
 * [computeTotalSales description]
 * @method computeTotalSales
 * @param  {[type]}          petrolSales    [description]
 * @param  {[type]}          desielSales    [description]
 * @param  {[type]}          product        [description]
 * @param  {[type]}          creditExpenses [description]
 * @param  {[type]}          total          [description]
 * @return {[type]}                         [description]
 */
function computeTotalSales(petrolSales, desielSales, product, creditExpenses, total) {
  if(petrolSales instanceof Object &&
     desielSales instanceof Object &&
     product instanceof Object &&
     creditExpenses instanceof Object &&
     total instanceof Object
    ) {
    total.calcauteTotal(petrolSales, desielSales, product, creditExpenses);
    return total.totalSales();
  }
}

/**
 * [totalSalesSummary description]
 * @method totalSalesSummary
 * @return {[type]}          [description]
 */
function totalSalesSummary() {
  var total = computeTotalSales(petrolSales, desielSales, productSalesTotal, creditExpenses, totalSales);
  salesSummary.total = total;
  $(document).find('.totalSales').html(total.toLocaleString());
}

/**
 * [computeProductSales description]
 * @method computeProductSales
 * @param  {[type]}            productSalesIds [description]
 * @return {[type]}                            [description]
 */
function computeProductSales(productSalesIds) {
   $(productSalesIds.join()).on('keyup change', function() {
     var productInputName = this.id.replace(/[0-9]/g, '');
     var productSalesId = parseInt(this.id.replace(/\D/g,''));
     if (isNaN(productSalesId)) {
        productSalesId = 1;
     }
     if (allProductSales.hasOwnProperty(productSalesId)) {
       allProductSales[productSalesId][productInputName] = $(this).val();
       allProductSales[productSalesId]['total'] = product.productSales(allProductSales[productSalesId]);
     } else {
       trackProductSales[productInputName] = $(this).val();
     }

     var productSalesIdLength = Object.keys(trackProductSales).length;

     if (productSalesIdLength === 3) {
       trackProductSales['total'] = product.productSales(trackProductSales);;
       allProductSales[productSalesId] = trackProductSales;
       trackProductSales = {};
     }

     if (productInputName === 'quantity' || productInputName === 'price'  ) {
       productSalesTotal.total = product.totalOfProductSales(allProductSales);
       totalSalesSummary();
     }


   });

  return false;
}

/**
 * [computeCreditExpenses description]
 * @method computeCreditExpenses
 * @param  {[type]}              creditExpenseIds [description]
 * @return {[type]}                               [description]
 */
function computeCreditExpenses(creditExpenseIds) {
  $(creditExpenseIds.join()).on('keyup change', function() {
     var creditExpenseName = this.id.replace(/[0-9]/g, '');
     var creditExpenseId = parseInt(this.id.replace(/\D/g,''));
     if (isNaN(creditExpenseId)) {
        creditExpenseId = 1;
     }
    console.log(creditExpenseId);
     if (allCreditExpenses.hasOwnProperty(creditExpenseId)) {
       allCreditExpenses[creditExpenseId][creditExpenseName] = $(this).val();
     } else {
       trackCreditExpenses[creditExpenseName] = $(this).val();
     }

     var productSalesIdLength = Object.keys(trackCreditExpenses).length;

     if (productSalesIdLength === 1) {
       allCreditExpenses[creditExpenseId] = trackCreditExpenses;
       trackCreditExpenses = {};
     }

     if (creditExpenseName === 'creditAmount') {
         creditExpenses.creditExpenses(allCreditExpenses);
         totalSalesSummary();
     }

  });

  return false;
}

/**
 * [copyForm description]
 * @method copyForm
 * @param  {[type]} template  [description]
 * @param  {[type]} element   [description]
 * @param  {[type]} formCount [description]
 * @return {[type]}           [description]
 */
function copyForm(template, element, formCount) {
  var newTemplate = template.clone(true);
  generateElementIds(newTemplate, formCount);
  newTemplate.appendTo(element);

  return newTemplate;
}

/**
 * [generateElementIds description]
 * @method generateElementIds
 * @param  {[type]}           template  [description]
 * @param  {[type]}           formCount [description]
 * @return {[type]}                     [description]
 */
function generateElementIds(template, formCount) {
  template.find(':input').each(function(){
    //set id to store the updated section number
    if (this.id) {
      var newId = this.id + formCount;
      //update for label
      $(this).prev().attr('for', newId);
      //update id
      this.id = newId;
    }
  }).end();

  return false;
}

/**
 * [getNewElementIds description]
 * @method getNewElementIds
 * @param  {[type]}         template [description]
 * @return {[type]}                  [description]
 */
function getNewElementIds(template) {
  var elementIds = [];
  template.find(':input').each(function(){
    //set id to store the updated section number
    if (this.id) {
      elementIds.push('#' + this.id);
    }
  }).end();

  return elementIds;
}

$(function () {
  $('#petrolOpen, #petrolClose, #petrolPrice, #desielOpen, #desielClose, #desielPrice, #prodcutName, #quantity, #price'
   ).on('keyup change', function() {
    var petrolOpenMeterNumber = $('#petrolOpen').val();
    var petrolCloseMeterNumber = $('#petrolClose').val();
    var desielOpenMeterNumber = $('#desielOpen').val();
    var desielCloseMeterNumber = $('#desielClose').val();
    var petrolUnitPrice = $('#petrolPrice').val();
    var desielUnitPrice = $('#desielPrice').val();

    var petrolCalucation = computeFuelSales(petrol, petrolOpenMeterNumber, petrolCloseMeterNumber, petrolUnitPrice, petrolSales);
    var desielCalucation = computeFuelSales(desiel, desielOpenMeterNumber, desielCloseMeterNumber, desielUnitPrice, desielSales);

    if (petrolCloseMeterNumber) {
        $(document).find('.petrolLitres').html(petrolCalucation.litresSold.toLocaleString());
    }
    if (petrolUnitPrice) {
        $(document).find('.petrolSales').html(petrolCalucation.totalSales.toLocaleString());
     }

    if (desielCloseMeterNumber) {
        $(document).find('.desielLitres').html(desielCalucation.litresSold.toLocaleString());
    }
    if (desielUnitPrice) {
      $(document).find('.desielSales').html(desielCalucation.totalSales.toLocaleString());
    }

    totalSalesSummary();
  });

 if (template) {
    var productSalesIds = getNewElementIds(template);
    computeProductSales(productSalesIds);
    //add new product row
    $('body').on('click', '.product-sales-add, .other-sales-add', function() {
      formCount++;
      var element = this.id === 'other-sales-add' ? '#other-sales-form' : '#product-sales-form';
      var newTemplate = copyForm(template, element, formCount);
      var productSalesIds = getNewElementIds(newTemplate);
      computeProductSales(productSalesIds);
      return false;
    });

    //remove product row
    $('#product-sales-form, #other-sales-form').on('click', '.product-sales-remove, .other-sales-remove', function(event) {
      event.stopPropagation();
      var elementId = $(this).parent().parent()[0].children[0].id;
      var productSalesId = parseInt(elementId.replace(/\D/g,''));
      if (isNaN(productSalesId)) {
          productSalesId = 1;
      }
      if (allProductSales.hasOwnProperty(productSalesId)){
        delete allProductSales[productSalesId];
        productSalesTotal.total = product.totalOfProductSales(allProductSales);
        totalSalesSummary();

      }
      //fade out row
      $(this).parent().fadeOut(300, function(){
        //remove parent element (main form)
        $(this).parent().parent().parent().empty();
        return false;
      });
      return false;
    });
 }

 if (creditExpenseTemplate) {
   var creditExpenseIds = getNewElementIds(creditExpenseTemplate);
   computeCreditExpenses(creditExpenseIds);
   var creditFormSelectors = {
     creditExpense : '#creditExpenseForm',
     expenseAdd : '#expenseForm',
     otherExpenseAdd : '#otherExpenseForm'
   };
   //add new product row
   $('body').on('click', '.credit-expense-add, .expense-add, .other-expense-add', function() {
     creditFormCount++;
     var newTemplate = copyForm(creditExpenseTemplate, creditFormSelectors[this.id], creditFormCount);
     var creditExpenseIds = getNewElementIds(newTemplate);
     computeCreditExpenses(creditExpenseIds);
     return false;
   });

   //remove product row
   $('#creditExpenseForm, #expenseForm, #otherExpenseForm').on('click', '.credit-expense-remove, .other-sales-remove', function(event) {
     event.stopPropagation();
     var elementId = $(this).parent().parent()[0].children[0].id;
     var creditExpenseId = parseInt(elementId.replace(/\D/g,''));
     if (isNaN(creditExpenseId)) {
        creditExpenseId = 1;
     }
     if (allCreditExpenses.hasOwnProperty(creditExpenseId)){
       delete allCreditExpenses[creditExpenseId];
       creditExpenses.creditExpenses(allCreditExpenses);
       totalSalesSummary();

     }
     //fade out row
     $(this).parent().fadeOut(300, function(){
       //remove parent element (main form)
       $(this).parent().parent().parent().empty();
       return false;
     });
     return false;
   });
 }

});
