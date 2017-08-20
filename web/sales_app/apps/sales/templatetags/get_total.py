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
