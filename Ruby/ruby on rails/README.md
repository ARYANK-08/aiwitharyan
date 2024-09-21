# Rails and the MVC Architecture

![image](https://github.com/user-attachments/assets/5d9cd810-09c2-4ec2-ad55-db33bda0423e)

Ruby on Rails (Rails) is a web application framework that follows the Model-View-Controller (MVC) architecture. This design pattern separates an application into three interconnected components:

- **Model**: Manages the database and business logic. In Rails, this often involves interacting with databases like MySQL.
- **View**: Handles the presentation layer, i.e., the web pages that users interact with.
- **Controller**: Acts as the intermediary between the Model and the View, processing requests and directing responses.

In Django, a similar pattern is used where `views.py` handles controller-like logic.

## Directory Structure Overview

Here's a brief overview of some key directories and files in a Rails application:

- **`app/assets`**: Contains CSS files, JavaScript files, and images.
- **`app/channels`**: Manages WebSocket channels (if used).
- **`app/controllers`**: Holds the controller files.
- **`app/models`**: Contains model files that interact with the database.
- **`app/views`**: Stores view files (e.g., HTML templates).
- **`config`**: Configuration files for routes, initializers, and other settings.

## Route Configuration

In Rails, routing is configured in `config/routes.rb`. This file defines URL patterns and maps them to controllers and actions.

## Generating Your First Webpage

To create a new controller and view, you can use Rails generators. Here’s how you can create a simple webpage:

1. **Generate a Controller**:
   ```bash
   rails g controller home index
   ```
   This command creates:
   - `app/controllers/home_controller.rb`
   - `app/views/home/index.html.erb`
   - A route for `home#index`
   - A test file `test/controllers/home_controller_test.rb`
   - A helper file `app/helpers/home_helper.rb`

2. **Start the Rails Server**:
   ```bash
   rails s
   ```

3. **Set the Root Route**:
   Add this line to `config/routes.rb`:
   ```ruby
   root "home#index"
   ```

4. **Check Routes**:
   Run:
   ```bash
   rails routes
   ```
   You will see routes like:
   ```
   Prefix   Verb   URI Pattern             Controller#Action
   home_index GET   /home/index(.:format)   home#index
   root        GET   /                        home#index
   ```

## Adding New Pages

To add an "About Us" page:

1. **Create a New Action**:
   In `app/controllers/home_controller.rb`:
   ```ruby
   def about
   end
   ```

2. **Create the View**:
   Add `app/views/home/about.html.erb` and include your content.

3. **Update Routes**:
   Add to `config/routes.rb`:
   ```ruby
   get "home/about"
   ```

4. **Link to the About Page**:
   In your layout file `app/views/layouts/application.html.erb`:
   ```erb
   <%= link_to "About Us", home_about_path, class: "nav-link" %>
   ```

## Rails and CRUD Operations

Rails makes CRUD (Create, Read, Update, Delete) operations incredibly simple with scaffolding:

1. **Generate a Scaffold**:
   ```bash
   rails g scaffold Friend first_name:string last_name:string email:string phone:string twitter:string
   ```

2. **Migration File**:
   This creates a migration file like `db/migrate/20240913155443_create_friends.rb`:
   ```ruby
   class CreateFriends < ActiveRecord::Migration[7.2]
     def change
       create_table :friends do |t|
         t.string :first_name
         t.string :last_name
         t.string :email
         t.string :phone
         t.string :twitter

         t.timestamps
       end
     end
   end
   ```

3. **Migrate the Database**:
   ```bash
   rails db:migrate
   ```

4. **Access the Scaffolded Resources**:
   Navigate to `/friends` and see the automatically generated CRUD interface.


> [!NOTE] 
> **As I went to `/friends`, I was amazed. I felt the beauty of Rails for the first time. Coming from a Django background, I needed to write HTML, POST methods, and form requests even for a simple CRUD. But here, I just gave a command, and it automatically generated HTML, with data easily being stored in the database. It was a revelation! What the actual FFFF!!! ????**

> [!TIP] 
> **Coming from Django and learning Rails is like transitioning from driving a manual car to driving an automatic car. 😄**

> [!QUESTION] 
> **How did URLs or routes get configured automatically? With `resources :friends`, you get everything you need: add, delete, update, and more.**


## Forms and Error Handling

The scaffold generates form views like this for creating or editing records:

> [!TIP] 
> **In Django, you would write separate `urls.py` files for update, views, and delete operations, but in Rails, everything is bundled under `resources`.**

> [!NOTE] 
> **Now I feel dumb! Am I so noob?**


```erb
<%= form_with(model: friend) do |form| %>
  <% if friend.errors.any? %>
    <div style="color: red">
      <h2><%= pluralize(friend.errors.count, "error") %> prohibited this friend from being saved:</h2>
      <ul>
        <% friend.errors.each do |error| %>
          <li><%= error.full_message %></li>
        <% end %>
      </ul>
    </div>
  <% end %>

  <div>
    <%= form.label :first_name, style: "display: block" %>
    <%= form.text_field :first_name %>
  </div>

  <div>
    <%= form.label :last_name, style: "display: block" %>
    <%= form.text_field :last_name %>
  </div>

  <div>
    <%= form.label :email, style: "display: block" %>
    <%= form.text_field :email %>
  </div>

  <div>
    <%= form.label :phone, style: "display: block" %>
    <%= form.text_field :phone %>
  </div>

  <div>
    <%= form.label :twitter, style: "display: block" %>
    <%= form.text_field :twitter %>
  </div>

  <div>
    <%= form.submit %>
  </div>
<% end %>
```

> [!TIP] 
> **Normally, creating a CRUD application like this without GPT would take 1 week.**  
> **With GPT, it might still take a week.**  
> **With Ruby on Rails, it takes just 1 second! :p**
>  **Boom—CRUD is done!**  
> **95% of software is CRUD, and Rails makes setting up and writing all these CRUD operations incredibly fast and easy. Even Django isn’t as quick in automating CRUD operations.**

Rails simplifies many aspects of web development, from generating code to managing routes and creating CRUD operations. If you're familiar with Django, you'll find Rails' conventions and scaffolding incredibly efficient. Rails offers a streamlined approach, reducing the amount of boilerplate code and configuration required, which can make web development feel faster and more intuitive.

# Day 2 started with an error

I wasn't able to solve the gem file errors. I guess `rails s` was not running.

### The psych gem (v5.1.2) failed to install during `bundle install`.
- The error is due to failing to build native extensions, specifically missing `yaml.h`.
- This is likely caused by missing YAML development libraries on your Windows system.
- The failed installation of psych is blocking other dependent gems from installing.

---

### Sign In, Sign Up, Generate a Password, Forget Password
It's insanely easy using Ruby on Rails to do all this!  
In Django, we `pip install` something, and in Rails, we `gem install devise`.  
Devise handles all of the user management.

---

### rubygems.org -> hub

Now I'm recalling my memories with Flutter,  
where in `pubspec.yaml`, we add dependencies of a library.  
In the same way, we have the `Gemfile`:

```ruby
gem 'devise', '~> 4.9', '>= 4.9.4'
```

---

### Setup Devise

```bash
$ rails generate devise:install
```

- Creates `config/initializers/devise.rb`
- Creates `config/locales/devise.en.yml`

---

### Manual Setup (if required)

Depending on your application's configuration, some manual setup may be required:

1. Ensure you have defined default URL options in your environments files.  
   Example for development environment (`config/environments/development.rb`):

   ```ruby
   config.action_mailer.default_url_options = { host: 'localhost', port: 3000 }
   ```

   In production, `:host` should be set to the actual host of your application.

   *Required for all applications.*

2. Ensure you have defined `root_url` in your `config/routes.rb`.  
   Example:

   ```ruby
   root to: "home#index"
   ```

   *Not required for API-only applications.*

3. Ensure you have flash messages in `app/views/layouts/application.html.erb`.  
   Example:

   ```erb
   <p class="notice"><%= notice %></p>
   <p class="alert"><%= alert %></p>
   ```

   *Not required for API-only applications.*

4. You can copy Devise views (for customization) to your app by running:

   ```bash
   rails g devise:views
   ```

   *Not required.*

---

### Custom Pages for Sign-Up and Forgot Password
All the different pages can be created via:

```bash
rails g devise:views
```

All the views are created, just like friends.

---

I literally hardcoded the "Forget Password" mail sending link in Django a year ago.  
It feels magical how all these things are set up using one library like Devise.  
It's like building a whole CRUD just by installing libraries and tweaking here and there.

---

### User Table:

```bash
rails generate devise user
rails db:migrate
```

---

### `user_signed_in?` Check

Remember:

```erb
{% if user_loggedin or authenticated %}
```

in Django?  
We used to show different navbars if logged in or logged out.

---

### Routes

To check routes in Rails:

```bash
rails routes
```

Example output:

```bash
Prefix Verb   URI Pattern                         Controller#Action
new_user_session GET    /users/sign_in(.:format)     devise/sessions#new
user_session POST   /users/sign_in(.:format)     devise/sessions#create
destroy_user_session DELETE /users/sign_out(.:format) devise/sessions#destroy
new_user_password GET    /users/password/new(.:format) devise/passwords#new
edit_user_password GET    /users/password/edit(.:format) devise/passwords#edit
user_password PATCH
```


## Why Associations?
[Link](https://guides.rubyonrails.org/association_basics.html)

In Rails, an **association** is a connection between two Active Record models. Why do we need associations between models? Because they make common operations simpler and easier in your code.

For example, consider a simple Rails application that includes a model for authors and a model for books. Each author can have many books.

Without associations, the model declarations would look like this:

```ruby
class Author < ApplicationRecord
end

class Book < ApplicationRecord
end
```

Now, suppose we wanted to add a new book for an existing author. We'd need to do something like this:

```ruby
@book = Book.create(published_at: Time.now, author_id: @author.id)
```

Or consider deleting an author, and ensuring that all of its books get deleted as well:

```ruby
@books = Book.where(author_id: @author.id)
@books.each do |book|
  book.destroy
end
@author.destroy
```

With Active Record associations, we can streamline these—and other—operations by **declaratively** telling Rails that there is a connection between the two models. Here's the revised code for setting up authors and books:

```ruby
class Author < ApplicationRecord
  has_many :books, dependent: :destroy
end

class Book < ApplicationRecord
  belongs_to :author
end
```

With this change, creating a new book for a particular author is easier:

```ruby
@book = @author.books.create(published_at: Time.now)
```

Deleting an author and all of its books is much easier:

```ruby
@author.destroy
```

To learn more about the different types of associations, read the next section of this guide. That's followed by some tips and tricks for working with associations, and then by a complete reference to the methods and options for associations in Rails.

---


## The Types of Associations

Rails supports **six types of associations**, each with a particular use-case in mind.

Here is a list of all the supported types with a link to their API docs for more detailed information on how to use them, their method parameters, etc.

- `belongs_to`
- `has_one`
- `has_many`
- `has_many :through`
- `has_one :through`
- `has_and_belongs_to_many`

Associations are implemented using **macro-style calls**, so that you can declaratively add features to your models. For example, by declaring that one model `belongs_to` another, you instruct Rails to maintain **Primary Key-Foreign Key** information between instances of the two models, and you also get a number of utility methods added to your model.

---

```ruby
class Friend < ApplicationRecord
  belongs_to :user
end
```

```ruby
class User < ApplicationRecord
  has_many :friends
end
```

---

### Adding `user_id` to friends table in `schema.rb`

To add `user_id` to the friends table, run the following migration:

```bash
rails g migration add_user_id_to_friends user_id:integer:index
```

The `index` speeds up the searching process.

Then, run:

```bash
rails db:migrate
```

This will add the following line to your schema:

```ruby
t.integer "user_id"
t.index ["user_id"], name: "index_friends_on_user_id"
```

---

Afterward, delete all friends because they haven't been tagged to the `user_id`. You can inspect the current user with:

```erb
<%= current_user.inspect %>
<%= current_user.id %>
```

To ensure the `user_id` gets passed when creating a friend, use a hidden form field:

```erb
<div class="form-group">
  <%= form.number_field :user_id, id: :friend_user_id, class: "form-control", value: current_user.id, type: :hidden %>
</div>
```

---

### Error: **"User must exist"**

If you're getting this error, it means that the `user_id` is not being passed properly, which is causing the failure.

Make sure the `friend_params` method includes `user_id` in the permitted parameters, like this:

```ruby
def friend_params
  params.require(:friend).permit(:first_name, :last_name, :email, :phone, :twitter, :user_id)
end
```

---

### Issue: **Friends of Other Users Being Displayed**

If when creating a new account and going to the friends page, friends created by other users are still being displayed, you need to ensure that you **only show friends that belong to the current user**. You can filter friends by `current_user` like this:

```ruby
@friends = current_user.friends
```

This will ensure that the friends displayed are the ones associated with the logged-in user's ID only.

```ruby
# Ensures user is authenticated before taking actions, except for viewing (index, show)
before_action :authenticate_user!, except: [:index, :show]

# Only show the edit button if the friend belongs to the current user
<% if friend.user == current_user %>

# Ensures only the correct user can edit, update, or destroy a friend
def correct_user
  @friend = current_user.friends.find_by(id: params[:id])
  redirect_to friends_path, notice: "Not Authorized" if @friend.nil?
end

before_action :correct_user, only: [:edit, :update, :destroy]

# Initialize a new friend associated with the current user
def new
  @friend = current_user.friends.build
end

# Create a friend record linked to the current user
def create
  @friend = current_user.friends.build(friend_params)
end
```

### Explanation:
1. **`before_action :authenticate_user!`**: Ensures that users must be logged in to take most actions, except viewing friends.
2. **Edit Button Condition**: Only allows the edit button to show if the friend belongs to the current user.
3. **`correct_user` method**: Verifies the friend belongs to the current user, redirecting if not authorized.
4. **`new` and `create` methods**: Associates new friend records with the current user.

# 🌐 Deploying Ruby on Rails on Heroku

Follow these steps to deploy your Rails app on Heroku:

### 1. 📥 Install Heroku CLI

- [Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Verify installation:

  ```bash
  heroku --version
  ```

### 2. 🔑 Login to Heroku

Login to your Heroku account:

```bash
heroku login
```

### 3. 🛠️ Create a Heroku App

Create a Heroku app:

```bash
heroku create
```

Rename your app:

```bash
heroku rename rails_friends
```

### 4. 🔑 Add SSH Keys

Add your SSH key to Heroku:

```bash
heroku keys:add
```

### 5. 🛠️ Update Gemfile

In `Gemfile`, replace `sqlite3` with `pg` for production:

```ruby
group :production do
  gem 'pg'
end
```

### 6. 💎 Install Dependencies

Run `bundle install`:

```bash
bundle install
```

### 7. 🚀 Push to GitHub

Commit your changes and push to GitHub:

```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push origin main
```

### 8. 🚢 Deploy to Heroku

Push your app to Heroku:

```bash
git push heroku main
```

### 9. 🛠️ Run Migrations

Run database migrations on Heroku:

```bash
heroku run rails db:migrate
```

### 10. 🌍 Open Your App

Launch your app:

```bash
heroku open
```


