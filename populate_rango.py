import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')


import django
django.setup()
from rango.models import Category, Page


def populate():
    python_cat = add_cat('Python', 142, 36)

    add_page(cat=python_cat,
            title="Google",
            url="http://google.com")

    add_page(cat=python_cat,
            title="Microsoft",
            url="http://microsoft.com")

    add_page(cat=python_cat,
            title="Instagram",
            url="http://instagram.com")
    
    django_cat = add_cat('Django', 64, 16)

    add_page(cat=django_cat,
            title='Facebook',
            url="http://facebook.com")

    add_page(cat=django_cat,
            title="Eventbrite",
            url="http://eventbrite.com")

    add_page(cat=django_cat,
            title="Amazon",
            url="http://amazon.com")

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0}-{1}".format(str(c), str(p)))

def add_cat(cat, views=0, likes=0):
    c = Category.objects.get_or_create(name=cat)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


if __name__ == "__main__":
    print("Starting rango population script..")
    import pdb; pdb.set_trace()
    populate()


