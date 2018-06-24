from django.db import models

class customer(models.Model):
    name = models.CharField(max_length=128, help_text="Enter Your Name")
    email = models.EmailField()

    # methdos:
    # for representing in admin site model-object
    def __str__(self):
        return "Клиент {0} {1}".format(self.name, self.email)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'