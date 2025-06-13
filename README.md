# Little Lemon Web Site

## Set Environments

1. Spin up a new DB
```bash
docker run --name mysql01 -e MYSQL_ROOT_PASSWORD=root@123 -p 3306:3306 -d mysql

mysql -h127.0.0.1 -uroot -p

CREATE DATABASE LittleLemon;
```

2. Make a new python dev env
```bash
pipenv shell
pipenv install
```

3. Set database on MySQL
```bash
cd littlelemon
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser
```bash
python manage.py createsuperuser
```

5. Run the server
```bash
python manage.py runserver
```

6. Get an admin token
Go to http://127.0.0.1:8000/auth/token/login/
or
```bash
curl --request POST \
  --url http://127.0.0.1:8000/restaurant/api-token-auth/ \
  --header 'Content-Type: multipart/form-data' \
  --form username=<your_username> \
  --form password=<your_password>
curl --request POST \
  --url http://127.0.0.1:8000/restaurant/api-token-auth/ \
  --header 'Content-Type: multipart/form-data' \
  --form username=tester \
  --form password=test123
```

## API Endpoints

### Authentication
- `POST /restaurant/api-token-auth/` - Obtain authentication token
  - Returns a token that must be included in the Authorization header for protected endpoints
  - Required headers: `Authorization: Token <your_token>`

### Menu Items
- `GET /restaurant/menu/` - List all menu items
  - Returns a list of all menu items

- `POST /restaurant/menu/` - Create a new menu item
  - Request body: Menu item details
  - Returns the created menu item

Sample data:
```json
{
    "title": "Grilled Salmon",
    "price": "24.99",
    "inventory": 15,
    "description": "Fresh Atlantic salmon fillet grilled to perfection, served with seasonal vegetables and lemon butter sauce. Accompanied by roasted potatoes and a side of our house-made tartar sauce."
}

{
    "title": "Classic Margherita Pizza",
    "price": "16.99",
    "inventory": 20,
    "description": "Traditional Italian pizza topped with fresh mozzarella, ripe tomatoes, and fragrant basil leaves. Baked in our wood-fired oven for that perfect crispy crust. Made with our house-made tomato sauce and premium buffalo mozzarella."
}
```

- `GET /restaurant/menu/<int:pk>` - Get a specific menu item
  - Parameters: `pk` (menu item ID)
  - Returns details of the specified menu item

### Bookings
- `GET /restaurant/bookings/` - List all bookings
  - *Authentication required*
  - Returns a list of all bookings

- `POST /restaurant/bookings/` - Create a new booking
  - *Authentication required*
  - Request body: Booking details
  - Returns the created booking

- `GET /restaurant/bookings/<int:pk>/` - Get a specific booking
  - *Authentication required*
  - Parameters: `pk` (booking ID)
  - Returns details of the specified booking

- `PUT /restaurant/bookings/<int:pk>/` - Update a booking
  - *Authentication required*
  - Parameters: `pk` (booking ID)
  - Request body: Updated booking details
  - Returns the updated booking

- `DELETE /restaurant/bookings/<int:pk>/` - Delete a booking
  - *Authentication required*
  - Parameters: `pk` (booking ID)
  - Returns 204 No Content on success

Note: All protected endpoints require authentication using a token obtained from the `/restaurant/api-token-auth/` endpoint. Include the token in the request header as `Authorization: Token <your_token>`.
