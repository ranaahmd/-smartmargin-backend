# SmartMargin

SmartMargin is a full-stack web application designed to help users manage their products and ingredients efficiently. It calculates total cost, profit, and selling price based on ingredient data and user-defined profit margins.

---

##  Project & Repository Descriptions

- **Frontend Repository:** [smartmargin-frontend](https://github.com/ranaahmd/smartmargin-frontend)
- **Backend Repository:** [smartmargin-backend](https://github.com/ranaahmd/-smartmargin-backend)


---

## Tech Stack

| Layer         | Technologies Used                  |
|---------------|------------------------------------|
| Frontend      | React.js, Tailwind CSS             |
| Backend       | Django REST Framework              |
| Database      | PostgreSQL                         |
| Containerization | Docker                         |
| Authentication| JWT (JSON Web Token)               |
| Version Control| Git & GitHub                      |

---

## ERD Diagram
https://github.com/ranaahmd/-smartmargin-backend/commit/8fe3db66ce97539ebcf3652f2d5e1bc019e41923#diff-27f6aaa225fbb53364b10d5a11e6f43e7e06f1386d15329e910786164ef21180

---

## Frontend Routing Table

| Route             | Component         | Description                                 |
|-------------------|-------------------|---------------------------------------------|
| `/signup`         | SignUp            | User Registration page                      |
| `/login`          | Login             | User Login page                             |
| `/dashboard`      | Dashboard         | Overview of products and profit summary     |
| `/ingredients`    | IngredientsList   | Show all ingredients                        |
| `/ingredients/add`| IngredientsForm   | Add new ingredients                         |
| `/products`       | ProductsList      | Show all products                           |
| `/products/add`   | ProductsForm      | Add new products                            |
| `/products/:id`   | ProductsDetail    | Show product ingredients and calculations   |
| `/notes`          | Notes             | Write and manage notes                      |

---

## Backend RESTful Routing Table

| Method | URL                                | Description                                 |
|--------|------------------------------------|---------------------------------------------|
| GET    | `/api/home`                        | Home page                                   |
| POST   | `/api/signup`                      | Create a new account                        |
| POST   | `/api/login`                       | Login                                       |
| GET    | `/api/ingredients/`                | Get list of ingredients for current user    |
| POST   | `/api/ingredients/`                | Create new ingredient                       |
| PUT    | `/api/ingredients/:id/`            | Update ingredient                           |
| DELETE | `/api/ingredients/:id/`            | Delete ingredient                           |
| GET    | `/api/products/`                   | Get all products for current user           |
| POST   | `/api/products/`                   | Create new product                          |
| GET    | `/api/products/:id/`               | View single product                         |
| PUT    | `/api/products/:id/`               | Update single product                       |
| DELETE | `/api/products/:id/`               | Delete single product                       |
| POST   | `/api/products/:id/ingredients`    | Add ingredient to product                   |
| GET    | `/api/products/:id/calculate`      | Calculate cost, profit, suggested price     |

---

## Installation Instructions (Docker)

```bash
# 1. Clone the frontend repository
git clone https://github.com/ranaahmd/smartmargin-frontend
cd smartmargin-frontend

# 2. Build and start the containers
docker-compose up --build

# 4. To stop the containers
docker-compose down
