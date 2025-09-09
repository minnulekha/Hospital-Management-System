from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient, Appointment, MYUSER,Contact

def home_view(request):
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')

def experts(request):
    return render(request, 'expert.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, 'contact.html', {'success': True})
    
    return render(request, 'contact.html')

def patient_register(request):
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        un = request.POST['username']
        ag = request.POST['age']
        gn = request.POST['gender']
        pw = request.POST['password']

        
        user = MYUSER.objects.create_user(
            first_name=fn,
            last_name=ln,
            email=em,
            username=un,
            password=pw,
            user_type="patient",
            is_active=False  
        )
        user.save()

      
        Patient.objects.create(
            Patient_id=user,
            name=f"{fn} {ln}",
            age=int(ag),
            gender=gn
        )

        return redirect('login')

    return render(request, "pati_reg.html")


def doctor_register(request):
    if request.method == "POST":
        fn = request.POST["firstname"]
        ln = request.POST["lastname"]
        e = request.POST["email"]
        u = request.POST['username']
        p = request.POST['password']
        na = request.POST["name"]
        doc = request.FILES.get("doc_image")

        if MYUSER.objects.filter(username=u).exists():
            return HttpResponse("Username already exists. Try another one.")

        x = MYUSER.objects.create_user(
            first_name=fn,
            last_name=ln,
            username=u,
            email=e,
            password=p,
            user_type="doctor",
            is_active=True,
            is_staff=True
        )
        Doctor.objects.create(Doctor_id=x, name=na, doc_image=doc)
        return redirect('login')
    return render(request, "doctor_reg.html")

def login_all(request):
    if request.method == "POST":
        us = request.POST["username"]
        pas = request.POST["password"]
        user = authenticate(request, username=us, password=pas)

        if user:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('adminpage')
            elif user.user_type == 'doctor':
                request.session['doctor_id'] = user.id
                return redirect('dhome')
            elif user.user_type == 'patient':
                request.session['patient_id'] = user.id
                return redirect('phome')
        return HttpResponse("Invalid credentials")
    return render(request, "login.html")

def adminpage(request):
    return render(request, 'adminhome.html')

def Doctor_home_page(request):
    if not request.user.is_authenticated:
        return redirect(login_all)
    y = get_object_or_404(Doctor, Doctor_id=request.user)
    return render(request, 'doctorhome.html', {'f': y.Doctor_id.first_name, 'l': y.Doctor_id.last_name})

def patient_home_page(request):
    if not request.user.is_authenticated:
        return redirect(login_all)
    y = get_object_or_404(Patient, Patient_id=request.user)
    return render(request, 'patienthome.html', {'f': y.Patient_id.first_name, 'l': y.Patient_id.last_name})

@login_required
def view_patient_by_admin(request):
    patients = Patient.objects.select_related('Patient_id').all()
    return render(request, 'view_patient_by_admin.html', {'views': patients})

@login_required
def delete_patient_by_admin(request, id):
    patient = get_object_or_404(Patient, id=id)
    user = patient.Patient_id
    patient.delete()
    user.delete()
    return redirect('view_patient_by_admin')

@login_required
def approve_patient_by_admin(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.is_approved = True         # ✅ set approved status
    patient.save()

    user = patient.Patient_id
    user.is_active = True              # ✅ allow login
    user.save()

    return redirect('view_patient_by_admin')


@login_required
def view_contacts(request):
    contacts = Contact.objects.all().order_by('-submitted_at')
    return render(request, 'view_contacts.html', {'contacts': contacts})


def view_patient_by_doctor(request):
    s = Patient.objects.select_related('Patient_id').all()
    return render(request, 'view_patient_doctor.html', {'view': s})

def view_all_doctors(request):
    doctors = Doctor.objects.select_related('Doctor_id').all()
    return render(request, 'view_doctor_doctor.html', {'view': doctors})

def edit_doctor(request):
    doctor_id = request.session.get('doctor_id')
    if not doctor_id:
        return redirect('login')
    
    doctor = get_object_or_404(Doctor, Doctor_id_id=doctor_id)
    user = get_object_or_404(MYUSER, id=doctor_id)
    
    return render(request, 'edit_doctor.html', {'views': doctor, 'data': user})

def update_doctor(request, id):
    if request.method == 'POST':
        user = get_object_or_404(MYUSER, id=id)
        doctor = get_object_or_404(Doctor, Doctor_id=user)

        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.username = request.POST['username']

        new_password = request.POST['password']
        if new_password:
            user.set_password(new_password)  

        user.save()
        doctor.save()

        return redirect('dhome')
    else:
        return HttpResponse("Invalid request")
    

def edit_patient_profile(request, id):
    user = get_object_or_404(MYUSER, id=id)
    patient = get_object_or_404(Patient, Patient_id=user)

    if request.method == "POST":
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.username = request.POST['username']
        if request.POST['password']:
            user.set_password(request.POST['password'])
        user.save()

        patient.age = request.POST['age']
        patient.gender = request.POST['gender']
        patient.name = user.first_name + ' ' + user.last_name
        patient.save()

        return redirect('phome')  

    return render(request, "edit_patient.html", {"user": user, "patient": patient})

def view_doctors_by_patients(request):
    doctors = Doctor.objects.all()
    return render(request, "view_doctors_patient.html", {'view': doctors})

@login_required
def book_appointment(request):
    patient = get_object_or_404(Patient, Patient_id=request.user)
    doctors = Doctor.objects.all()
    time_slots = ["09:00", "13:00", "17:00"]

    if request.method == "POST":
        doctor_id = request.POST["doctor"]
        date = request.POST["date"]
        time = request.POST["time"]

        doctor = get_object_or_404(Doctor, id=doctor_id)
        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time=time
        )
        return redirect("phome")

    return render(request, "book_appointment.html", {"doctors": doctors, "slots": time_slots})

@login_required
def view_appointments_doctor(request):
    doctor = get_object_or_404(Doctor, Doctor_id=request.user)
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, "view_appointments_doctor.html", {"appointments": appointments})

@login_required
def approve_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.status = "Appointed"
    appointment.save()
    return redirect("view_appointments_doctor")

@login_required
def view_appointments_patient(request):
    patient = get_object_or_404(Patient, Patient_id=request.user)
    appointments = Appointment.objects.filter(patient=patient).select_related('doctor').order_by('-date', '-time')
    return render(request, 'view_appointments_patient.html', {'appointments': appointments})




def logout_user(request):
    logout(request)
    return redirect('login')

