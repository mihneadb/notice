from notice import settings
from django.core.management import setup_environ
setup_environ(settings)

from board.models import Category


CATEGORIES = ['Stiri', 'Burse', 'Stagii']
for category_name in CATEGORIES:
    cat = Category.objects.get_or_create(name=category_name)
    cat[0].save()
print 'Added %d categories.' % len(CATEGORIES)
