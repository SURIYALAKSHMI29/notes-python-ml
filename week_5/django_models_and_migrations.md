# Django Notes

## Table of Contents
1. [Django](#django)
2. [Django Models](#django-models)
3. [Migrations](#migrations)
   - [Insert data](#insert-data)
   - [Adding Foreign Key](#adding-foreign-key)
   - [Select data](#select-data)
   - [Specify URL path](#specify-url-path)
   - [View function](#view-function)
4. [Django Admin app](#django-admin-app)
5. [Django Website Flow](#django-website-flow)
6. [render() vs HttpResponseRedirect()](#render-vs-httponresponseredirect)
7. [reverse()](#reverse)
8. [csrf_token](#csrf_token)
9. [Authentication features](#authentication-features)
10. [Django Admin customization](#django-admin-customization)
11. [Field Options](#field-options)
12. [Model Relationships](#model-relationships)
13. [Querying Models](#querying-models)

---

# Django

- High-level python web framework → allows to build web applications quickly and cleanly
- Handles Database interactions, URL routing, User authentication, Admin interface, security features

# Django Models

- Way of representing the data inside the django application
- Python classes that define the structure of the database tables; Each model maps to a single table, and each class attribute represents a database field
- Install *django*
    
    ```python
    pip install django
    django-admin --version
    ```
    
- django-admin → command line tool installed with django
- In Django, project → full website, app → a part or module of that website
- Start a Django project by using
    
    ```python
    ## django-admin startproject project_name
    
    django-admin startproject grocery
    ```
    
- To run the django web application (should be inside the current project folder)
    
    ```python
    python manage.py run server
    ```
    
- Every Django project needs to have one or more apps within it
    
    ```python
    ## python manage.py startapp app_name
    # creates an app
    
    python manage.py startapp products
    ```
    
- Modify the grocery folder → settings.py → add the app created with start app inside the INSTALLED APPS
    - This ensures to include the module(app) created into the website → Like registering the app with the main website
    
    ```
    INSTALLED_APPS = [
        'products',
        ... ]
    ```
    
- grocery folder → urls.py, include the created app path
    - urls.py → has all the urls that we can get for the particular web application
    
    ```python
    from django.urls import include, path
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path("products/", include("products.urls"))
        # if the url starts with products/, then oit will be passed to products/urls.py
    ]
    ```
    
- Now, inside the products we need to have urls.py where it route the user for anything they accessed via products/
    
    ```python
    from django.urls import path
    from . import views
    
    urlpatterns = [
        
    ]
    ```
    

# Migrations

- In Django, Migrations are used to keep the database schema in sync with the models
- Model is defined in python, then django generates migration files (which are like SQL scripts) that create or update the database tables automatically
- 2 step process
    - Creating a migration, the instructions for how to manipulate the database
    - Take migration step → apply those instructions to the underlying database
- Can make migrations via command as,
    - Creates migration files in the apps's migrations/ folder
    - the migration file is instructions to django for how to manipulate the database to reflect the changes made to the model
    
    ```python
    python [manage.py](http://manage.py/) makemigrations
    
    # output
    # Migrations for 'products':
    #   products\migrations\0001_initial.py
    #     + Create model Product
    ```
    
    - Apply the migration by
    
    ```python
    python manage.py migrate
    ```
    
- After migration, db.sqlite3 file is created; A SQLite database → that contain a table that store all of the products

## Insert data

- python manage.py shell → opens a python shell
    
    ```python
    >>> from products.models import Product
    >>> p = Product(name="Lays", price=10)
    >>> p.save()
    ```
    
- When the instance of the model is created, Django add a new row of values into the table
- Query the data
    
    ```python
     >>> Product.objects.all()
     
     # Output
     <QuerySet [<Product: Product object (1)>]>  
     # indicates successful insertion
    ```
    
- It returns object (1) → we can customize this, by adding __str__ func in that model
    
    ```
    def __str__(self):
         return f"{self.id}: {self.name} costs {self.price} per unit, available: {self.available}"
    ```
    
    - After this,
        
        ```python
        >>> Product.objects.all()
        
        # output
        <QuerySet [<Product: 1: Lays costs 10.0 per unit, available: 0>]>
        ```
        
- Can access the attributes
    
    ```python
    >>> prod = Product.objects.all().first()
    >>> prod.name
    'Lays'
    ```
    
- Can delete
    
    ```python
    >>> prod.delete()
    ```
    

## Adding Foreign Key

- Foreign key → used to link tables (reference)
- Syntax
    
    ```python
    foreign_key_field = models.ForeignKey(
        RelatedModel,       # the model linking to
        on_delete=CASCADE,  # what happens if the related object is deleted
        related_name=None,  # Optional: reverse lookup name
        null=False,         # Optional: allow NULL values
        blank=False         # Optional: allow empty values in forms
    )
    ```
    

## Select data

- **model_name.objects.all()** → returns all the data
- **model_name.objects.filter(condition)** → returns the filtered data (list of objects)

```python
>>> Product.objects.filter(price__lte=50)
```

- **model_name.objects.get(condition)** → returns a single object
    - Used when we expect exaclty one result
    - If no object or more than one matches, it raises an error

## Specify URL path

**Syntax**

```python
path('url-pattern/', view_function, name='url_name')
```

- 'url-pattern/' -> the URL path want to match
Example: 'products/' -> example.com/products/, "" -> empty string, default URL of the app
- view_function -> the function in views.py that will handle this URL
 Example: views.index -> calls the index function
- name='url_name' → an optional name for the URL
Useful for referencing in templates
Example: name='index'

# View function

- handles a web request and returns a response (like an HTML page)
- Decides what data to show, how to process it, and which template to use
- *request* is an HTTP request object that django automatically passes to the view
    - *request* contains all the information about the user’s visit → URL they accessed, Form data, cookies, session info
- Fetches data from the database usig models, if needed process user input or perform operations
- Sends a HTTP response to the user using render()

# Django Admin app

- Designed for the manipulation of the models
- In order to use the admin app, we need to create an adminstrative account inside of Django web application

```python
> python manage.py createsuperuser
Username (leave blank to use 'zadmin'): suriya
Email address: suriyalakshmi413@gmail.com
Password:
Password (again):
Error: Your passwords didn't match.
Password:
Password (again):
Superuser created successfully.
```

- If we deleted db.sqlite3, → deleted the superuser account also
- To manipulate the database from the admin Dashboard, need to register them in admin.py
    
    ```python
    from django.contrib import admin
    from models import Product, Order
    
    # this allows to manipulate them from admin dashboard
    admin.site.register(Product)
    ```
    

# **Django Website Flow**

When a user request is received,

- Django first checks the **project’s *urls.py*** to find which app/module handles that URL.
- It then goes to the **app’s *urls.py***, where it maps the URL to a specific **view function**.
- The **view function** processes the request, fetching data from **models (database)** if needed and sends it to a **template (HTML)** using the *render()* function.
- Django then combines (binds) the data and the template to form an **HTML response**, which is sent back to the user’s browser.

# render() vs HttpResponseRedirect()

## render()

- Renders an HTML template as a response to the same request
- URL in browser doesn’t change
- Refreshing the page casues form resubmission, can create duplicates

## HttpResponseRedirect()

- Django class used to redirect a user to another URL
- Browser makes a new GET request to the target URL → URL in browser changes to new URL
- Usecase: After a form is submitted, usually redirects to another page instead of rendering a template directly → prevents duplicate submissions if the user refreshed the page

# reverse()

- Takes the name of the particular view and returns the url
- Allows to refer the urls by name

> In Django, *request.POST* **always returns strings**, even if the form input type is number.
> 

# csrf_token

- CSRF - Cross Site Request Forgery
- Django protects POST forms from malicious requests from other sites
- {% csrf_token %} adds a hidden input with a unique token:
    
    ```html
    <input type="hidden" name="csrfmiddlewaretoken" value="random_token_here">
    ```
    
- When the form is submitted, it checks this token to ensure the request is from our site
- If not included, then django rejects it with 403 Forbidden error

# Authentication features

- Provides authentication features

### request.user.is_authenticated

- every user in django automatically has a *User* object
- is_authenticated attribute tells whether the user is signed in or not

## django.contrib.auth

### authenticate()

- a function that checks if the username and password are correct
- Takes 3 arguments → request, username and password
- Returns the **User object** if credentials are valid, else returns **None**.

### login

- A function that is used to logs in a user
- Arguments: request and User object (from authenticate).
- Sets session cookies so the user stays signed in.

### logout

- a Function that is used to log out a user
- Arguments: request
- Clears the session so the user is signed out

# Django Admin customization

Allows to manage the models easily

## Basic Registration

Registering models in *admin.py →* make them visible in the admin interface

```python
from django.contrib import admin
from .models import Product, Order

admin.site.register(Product)
admin.site.register(Order)
```

## ModelAdmin class

Used to control how the model appears

```python
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "qty_on_hand")  # Columns in list view
    search_fields = ("name",)  # Adds a search box
    list_filter = ("qty_on_hand",)  # Filter sidebar
    ordering = ("name",)  # Default sorting

admin.site.register(Product, ProductAdmin)
```

- list_display  → fields shown in a list view
- search_fields → searchable fields
- list_filter → sidebar filters
- ordering → default sort order

## Inline Related Models

- Can show related models inside another model’s page
- allows to add/edit related items directly

> Can change the admin site header and title
Can customie fzield layouts as *readonly_fields*, *list_editable*
*actions* → used to perform bulk operations on selected rows
> 

---

## Field Options

- null = True → database column can be null
- blank = True → field to be empty in forms (doesn’t cause a validation error)
- choices → restrict field set of values
- unique = True → unique values across rows
- default= value

## Model Relationships

### One-to-One

- Links exactly one object of another model

```python
profile = models.OneToOneField(User, on_delete=models.CASCADE)
```

### Many-to-many

- multiple objects can be linked mutually

```python
	# in orders model
	customer = models.ManyToManyField(Customer, on_delete=models.PROTECT)
```

### Many-to-One

- Mutiple objects link to a single object
- Foreign Key

```python
# in OrderItem model
order= models.ForeignKey(Order, on_delete=models.CASCADE)
```

## Querying Models

Django Object Relational Models (ORM)

- Model.objects.get(pk=1) → fetch a single object
- Model.objects.all() → fetch all objects
- Model.objects.filter(field=value) → fetch filtered objects
- Model.objects.exclude(field=value) → exclude certain objects
- Model.objects.order_by('field') → sort objects
- Model.objects.count() → count objects
- Model.objects.first()/last() → get first or last object
- Model.objects.values('field1', 'field2') → get only specific fields
