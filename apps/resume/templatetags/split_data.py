from django import template
  
register = template.Library()
  
@register.filter(name='split')
def split(value):
    val = value.split('\n')
    val = list(filter(None, val))
    return val

