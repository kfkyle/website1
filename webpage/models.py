from django.db import models

# Create your models here.
class Home(models.Model):
    title_page = 'Title Page'
    services_header = 'Services Header'
    service_1 = 'Service 1'
    service_2 = 'Service 2'
    service_3 = 'Service 3'
    why_us = 'Why Us'
    careers = 'Careers'
    about_us = 'About Us'

    home_choices = (
        (title_page, 'Title Page'),
        (services_header, 'Services Header'),
        (service_1, 'Service 1'),
        (service_2, 'Service 2'),
        (service_3, 'Service 3'),
        (why_us, 'Why Us'),
        (careers, 'Careers'),
        (about_us, 'About Us'),
    )
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=15,
    choices = home_choices,
    default = title_page)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.name
