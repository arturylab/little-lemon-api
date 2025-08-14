# Little Lemon API

This is the final project for Meta's Back-End Developer Professional Certificate on Coursera. The project implements a REST API for the Little Lemon restaurant, allowing users to browse menu items, make reservations, and manage bookings.

## Features

- User authentication using Djoser and Token Authentication
- API endpoints for menu items management
- API endpoints for table bookings
- Static files serving (images and CSS)
- Unit tests for models and views

## API Endpoints

### Authentication Endpoints
- `/auth/users/` - Register new users
- `/auth/token/login/` - Obtain authentication token
- `/api-token-auth/` - Alternative endpoint for obtaining auth token

### Menu Endpoints
- `GET /restaurant/menu/` - List all menu items
- `POST /restaurant/menu/` - Create a new menu item (Auth required)
- `GET /restaurant/menu/{id}/` - Retrieve a specific menu item
- `PUT /restaurant/menu/{id}/` - Update a menu item (Auth required)
- `DELETE /restaurant/menu/{id}/` - Delete a menu item (Auth required)

### Booking Endpoints
- `GET /restaurant/booking/tables/` - List all bookings (Auth required)
- `POST /restaurant/booking/tables/` - Create a new booking (Auth required)
- `GET /restaurant/booking/tables/{id}/` - Retrieve a specific booking (Auth required)
- `PUT /restaurant/booking/tables/{id}/` - Update a booking (Auth required)
- `DELETE /restaurant/booking/tables/{id}/` - Delete a booking (Auth required)

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/arturylab/little-lemon-api.git
cd little-lemon-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django djangorestframework djoser
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Testing the API

1. First, obtain an authentication token by sending a POST request to `/api-token-auth/` with your username and password.

2. Include the token in the Authorization header for protected endpoints:
```
Authorization: Token your_token_here
```

### Example API Calls

Using curl:

1. Get menu items:
```bash
curl http://127.0.0.1:8000/restaurant/menu/
```

2. Create a booking (requires authentication):
```bash
curl -X POST http://127.0.0.1:8000/restaurant/booking/tables/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{"Name": "John Doe", "No_of_guests": 4, "BookingDate": "2025-08-14T19:00:00Z"}'
```

## Running Tests

To run the unit tests:
```bash
python manage.py test
```

## Technologies Used

- Django
- Django REST Framework
- Djoser (for authentication)
- SQLite (database)

## Project Structure

- `littlelemon/` - Project settings and main URL configuration
- `restaurant/` - Main application with models, views, and serializers
- `static/` - Static files (images, CSS)
- `templates/` - HTML templates
- `tests/` - Unit tests

## Peer Review Notes

When reviewing this project, please verify:

1. All API endpoints are working as described above
2. Authentication is properly implemented
3. CRUD operations work for both menu items and bookings
4. Unit tests pass successfully
5. The project follows REST API best practices
6. Static files are properly served
7. Error handling is implemented appropriately

## License

This project is part of the Meta Back-End Developer Professional Certificate and should be used according to Coursera's Honor Code.