# social_media_api
Social Media API

Overview

This project is a Social Media API built with Django and Django REST Framework (DRF). It provides backend functionality for a social media platform, allowing users to create, manage, and interact with posts, follow other users, and view a personalized feed. The project uses PostgreSQL as the database and is deployed on PythonAnywhere.

Features

Core Functionalities

Post Management (CRUD):

Create, read, update, and delete posts.

Posts include content, timestamp, and optional media.

Users can only update or delete their own posts.

User Management (CRUD):

User registration, login, and profile updates.

Each user has a unique username, email, and password, with optional profile fields like bio and profile picture.

Follow System:

Users can follow and unfollow other users.

Validations to prevent self-following.

Feed of Posts:

Displays posts from followed users in reverse chronological order.

Supports pagination for large datasets.

Allows filtering by date and searching posts by keywords.

Technical Highlights

Database: PostgreSQL for efficient relational data handling.

Authentication: JWT-based authentication for secure API access.

Error Handling: Robust error messages with appropriate HTTP status codes.

Deployment: Hosted on PythonAnywhere.

Optional Features: Potential for adding likes, comments, and notifications.

Setup Instructions

Prerequisites

Python 3.9+

PostgreSQL

pip (Python package manager)

Installation

Clone the repository:

git clone https://github.com/yourusername/social-media-api.git
cd social-media-api

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Configure the database:

Update the DATABASES settings in settings.py with your PostgreSQL credentials.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Run the development server:

python manage.py runserver

Testing

Run tests to ensure everything is working correctly:

python manage.py test

Deployment

To deploy on PythonAnywhere:

Set up an account and create a new web app.

Upload your project files or clone the repository directly.

Configure your environment (e.g., virtualenv and database settings).

Restart the web app to apply changes.

API Endpoints

Authentication

POST /auth/login/: Login with username and password.

POST /auth/register/: Register a new user.

User Management

GET /users/: List all users.

GET /users/<id>/: Retrieve user details.

PUT /users/<id>/: Update user profile.

DELETE /users/<id>/: Delete user account.

Post Management

POST /posts/: Create a new post.

GET /posts/: List all posts (paginated).

GET /posts/<id>/: Retrieve post details.

PUT /posts/<id>/: Update a post (author only).

DELETE /posts/<id>/: Delete a post (author only).

Follow System

POST /follow/: Follow a user.

POST /unfollow/: Unfollow a user.

Feed

GET /feed/: Retrieve posts from followed users.

Future Enhancements

Likes and Comments: Allow users to interact with posts.

Notifications: Notify users of new followers, likes, and comments.

Advanced Filters: Enable more dynamic filtering options for posts and feeds.
