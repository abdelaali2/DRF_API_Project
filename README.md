<h1 align="center">E-Commerce Web Application</h1>

---

<p align="center"> The ecommerce API project aims to create a secure and functional online shopping platform using Django Rest Framework (DRF). The API allows users to authenticate using tokens, browse and search for products by categories, manage user accounts, and complete checkouts. This documentation provides an overview of the key features, requirements, deliverables, and instructions on how to use the API.
    <br>
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Built Using](#built_using)


---

## 🧐 About <a name = "about"></a>

Key Features :

1. User Authentication using Tokens: Users can authenticate using token-based authentication. Tokens are generated upon successful login and are required for accessing protected endpoints. Tokens expire after an hour, ensuring security.
2. Category Management System: The API allows the management of categories through API endpoints provided by DRF. Categories can be created, retrieved, updated, and deleted using the API.
3. Product Catalog with Search and Filter Functionality: Users can browse products by categories and search for specific products using keywords. The API provides endpoints for retrieving products by category and searching for products based on keywords. Products can be filtered based on various criteria such as price, ratings, etc.
4. User Management System: Users can create an account, update their profile, and view their order history through the API endpoints. User accounts are protected with token-based authentication, ensuring secure access to user information.
5. Checkout Functionality: The API allows users to complete the checkout process by collecting user information, shipping details, and payment information. Checkout functionality is implemented through API endpoints that handle order creation, order retrieval, and payment processing.

---

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

```
  1. Python installed on your machine

  2. Git installed on your machine

  3. MySQL Server

  4. Postman (or any other API Client you prefer)
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
1. Open the terminal in directory where you want to install the software.

2. run the following commands:

  git clone https://github.com/abdelaali2/DRF_API_Project

  cd DRF_API_Project

  python -m venv .venv

  source .venv/Scripts/Activate
  // You should see (.venv) written in the terminal before your username

  pip install -r requirements.txt

  cd ECommerce_DRF

  python manage.py makemigrations

  python manage.py migrate

  python manage.py runserver

3. From your browser navigate to localhost:8000

4. from your API Client navigate through the different links mentioned in the webpage.
```

---

## ⛏️ Built Using <a name = "built_using"></a>

- [MySQL](https://www.mysql.com/) - Database
- [Django REST Framework (DRF)](https://www.django-rest-framework.org/) - Web Framework

## ✍️ Authors <a name = "authors"></a>

- [@Ibrahim Badr (abdelaali2)](https://github.com/abdelaali2)
- [@Ahmed Yasser (AhmedYasser136)](https://github.com/AhmedYasser136)
