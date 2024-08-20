from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.email}, {self.country}, {self.city}, {self.street}, {self.house_number}'

class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return f'{self.name} ({self.model})'

class ENetwork(models.Model):
    ELECTRONIC_CHOICES = [
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Sole Trader'),
    ]

    name = models.CharField(max_length=255)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='supplied'
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    level_network = models.PositiveIntegerField(choices=ELECTRONIC_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
