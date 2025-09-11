# Hospital Management System

[Live Demo](https://hospital-management-system-obzb.onrender.com/)

A full-featured Django-based Hospital Management System that allows **patients**, **doctors**, and **admins** to manage hospital operations efficiently. The system handles appointments, user registration, doctor approvals, patient management, and contact submissions.

---

## Features

### General
- Homepage, About, Experts, and Contact pages.
- Contact form stores messages in the database for admin review.

### Authentication
- Patient and Doctor registration.
- Doctor accounts require admin approval to log in.
- Login system for **admin**, **doctor**, and **patient**.
- Logout functionality.

### Admin Panel
- View, approve, and delete doctors.
- View, edit, and delete patient profiles.
- View all contact messages submitted through the contact form.

### Doctor Panel
- View personal profile.
- Edit personal information.
- View patients assigned.
- View and approve appointments.

### Patient Panel
- View personal profile.
- Edit personal information.
- View list of approved doctors.
- Book appointments with doctors.
- View appointments and status.

### Models
- **MYUSER** – Custom user model with user_type (patient, doctor, admin).
- **Doctor** – Stores doctor profile, department, and image.
- **Patient** – Stores patient profile, age, and gender.
- **Appointment** – Handles appointment details and status.
- **Contact** – Stores messages sent from contact form.

---

## Installation

1. Clone the repository:

```bash
git clone [<your-repo-url>](https://github.com/minnulekha/Hospital-Management-System.git)
````

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:

```bash
python manage.py createsuperuser
```

6. Run the server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## Usage

* **Patients:** Register, log in, edit profile, view doctors, and book appointments.
* **Doctors:** Register, wait for admin approval, log in, edit profile, view patients and appointments.
* **Admin:** Log in with superuser account, manage doctors, patients, and contact messages.

---

## Technologies Used

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default) / can be switched to PostgreSQL or MySQL
* **Deployment:** Render

---

## Deployment

This project is deployed on Render: [Hospital Management System](https://hospital-management-system-obzb.onrender.com/)

---

## Folder Structure

```
├── app/              # Django app
│   ├── migrations/
│   ├── templates/         # HTML templates
│   ├── static/            # CSS, JS, images
│   ├── models.py          # All models
│   ├── views.py           # All views
│   └── urls.py
├── projet/   # Project settings
├── manage.py
└── requirements.txt
```

---

## Notes

* Doctor accounts require **admin approval** before they can log in.
* Patient registration is **immediately active**.
* Appointment slots are pre-defined: `09:00`, `13:00`, `17:00`.
* Users can edit their profiles after registration.
* Admin can view and manage all users and contact submissions.

---

## License

This project is licensed under the MIT License.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
