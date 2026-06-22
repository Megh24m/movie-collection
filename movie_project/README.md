  # Movie Collection

A Django-based Movie Collection web application where users can browse movies, search and filter them, view detailed information, discover related movies, and manage a personal wishlist.

## Features

 #### User Authentication

* User Registration
* User Login
* User Logout
* Automatic Login After Registration

 #### Movie Management

* Browse All Movies
* Movie Poster Display
* Movie Detail Page
* Movie Genres and Languages
* Related Movies Section
* Trailer Links

 #### Search and Filter

* Search Movies by Name
* Filter by Language
* Filter by Genre
* Top Rated Movies
* Popular Movies
* New Releases

#### Wishlist System

* Add Movies to Wishlist
* Remove Movies from Wishlist
* View Personal Wishlist
* Select Individual Movies
* Select Multiple Movies
* Delete Selected Movies
* Delete Entire Wishlist
* Select All Option

#### Recommendation System

* Related Movies Based on Genre
* Quick Navigation Between Similar Movies

 #### User Interface

* Responsive Movie Cards
* Modern Dark Theme
* Interactive Hover Effects
* Poster-Based Layout
* User-Friendly Navigation
* Organized Wishlist Dashboard
* Clean Authentication Pages

## Technology Stack

 Backend

* Python
* Django

 Frontend

* HTML5
* CSS3

 Database

* SQLite

 Authentication

* Django Authentication System

 Media Handling

* Pillow
* Django Media Files

 ## Project Structure
```text
Movie-Collection/

├── movie_project/
│
├── media/
│   └── movie_posters/
│
├── movie_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
├── movies/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       ├── movie_list.css
│   │       ├── movie_detail.css
│   │       └── auth.css
│   │
│   ├── templates/
│   │   ├── movie_list.html
│   │   ├── movie_detail.html
│   │   ├── register.html
│   │   ├── login.html
│   │   └── wishlist.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   └── __init__.py
│
├── screenshots/
│
├── db.sqlite3
├── manage.py
└── README.md
```

 ## Application Workflow
```text
User Registration
      ↓
User Login
      ↓
Browse Movies
      ↓
Search / Filter Movies
      ↓
View Movie Details
      ↓
Add Movies To Wishlist
      ↓
Manage Wishlist
      ↓
Explore Related Movies
```

## Movie Information
Each movie record contains:

* Movie Name
* Genre
* Language
* Director
* Actor
* Actress
* Release Year
* Collection
* Rating
* Trailer URL
* Poster Image
* Created Date

 ## Wishlist Workflow
```text
Add Movie
    ↓
Wishlist
    ↓
Select Individual Movies
         OR
Select All Movies
    ↓
Delete Selected
         OR
Delete All
```

 ## Installation

### Clone Repository

git clone https://github.com/your-username/movie-collection.git

cd movie-collection


### Create Virtual Environment

python -m venv venv


### Activate Virtual Environment (Windows)

venv\Scripts\activate


### Install Dependencies

pip install django pillow

### Apply Migrations

python manage.py makemigrations

python manage.py migrate

### Create Superuser

python manage.py createsuperuser

### Run Development Server

python manage.py runserver

Open:
http://127.0.0.1:8000/

 ## Screenshots

* Home Page
* Search and Filters
* Movie Detail Page
* Related Movies Section
* Registration Page
* Login Page
* Wishlist Page
* Select and Delete Wishlist Items

## Key Highlights

* User Authentication System
* Search and Filter Functionality
* Genre-Based Recommendations
* Wishlist Management
* Bulk Delete Operations
* Movie Posters and Media Support
* Responsive User Interface
* Django Class-Based Views
* Secure Access Control
* Organized Database Structure

## Future Enhancements

* Movie Reviews and Comments
* User Ratings
* Watch Later Feature
* Recently Viewed Movies
* Personalized Recommendations
* Email Notifications
* REST API Integration
* TMDB API Integration
* Pagination
* Dark and Light Mode Toggle
* Mobile Responsive Optimization

## Author

Meghana M

Built using Django, Python, HTML, CSS, SQLite, and Pillow. """
