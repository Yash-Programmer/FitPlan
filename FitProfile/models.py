from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    current_weight = models.FloatField()  # In kg
    target_weight = models.FloatField()    # In kg
    current_height = models.FloatField()    # In cm
    gender = models.CharField(max_length=10)  # e.g., 'Male', 'Female', 'Other'
    body_type = models.CharField(max_length=50)  # e.g., 'Ectomorph', 'Mesomorph', 'Endomorph'
    body_fat = models.FloatField()  # In percentage
    self_assessment = models.TextField()  # User's assessment of their own health
    diet = models.CharField(max_length=100)  # e.g., 'Vegetarian', 'Vegan', 'Keto'
    motivation = models.TextField()  # User's motivation for the plan
    exercise_frequency = models.IntegerField()  # Times per week
    type_of_workout = models.CharField(max_length=100)  # e.g., 'Cardio', 'Strength', 'Flexibility'
    stress_level = models.CharField(max_length=20)  # e.g., 'Low', 'Moderate', 'High'
    sleep = models.FloatField()  # Hours of sleep per night
    tracking_method = models.CharField(max_length=100)  # e.g., 'App', 'Journal', 'None'

    nutritional_plan = models.TextField()
    workout_plan = models.TextField()
    progression_plan = models.TextField()

    def __str__(self):
        return f"Plan for {self.name}"