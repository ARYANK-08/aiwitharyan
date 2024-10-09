# Django ORM's : The beauty of Django with SQL 

## Models of Django :

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
# Django ORM: Querying and Updating Records with Real-World Examples

In Django, manipulating the database using querysets is one of the most powerful features of the ORM (Object Relational Mapper). Let's break down how to **update**, **filter**, and **delete** records, including **field lookups** and the effect of the `on_delete` argument in ForeignKey relationships, with real-world examples.

## Updating Records in Django

When you update a record in Django, you can either save all fields or specify which fields to update. This can optimize your query by only touching the fields you need.

### Example 1: Updating a Single Record

```python
restaurant = Restaurant.objects.first()
print(restaurant.name)  # Output: Current Restaurant Name

# Update the name and save it to the database
restaurant.name = 'New Restaurant Name'
restaurant.save()

# OR, update only the 'name' field
restaurant.save(update_fields=['name']) 
```

Here, using `update_fields=['name']` ensures that only the `name` field gets updated, instead of updating all fields in the model, improving efficiency.

### Example 2: Updating Multiple Records

You can update multiple records at once using the `update()` method on a queryset.

```python
from django.utils import timezone

# Update the `date_opened` field for all restaurants
Restaurant.objects.all().update(date_opened=timezone.now())
```

This executes a single SQL query that updates **all records**. The query looks like this:

```sql
UPDATE "core_restaurant" SET "date_opened" = '2024-10-06';
```

### Example 3: Field Lookups

Field lookups are used to specify conditions in querysets, similar to SQL `WHERE` clauses.

1. **Exact Match**:
   - `Entry.objects.get(id__exact=14)` becomes `WHERE id = 14`
   - `Entry.objects.get(id__exact=None)` becomes `WHERE id IS NULL`

2. **Case-Insensitive Match**:
   - `Blog.objects.get(name__iexact="beatles blog")` becomes `WHERE name ILIKE 'beatles blog'`
   - This will match entries like "Beatles Blog", "beatles blog", "BeAtLes BLoG", etc.

3. **Contains**:
   - `Entry.objects.get(headline__contains="Lennon")` becomes `WHERE headline LIKE '%Lennon%'`
   - Use `icontains` for case-insensitive search.

4. **Greater Than and Less Than**:
   - `Entry.objects.filter(id__gt=4)` becomes `WHERE id > 4`
   - `Entry.objects.filter(id__gte=4)` becomes `WHERE id >= 4`

5. **Startswith**:
   - `Entry.objects.filter(headline__startswith="Lennon")` becomes `WHERE headline LIKE 'Lennon%'`
   - **SQLite Note**: SQLite doesn’t support case-sensitive LIKE statements.

### Example 4: Querying and Updating with Field Lookups

```python
# Get restaurants whose names start with 'P'
restaurant_qs = Restaurant.objects.filter(name__startswith='P')

# Update the `date_opened` field for these restaurants
restaurant_qs.update(date_opened=timezone.now() - timezone.timedelta(days=365))

print(connection.queries)  # To see the SQL queries being run
```

This updates all restaurants starting with "P" and sets their opening date to one year ago.

## Deleting Records in Django

Django makes it easy to delete records, whether it's a single object or multiple ones.

### Example 1: Deleting a Single Object

```python
restaurant = Restaurant.objects.first()

# Deleting the restaurant
print(restaurant.delete())  # (7, {'core.Rating': 6, 'core.Restaurant': 1})
```

When you delete a `Restaurant`, if it has a ForeignKey relation with `Rating` (using `on_delete=models.CASCADE`), the associated ratings are deleted as well. The numbers in the output indicate how many objects were deleted (`6` ratings and `1` restaurant).

### Example 2: Deleting Multiple Objects

```python
Restaurant.objects.all().delete()  # Deletes all restaurants
```

This will delete all the records in the `Restaurant` table.

## Foreign Key `on_delete` Behavior

Django provides options on how to handle the deletion of related objects when a referenced object is deleted.

### Example 1: `CASCADE`
When a `Restaurant` is deleted, any related `Rating` objects will be deleted as well.

```python
restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
```

If you delete the restaurant, the SQL query generated looks like this:

```sql
DELETE FROM "core_rating" WHERE "core_rating"."restaurant_id" IN (2);
```

### Example 2: `SET_NULL`
This sets the ForeignKey to `NULL` if the related object is deleted. This is useful if the relationship is optional.

```python
restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='ratings')
```

### Example 3: `PROTECT`
This prevents deletion of a referenced object. If a restaurant is referenced by a rating, attempting to delete the restaurant will raise an exception.

```python
restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT, related_name='ratings')
```

## Performance Considerations

Using Django ORM provides the convenience of abstracting SQL, but be mindful of performance. For example, using `__in` lookups with large datasets may generate inefficient SQL queries. You may need to benchmark your queries, especially with nested queries, to avoid performance bottlenecks.

### Example 1: Avoiding Nested Queries

Instead of running a nested query, you can split it into two queries for performance reasons:

```python
# Inefficient Nested Query
inner_qs = Blog.objects.filter(name__contains="Cheddar").values_list("pk", flat=True)
entries = Entry.objects.filter(blog__in=list(inner_qs))
```

## Conclusion

Django provides a powerful ORM that simplifies database interactions with Pythonic syntax. Understanding how to update, filter, and delete records, and how field lookups work, is essential for working efficiently with Django models. Keep in mind performance considerations and the behavior of `on_delete` for ForeignKey relationships to avoid unintended side effects.

---

**Real-World Example**: Think about a restaurant rating system like **Zomato**. If a restaurant is removed from the platform, all related user ratings and reviews might need to be deleted as well (using `CASCADE`), but if you simply want to **archive** the restaurant, you might use `SET_NULL` for ratings so the history remains, but the restaurant is marked as inactive.

---
### 1. **Counting Objects in the Database**

```python
print(Restaurant.objects.count())
print(Rating.objects.count())
print(Sale.objects.count())
```

**Explanation**: These commands are used to count the number of entries in the `Restaurant`, `Rating`, and `Sale` tables. 
- Imagine you're counting how many restaurants, ratings, or sales records you have in your database, just like counting items in a to-do list.

---

### 2. **Filtering Objects**

```python
Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.CHINESE)
```

**Explanation**: This query will return all restaurants that are of type **Chinese**.
- **Real-world analogy**: Think of filtering your emails by the subject line—here, you're filtering restaurants by their type (e.g., Chinese, Indian, etc.).

```python
restaurant = Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
```

If more than one Italian restaurant exists, you can use `.filter()` which returns multiple objects in a **QuerySet**. To fetch a specific one, use `.get()` (if you expect only one result), but it will throw a `MultipleObjectsReturned` error if there are multiple matches.

---

### 3. **Using `.get()` vs `.filter()`**

- **`.get()`**: Use this when you expect **exactly one result**. If more than one object matches, it raises a `MultipleObjectsReturned` error.
  ```python
  Restaurant.objects.get(name='Pizzeria 1')
  ```
- **`.filter()`**: Use this when you want to get **multiple results**. It returns a **QuerySet**, which is like a list of objects.
  ```python
  Restaurant.objects.filter(restaurant_type=Restaurant.TypeChoices.ITALIAN)
  ```

**Real-world example**: If you search for a specific book by its ISBN (`.get()`), there should be only one match. However, if you search by author (`.filter()`), you may get multiple books.

---

### 4. **Combining Conditions in `.filter()`**

```python
restaurant = Restaurant.objects.filter(restaurant_type=chinese, name__startswith='C')
```

**Explanation**: This query returns all Chinese restaurants whose names start with "C". The `name__startswith` condition checks the beginning of the name, like filtering contacts on your phone by names that start with "C".

---

### 5. **Filtering with `.in()`**

```python
restaurant = Restaurant.objects.filter(restaurant_type__in=(chinese, indian, mexican))
```

**Explanation**: This returns restaurants that are of type **Chinese**, **Indian**, or **Mexican**. The `__in` filter checks if the `restaurant_type` is within the given list of values.
- **Real-world analogy**: You might want to search for movies that are in the **Action**, **Comedy**, or **Drama** genres.

---

### 6. **Excluding Objects with `.exclude()`**

```python
restaurant = Restaurant.objects.exclude(restaurant_type=chinese)
```

**Explanation**: This query excludes Chinese restaurants and returns all other types. It’s like setting a filter to show **everything except** a specific category.
- **Real-world analogy**: Filtering out emails from a certain sender in your inbox, so you only see emails from others.

---

### 7. **Range Lookups**

```python
sale = Sale.objects.filter(income__range=(50, 60))
```

**Explanation**: This query returns sales where the `income` is between 50 and 60. 
- **Real-world analogy**: Filtering items on an e-commerce site by price range (e.g., show me products between $50 and $60).

---

### 8. **Ordering Query Results**

```python
restaurants = Restaurant.objects.order_by('name')
restaurants = Restaurant.objects.order_by('-name') # reverse order
```

**Explanation**: This sorts restaurants by name alphabetically. Adding `-` orders it in reverse.
- **Real-world analogy**: Sorting files on your computer by name in ascending or descending order.

```python
restaurants = Restaurant.objects.order_by('date_opened')
```

This sorts restaurants by their opening date, showing the oldest restaurant first.
- **Real-world analogy**: Sorting your photos by date, showing the oldest ones first.

You can also **slice** the result, like in a list:

```python
restaurants = Restaurant.objects.order_by('date_opened')[:5]
```

This returns only the first 5 restaurants by their opening date.
- **Real-world analogy**: It’s like only looking at the first 5 items in a sorted to-do list.

---

### 9. **Using `.exists()` to Check for Records**

```python
restaurant = Restaurant.objects.filter(name='Pizzeria 1').exists()
```

**Explanation**: This returns `True` if a restaurant with the name "Pizzeria 1" exists, and `False` otherwise.
- **Real-world analogy**: Checking if an item is in stock on an e-commerce site.

---

### 10. **Indexing and Slicing Querysets**

You can access individual restaurants from the ordered result like a list:

```python
restaurants = Restaurant.objects.order_by('date_opened')[1]
```

This retrieves the **second** restaurant by opening date.
- **Real-world analogy**: Accessing the second item on your to-do list.

---

### 11. **Default Ordering in Models**

To ensure results are always ordered in a specific way, you can set a default order in the model itself:

```python
class Restaurant(models.Model):
    class Meta:
        ordering = ['name']  # Sort by name by default
```

Now, anytime you query restaurants, they will automatically be sorted by name unless specified otherwise.

---

### 12. **Fetching the First and Last Items**

```python
Restaurant.objects.first()  # First restaurant by default ordering (primary key)
Restaurant.objects.last()   # Last restaurant by default ordering (primary key)
```

This fetches the **first** and **last** restaurants based on the default ordering (by primary key, unless changed).

---


### 1. **Initial Issue: Too Many Queries**
When displaying restaurants and their ratings:
```python
restaurants = Restaurant.objects.all()
```
This leads to **N+1 queries** since each restaurant triggers a separate query for its ratings. This can cause **15+ queries** for just a few restaurants.

---

### 2. **Optimization: Using `prefetch_related`**
To reduce the number of queries, you can use **`prefetch_related`** for related models like ratings and sales.

#### Example:
```python
def index(request):
    restaurants = Restaurant.objects.prefetch_related('ratings', 'sales')
    context = {'restaurants': restaurants}
    return render(request, 'index.html', context)
```
- **Improvement**: This fetches all related data in a **single query**, reducing the total number of SQL queries.
  
#### SQL Generated:
```sql
SELECT ••• FROM "core_rating" WHERE "core_rating"."restaurant_id" IN (...)
```

![Screenshot 2024-10-07 094702](https://github.com/user-attachments/assets/77df8879-a07a-48ce-a412-c53c408fbd43)

![Screenshot 2024-10-07 094649](https://github.com/user-attachments/assets/d0d25193-a53a-4555-900a-16d7da11a998)

---

### 3. **Using `select_related` for Foreign Keys**
If you are querying **foreign keys**, use `select_related` to fetch related objects in one go.

#### Example:
```python
def index(request):
    ratings = Rating.objects.select_related('restaurant')
    context = {'ratings': ratings}
    return render(request, 'index.html', context)
```
- **Before**: 31 queries
- **After**: **1 query**

#### SQL Generated:
```sql
SELECT "core_rating"."id", "core_restaurant"."name", ... 
FROM "core_rating" 
INNER JOIN "core_restaurant" ON "core_rating"."restaurant_id" = "core_restaurant"."id"
```

---

### 4. **Fetching Only Required Columns with `.only()`**
Fetching only the necessary columns reduces the data load.

#### Example:
```python
ratings = Rating.objects.only('restaurant__name', 'rating').select_related('restaurant')
```
- **Improvement**: Limits fetched data to just the `restaurant.name` and `rating` fields, optimizing bandwidth and query execution time.

---

### 5. **Combining with `annotate` for Aggregation**
You can annotate your query with aggregated fields, like summing up the sales.

#### Example:
```python
restaurants = Restaurant.objects.prefetch_related('ratings', 'sales') \
    .filter(ratings__rating=5) \
    .annotate(total=Sum('sales__income'))
```
- **Improvement**: Fetches restaurants with 5-star ratings and calculates the total sales.

---

### 6. **Advanced `prefetch_related` with Custom Querysets**
You can customize `prefetch_related` to filter related objects like monthly sales.

#### Example:
```python
month_ago = timezone.now() - timezone.timedelta(days=30)
monthly_sales = Prefetch('sales', queryset=Sale.objects.filter(datetime__gte=month_ago))

restaurants = Restaurant.objects.prefetch_related('ratings', monthly_sales) \
    .filter(ratings__rating=5) \
    .annotate(total=Sum('sales__income'))
```
- **Improvement**: Prefetches only the sales from the last 30 days, further optimizing your queries.

#### SQL Generated:
```sql
SELECT "core_restaurant"."id", "core_restaurant"."name", ...
FROM "core_restaurant"
INNER JOIN "core_rating" ON ...
WHERE "core_rating"."rating" = 5
```

### Conclusion:
By using `select_related` and `prefetch_related`, and optimizing queries with `only()`, you significantly reduce the number of database queries and the load on your database.


### Many-to-Many Relationships in Django

In Django, **many-to-many (M2M)** relationships allow a model to be related to multiple records of another model and vice versa. It's useful when you need multiple records from two models to be associated with each other.

#### Example Models:
Let's explore M2M relationships using an example of **Publications** and **Articles**, and then customize it with **Staff** and **Restaurant** relationships.

```python
from django.db import models

# Publications and Articles Example
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
```

#### Add M2M Field for Restaurants and Staff:

Now, let's add a **Staff** model that has a many-to-many relationship with the **Restaurant** model. We will also add an intermediate model (`StaffRestaurant`) to store additional data, such as the **salary** of staff at each restaurant.

```python
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    restaurant_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=120)
    restaurants = models.ManyToManyField(Restaurant, through='StaffRestaurant')

    def __str__(self):
        return self.name


class StaffRestaurant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)

    def __str__(self):
        return f"{self.staff.name} works at {self.restaurant.name} earning {self.salary}"
```

In this case, we’ve added an intermediate model `StaffRestaurant` to store **extra fields** like `salary`. The `through` keyword specifies that we are using this intermediate model for the relationship.

---

### Querying Many-to-Many Relationships

Here’s how you can create, query, and manipulate many-to-many relationships.

#### Create Staff and Associate with Restaurants:

```python
# Creating a new staff
staff, created = Staff.objects.get_or_create(name="John Wick")

# Associating staff with restaurants
restaurant = Restaurant.objects.first()  # Get the first restaurant
staff.restaurants.add(restaurant)  # Add the relationship

# Checking the associated restaurants
print(staff.restaurants.all())  # QuerySet of all restaurants associated with this staff
```

#### Remove and Set Relationships:

- **Remove** a restaurant from staff:
    ```python
    staff.restaurants.remove(Restaurant.objects.first())
    print(staff.restaurants.count())  # Count remaining restaurants
    ```

- **Set** new restaurants (overwrite existing relationships):
    ```python
    staff.restaurants.set(Restaurant.objects.all()[:5])  # Set first 5 restaurants
    ```

- **Clear** all relationships:
    ```python
    staff.restaurants.clear()  # Remove all associated restaurants
    ```

#### Add Through Model (with Extra Field):

You can associate restaurants and staff while specifying additional fields (e.g., salary):

```python
restaurant = Restaurant.objects.get(pk=1)
StaffRestaurant.objects.create(staff=staff, restaurant=restaurant, salary=28000)

restaurant2 = Restaurant.objects.get(pk=2)
StaffRestaurant.objects.create(staff=staff, restaurant=restaurant2, salary=24000)

# Retrieve and print salary for each restaurant-staff association
staff_restaurants = StaffRestaurant.objects.filter(staff=staff)
for s in staff_restaurants:
    print(s.salary)  # Prints the salary for each restaurant-staff association
```

#### Prefetching Many-to-Many Fields for Optimization

To improve performance when querying many-to-many relationships, **`prefetch_related()`** can be used to reduce the number of SQL queries executed.

```python
def index(request):
    # Prefetch restaurants and staff using the StaffRestaurant model
    jobs = StaffRestaurant.objects.prefetch_related('restaurant', 'staff')
    
    for job in jobs:
        print(f"{job.staff.name} works at {job.restaurant.name} with salary {job.salary}")
    
    return render(request, 'index.html')
```

### Real-World Example:
Consider a system where staff works at multiple restaurants, and each staff member earns different salaries at different restaurants. This setup models a common scenario in hospitality management where staff rotate between restaurants, and their salary varies.

### Output Example:
```python
# Example Output:
John Wick works at Restaurant A earning 28000
John Wick works at Restaurant B earning 24000
```

By **prefetching** related fields and using intermediate models to store extra information (like salary), you ensure efficient querying even with large datasets.

---

### Summary of Key Methods in M2M Relationships:

- **add**: Adds an object to the many-to-many relationship.
- **remove**: Removes an object from the relationship.
- **clear**: Removes all relationships.
- **set**: Replaces the current relationships with a new set of objects.
- **all**: Retrieves all related objects.




## **Aggregation Over QuerySets (Min, Max, Sum, Count, Avg)**

**Aggregation** is used to compute values (like `sum`, `average`, `min`, `max`, etc.) over a set of rows in the database. The result is a **single value** for the entire queryset.

### **Example: Counting the Number of Restaurants**
```python
from django.db.models import Count

restaurants = Restaurant.objects.aggregate(total=Count('id'))
print(restaurants)
```
**Output:**
```python
{'total': 14}
```
**SQL Query:**
```sql
SELECT COUNT("core_restaurant"."id") AS "total" FROM "core_restaurant";
```

---

### **Example: Calculating the Average Rating of a Restaurant**
```python
from django.db.models import Avg

average_rating = Rating.objects.aggregate(avg_rating=Avg('rating'))
print(average_rating)
```
**Output:**
```python
{'avg_rating': 2.36}
```
**SQL Query:**
```sql
SELECT AVG("core_rating"."rating") AS "avg_rating" FROM "core_rating";
```

---

### **Real-World Scenario: Aggregating Sales Data**
Imagine a sales reporting tool that needs to display the **total sales**, **minimum income**, **maximum income**, and the **average income** of restaurants in the last month.

```python
from django.db.models import Sum, Min, Max, Avg
from django.utils import timezone

one_month_ago = timezone.now() - timezone.timedelta(days=30)
sales = Sale.objects.filter(date__gte=one_month_ago)

report = sales.aggregate(
    total_sales=Sum('income'),
    min_income=Min('income'),
    max_income=Max('income'),
    avg_income=Avg('income')
)

print(report)
```
**Output:**
```python
{'total_sales': 5743.40, 'min_income': Decimal('6.25'), 'max_income': Decimal('99.22'), 'avg_income': Decimal('57.43')}
```
**SQL Query:**
```sql
SELECT SUM("core_sale"."income") AS "total_sales", MIN("core_sale"."income") AS "min_income", 
MAX("core_sale"."income") AS "max_income", AVG("core_sale"."income") AS "avg_income" 
FROM "core_sale" WHERE "core_sale"."date" >= '2024-09-05';
```

---

## **Annotating Querysets**

**Annotations** allow you to add **calculated fields** to each row of the queryset. Instead of a single value for the entire queryset (like aggregation), each object in the queryset gets the annotated value.

### **Example: Adding the Length of a Restaurant’s Name**
```python
from django.db.models.functions import Length

restaurants = Restaurant.objects.annotate(len_name=Length('name'))
print(restaurants.values('name', 'len_name'))
```
**Output:**
```python
<QuerySet [{'name': 'Bombay Bustle', 'len_name': 13}, {'name': 'Chinese 2', 'len_name': 9}, ...]>
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name", LENGTH("core_restaurant"."name") AS "len_name" 
FROM "core_restaurant";
```

---

### **Example: Annotating Total Sales for Each Restaurant**
```python
from django.db.models import Sum

restaurants = Restaurant.objects.annotate(total_sales=Sum('sales__income'))
for r in restaurants:
    print(r.name, r.total_sales)
```
**Output:**
```python
Bombay Bustle 3000.0
Chinese 2 2000.0
...
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name", SUM("core_sale"."income") AS "total_sales" 
FROM "core_restaurant" LEFT OUTER JOIN "core_sale" ON ("core_restaurant"."id" = "core_sale"."restaurant_id") 
GROUP BY "core_restaurant"."name";
```

---

### **Real-World Scenario: Annotating the Number of Reviews per Restaurant**
You’re building a restaurant review app and need to show the **number of reviews** and the **average rating** for each restaurant.

```python
from django.db.models import Count, Avg

restaurants = Restaurant.objects.annotate(
    num_reviews=Count('ratings'),
    avg_rating=Avg('ratings__rating')
)

for r in restaurants:
    print(f'{r.name}: {r.num_reviews} reviews, {r.avg_rating} avg rating')
```
**Output:**
```python
Pizzeria 1: 2 reviews, 2.5 avg rating
Pizzeria 2: 4 reviews, 2.5 avg rating
...
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name", COUNT("core_rating"."id") AS "num_reviews", 
AVG("core_rating"."rating") AS "avg_rating" 
FROM "core_restaurant" 
LEFT OUTER JOIN "core_rating" ON ("core_restaurant"."id" = "core_rating"."restaurant_id") 
GROUP BY "core_restaurant"."name";
```

---

## **Using `values()` and `values_list()`**

- **`values()`** returns a **dictionary** for each object in the queryset.
- **`values_list()`** returns a **tuple** for each object in the queryset.

### **Example: Using `values()`**
```python
restaurants = Restaurant.objects.values('name', 'date_opened')
print(restaurants)
```
**Output:**
```python
<QuerySet [{'name': 'Bombay Bustle', 'date_opened': datetime.date(2024, 8, 24)}, {'name': 'Chinese 2', 'date_opened': datetime.date(2024, 9, 6)}]>
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name", "core_restaurant"."date_opened" 
FROM "core_restaurant";
```

---

### **Example: Using `values_list()`**
```python
restaurants = Restaurant.objects.values_list('name', flat=True)
print(restaurants)
```
**Output:**
```python
<QuerySet ['Bombay Bustle', 'Chinese 2', 'Golden Dragon', ...]>
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name" FROM "core_restaurant";
```

---

## **Transforming Values with `Upper()` and `Concat()`**

### **Example: Uppercasing Restaurant Names**
```python
from django.db.models.functions import Upper

restaurants = Restaurant.objects.values(name_upper=Upper('name'))
print(restaurants)
```
**Output:**
```python
<QuerySet [{'name_upper': 'BOMBAY BUSTLE'}, {'name_upper': 'CHINESE 2'}, ...]>
```
**SQL Query:**
```sql
SELECT UPPER("core_restaurant"."name") AS "name_upper" FROM "core_restaurant";
```

---

### **Example: Concatenating Fields with `Concat()`**
```python
from django.db.models import Value, CharField
from django.db.models.functions import Concat

restaurants = Restaurant.objects.annotate(
    message=Concat('name', Value(' [Rating: '), Avg('ratings__rating'), Value(']'), output_field=CharField())
)

for r in restaurants:
    print(r.message)
```
**Output:**
```python
Bombay Bustle [Rating: 2.0]
Chinese 2 [Rating: 2.5]
...
```
**SQL Query:**
```sql
SELECT "core_restaurant"."name" || ' [Rating: ' || AVG("core_rating"."rating") || ']' AS "message" 
FROM "core_restaurant" LEFT OUTER JOIN "core_rating" ON ("core_restaurant"."id" = "core_rating"."restaurant_id") 
GROUP BY "core_restaurant"."name";
```

---

### Understanding `F` Expressions and `Q` Objects in Django ORM

`F()` expressions and `Q()` objects are powerful tools in Django that help perform complex database operations directly at the SQL level without loading data into Python memory. These help improve performance by reducing the number of database queries and eliminating the need to pull data into memory for calculations or comparisons.

---

#### **F Expressions**

`F()` expressions represent the value of a model field or an annotated column in the database. They allow you to reference a field's value directly in SQL, enabling operations such as incrementing or updating field values without loading them into memory.

#### Example: Incrementing a Field

##### **Without F Expressions:**

```python
reporter = Reporters.objects.get(name='Tintin')
reporter.stories_field += 1
reporter.save()
```

- **SQL Equivalent**: 
    ```sql
    SELECT "stories_field" FROM "reporters" WHERE "name" = 'Tintin';
    UPDATE "reporters" SET "stories_field" = stories_field + 1 WHERE "name" = 'Tintin';
    ```
- This pulls the field from the database, modifies it in Python, and then updates it.

##### **With F Expressions:**

```python
from django.db.models import F
reporter = Reporters.objects.get(name="Tintin")
reporter.stories_field = F("stories_field") + 1
reporter.save()
```

- **SQL Equivalent**: 
    ```sql
    UPDATE "reporters" SET "stories_field" = "stories_field" + 1 WHERE "name" = 'Tintin';
    ```

This is more efficient as it performs the update directly at the database level without loading the value into memory.

---

### **Performance Improvement for Bulk Updates**

You can use `F()` expressions to perform operations on multiple rows efficiently, such as updating every row in the table:

```python
Rating.objects.update(rating=F('rating') * 2)
```

- **SQL Equivalent**:
    ```sql
    UPDATE "core_rating" SET "rating" = ("core_rating"."rating" * 2);
    ```

This will double the `rating` field for all records in the `Rating` table.

---

#### **Using F Expressions for Calculations and Annotations**

You can perform calculations directly at the database level using `F()` expressions.

##### **Example: Annotating Profit**

```python
from django.db.models import F

sales = Sale.objects.annotate(
    profit=F('income') - F('expenditure')
)

for sale in sales:
    print(sale.profit)
```

- **SQL Equivalent**:
    ```sql
    SELECT "income" - "expenditure" AS "profit" FROM "core_sale";
    ```

This calculates the `profit` for each sale directly in the SQL query, improving performance.

---

### **Q Objects for Complex Queries**

`Q()` objects allow you to build complex SQL queries involving `AND`, `OR`, and `NOT` conditions. 

#### **Simple Example: Filtering with OR**

Suppose you want to find restaurants that are either Italian or Mexican:

##### **Without Q Objects (Error)**

```python
Restaurant.objects.filter(restaurant_type=IT, restaurant_type=MEX)
```
- This query will raise an error because you can't have the same field in two conditions simultaneously.

##### **With Q Objects:**

```python
from django.db.models import Q

Restaurant.objects.filter(
    Q(restaurant_type=IT) | Q(restaurant_type=MEX)
)
```

- **SQL Equivalent**:
    ```sql
    SELECT * FROM "core_restaurant" WHERE "restaurant_type" = 'IT' OR "restaurant_type" = 'MEX';
    ```

This returns restaurants that are either Italian or Mexican.

---

#### **Using Q Objects with F Expressions:**

You can also combine `Q()` objects with `F()` expressions for complex queries.

##### **Example: Sales Where Profit > Expenditure OR Restaurant Name Has a Number**

```python
from django.db.models import Q

name_has_num = Q(restaurant__name__regex=r"[0-9]+")
profited = Q(income__gt=F('expenditure'))

sales = Sale.objects.filter(name_has_num | profited)
```

- **SQL Equivalent**:
    ```sql
    SELECT * FROM "core_sale" 
    WHERE "income" > "expenditure" 
    OR "restaurant"."name" ~ '[0-9]+';
    ```

This will return all sales where the restaurant name contains a number or the sale has made a profit.

---

#### **Negation with Q Objects (~Q)**

You can negate conditions using `~Q()`, which translates to `NOT` in SQL.

##### **Example: Excluding Restaurants of a Specific Type**

```python
# Find restaurants that are not Mexican
restaurants = Restaurant.objects.filter(~Q(restaurant_type=MEX))
```

- **SQL Equivalent**:
    ```sql
    SELECT * FROM "core_restaurant" WHERE NOT "restaurant_type" = 'MEX';
    ```

---

### **Complex Q Example: Filtering Multiple Conditions**

You can use multiple `Q()` objects and group them with parentheses for more complex queries.

##### **Example: Find Recently Opened Restaurants or Italian/Mexican Restaurants**

```python
it_or_mex = Q(name__icontains="italian") | Q(name__icontains="mexican")
recently_opened = Q(date_opened__gt=timezone.now() - timezone.timedelta(days=40))

restaurants = Restaurant.objects.filter(it_or_mex | recently_opened)
```

- **SQL Equivalent**:
    ```sql
    SELECT * FROM "core_restaurant" 
    WHERE "name" LIKE '%italian%' 
    OR "name" LIKE '%mexican%' 
    OR "date_opened" > '2024-08-30';
    ```

This query returns restaurants that are Italian, Mexican, or have opened in the last 40 days.

---

### **Summary**

- **`F()` Expressions**: Used to refer to and manipulate model fields at the SQL level.
- **`Q()` Objects**: Used to build complex queries with `AND`, `OR`, and `NOT` conditions.
- Combining `F()` and `Q()` objects can help optimize performance and create powerful queries without pulling data into Python memory.

These techniques can improve the efficiency of your Django queries, especially when dealing with large datasets or complex conditions!