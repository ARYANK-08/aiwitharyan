### Django Models: Understanding Database Models in Django

In Django, **models** are essential to define the structure and behavior of the data you are storing. Each model maps to a single **database table**, and every model is represented as a Python class that subclasses `django.db.models.Model`. Each attribute of the model represents a field in the database.

Let's walk through an example of a basic Django project with models for a restaurant, users, and ratings.

---

### Model Definition Example

Here's an example of defining Django models for **Restaurants**, **Ratings**, and **Sales**:

```python
from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GK', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating: {self.rating}"

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2)
```

#### Explanation of Models:

- **Restaurant**: Stores details about the restaurant like name, website, date opened, coordinates (latitude, longitude), and type of cuisine. `TypeChoices` is used for selecting the restaurant type.
  
- **Rating**: Links users and restaurants. Each user can rate a restaurant. The rating is an integer between 1-5.

- **Sale**: Tracks the sales/income for each restaurant.

---

### Inserting Data into the Models

You can insert records into the database using the Django ORM. Let's see an example where we add a new restaurant:

```python
from core.models import Restaurant
from django.utils import timezone

restaurant = Restaurant()
restaurant.name = 'My Tasty Restaurant'
restaurant.latitude = 50.2
restaurant.longitude = 50.1
restaurant.date_opened = timezone.now()
restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
restaurant.website = 'https://www.letsziti.com'

restaurant.save()  # This saves the record to the database
```

This will insert a new restaurant entry into the `Restaurant` table in the database.

---

### Querying Data from Models

Django provides powerful querying options through its ORM. Here's an example of how to query all restaurants from the database:

```python
from core.models import Restaurant
from django.db import connection

restaurants = Restaurant.objects.all()
print(restaurants)
print(connection.queries)  # Outputs the SQL query Django generated
```

The result will display all restaurant entries and show the actual SQL query executed by Django:

```
<QuerySet [<Restaurant: My Tasty Restaurant>]>
[{'sql': 'SELECT "core_restaurant"."id", "core_restaurant"."name", "core_restaurant"."website", "core_restaurant"."date_opened", "core_restaurant"."latitude", "core_restaurant"."longitude", "core_restaurant"."restaurant_type" FROM "core_restaurant"', 'time': '0.001'}]
```

You can also fetch the **first restaurant** using:

```python
restaurant = Restaurant.objects.first()  # Returns the first restaurant (LIMIT 1)
```

---

### Shell Plus and Advanced Queries

Using **Django Extensions** (`shell_plus`), you can easily interact with your models:

```bash
python manage.py shell_plus --print-sql
```

With this, you'll get auto-imports of models and see the SQL queries executed during operations.

Common imports for Shell Plus:

```python
from core.models import Rating, Restaurant, Sale
from django.contrib.auth.models import User
from django.db.models import Avg, Count, F, Max, Sum
from django.utils import timezone
```

---

### Creating Records Without `.save()`

Instead of creating an object and calling `.save()`, you can use Django’s shortcut method `create()` to insert records in a single step:

```python
from core.models import Restaurant
from django.utils import timezone

Restaurant.objects.create(
    name="Pizza Shop",
    date_opened=timezone.now(),
    restaurant_type=Restaurant.TypeChoices.ITALIAN,
    latitude=20.2,
    longitude=20.1,
)
```

This will immediately insert the record into the database without needing to call `.save()`.

The generated SQL query would look like this:

```
[{'sql': 'INSERT INTO "core_restaurant" ("name", "website", "date_opened", "latitude", "longitude", "restaurant_type") VALUES (\'Pizza Shop\', \'\', \'2024-10-05\', 20.2, 20.1, \'IT\')', 'time': '0.016'}]
```

---

### Indexing and Fetching Efficiently

If you need to fetch specific records, you can index into a queryset:

```python
restaurants = Restaurant.objects.all()[0]  # Gets the first restaurant using array indexing
```



---
Here’s an improved and well-structured version of your Django ORM code with Markdown formatting, real-world examples, and simplified explanations.

---

## Django ORM Queries with Real-World Examples

This guide covers some common Django ORM queries using real-world scenarios like restaurants, ratings, and sales. By the end, you'll be able to easily perform basic database operations with Django's ORM.

---

### 1. **Counting Records**

To get the total number of **restaurants** in the database:

```python
restaurants = Restaurant.objects.count()
print(restaurants)  # Output: 2
```

- **SQL Equivalent**: `SELECT COUNT(*) FROM "core_restaurant"`
  
---

### 2. **Fetching the Last Record**

To get the **last restaurant** (based on `id` or any other sorting criteria):

```python
restaurant = Restaurant.objects.last()
print(restaurant)
```

- **SQL Equivalent**: `SELECT * FROM "core_restaurant" ORDER BY "id" DESC LIMIT 1`

---

### 3. **Working with Foreign Keys**

Let's say we have a **Rating** model where:
- **Users** can rate restaurants (1 - M relationship).
- A **restaurant** can have multiple ratings.

#### Example:

```python
restaurant = Restaurant.objects.first()  # Get the first restaurant
user = User.objects.first()              # Get the first user
Rating.objects.create(user=user, restaurant=restaurant, rating=3)
print(restaurant, user)
```

To view all **ratings**:

```python
print(Rating.objects.all())  # Output: [<Rating: Rating: 3>]
```

---

### 4. **Filtering Records**

#### Filter ratings by value:
- To find all ratings of **3 stars**:
```python
print(Rating.objects.filter(rating=3))
```
- To find all ratings of **5 stars**:
```python
print(Rating.objects.filter(rating=5))
```

#### Example: Find a restaurant by its website:
```python
restaurant = Restaurant.objects.filter(website='https://www.letsziti.com')
print(restaurant)  # Output: <QuerySet [<Restaurant: My Tasty Restaurant>]>
```

- **SQL Equivalent**: `SELECT * FROM "core_restaurant" WHERE "website" = 'https://www.letsziti.com'`

---

### 5. **Greater Than and Less Than Filters**

- **Greater than or equal to (gte)**: 
  Get ratings **greater than or equal to 3**.
  
```python
print(Rating.objects.filter(rating__gte=3))  # SQL: rating >= 3
```

- **Less than or equal to (lte)**: 
  Get ratings **less than or equal to 3**.

```python
print(Rating.objects.filter(rating__lte=3))  # SQL: rating <= 3
```

- **Exclude certain conditions**:
  
```python
print(Rating.objects.exclude(rating__lte=3))  # SQL: WHERE NOT rating <= 3
```

---

### 6. **Updating Existing Records**

To **update** an existing restaurant’s name:

```python
restaurant = Restaurant.objects.first()  # Get the first restaurant
print(restaurant)

# Update the restaurant name
restaurant.name = "Tanjiro Restaurant"
restaurant.save()

# SQL Equivalent: UPDATE "core_restaurant" SET "name" = 'Tanjiro Restaurant' WHERE "id" = 1
```

---

### 7. **Querying Related Records**

When a model has a **foreign key**, instances of the related model can be accessed via the **reverse relationship**.

#### Example:
Get the **ratings** for a restaurant using the default `rating_set` manager:

```python
restaurant = Restaurant.objects.first()
print(restaurant.rating_set.all())  # Get all ratings for the restaurant
```

You can customize this manager using `related_name`.

```python
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()
```

Now, you can use `restaurant.ratings.all()` to access all ratings for a restaurant.

---

### 8. **Creating and Querying Sales Data**

#### Defining a Sale Model:
```python
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
```

#### Adding sales for restaurants:
```python
from django.utils import timezone

Sale.objects.create(
    restaurant=Restaurant.objects.first(),
    income=233.2,
    datetime=timezone.now()
)
Sale.objects.create(
    restaurant=Restaurant.objects.first(),
    income=23.2,
    datetime=timezone.now()
)
Sale.objects.create(
    restaurant=Restaurant.objects.first(),
    income=2.2,
    datetime=timezone.now()
)
```

To view the SQL queries generated by Django:
```python
from django.db import connection
print(connection.queries)
```

---

### 9. **Get or Create Data**

To **fetch or create** a rating record:

```python
user = User.objects.first()
restaurant = Restaurant.objects.first()

rating, created = Rating.objects.get_or_create(
    restaurant=restaurant,
    user=user,
    rating=4,
)

if created:
    # Send an email or take some action
    print(f"New rating created: {rating}")
else:
    print(f"Existing rating retrieved: {rating}")
```

- `created` is `True` if the object was created and `False` if retrieved.

---

### 10. **Summary of Query Types**

| Query Type       | Example                                                    | SQL Equivalent                                            |
|------------------|------------------------------------------------------------|-----------------------------------------------------------|
| **Count**        | `Restaurant.objects.count()`                                | `SELECT COUNT(*) FROM core_restaurant`                    |
| **Last Record**  | `Restaurant.objects.last()`                                 | `SELECT * FROM core_restaurant ORDER BY id DESC LIMIT 1`   |
| **Filter**       | `Restaurant.objects.filter(website='https://www.letsziti.com')` | `SELECT * FROM core_restaurant WHERE website = '...'`      |
| **Greater Than** | `Rating.objects.filter(rating__gte=3)`                      | `SELECT * FROM core_rating WHERE rating >= 3`             |
| **Exclude**      | `Rating.objects.exclude(rating__lte=3)`                     | `SELECT * FROM core_rating WHERE NOT rating <= 3`         |

---

Here’s an improved version of the content you provided, with real-world examples, clearer explanations, and easy-to-understand Markdown formatting:

---

## Validators in Django: Adding Business Logic to Forms and Models

Validators in Django ensure that data meets certain criteria before it gets saved into the database. These are callable functions that raise a `ValidationError` when a condition is violated.

For example, let's consider a case where **only even numbers** are allowed:

```python
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError('Only even numbers are allowed.')
```

Now, let's dive into a more practical case with a **rating system**.

---

### Example: Rating System (1 to 5)

Imagine you are building a restaurant review system where users can rate restaurants between 1 to 5 stars. You want to ensure that:
- Ratings below 1 or above 5 should not be allowed.
- This should be checked both at the form level (when users submit ratings) and at the model level (to prevent direct invalid data entry).

```python
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # Restricts ratings between 1 and 5
    )
```

### Why Not Database Constraints?

Note that these validators are **not** database constraints. They only validate data when forms are submitted or when the `.save()` method is called on the model. This means if you directly create an entry via the ORM (as shown below), the validation won't stop invalid data:

```python
# Direct creation of a rating with an invalid value (rating=9)
user = User.objects.first()
restaurant = Restaurant.objects.first()

Rating.objects.create(user=user, restaurant=restaurant, rating=9)
```

This will successfully create an invalid entry in the database.

---

### Form Validation in Django

In Django, you typically validate data in forms before saving it to the database. Let's look at a form for our rating system:

```python
from django import forms
from core.models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('restaurant', 'user', 'rating')
```

### Form Submission Example

Here’s how the form could be used to handle POST requests for submitting ratings:

```python
def index(request):
    if request.method == 'POST':
        form = RatingForm(request.POST or None)
        if form.is_valid():
            form.save()  # Save the rating if valid
        else:
            return render(request, 'index.html', {'form': form})  # Re-render the form with errors
    context = {'form': RatingForm()}
    return render(request, 'index.html', context)
```

The HTML for this form might look like:

```html
<form method='POST'>
    {% csrf_token %}
    {{ form.as_p }}
    <button class="btn btn-primary" type="submit">Submit</button>
</form>
```

If a rating outside the range of 1-5 is submitted (e.g., rating=9), Django will return an error like:

```python
{'rating': ['Ensure this value is less than or equal to 5.']}
```

---

### Writing Custom Validators: Real-World Example

Let’s say you have a business rule where the **restaurant name must always start with the letter 'A'**. You can create a custom validator to enforce this rule:

```python
from django.core.exceptions import ValidationError

def validate_restaurant_name_begins_with_a(value):
    if not value.lower().startswith('a'):
        raise ValidationError('Restaurant name must begin with the letter "A".')
```

Now, apply this custom validator to your `Restaurant` model:

```python
class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_restaurant_name_begins_with_a]  # Custom validator
    )
```

If someone tries to create or update a restaurant with a name that doesn't start with "A", Django will raise a validation error.

---

### Going One Step Further: Adding Database Constraints

While validators are great for form-level and model-level validation, sometimes you want **database-level constraints** to ensure that invalid data can’t even be inserted into the database (e.g., by accident or through direct SQL queries).

You can add a **Check Constraint** at the database level to enforce these rules:

```python
class Rating(models.Model):
    rating = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1, rating__lte=5), name='rating_between_1_and_5')
        ]
```

This way, even if someone tries to bypass your form validation, the database will reject any rating outside the 1-5 range.

---

### Example: Using `get_or_create`

Let’s assume you want to create a rating for a user and restaurant, but only if it doesn’t already exist. You can use Django’s `get_or_create()` for this:

```python
user = User.objects.first()
restaurant = Restaurant.objects.first()

rating, created = Rating.objects.get_or_create(
    restaurant=restaurant,
    user=user,
    rating=4
)

if created:
    print("New rating created!")
else:
    print("Rating already exists.")
```



### Conclusion

Validators provide an excellent way to ensure data integrity at the form and model level in Django. For more robust data enforcement, adding **database constraints** is also a great option.

- **Form and Model Validation**: Ensure that invalid data doesn’t even reach the database.
- **Custom Validators**: Allow you to implement business-specific rules, like enforcing naming conventions.
- **Database Constraints**: Add an extra layer of security by restricting data at the database level.

By combining these techniques, you can build robust and error-resistant applications.


---