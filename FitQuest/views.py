from django.shortcuts import render
import math

# Create your views here.
def form(request):
    return render(request, "form.html")

def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI)"""
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)  # BMI formula
    return bmi

def calculate_caloric_needs(age, weight, height, activity_level):
    """Estimate daily caloric needs based on Mifflin-St Jeor Equation."""
    if activity_level == 'Moderate':
        activity_factor = 1.55
    elif activity_level == 'Intense':
        activity_factor = 1.725
    elif activity_level == 'Very Intense':
        activity_factor = 1.9
    else:
        activity_factor = 1.2  # Sedentary

    # Mifflin-St Jeor Equation for men
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    caloric_needs = bmr * activity_factor
    return caloric_needs

def calculate_weight_loss_calories(maintenance_calories):
    """Calculate calories for different weight loss goals."""
    mild_loss = maintenance_calories - 250  # 0.25 kg/week
    moderate_loss = maintenance_calories - 500  # 0.5 kg/week
    extreme_loss = maintenance_calories - 1000  # 1 kg/week
    return mild_loss, moderate_loss, extreme_loss

def calorie(request):
    return render(request, "calorie.html")

def calorie_result(request):
    context = {}
    
    if request.method == "GET":
        weight = int(request.GET.get('weight'))
        height = int(request.GET.get('height'))
        age = int(request.GET.get('age'))
        activity_level = request.GET.get('activity')

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Calculate maintenance calories
        maintenance_calories = calculate_caloric_needs(age, weight, height, activity_level)

        # Calculate weight loss calories
        mild_loss, moderate_loss, extreme_loss = calculate_weight_loss_calories(maintenance_calories)
        context = {}
        # Store results in context
        context['bmi'] = round(bmi, 2)
        context['maintenance_calories'] = maintenance_calories
        context['mild_loss_calories'] = mild_loss
        context['moderate_loss_calories'] = moderate_loss
        context['extreme_loss_calories'] = extreme_loss

    return render(request, 'calorie-result.html', context)