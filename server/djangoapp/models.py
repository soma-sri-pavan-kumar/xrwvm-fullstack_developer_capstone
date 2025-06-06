from django.db import models


class CarMake(models.Model):
    """
    Model representing a car manufacturer.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    class Meta:
        verbose_name = "Car Make"
        verbose_name_plural = "Car Makes"

    def __str__(self):
        return self.name  # Return the name as the string representation


from django.core.validators import MaxValueValidator, MinValueValidator

class CarModel(models.Model):
    """
    Model representing a specific car model.
    """
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    dealer_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    # Other fields as needed

    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"

    def __str__(self):
        return f"{self.car_make} {self.name}"  # Return car make and model as string


class Review(models.Model):
    """
    Model representing a review for a dealer.
    """
    dealer_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField()
    purchase = models.BooleanField(default=False)
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.CharField(max_length=100, null=True, blank=True)
    car_model = models.CharField(max_length=100, null=True, blank=True)
    car_year = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"Review by {self.name} for dealer {self.dealer_id}"
