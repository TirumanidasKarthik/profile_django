from django import template

register = template.Library()

@register.filter(name="join")
def join(iterable, _str):
    return _str.join(iterable)


@register.filter(name="join_education")
def join_education(iterable):
    print(iterable)
    l = []
    for key, val in iterable.items():
        if key != 'period' and val != '':
            l.append(val)
    return ' - '.join(l)