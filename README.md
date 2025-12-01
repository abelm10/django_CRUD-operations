# Django CRUD Application – Testproject

This project is a basic Django CRUD (Create, Read, Update, Delete) application built inside a Django project named **testproject**, with an app called **crudoperations**.  
It demonstrates how models, forms, views, templates, and URL configurations work together to create a functional CRUD system.

---

## Project Structure

### **Project:** `testproject`  
### **Application:** `crudoperations`

---

## 1. Project Configuration

### **`testproject/settings.py`**

- The `crudoperations` app is added to the `INSTALLED_APPS` list.
- This allows Django to detect the app and include its models, views, and templates.

### **`testproject/urls.py`**

- The admin route is enabled.
- The project includes the URL configuration from the `crudoperations` app.
- This makes the app accessible from the project’s root URL.

---

## 2. Application Components

### **`crudoperations/models.py`**

- Contains a model named **Person** with fields:
  - `name` (text)
  - `age` (integer)
  - `qualified` (boolean)
- Each field becomes a column in the database.
- The `__str__` method is defined so Django displays readable text in admin, shell, and UI elements.

---

### **`crudoperations/urls.py`**

Defines all routes for the CRUD operations:

- `''` → list all persons  
- `'add/'` → create a new person  
- `'edit/<int:pk>/'` → update a person  
- `'delete/<int:pk>/'` → delete a person  

Dynamic values like `<int:pk>` capture the model’s primary key.

---

### **`crudoperations/forms.py`**

- Uses Django’s `ModelForm` to generate a form directly from the `Person` model.
- Only selected fields (`name`, `age`, `qualified`) are included.
- Handles form validation and POST submission automatically.

---

## 3. Views (CRUD Operations)

### **`crudoperations/views.py`**

Handles the main application logic:

#### **Create**
- Accepts POST data.
- Validates using `PersonForm`.
- Saves the record to the database.
- Redirects back to the list page.

#### **Read (List)**
- Fetches all Person objects.
- Passes them to the template for display.

#### **Update**
- Loads the selected Person (using primary key).
- Prefills the form with existing data.
- Saves updates when submitted.

#### **Delete**
- Confirms deletion.
- Deletes the selected Person from the database after POST submission.

Views use context dictionaries to send data from Python to templates.

---

## 4. Templates

All template files are inside **`templates/crudoperations/`**.

### **`create_person.html`**
- Displays a form to add a new record.
- Uses `{{ form.as_p }}` to render form fields.
- Includes `{% csrf_token %}` for security.

### **`list_persons.html`**
- Shows all records in a table format.
- Provides links to edit or delete each entry.
- Displays an “Add person” button.
- Uses a loop to list all persons or show a fallback message if no data exists.

### **`update_person.html`**
- Displays a pre-filled form for editing existing records.
- Submits changes using POST.

### **`delete_person.html`**
- Asks for confirmation before deleting a record.
- Includes a POST form with CSRF protection.

---

## 5. How the App Works Together

- **Models** define the database structure.  
- **Forms** convert models into usable HTML forms.  
- **Views** control the logic for each operation.  
- **URLs** map browser requests to the correct view.  
- **Templates** render the user interface.  

Together, they implement a simple and clean CRUD workflow.

---

## 6. Features

- Add new records  
- Update existing records  
- Delete records safely  
- View all records in a clean table  
- Form validation  
- CSRF protection  
- Model-driven forms  

---

If you want, I can also format this README with badges, screenshots, setup instructions, or installation steps.
