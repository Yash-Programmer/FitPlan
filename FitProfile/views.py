from django.shortcuts import render
import google.generativeai as ai
from .models import Login
import re
from django.core.mail import send_mail
import random

# Create your views here.
def login(request):
    return render(request, 'login.html')

def profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        request.POST.get('password')

    def format_nutritional_plan(text):
        formatted_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        
        formatted_text = formatted_text.replace('\n\n', '<br><br>')
        formatted_text = formatted_text.replace('\n', '<br>')

        formatted_text = re.sub(r'\*\s*(.*?)<br>', r'<li>\1</li>', formatted_text)
        formatted_text = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', formatted_text)
        
        formatted_text = re.sub(r'<ul>(<li>.*?</li>)<ul>', r'<ul>\1', formatted_text)
        formatted_text = re.sub(r'</ul><ul>', r'</ul><ul>', formatted_text)
        
        formatted_text = re.sub(r'(<ul>.*?</ul>)(<ul>)', r'\1', formatted_text)
        
        return formatted_text
    
    user = Login.objects.filter(username=username).first()  # Get the first user with the username
    print(user)  # This should print a single user object or None, not a QuerySet
   

    return render(request, 'user.html', {'user': user,
                                         'p': format_nutritional_plan(user.progression_plan),
                                         'n': format_nutritional_plan(user.nutritional_plan),
                                         'w': format_nutritional_plan(user.workout_plan),
                                         "i": format_nutritional_plan(user.introduction),
                                         "date": user.date})

def user(request):
    if request.method == 'GET':
        current_weight = request.GET.get('currentWeight')
        target_weight = request.GET.get('targetWeight')
        current_height = request.GET.get('currentHeight')
        name = request.GET.get('name')
        age = request.GET.get('age')
        email = request.GET.get('email')
        username = request.GET.get('username')
        password = request.GET.get('password')  # Be cautious with passwords in URLs
        focus = request.GET.get('focus')
        gender = request.GET.get('gender')
        body_type = request.GET.get('bodyType')
        body_fat = request.GET.get('bodyFat')
        self_assessment = request.GET.get('selfAssessment')
        diet = request.GET.get('diet')
        motivation = request.GET.get('motivation')
        exercise_frequency = request.GET.get('exerciseFrequency')
        type_of_workout = request.GET.get('typeOfWorkout')
        stress_level = request.GET.get('stressLevel')
        sleep = request.GET.get('sleep')
        tracking_method = request.GET.get('trackingMethod')
    
        workout = (
            f" how a Workout Plan of a week would look like for {name}:\n"
            f"Age: {age}\n"
            f"Email: {email}\n"
            f"Current Weight: {current_weight} kg\n"
            f"Target Weight: {target_weight} kg\n"
            f"Current Height: {current_height} cm\n"
            f"Gender: {gender}\n"
            f"focus: {focus}\n"
            f"Body Type: {body_type}\n"
            f"Body Fat: {body_fat}%\n"
            f"Self-Assessment: {self_assessment}\n"
            f"Diet Preference: {diet}\n"
            f"Motivation: {motivation}\n"
            f"Exercise Frequency: {exercise_frequency} times/week\n"
            f"Type of Workout: {type_of_workout}\n"
            f"Stress Level: {stress_level}\n"
            f"Sleep Duration: {sleep} hours/night\n"
            f"Tracking Method: {tracking_method}"
        )

        nutritional = (
            f"nutritional Plan for, also give scientific value like daily calories, nutritions in carbohyrates, fat, protein etc. {name}:\n"
            f"Age: {age}\n"
            f"Email: {email}\n"
            f"Current Weight: {current_weight} kg\n"
            f"Target Weight: {target_weight} kg\n"
            f"Current Height: {current_height} cm\n"
            f"Gender: {gender}\n"
            f"Body Type: {body_type}\n"
            f"Body Fat: {body_fat}%\n"
            f"Self-Assessment: {self_assessment}\n"
            f"Diet Preference: {diet}\n"
            f"Motivation: {motivation}\n"
            f"Exercise Frequency: {exercise_frequency} times/week\n"
            f"Type of Workout: {type_of_workout}\n"
            f"Stress Level: {stress_level}\n"
            f"Sleep Duration: {sleep} hours/night\n"
            f"Tracking Method: {tracking_method}"
        )

        progressions = (
            f"progressions tracking assumption if you follow for 1 monthfor {name}:\n"
            f"Age: {age}\n"
            f"Email: {email}\n"
            f"Current Weight: {current_weight} kg\n"
            f"Target Weight: {target_weight} kg\n"
            f"Current Height: {current_height} cm\n"
            f"Gender: {gender}\n"
            f"Body Type: {body_type}\n"
            f"Body Fat: {body_fat}%\n"
            f"Self-Assessment: {self_assessment}\n"
            f"Diet Preference: {diet}\n"
            f"Motivation: {motivation}\n"
            f"Exercise Frequency: {exercise_frequency} times/week\n"
            f"Type of Workout: {type_of_workout}\n"
            f"Stress Level: {stress_level}\n"
            f"Sleep Duration: {sleep} hours/night\n"
            f"Tracking Method: {tracking_method}"
        )

        introduction = (
            f"create a introduction for this person. {name}:\n"
            f"Age: {age}\n"
            f"Email: {email}\n"
            f"Current Weight: {current_weight} kg\n"
            f"Target Weight: {target_weight} kg\n"
            f"Current Height: {current_height} cm\n"
            f"Gender: {gender}\n"
            f"Body Type: {body_type}\n"
            f"Body Fat: {body_fat}%\n"
            f"Self-Assessment: {self_assessment}\n"
            f"Diet Preference: {diet}\n"
            f"Motivation: {motivation}\n"
            f"Exercise Frequency: {exercise_frequency} times/week\n"
            f"Type of Workout: {type_of_workout}\n"
            f"Stress Level: {stress_level}\n"
            f"Sleep Duration: {sleep} hours/night\n"
            f"Tracking Method: {tracking_method}"
        )

        API_KEY = "AIzaSyC71aIp7u9YeRa67G1ORzgPYXtJXDnRwqY"
        ai.configure(api_key=API_KEY)
        model = ai.GenerativeModel("gemini-pro")
        chat = model.start_chat()

        current_description = chat.send_message(introduction)

        workout_plan = chat.send_message(workout)
        # print(response.text)
        nutritional_plan = chat.send_message(nutritional)
        # print(response.text)
        progressions_plan = chat.send_message(progressions)
        # print(response.text)

        instance = Login.objects.create(introduction=current_description.text, username=username, password=password, name=name, age=age, email=email, current_weight=current_weight, target_weight=target_weight, current_height=current_height, gender=gender, body_type=body_type, body_fat=body_fat, self_assessment=self_assessment, diet=diet, motivation=motivation, exercise_frequency=exercise_frequency, type_of_workout=type_of_workout, stress_level=stress_level, sleep=sleep, tracking_method=tracking_method, nutritional_plan=nutritional_plan.text, workout_plan=workout_plan.text, progression_plan=progressions_plan.text, otp="None")
        instance.save()

    return render(request, 'usermade.html')

def update(request):
    return render(request, 'update.html')

def otp(request):
    
    if request.method == 'POST':
        username_valid = request.POST.get('username')
        password = request.POST.get('password')
    
    user = Login.objects.filter(username=username_valid).first()   
    otp = random.randint(1000, 9999)    

    send_mail(
        "OTP",
        f"Your OTP is {otp}",
        "settings.EMAIL_HOST_USER",
        [user.email],
        fail_silently=False
    )

    user.otp = otp
    user.save()

    return render(request, 'otp.html', {'username': user.username})

def confirm(request):
    otp = request.POST.get('otp')
    username_valid = request.POST.get('username')
    user = Login.objects.filter(username=username_valid).first()

    print(user.otp)
    print(otp)

    if otp == user.otp:            
        user.delete()
        print("deleted")
        return render(request, 'form.html')
    else:
        print("otp")
        return render(request, 'confirm.html')