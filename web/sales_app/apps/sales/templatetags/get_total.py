"""
 Custom django template tag to get totals
"""
from django import template
import operator

register = template.Library()


@register.simple_tag
def get_total(quantity, price):
    """
     Get total for each product sale

     returns an integer
    """

    return operator.mul(quantity, price)


@register.simple_tag(takes_context=True)
def get_total_products(context):
    """
     Gets the total of product sales

     returns an integer
    """

    return sum(map(lambda x: operator.mul(x.quantity, x.unit_price),
                   context['Products']))


@register.simple_tag(takes_context=True)
def get_total_expenses(context):
    """
     Gets the total of all expenses

     returns an integer
    """

    return sum(map(lambda x: x.amount, context['Expenses']))


@register.simple_tag(takes_context=True)
def process_fuel(context):
    """
     Reformats Fuel consumed
    """
    fuel = {
      0: 'Petrol',
      1: 'Desiel'
    }
    data = []
    totals = []

    for index, type in enumerate(context['Fuel']):
        litresSold = operator.sub(type.closing_meter, type.opening_meter)
        total = operator.mul(litresSold, type.unit_price)
        totals.append(total)
        data.append([
                    {'type': fuel[index],
                     'opening_meter': type.opening_meter,
                     'closing_meter': type.closing_meter,
                     'unit_price': type.unit_price,
                     'litresSold': litresSold,
                     'total': total}])
    return {
        'data': data,
        'total': totals
    }


@register.simple_tag
def get_fuel_total(totals):
    """
     return the total cash
    """
    return sum(totals)
