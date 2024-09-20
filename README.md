# Car Auto Shop

This is a command-line interface (CLI) application for a car shop that manages products, users, and purchases. The application allows users to perform CRUD operations on products and users, as well as track purchases made by users.

## Features

- **Manage Products**: Create, delete, view all products, and find products by ID.
- **Manage Users**: Create, delete, view all users, and find users by ID.
- **Manage Purchases**: Create, delete, view all purchases, and find purchases by ID.

## Data Model

The application includes the following tables:

### 1. Products

- **Table Name**: `products`
- **Columns**:
  - `id`: Integer, primary key, auto-incremented identifier for each product.
  - `product_name`: String, the name of the product (e.g., "Brake Pad").
  - `type`: String, the type/category of the product (e.g., "Brakes", "Engine Parts").
  - `price`: Float, the price of the product.

### 2. Users

- **Table Name**: `users`
- **Columns**:
  - `id`: Integer, primary key, auto-incremented identifier for each user.
  - `name`: String, the name of the user (e.g., "John Doe").
  - `contact`: String, the contact information of the user (e.g., phone number or email).

### 3. Purchased

- **Table Name**: `purchased`
- **Columns**:
  - `id`: Integer, primary key, auto-incremented identifier for each purchase.
  - `user_id`: Integer, foreign key referencing `users.id`, identifying the user who made the purchase.
  - `product_name`: String, the name of the purchased product.
  - `price`: Float, the price of the product at the time of purchase.
  - `quantity`: Integer, the quantity of the product purchased.
  - `total_cost`: Float, the total cost of the purchase (calculated as `price * quantity`).

## Requirements

You need to implement a Python CLI Application that meets the following requirements:

- Python 3.8+
- Pipenv

### ORM Requirements

- The application must include a database created and modified with Python ORM methods that you write.

  - The data model must include **at least 2** model classes.
  - The data model must include **at least 1** one-to-many relationships.
  - Property methods should be defined to add appropriate constraints to each model class.
  - Each model class should include ORM methods (create, delete, get all, and find by id at minimum).

### CLI Requirements

- The CLI must display menus with which a user may interact.
- The CLI should use loops as needed to keep the user in the application until they choose to exit.
- For **EACH** class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
- The **CLI** should validate user input and object creations/deletions, providing informative errors to the user.
- The project code should follow OOP best practices.
- Pipfile contains all needed dependencies and no unneeded dependencies.
- Imports are used in files only where necessary.
- Project folders, files, and modules should be organized and follow appropriate naming conventions.
- The project should include a `README.md` that describes the application.

You do **not** need to implement tests for `pytest`, although you should test your code thoroughly using your CLI. Try entering bad data when prompted for input, and confirm your application prints a useful error message.

## Installation

Clone the repository:

    `git clone git@github.com:ohnoitsmoraa/Car_Autospare.git`

Open the directory:

    `cd [Folder Name]`

To view the folder in your editor of choice:

    `code .`

To run the path / review functions passed, you use:

    `python [folder/file]`

To install the virtual environment:

    `pipenv install(To install dependencies needed for running of the app)

    then

    pipenv shell(To start working in the virtual environment created)`

### _Authors_

This work was implemented to by:

- Maureen Nyanamba (`https://github.com/ohnoitsmoraa`)

- Titus Ouko(`https://github.com/costamay`)
