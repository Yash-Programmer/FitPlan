from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    current_weight = models.CharField(max_length=100)  # In kg
    target_weight = models.CharField(max_length=100)    # In kg
    current_height = models.CharField(max_length=100)    # In cm
    gender = models.CharField(max_length=10)  # e.g., 'Male', 'Female', 'Other'
    body_type = models.CharField(max_length=50)  # e.g., 'Ectomorph', 'Mesomorph', 'Endomorph'
    body_fat = models.CharField(max_length=100)  # In percentage
    self_assessment = models.TextField(max_length=100)  # User's assessment of their own health
    diet = models.CharField(max_length=100)  # e.g., 'Vegetarian', 'Vegan', 'Keto'
    motivation = models.TextField(max_length=100)  # User's motivation for the plan
    exercise_frequency = models.CharField(max_length=100)  # Times per week
    type_of_workout = models.CharField(max_length=100)  # e.g., 'Cardio', 'Strength', 'Flexibility'
    stress_level = models.CharField(max_length=20)  # e.g., 'Low', 'Moderate', 'High'
    sleep = models.CharField(max_length=100)  # Hours of sleep per night
    tracking_method = models.CharField(max_length=100)  # e.g., 'App', 'Journal', 'None'
    username = models.CharField(max_length=10000)
    password = models.CharField(max_length=10000)

    nutritional_plan = models.TextField()
    workout_plan = models.TextField()
    progression_plan = models.TextField()

    introduction = models.TextField()

    def __str__(self):
        return self.username