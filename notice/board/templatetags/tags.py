from django import template
register = template.Library()

@register.filter(name="is_imp")
def is_imp(user):
    print "HERE"
    print user
    return user.has_perm('board.important')

@register.simple_tag
def has_rights(user):
    return user.has_perm('board.rights')

print "LOADED"
