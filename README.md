Project Idea
My capstone project is a Fitness Tracker API. The goal is to create a backend service that allows users to log their fitness activities, update or delete them, and view a detailed history of their workouts. This API will form the backbone of my full FitGirlsTracker app.

Key Features
The API will include the following core functionalities:
User registration and authentication (using Django’s authentication system)


Create, Read, Update, and Delete (CRUD) fitness activities


View workout history, filterable by activity type or date


View personal statistics (like number of workouts or most frequent activity)


Add optional activity goals or tags (e.g., “abs”, “booty”, “cardio”)


View activities by category or goal



API (Optional)
At this stage, I will create and use my own Django REST API to serve all the required data.
 If needed later, I may integrate the API Ninjas Exercise API to supplement the database with workout examples or expert routines.

Planned Models and Structure
Django Apps
users – Handles user registration, login, and profile


workouts – Manages workout logging and history


goals – Allows users to add goals or tags to workouts (optional for Version 1)


Models (Basic Structure)
User (extends Django’s AbstractUser)
username


email


password


age


fitness_goal (optional)


WorkoutActivity
user (ForeignKey to User)


activity_type (CharField)


duration_minutes (IntegerField)


date (DateField)


notes (TextField, optional)


goal_tag (CharField, optional)



Planned Endpoints (Initial MVP)
Endpoint
Method
Description
/api/register/
POST
Create a new user
/api/login/
POST
Login a user
/api/activities/
GET
List all activities for logged-in user
/api/activities/
POST
Log a new workout
/api/activities/<id>/
GET
View one activity
/api/activities/<id>/
PUT
Update a workout
/api/activities/<id>/
DELETE
Delete a workout
/api/history/
GET
View workout history (filter by goal or date)


Project Timeline (5-Week Plan)
Week
Goal
Week 1
Set up project, initialize Django and apps, design models
Week 2
Build authentication (register/login/logout)
Week 3
Implement CRUD for workout activities
Week 4
Build filtering for activity history, add basic validations
Week 5
Polish API, test everything, document, and deploy to Heroku or PythonAnywhere


Tools & Stack
Backend Framework: Django + Django REST Framework


Database: SQLite (locally), PostgreSQL (for deployment)


Deployment: PythonAnywhere (free tier) or Heroku


Version Control: Git and GitHub


Testing: Django’s built-in test client



Notes
I will focus on writing clean, well-documented endpoints.


Deployment will be part of the final milestone to simulate a real-world project.


If time allows, I will explore Django filtering to enhance the /history/ endpoint.


I plan to connect this API to my React-based FitGirlsTracker frontend in the next development phase.

