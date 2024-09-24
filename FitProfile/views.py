from django.shortcuts import render
import google.generativeai as ai
from .models import Login

# Create your views here.
def login(request):
    return render(request, 'login.html')

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

        API_KEY = "AIzaSyC71aIp7u9YeRa67G1ORzgPYXtJXDnRwqY"
        ai.configure(api_key=API_KEY)
        model = ai.GenerativeModel("gemini-pro")
        chat = model.start_chat()

        workout_plan = chat.send_message(workout)
        # print(response.text)
        nutritional_plan = chat.send_message(nutritional)
        # print(response.text)
        progressions_plan = chat.send_message(progressions)
        # print(response.text)

        instance = Login.objects.create(name=name, age=age, email=email, current_weight=current_weight, target_weight=target_weight, current_height=current_height, gender=gender, body_type=body_type, body_fat=body_fat, self_assessment=self_assessment, diet=diet, motivation=motivation, exercise_frequency=exercise_frequency, type_of_workout=type_of_workout, stress_level=stress_level, sleep=sleep, tracking_method=tracking_method, nutritional_plan=nutritional_plan, workout_plan=workout_plan, progression_plan=progressions_plan)
        instance.save()

    return render(request, 'usermade.html')