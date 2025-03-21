# Midterm-Project

installation Steps

1. Clone the Repository

git clone https://github.com/yourusername/task_manager.git
cd task_manager

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies

pip install -r requirements.txt

4. Apply Database Migrations

python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (for Django Admin Panel)

python manage.py createsuperuser

6. Run the Development Server

python manage.py runserver

Now, open http://127.0.0.1:8000/ in your browser.

Features & Functionality

1. Task List Page

Displays all tasks with title, description, due date, and status.

Provides edit and delete options.

2. Create Task Page

Allows users to create a new task by filling out a form.

Includes input validation.

3. Edit Task Page

Enables users to modify task details.

Ensures due dates are valid.

4. Delete Task Page

Removes a task from the system instantly.

5. Status Management

Tasks are automatically marked as Overdue, Upcoming, or Completed based on the due date.
