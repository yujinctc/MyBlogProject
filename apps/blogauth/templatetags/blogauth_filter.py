
from django import template
from django.forms import Field, BoundField

register = template.Library()



@register.filter
def addwidget(field,extra_attrs):
    try:
        # 类型问题，将extra_attrs这种afeText类型的数据通过内置函数eval()转化为dict字典
        extra_attrs = eval(extra_attrs)
        if isinstance (field, BoundField) :
            return field.as_widget(attrs=extra_attrs)
    except Exception:
        return field


