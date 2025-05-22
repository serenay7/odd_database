# ODTU ODD Scholarship Management System

This project is a web application for managing scholarships, recipients, donators, and payments.

## Project Structure

*   `304_alt.py`: The main Flask application file.
*   `mock_data_generator.py`: A script to populate the database with initial mock data.
*   `templates/`: Contains HTML templates for the web interface.
*   `static/`: Contains static files (e.g., CSS).

## Setting up the Application

1.  **Prerequisites:**
    *   Python 3.x
    *   MySQL Server
    *   Required Python packages (see installation below).

2.  **Installation of Dependencies:**
    Install the necessary Python packages using pip:
    ```bash
    pip install Flask Flask-MySQLdb unidecode
    ```
    (`unidecode` is used in `304_alt.py` for report generation, so it's good to have it installed from the start).

3.  **Database Setup:**
    *   Ensure your MySQL server is running.
    *   Create a database named `odtu_odd`. The application and the mock data generator script expect this database to exist.
        ```sql
        CREATE DATABASE IF NOT EXISTS odtu_odd CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
        ```
    *   The application uses specific table structures. These are defined implicitly by the `CREATE TABLE` statements embedded (if any, or expected by the application logic) or should be created manually based on the application's needs. The `mock_data_generator.py` script is designed to populate tables that match the structure used in `304_alt.py`.

4.  **Application Configuration:**
    Both the main application (`304_alt.py`) and the mock data generator (`mock_data_generator.py`) contain database connection settings. Open these files and update the following configuration to match your MySQL setup:
    ```python
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'your_mysql_user' # UPDATE THIS
    app.config['MYSQL_PASSWORD'] = 'your_mysql_password' # UPDATE THIS
    app.config['MYSQL_DB'] = 'odtu_odd'
    ```
    It's crucial to update `MYSQL_USER` and `MYSQL_PASSWORD`. `MYSQL_HOST` might also need changing if your MySQL server is not running on localhost.

## Populating the Database with Mock Data

The `mock_data_generator.py` script is provided to fill the database with sample data. This is useful for testing and demonstrating the application.

**Prerequisites for running the mock data generator:**

*   MySQL server must be running.
*   The database `odtu_odd` must already exist. The script will not create it.
*   Required Python packages must be installed: `Flask`, `Flask-MySQLdb`. If you haven't installed them yet for the main application, use:
    ```bash
    pip install Flask Flask-MySQLdb
    ```
    (Note: `unidecode` is not strictly needed for `mock_data_generator.py` itself, but it's listed with main app dependencies.)

**Database Configuration for the mock data generator:**

*   As mentioned in the "Application Configuration" section, the `mock_data_generator.py` script has its own database connection settings at the top of the file:
    ```python
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root' # Default, ensure this is your MySQL user
    app.config['MYSQL_PASSWORD'] = 'sql123' # Default, CHANGE THIS to your actual password
    app.config['MYSQL_DB'] = 'odtu_odd'
    ```
*   **Important:** Before running the script, verify and update `MYSQL_USER` and `MYSQL_PASSWORD` in `mock_data_generator.py` to match your MySQL credentials.

**Running the Script:**

1.  Navigate to the project's root directory in your terminal.
2.  Execute the script using Python:
    ```bash
    python mock_data_generator.py
    ```
3.  The script will attempt to connect to the database and insert data into the tables: `scholarship`, `recipient`, `donator`, `donation`, `payment`, and `member`.
4.  You will see messages printed to the console indicating the progress, such as "Scholarships inserted successfully," or any errors encountered during the process.

**Verifying Data:**

After the script finishes:
*   You can run the main application (`python 304_alt.py`) and navigate through its web interface to see if the data appears (e.g., on scholarship listings, recipient details pages).
*   Alternatively, use a MySQL client (like MySQL Workbench, phpMyAdmin, or the `mysql` command-line tool) to connect to your `odtu_odd` database and inspect the tables directly (e.g., `SELECT * FROM recipient;`).

**Important Note on Existing Data:**

*   The current `mock_data_generator.py` script attempts to insert data with predefined primary keys (e.g., ScholarshipID 1, RecipientID 1, etc.).
*   **Warning:** If you run the script multiple times against a database that already contains data in these tables, you will likely encounter primary key constraint violations (errors for duplicate entries).
*   For a clean run, it's recommended to manually empty the relevant tables (e.g., using `DELETE FROM tablename;` or `TRUNCATE TABLE tablename;` in a MySQL client) before running the mock data generator if they already contain conflicting data. The script does **not** automatically clear existing data.

## Running the Main Application

Once the database is set up and (optionally) populated:

1.  Ensure your MySQL server is running.
2.  Verify that the database configuration in `304_alt.py` is correct.
3.  Run the Flask application:
    ```bash
    python 304_alt.py
    ```
4.  Open your web browser and go to `http://127.0.0.1:5000/` (or the address shown in the terminal output).

## Contributing
(Details to be added if contributions are open)

## License
(Details to be added - e.g., MIT, GPL)
