# InterIntel Bulk Notification API

A Django REST Framework (DRF) API that creates a sender and multiple notifications in a single request. The API validates incoming data and efficiently inserts notifications using Django's `bulk_create()`.

---

## Features

- Django REST Framework
- Class-Based API View (`APIView`)
- Nested serializers
- Request validation
- Bulk insertion using `bulk_create()`
- SQLite database
- Postman tested

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Git & GitHub
- Postman

---

## Project Structure

```text
interintel-bulk-notification-api/
│
├── Core/
├── Notifications/
├── manage.py
├── requirements.txt
└── README.md
```

---

## API Endpoint

**POST**

```http
/api/notification/bulk/
```

### Sample Request

```json
{
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com",
  "notifications": [
    {
      "title": "Welcome",
      "message": "Welcome to our platform!",
      "channel": "email"
    },
    {
      "title": "Promotion",
      "message": "Enjoy today's special offers.",
      "channel": "sms"
    }
  ]
}
```

### Successful Response

```json
{
  "status": "success",
  "message": "Sender and notifications created successfully."
  "notification_created" : 2
  "sender_id" : 1
}
```

---

## Validation

The API validates:

- Valid email addresses
- Required fields
- Valid notification channels
- Nested request data


---

## Screenshots

### Models

![Models](images\models.png)

### Models Migration

![Migrations]()

### Successful API Request

![Successful Request](images\postman_success.png)

### Successful Response

![Successful Response]( images\api-success_response.png )

### Validation Tests

**Invalid Email**

![Invalid Email](images\invalid_email.png)

**Empty Notification**

![Empty Notification](images\Empty_notification.png)

**Multiple Notifications**

![Multiple Notifications](images\multiple notifications.png)

---

## Installation

```bash
git clone https://github.com/shirley-girl/interintel-bulk-notification-api.git

cd interintel-bulk-notification-api

python -m venv env

source env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## Future Improvements

- PostgreSQL support
- Swagger/OpenAPI documentation
- Authentication
- Unit tests

---

## Author

**Shirley Mengesa**

GitHub: https://github.com/shirley-girl