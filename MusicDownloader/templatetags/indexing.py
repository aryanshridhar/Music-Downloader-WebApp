from django import template

register = template.Library()

@register.filter
def indexing(list1 , value):
    return list1[value] 
