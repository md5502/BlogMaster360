# Django Blog and Dashboard Application

This project is a Django-based web application that includes a blog and user dashboard with authentication, post management, and profile editing features.

## Features
- **User Authentication**
  - Signup, login, and logout functionality.
  - Password reset via email.
- **User Dashboard**
  - Manage posts (create, update, delete).
  - Edit user profiles.
- **Blog**
  - Post creation and commenting.
  - Post and comment management in the admin interface.
- **Admin Panel**
  - Manage users, posts, and profiles.
  - Custom admin model configuration.
- **Profile Management**
  - Users can edit their profiles with form validation.
  - Automatic profile creation on user registration.

## Project Structure

```bash
.
├── blog
│   ├── admin.py                # Blog admin configuration
│   ├── apps.py                 # Blog app configuration
│   ├── forms.py                # Blog forms (post, comments)
│   ├── models.py               # Blog models (Post, Category, Tag, Comment)
│   ├── templates/blog          # Blog templates (home, post detail)
│   ├── urls.py                 # Blog URL configuration
│   └── views.py                # Blog views
├── dashboard
│   ├── admin.py                # Dashboard admin configuration
│   ├── forms.py                # Dashboard forms (profile, posts)
│   ├── models.py               # Dashboard models
│   ├── signals.py              # User signals for profile creation
│   ├── templates/dashboard     # Dashboard templates (profile, post management)
│   ├── urls.py                 # Dashboard URL configuration
│   └── views.py                # Dashboard views
├── users
│   ├── forms.py                # User registration and profile forms
│   ├── models.py               # User profile model
│   ├── templates/users         # User templates (registration)
│   ├── urls.py                 # User URL configuration
│   └── views.py                # User views
├── config
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   └── wsgi.py                 # WSGI entry point
├── manage.py                   # Django's command-line utility
├── db.sqlite3                  # SQLite database file
├── requirements.txt            # Python dependencies
├── ruff.toml                   # Linter configuration
├── templates
│   ├── base.html               # Base template
│   └── registration            # Templates for Django authentication
└── media                       # Media files (user uploads)
```

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/md5502/django-blog-dashboard.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the site at `http://127.0.0.1:8000/`.

## Custom Commands

- **Populate Data**: Use the custom management command to generate fake data for testing:

  ```bash
  python manage.py populate_data
  ```

## Linting

The project uses `ruff` as a linter. You can run the linter with the following command:

```bash
ruff check .
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Developed by [md5502](https://github.com/md5502)
