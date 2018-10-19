from django.db import models

# Create your models here.
class Home(models.Model):
    title_page = 'Title Page'
    services_header = 'Services Header'
    services = 'Services'
    why_us = 'Why Us'
    careers = 'Careers'
    about_us = 'About Us'

    home_choices = (
        (title_page, 'Title Page'),
        (services_header, 'Services Header'),
        (services, 'Services'),
        (why_us, 'Why Us'),
        (careers, 'Careers'),
        (about_us, 'About Us'),
    )

    name = models.CharField(max_length=15,
    choices = home_choices)

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):

    services_choices = (
    ('Services', 'Services'),
    ('Services Home', 'Services Home'),
    )

    icons_choices = (
    ('fas fa-laptop-code', 'Laptop'),
    ('fas fa-user', 'User'),
    ('fas fa-network-wired', 'Network'),
    ('fas fa-globe-americas', 'Globe'),
    ('fas fa-layer-group', 'Layer'),
    ('fas fa-chart-pie', 'Pie Chart'),
    ('fas fa-chart-line', 'Line Chart'),
    )

    name = models.CharField(max_length=20,
    choices = services_choices)
    icon = models.CharField(max_length=20,
    choices = icons_choices)

    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f"{self.title} - Home"
