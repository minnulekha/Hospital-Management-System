from django.urls import path
from .views import home_view, about, experts, contact, patient_register, login_all, adminpage, doctor_register, patient_home_page, Doctor_home_page,view_patient_by_admin,delete_patient_by_admin,approve_patient_by_admin,view_patient_by_doctor,view_all_doctors,edit_doctor,update_doctor,edit_patient_profile,view_all_doctors,logout_user,view_contacts,book_appointment,view_appointments_doctor,approve_appointment,view_appointments_patient,view_doctors_by_patients

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about, name='about'),
    path('experts/', experts, name='experts'),
    path('contact/', contact, name='contact'),
    path('pat_reg/', patient_register, name='pat_reg'),
    path('login/', login_all, name='login'),
    path('admin1/', adminpage, name='adminpage'),
    path('doc_reg/', doctor_register, name='doc_reg'),
    path('phome/', patient_home_page, name='phome'),
    path('dhome/', Doctor_home_page, name='dhome'),
    path('admin1/view_patient_by_admin/', view_patient_by_admin, name='view_patient_by_admin'),
    path('admin1/view_patient_by_admin/del_patient/<int:id>/', delete_patient_by_admin, name='delete_patient_by_admin'),
    path('admin1/view_patient_by_admin/approvepati/<int:id>/', approve_patient_by_admin, name='approve_patient_by_admin'),
    path('dhome/view_pat_by_dr', view_patient_by_doctor),
    path('dhome/view_doctors/', view_all_doctors, name='view_doctors'),
    path('dhome/edit_doctor', edit_doctor, name='edit_doctor'),
    path('update_doc/<int:id>/', update_doctor, name='update_doctor'),
    path('phome/edit_patient/<int:id>/', edit_patient_profile, name='edit_patient'),
    path('phome/view_doctors_patient/', view_doctors_by_patients, name='view_doctors_patient'),
    path('phome/logout/', logout_user, name='logout'),
    path('dhome/logout/', logout_user, name='logout'),
    path('view_contacts/', view_contacts, name='view_contacts'),
    path('book_appointment/', book_appointment, name='book_appointment'),
    path('view_appointments_doctor/', view_appointments_doctor, name='view_appointments_doctor'),
    path('approve_appointment/<int:id>/', approve_appointment, name='approve_appointment'),
    path('phome/view_appointments_patient/', view_appointments_patient, name='view_appointments_patient'),


]