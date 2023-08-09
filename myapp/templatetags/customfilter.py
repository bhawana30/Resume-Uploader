from django import template
register=template.Library()

@register.filter(name='remove_special')
def remove_chars(value,arg):
    print("Arg" ,arg)
    print("Value ",value)
    v=value
    for charachter in arg:
        print(charachter)
        v=v.replace(charachter,"")
    return v
        