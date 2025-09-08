# Superuser
 - username: Mokhethi
 -Password: ILoveProgramming

# Maintenance Repair Tag System

A Django REST Framework (DRF) application for managing maintenance and repair tags in an organization. This system enables users to create, assign, and track repair tags and actions, with department-based restrictions and superuser privileges.

---

## Features

- **User Management**
  - Users can view and update their own profiles.
  - Superusers can edit all profiles.
  - Department-based access for tags and actions.

- **Repair Tags**
  - Create, view, and track repair tags.
  - Assign actions to users in the same department.
  - Tag statuses: Open, In Progress, Completed.
  - Priority levels and repair types.

- **Actions**
  - Automatically track who assigned an action (`assigned_by`).
  - Upload evidence files or images.
  - Action completion tracking.
  - Action status reflect automatically in the tag

- **Dashboard**
  - Department-based statistics.
  - Total tags, status breakdown, priority breakdown, and repair type breakdown.

- **Authentication**
  - Session Authentication using DRF.
  - Only authenticated users can interact with the API.
  - Regular users:
    - Can view and update their own profile.
    - Can create and view tags and actions for users in their department.
  - Superusers:
    - Can view and edit all profiles.
    - Full access to all repair tags and actions.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:mokhethi-k/Capstone_project.git
   cd Capstone_project


## Dependacies installation
    pip install -r requirements.txt


## Aplly migrations
    python manage.py migrate

## Create superuser
    python manage.py createsuperuser

## Run the server
    python manage.py runserver

## Access the admin site
    http://127.0.0.1:8000/admin/
    

## API Endpoints

    | Endpoint            | Description                         |
| ------------------- | ----------------------------------- |
| `/api/users/`       | List or create users                |
| `/api/profiles/`    | List or manage user profiles        |
| `/api/tags/`        | List, create, and view repair tags  |
| `/api/actions/`     | List and manage actions             |
| `/api/dashboard/`   | Department-based dashboard stats    |
| `/api/auth/login/`  | Login endpoint (DRF browsable auth) |
| `/api/auth/logout/` | Logout endpoint                     |

