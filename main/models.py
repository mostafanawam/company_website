from django.db import models



from django.contrib.auth.models import User


# python manage.py dumpdata main.Company --output main/fixtures/Company.static.json
class Company(models.Model):
    about = models.TextField(null=True,blank=True)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    address=models.TextField()

    class Meta:
        verbose_name_plural = "Company"


# python manage.py dumpdata main.SocialLinks --output main/fixtures/SocialLinks.static.json
class SocialLinks(models.Model):
    name=models.CharField(max_length=50)
    icon=models.CharField(max_length=50)
    url=models.CharField(max_length=250,default="")

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name_plural = "Social Links"


class ContactUs(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} - {self.subject}'

    class Meta:
        verbose_name_plural = "Contact Us"