# 🍲 Django Recipe Web App

A Django web application to manage cooking recipes. Authenticated users can create, edit, and delete their own recipes. Includes a custom "Chronos" view and stylish front-end design.

---

## 🚀 Features

- ✅ User authentication
- ✅ Recipe creation, editing, deletion
- ✅ Chronos time-based view
- ✅ Styled with custom CSS
- ✅ Admin dashboard

---

## 🛠 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/django-recipe-app.git
cd django-recipe-app
```

### 2. Create and activate a virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate it (Linux/macOS)
source venv/bin/activate

# OR for Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Then visit the app in your browser:  
http://127.0.0.1:8000/

---

## 🌐 Web Pages & Endpoints

| Method | URL Pattern                   | View Name        | Description                          |
|--------|-------------------------------|------------------|--------------------------------------|
| GET    | `/`                           | `home`           | Homepage with all recipes            |
| GET    | `/recipe/create/`             | `recipe_create`  | Recipe creation form                 |
| POST   | `/recipe/create/`             | `recipe_create`  | Submit a new recipe                  |
| GET    | `/recipe/<int:id>/edit/`      | `recipe_edit`    | Edit form for existing recipe        |
| POST   | `/recipe/<int:id>/edit/`      | `recipe_edit`    | Save edited recipe                   |
| POST   | `/recipe/<int:id>/delete/`    | `recipe_delete`  | Delete a recipe                      |
| GET    | `/chronos/`                   | `chronos`        | Custom view for time-related logic   |
| GET    | `/admin/`                     | Admin panel      | Django admin interface               |

---

## 🖌 Styling

This app uses custom CSS with the following aesthetic:

- **Background**: Light ecru (`#f5f5dc`)
- **Containers**: White boxes with subtle shadows
- **Borders**: Rounded or flat edges as needed
- **Typography**: Left-aligned, padded, modern font sizes
- **Buttons**: Styled with hover transitions

CSS file location:
static/css/styles.css

---

## 📁 Project Structure

final_project/
├── final_project/
│   ├── __init__.py
│   ├── commit.py.py
│   ├── forms.py
│   ├── models.py
│   ├── settings.py
│   ├── test.py
│   ├── views.py
│   ├── urls.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
│   |  ├── templates/
│   │       ├── home.html
│   │       ├── base.html
│   │       ├── login.html
│   │       ├── recipe_form.html
│   │       ├── recipe_list.html
│   │       ├── register.html

---

## 🧪 Run Tests

```bash
python manage.py test
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

Made with ❤️ using Django by **Gabriel Silai**.
