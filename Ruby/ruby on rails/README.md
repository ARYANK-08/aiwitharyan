# Rails and the MVC Architecture

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


