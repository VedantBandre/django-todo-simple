# Django To-Do App

A minimal but stylish **To-Do List application** built with **Django** + **Tailwind CSS**.  
Features CRUD functionality (Create, Read, Update, Delete) with a light/dark mode toggle.

---

## Screenshots

### Light Mode
<div align="center">
  <img width="30%" height="720" alt="homepage-light" src="https://github.com/user-attachments/assets/8a278ad0-35ab-4f82-b07b-d4f893aec86a" />
  <img width="30%" height="720" alt="update-light" src="https://github.com/user-attachments/assets/44f35b05-c6f1-4543-a51b-76d6daabbb77" />
  <img width="30%" height="720" alt="delete-light" src="https://github.com/user-attachments/assets/ea31d4a0-46ec-437f-9cc1-c19cd33f82bc" />
</div>

### Dark Mode
<div align="center">
  <img width="30%" height="720" alt="image" src="https://github.com/user-attachments/assets/38eb4eb6-8228-45d5-91f0-4835aa3f877c" />
  <img width="30%" height="720" alt="image" src="https://github.com/user-attachments/assets/dc7ac3f2-126e-4650-8945-f4732bb47045" />
  <img width="30%" height="720" alt="image" src="https://github.com/user-attachments/assets/0a9e30c0-2903-42d3-b850-6e3358156e90" />
</div>

---

## Features

-  Add new tasks  
-  Update tasks (edit title or mark as completed)  
-  Delete tasks with confirmation  
-  Dark/Light mode toggle (persisted via `localStorage`)  
-  Styled with Tailwind CSS  
-  Basic unit tests included  

---

##  Tech Stack

- [Django 5.x](https://www.djangoproject.com/) — backend framework  
- [Tailwind CSS](https://tailwindcss.com/) — styling & responsive UI  
- [SQLite](https://www.sqlite.org/) — default database  

---

##  Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/VedantBandre/django-todo-simple.git
   cd django-todo-simple


2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server**

   ```bash
   python manage.py runserver
   ```

6. Open your browser at  [http://localhost:8000](http://localhost:8000)

---

##  Running Tests

```bash
python manage.py test
```

---

##  Project Structure

```
django-todo-simple/
├── config/           # Project settings
├── tasks/            # Main app (models, views, urls, templates, static)
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── list.html
│   │       ├── update_task.html
│   │       └── delete.html
│   └── static/tasks/  # CSS, JS, Images
├── manage.py
└── README.md
```

---


##  License

This project is licensed under the MIT License.

---

 Built with Django & TailwindCSS by [Vedant Bandre](https://github.com/VedantBandre)
