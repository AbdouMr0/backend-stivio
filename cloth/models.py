from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('T-Shirt', 'T-Shirt'),
        ('Jeans', 'Jeans'),
        ('Jackets', 'Jackets'),
        ('Shoes', 'Shoes'),
        ('Tracksuit', 'Tracksuit')
    ]

    SIZE_CHOICES = {
        'T-Shirt': [
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
            ('XL', 'X-Large'),
            ('XXL', 'XX-Large'),

        ],
        'Jeans': [
            ('28', '28'),
            ('30', '30'),
            ('32', '32'),
            ('34', '34'),
            ('36', '36')
        ],
        'Jackets': [
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
            ('XL', 'X-Large'),
            ('XXL', 'XX-Large')
        ],
        'Shoes': [
            ('38', '38'),
            ('39', '39'),
            ('40', '40'),
            ('41', '41'),
            ('42', '42'),
            ('43', '43')
        ],
        'Tracksuit': [
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
            ('XL', 'X-Large'),
            ('XXL', 'XX-Large')
        ]
    }

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    available_sizes = models.TextField(default='')  # Store sizes as comma-separated values
    image_url = models.ImageField(upload_to='images/', blank=True, null=True)

    def get_available_sizes(self):
        return self.available_sizes.split(',')

    def save(self, *args, **kwargs):
        if self.category in self.SIZE_CHOICES:
            valid_sizes = [choice[0] for choice in self.SIZE_CHOICES[self.category]]
            entered_sizes = self.get_available_sizes()
            if not all(size in valid_sizes for size in entered_sizes):
                raise ValueError(f"Some sizes in '{self.available_sizes}' are not valid for category '{self.category}'")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

