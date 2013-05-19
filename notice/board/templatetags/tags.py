from django import template
from notice.settings import PROJECT_PATH
import os
register = template.Library()

@register.filter(name="is_imp")
def is_imp(user):
    return user.has_perm('board.important')

@register.simple_tag
def has_rights(user):
    return user.has_perm('board.rights')

@register.filter(name="theme")
def theme(user):
    return os.path.exists(os.path.join(PROJECT_PATH, "theme"))

print "LOADED"
