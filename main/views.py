from django.shortcuts import redirect, render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request,"base.html")

def HomeView(request):
    value = "None"
    name="None"
    if request.method == 'POST':
        l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze']

        disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
        'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo']

        l2=[]
        for x in range(0,len(l1)):
            l2.append(0)

        # TESTING DATA df -------------------------------------------------------------------------------------
        df=pd.read_csv("static/Symptoms-Training.csv")

        df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        # print(df.head())

        X= df[l1]

        y = df[["prognosis"]]
        np.ravel(y)
        # print(y)

        #TRAINING DATA tr --------------------------------------------------------------------------------
        tr=pd.read_csv("static/Symptoms-Testing.csv")
        tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        X_test= tr[l1]
        y_test = tr[["prognosis"]]
        np.ravel(y_test)

        from sklearn import tree

        clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
        clf3 = clf3.fit(X,y)

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.metrics import accuracy_score
        y_pred=clf3.predict(X_test)
        # print(accuracy_score(y_test, y_pred))
        # print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------

        psymptoms = [request.POST['Symptom1'],request.POST['Symptom2'],request.POST['Symptom3'],request.POST['Symptom4'],request.POST['Symptom5']]

        for k in range(0,len(l1)):
            # print (k,)
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        predict = clf3.predict(inputtest)
        predicted=predict[0]

        h='no'
        for a in range(0,len(disease)):
            if(predicted == a):
                h='yes'
                break


        if (h=='yes'):
            value=disease[a]
        else:
            value="No Output"

        name=request.POST['name']



    return render(request,
                  'main/index.html',
                  {
                      'context': value,
                      'title': 'Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'disease': True,
                      'background': 'bg-primary text-white',
                      'name': name
                  })
    


def Diabetes(request):
    """
    Reading the training data set. 
    """
    dfx = pd.read_csv('static/Diabetes_XTrain.csv')
    dfy = pd.read_csv('static/Diabetes_YTrain.csv')
    X = dfx.values
    Y = dfy.values
    Y = Y.reshape((-1,))

    """ 
    Reading data from user. 
    """
    value = ''
    if request.method == 'POST':

        pregnancies = float(request.POST['pregnancies'])
        glucose = float(request.POST['glucose'])
        bloodpressure = float(request.POST['bloodpressure'])
        skinthickness = float(request.POST['skinthickness'])
        bmi = float(request.POST['bmi'])
        insulin = float(request.POST['insulin'])
        pedigree = float(request.POST['pedigree'])
        age = float(request.POST['age'])

        user_data = np.array(
            (pregnancies,
             glucose,
             bloodpressure,
             skinthickness,
             bmi,
             insulin,
             pedigree,
             age)
        ).reshape(1, 8)

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X, Y)

        predictions = knn.predict(user_data)

        if int(predictions[0]) == 1:
            value = '1'
        elif int(predictions[0]) == 0:
            value = "2"

    return render(request,
                  'main/diabetes.html',
                  {
                      'context': value,
                      'title': 'Diabetes Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'diabetes': True,
                      'background': 'bg-dark text-white'
                  }
                  )


def Heart(request):
    """ 
    Reading the training data set. 
    """
    df = pd.read_csv('static/Heart_train.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1:]

    """ 
    Reading data from the user. 
    """

    value = ''

    if request.method == 'POST':

        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])

        user_data = np.array(
            (age,
             sex,
             cp,
             trestbps,
             chol,
             fbs,
             restecg,
             thalach,
             exang,
             oldpeak,
             slope,
             ca,
             thal)
        ).reshape(1, 13)

        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )

        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)
        predictions = rf.predict(user_data)

        if int(predictions[0]) == 1:
            value = '1'
        elif int(predictions[0]) == 0:
            value = '2'

    return render(request,
                  'main/heart.html',
                  {
                      'context': value,
                      'title': 'Heart Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'background': 'bg-danger text-white'
                  })


def Breast(request):
    """ 
    Reading training data set. 
    """
    df = pd.read_csv('static/Breast_train.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1]
    print(X.shape, Y.shape)

    """ 
    Reading data from user. 
    """
    value = ''
    if request.method == 'POST':

        radius = float(request.POST['radius'])
        texture = float(request.POST['texture'])
        perimeter = float(request.POST['perimeter'])
        area = float(request.POST['area'])
        smoothness = float(request.POST['smoothness'])

        """ 
        Creating our training model. 
        """
        rf = RandomForestClassifier(
            n_estimators=16, criterion='entropy', max_depth=5)
        rf.fit(np.nan_to_num(X), Y)

        user_data = np.array(
            (radius,
             texture,
             perimeter,
             area,
             smoothness)
        ).reshape(1, 5)

        predictions = rf.predict(user_data)
        print(predictions)

        if int(predictions[0]) == 1:
            value = '1'
        elif int(predictions[0]) == 0:
            value = "0"

    return render(request,
                  'main/breast.html',
                  {
                      'context': value,
                      'title': 'Breast Cancer Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'breast': True,
                      'background': 'bg-primary text-white'
                  })
    
from .models import Doctor_consultation, DoctorAdd
    
@csrf_exempt   
def consultation(request):
    
    disease = request.POST['submit']
    dis = disease.split(",")
    patiant_name = dis[0]
    patiant_disease = dis[1]
    
    disease1 = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis']
    disease2 = ['Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)']
    disease3 = ['Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo']
    
    if patiant_disease in disease1:
        doctors = DoctorAdd.objects.filter(Doctor_spacial__in=['Cardiologist', 'Dermatologist', 'Neurologist'])
    elif patiant_disease in disease2:
        doctors = DoctorAdd.objects.filter(Doctor_spacial__in=['Pediatrician', 'General', 'Orthopedic'])
    elif patiant_disease in disease3:
        doctors = DoctorAdd.objects.filter(Doctor_spacial__in=['Psychiatrist', 'Oncologist', 'Gynecologist', 'Urologist'])        
    else:
        doctors = ['none']
        
    
    return render(request,'main/consultation.html',{'disease':patiant_disease,'name':patiant_name,'doctors':doctors})

def appointment(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        patia_disease = request.POST['disease']
        doctor = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        dcount  = Doctor_consultation.objects.filter(Doctor_name = doctor ) 
        
        if Doctor_consultation.objects.filter(Doctor_name = doctor, appointment_date = date,appoiment_time = time).exists():
            messages.info(request,"Booking is not avilable on this time try different time")
            return redirect('RedirectError')
        if len(dcount) >= 30:
            messages.info(request,"This Doctor Alreay Finished the booking...")
            return redirect('RedirectError')
        else:
            appointment = Doctor_consultation.objects.create(Patiant_name = name,Patiant_disease = patia_disease,Doctor_name = doctor,appoiment_time = time ,appointment_date = date )
            appointment.save()
            return render(request,'main/appointment_confirm.html')
    else:
        return redirect('RedirectError')
    
def RedirectError(request):
    return render(request,"noconsultaion.html")
    
from .forms import UserRegistration
from .decorators import unautenticated_user,admin_only
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
    
@unautenticated_user
def signup(request):
    
    
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        
        if user is not None:
            request.session['username'] = username
            request.session['password'] = password
            login(request, user)
            return redirect('admin_view')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('signup')
    
    
    return render(request,'login.html')




@unautenticated_user
def registration(request):
    
    form = UserRegistration()
    
    if request.method == 'POST':
        
        form = UserRegistration(request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('registration')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('registration')
            
            else:
                user = form.save()
                user.save()
                
                group = Group.objects.get(name='patient')
                user.groups.add(group)
                
                username = form.cleaned_data.get('username')
                messages.info(request,"Account Was Created")
                return redirect('signup')
    
    return render(request,'register.html',{"form":form})

@admin_only
def admin_view(request):
    return redirect('doctor_list')

def signout(request):
    logout(request)
    return redirect('signup')

###############   ADD DOCTOR ######################

def add_doctor(request):
    
    if request.method == 'POST':
        
        name = request.POST['name']
        special = request.POST['spacial']
        date = request.POST['date']
        doctor = DoctorAdd.objects.create(Doctor_name = name,Doctor_spacial = special)
        doctor.save()
        messages.info(request,"Doctor Add Successful")
        return redirect('admin_view')
    
    return render(request,'main/add_doctor.html')


############## View Consultation Request ##########################

def consultation_request(request):
    
    requ = Doctor_consultation.objects.all()
    
    return render(request,'main/consultaion_request.html',{'requests':requ})

############## Delete consultation_delete##################


def consultation_delete(request):
    
    if request.method == 'POST':
        
        consult_id = request.POST['submit']
        consult  = Doctor_consultation.objects.get(id = consult_id)
        consult.delete()
        messages.info(request,"Consultaion Deleted successfuly")
        return redirect('consultation_request')
    
    return redirect('consultation_request')

def doctor_list(request):
    
    doctors = DoctorAdd.objects.all()
    if request.method == 'POST':
        doctor_id = request.POST['submit']
        doct = DoctorAdd.objects.get(id = doctor_id)
        doct.delete()
        messages.info(request,"Doctor Deleted successfuly")
        return redirect('doctor_list')
        
    return render(request,'main/doctor_list.html',{"doctors":doctors})

from .forms import DoctorAddForm

def doctor_edit(request, pk):
    doctor = DoctorAdd.objects.get(id = pk)
    form = DoctorAddForm()
    if request.method == 'POST':
        form = DoctorAddForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor updated successfully")
            return redirect('doctor_list')
    else:
        form = DoctorAddForm(instance=doctor)
    return render(request, 'main/doctor_edit.html', {'form': form})
        
    
def chat_bot(request):
    return render(request,"chat_bot.html")



# stress identification by virtual assistant


import google.generativeai as genai

import re

def preprocess_response(text):
    """
    Preprocess the response to handle markdown-like syntax.
    Converts:
    - ***text*** to <b><i>text</i></b> (bold + italic)
    - **text** to <b>text</b> (bold)
    - *text* to <i>text</i> (italic)
    - Newlines (\n) to <br> for line breaks
    """
    # Handle ***text*** (bold + italic)
    text = re.sub(r"\*\*\*(.*?)\*\*\*", r"<b><i>\1</i></b>", text)

    # Handle **text** (bold)
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)

    # Handle *text* (italic)
    text = re.sub(r"\*(.*?)\*", r"<i>\1</i>", text)

    # Convert newline characters (\n) to <br>
    text = text.replace("\n", "<br>")

    return text
from django.http import JsonResponse
def Suggestion(request):
    if request.method == "POST":
        question = request.POST.get("message", "").lower().strip()

        

        # Format the prompt
        prompt = f"""
            You are a healthcare chatbot of Web Doctor. Answer the customer's questions.
            The output should include healthcare suggestions, disease predictions, etc.
            Customer prompt: {question}
        """

        try:
            # Configure the GenAI API
            genai.configure(api_key="AIzaSyDfUGYziPuXs8yjd4dJdgkTiPU0CZWEvX0")
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            # Process the response
            val = preprocess_response(response.text)

            return JsonResponse({"status": "success", "response": val})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)
    



# def Symptoms(request):
#     l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
#     'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
#     'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
#     'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
#     'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
#     'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
#     'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
#     'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
#     'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
#     'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
#     'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
#     'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
#     'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
#     'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
#     'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
#     'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
#     'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
#     'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
#     'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
#     'yellow_crust_ooze']

#     disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
#     'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
#     ' Migraine','Cervical spondylosis',
#     'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
#     'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
#     'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
#     'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
#     'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
#     'Impetigo']

#     l2=[]
#     for x in range(0,len(l1)):
#         l2.append(0)

#     # TESTING DATA df -------------------------------------------------------------------------------------
#     df=pd.read_csv("static/Symptoms-Training.csv")

#     df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
#     'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
#     'Migraine':11,'Cervical spondylosis':12,
#     'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
#     'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
#     'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
#     'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
#     '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
#     'Impetigo':40}},inplace=True)

#     # print(df.head())

#     X= df[l1]

#     y = df[["prognosis"]]
#     np.ravel(y)
#     # print(y)

#     # TRAINING DATA tr --------------------------------------------------------------------------------
#     tr=pd.read_csv("Testing.csv")
#     tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
#     'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
#     'Migraine':11,'Cervical spondylosis':12,
#     'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
#     'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
#     'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
#     'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
#     '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
#     'Impetigo':40}},inplace=True)

#     X_test= tr[l1]
#     y_test = tr[["prognosis"]]
#     np.ravel(y_test)

#     value = None
#     if request.method == 'POST':

#         from sklearn import tree

#         clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
#         clf3 = clf3.fit(X,y)

#         # calculating accuracy-------------------------------------------------------------------
#         from sklearn.metrics import accuracy_score
#         y_pred=clf3.predict(X_test)
#         # print(accuracy_score(y_test, y_pred))
#         # print(accuracy_score(y_test, y_pred,normalize=False))
#         # -----------------------------------------------------

#         psymptoms = [request.POST['Symptom1'],request.POST['Symptom2'],request.POST['Symptom3'],request.POST['Symptom4'],request.POST['Symptom5']]

#         for k in range(0,len(l1)):
#             # print (k,)
#             for z in psymptoms:
#                 if(z==l1[k]):
#                     l2[k]=1

#         inputtest = [l2]
#         predict = clf3.predict(inputtest)
#         predicted=predict[0]

#         h='no'
#         for a in range(0,len(disease)):
#             if(predicted == a):
#                 h='yes'
#                 break


#         if (h=='yes'):
#             value=disease[a]
#         else:
#             value=None

#     return render(request,
#                   'main/breast.html',
#                   {
#                       'context': value,
#                       'title': 'Disease Prediction',
#                       'active': 'btn btn-success peach-gradient text-white',
#                       'disease': True,
#                       'background': 'bg-primary text-white'
#                   })
# ------------------------------------------------------------------------------------------------------


# def randomforest():
#     from sklearn.ensemble import RandomForestClassifier
#     clf4 = RandomForestClassifier()
#     clf4 = clf4.fit(X,np.ravel(y))

#     # calculating accuracy-------------------------------------------------------------------
#     from sklearn.metrics import accuracy_score
#     y_pred=clf4.predict(X_test)
#     print(accuracy_score(y_test, y_pred))
#     print(accuracy_score(y_test, y_pred,normalize=False))
#     # -----------------------------------------------------

#     psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

#     for k in range(0,len(l1)):
#         for z in psymptoms:
#             if(z==l1[k]):
#                 l2[k]=1

#     inputtest = [l2]
#     predict = clf4.predict(inputtest)
#     predicted=predict[0]

#     h='no'
#     for a in range(0,len(disease)):
#         if(predicted == a):
#             h='yes'
#             break

#     if (h=='yes'):
#         t2.delete("1.0", END)
#         t2.insert(END, disease[a])
#     else:
#         t2.delete("1.0", END)
#         t2.insert(END, "Not Found")


# def NaiveBayes():
#     from sklearn.naive_bayes import GaussianNB
#     gnb = GaussianNB()
#     gnb=gnb.fit(X,np.ravel(y))

#     # calculating accuracy-------------------------------------------------------------------
#     from sklearn.metrics import accuracy_score
#     y_pred=gnb.predict(X_test)
#     print(accuracy_score(y_test, y_pred))
#     print(accuracy_score(y_test, y_pred,normalize=False))
#     # -----------------------------------------------------

#     psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
#     for k in range(0,len(l1)):
#         for z in psymptoms:
#             if(z==l1[k]):
#                 l2[k]=1

#     inputtest = [l2]
#     predict = gnb.predict(inputtest)
#     predicted=predict[0]

#     h='no'
#     for a in range(0,len(disease)):
#         if(predicted == a):
#             h='yes'
#             break

#     if (h=='yes'):
#         t3.delete("1.0", END)
#         t3.insert(END, disease[a])
#     else:
#         t3.delete("1.0", END)
#         t3.insert(END, "Not Found")

# gui_stuff------------------------------------------------------------------------------------

# root = Tk()
# root.configure(background='blue')

# # entry variables
# Symptom1 = StringVar()
# Symptom1.set(None)
# Symptom2 = StringVar()
# Symptom2.set(None)
# Symptom3 = StringVar()
# Symptom3.set(None)
# Symptom4 = StringVar()
# Symptom4.set(None)
# Symptom5 = StringVar()
# Symptom5.set(None)
# Name = StringVar()

# # Heading
# w2 = Label(root, justify=CENTER, text="Disease Predictor using Machine Learning", fg="white", bg="blue")
# w2.config(font=("Elephant", 30))
# w2.grid(row=1, column=0, columnspan=2, padx=100)
# w2 = Label(root, justify=CENTER, text="A Project by Parth Pathak", fg="white", bg="blue")
# w2.config(font=("Aharoni", 30))
# w2.grid(row=2, column=0, columnspan=2, padx=100)

# # labels
# NameLb = Label(root, text="Name of the Patient", fg="yellow", bg="black")
# NameLb.grid(row=6, column=0, pady=15, sticky=W)


# S1Lb = Label(root, text="Symptom 1", fg="yellow", bg="black")
# S1Lb.grid(row=7, column=0, pady=10, sticky=W)

# S2Lb = Label(root, text="Symptom 2", fg="yellow", bg="black")
# S2Lb.grid(row=8, column=0, pady=10, sticky=W)

# S3Lb = Label(root, text="Symptom 3", fg="yellow", bg="black")
# S3Lb.grid(row=9, column=0, pady=10, sticky=W)

# S4Lb = Label(root, text="Symptom 4", fg="yellow", bg="black")
# S4Lb.grid(row=10, column=0, pady=10, sticky=W)

# S5Lb = Label(root, text="Symptom 5", fg="yellow", bg="black")
# S5Lb.grid(row=11, column=0, pady=10, sticky=W)


# lrLb = Label(root, text="DecisionTree", fg="white", bg="red")
# lrLb.grid(row=15, column=0, pady=10,sticky=W)

# destreeLb = Label(root, text="RandomForest", fg="white", bg="red")
# destreeLb.grid(row=17, column=0, pady=10, sticky=W)

# ranfLb = Label(root, text="NaiveBayes", fg="white", bg="red")
# ranfLb.grid(row=19, column=0, pady=10, sticky=W)

# # entries
# OPTIONS = sorted(l1)

# NameEn = Entry(root, textvariable=Name)
# NameEn.grid(row=6, column=1)

# S1En = OptionMenu(root, Symptom1,*OPTIONS)
# S1En.grid(row=7, column=1)

# S2En = OptionMenu(root, Symptom2,*OPTIONS)
# S2En.grid(row=8, column=1)

# S3En = OptionMenu(root, Symptom3,*OPTIONS)
# S3En.grid(row=9, column=1)

# S4En = OptionMenu(root, Symptom4,*OPTIONS)
# S4En.grid(row=10, column=1)

# S5En = OptionMenu(root, Symptom5,*OPTIONS)
# S5En.grid(row=11, column=1)


# dst = Button(root, text="DecisionTree", command=DecisionTree,bg="green",fg="yellow")
# dst.grid(row=8, column=3)

# rnf = Button(root, text="Randomforest", command=randomforest,bg="green",fg="yellow")
# rnf.grid(row=9, column=3,padx=10)

# lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="green",fg="yellow")
# lr.grid(row=10, column=3,padx=10)

# #textfileds
# t1 = Text(root, height=1, width=40,bg="orange",fg="black")
# t1.grid(row=15, column=1, padx=10)

# t2 = Text(root, height=1, width=40,bg="orange",fg="black")
# t2.grid(row=17, column=1 , padx=10)

# t3 = Text(root, height=1, width=40,bg="orange",fg="black")
# t3.grid(row=19, column=1 , padx=10)

# root.mainloop()



# Create your views here.
