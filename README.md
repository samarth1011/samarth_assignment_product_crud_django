
# SDE 1 Python Assignment

Name: Samarth Godase
mail: samarth.mailme@gmail.com

I have implemented the assignment using Django Rest Framework and have used class based views and model serializers for the implementation of API.



## API Reference

#### Below is example for api with urls and what operations it can perform

```http
  [
    {
        "url": "/api/v1/products/",
        "description": "View and create products, Delete all Products"
    },
    {
        "url": "/api/v1/products/1/",
        "description": "Update or delete a product by ID."
    },
    {
        "url": "/api/v1/products/saree/",
        "description": "Find product by title."
    },
    {
        "url": "/api/v1/categorys/men/",
        "description": "Find product by category."
    },
    {
        "url": "/api/v1/products_price_greater_then/399/",
        "description": "Find products with price greater than the specified value."
    }
]
```




## Environment Variables

The environment file .env.prod is present in which below variables are present

`SECRET_KEY`
`DEBUG`

Generally we dont expose these `SECRET_KEY` variable publically and in production application should keep `DEBUG` as False


## Run on Docker

Follow below command to run docker container

```bash
  - git clone https://github.com/samarth1011/samarth_assignment_product_crud_django.git
  - cd inventory_management
  - docker-compose build
  - docker-compose up -d
```

The API would be running on localhost on port 8000
link: http://localhost:8000/api/v1
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/samarth1011/samarth_assignment_product_crud_django.git
```

Go to the project directory

```bash
  cd inventory_management
```

Install dependencies

```bash
  - python -m venv env #create virtual environment
  - cd env/scripts
  - activate
  - pip install -r requirements.txt
  - python manage.py migrate

```

Start the server

```bash
  python manage.py runserver
```

server would be running on http://127.0.0.1:8000/

Django Admin Access - superuser
http://localhost:8000/admin
```bash
  username: sam
  password: Pccoe@123
```


## Some Screenshots

![App Screenshot](https://github.com/samarth1011/samarth_assignment_product_crud_django/blob/main/screenshots/image.png?raw=true)


#### Exception Handling

![App Screenshot](https://github.com/samarth1011/samarth_assignment_product_crud_django/blob/main/screenshots/abc.png?raw=true)




