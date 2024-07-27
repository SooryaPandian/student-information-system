---

# Student Information System

This repository contains a Student Information System built to manage student data efficiently. This system allows users to add, update, view, and delete student records.

## Features

- Add new student information
- Update existing student records
- View all student information
- Delete student records

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x
- You have installed the required Python packages listed in `requirements.txt`
- You have a MySQL database setup

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SooryaPandian/student-information-system.git
cd student-information-system
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create the MySQL database and tables. Connect to your MySQL database and run the following query:

```sql
CREATE DATABASE student_information_system;

USE student_information_system;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15),
    address VARCHAR(255)
);
```

## Usage

1. Update the database connection details in `app.py`:

```python
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'student_information_system'
```

2. Run the application:

```bash
python app.py
```

3. Open your web browser and navigate to `http://localhost:5000` to access the Student Information System.

## Project Structure

```
student-information-system/
├── app.py
├── templates/
│   ├── index.html
│   ├── add_student.html
│   ├── update_student.html
├── static/
│   ├── css/
│   ├── js/
├── models/
│   ├── student.py
├── requirements.txt
└── README.md
```

- `app.py`: The main application file.
- `templates/`: Contains HTML templates for the web interface.
- `static/`: Contains static files like CSS and JavaScript.
- `models/`: Contains the data models for the application.
- `requirements.txt`: Lists the Python packages required for the project.
- `README.md`: This file.


## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---
