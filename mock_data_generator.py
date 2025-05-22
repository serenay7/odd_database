from flask import Flask
from flask_mysqldb import MySQL

# Data definitions (as previously defined)
scholarship_data = [
    {"ScholarshipID": 1, "Name": "Merit Scholarship", "MonthlyStipendPayment": 500, "Status": "Active", "DetailedDescription": "Awarded based on academic excellence."},
    {"ScholarshipID": 2, "Name": "Needs-Based Grant", "MonthlyStipendPayment": 700, "Status": "Active", "DetailedDescription": "Awarded to students with demonstrated financial need."},
    {"ScholarshipID": 3, "Name": "Athletic Scholarship", "MonthlyStipendPayment": 600, "Status": "Inactive", "DetailedDescription": "Awarded to exceptional athletes."},
    {"ScholarshipID": 4, "Name": "STEM Scholarship", "MonthlyStipendPayment": 800, "Status": "Active", "DetailedDescription": "For students pursuing STEM fields."},
]

recipient_data = [
    {"RecipientID": 1, "Name": "Alice Smith", "Address": "123 Main St", "PhoneNumber": "555-1234", "E-mail": "alice@example.com", "Department": "Computer Science", "StudentID": "1001", "CitizenID": "12345678901", "FirstPaymentDate": "2023-09-01", "BranchNo": "101", "AccountNo": "987654321", "IBAN": "DE89370400440532013000", "Status": "Active", "ScholarshipID": 1},
    {"RecipientID": 2, "Name": "Bob Johnson", "Address": "456 Oak Ave", "PhoneNumber": "555-5678", "E-mail": "bob@example.com", "Department": "Engineering", "StudentID": "1002", "CitizenID": "23456789012", "FirstPaymentDate": "2023-09-01", "BranchNo": "102", "AccountNo": "123456789", "IBAN": "GB29NWBK60161331926819", "Status": "Active", "ScholarshipID": 2},
    {"RecipientID": 3, "Name": "Charlie Brown", "Address": "789 Pine Ln", "PhoneNumber": "555-9012", "E-mail": "charlie@example.com", "Department": "Arts", "StudentID": "1003", "CitizenID": "34567890123", "FirstPaymentDate": "2024-01-15", "BranchNo": "103", "AccountNo": "456789123", "IBAN": "FR1420041010050500013M02606", "Status": "Inactive", "ScholarshipID": 1},
    {"RecipientID": 4, "Name": "Diana Prince", "Address": "101 Wonder Way", "PhoneNumber": "555-3456", "E-mail": "diana@example.com", "Department": "Physics", "StudentID": "1004", "CitizenID": "45678901234", "FirstPaymentDate": "2023-10-01", "BranchNo": "101", "AccountNo": "321654987", "IBAN": "IT60X0542811101000000123456", "Status": "Active", "ScholarshipID": 4},
    {"RecipientID": 5, "Name": "Eve Adams", "Address": "202 Garden St", "PhoneNumber": "555-7890", "E-mail": "eve@example.com", "Department": "Biology", "StudentID": "1005", "CitizenID": "56789012345", "FirstPaymentDate": "2024-02-01", "BranchNo": "102", "AccountNo": "654987321", "IBAN": "ES9121000418450200051332", "Status": "Active", "ScholarshipID": 2},
    {"RecipientID": 6, "Name": "Frank Miller", "Address": "303 River Rd", "PhoneNumber": "555-2345", "E-mail": "frank@example.com", "Department": "Mathematics", "StudentID": "1006", "CitizenID": "67890123456", "FirstPaymentDate": "2023-09-10", "BranchNo": "104", "AccountNo": "789123456", "IBAN": "NL91ABNA0417164300", "Status": "Active", "ScholarshipID": 4},
    {"RecipientID": 7, "Name": "Grace Lee", "Address": "404 Hilltop Dr", "PhoneNumber": "555-6789", "E-mail": "grace@example.com", "Department": "Chemistry", "StudentID": "1007", "CitizenID": "78901234567", "FirstPaymentDate": "2024-03-01", "BranchNo": "101", "AccountNo": "159753246", "IBAN": "CH9300762011623852957", "Status": "Active", "ScholarshipID": 1},
    {"RecipientID": 8, "Name": "Henry Wilson", "Address": "505 Lakeview Blvd", "PhoneNumber": "555-1230", "E-mail": "henry@example.com", "Department": "History", "StudentID": "1008", "CitizenID": "89012345678", "FirstPaymentDate": "2023-11-01", "BranchNo": "103", "AccountNo": "357159486", "IBAN": "BE68539007547034", "Status": "Inactive", "ScholarshipID": 2},
    {"RecipientID": 9, "Name": "Ivy Green", "Address": "606 Forest Ave", "PhoneNumber": "555-4567", "E-mail": "ivy@example.com", "Department": "English", "StudentID": "1009", "CitizenID": "90123456789", "FirstPaymentDate": "2024-01-20", "BranchNo": "102", "AccountNo": "951753684", "IBAN": "LU280019400644750000", "Status": "Active", "ScholarshipID": 1},
    {"RecipientID": 10, "Name": "Jack Black", "Address": "707 Mountain Rd", "PhoneNumber": "555-8901", "E-mail": "jack@example.com", "Department": "Geology", "StudentID": "1010", "CitizenID": "11223344556", "FirstPaymentDate": "2023-12-01", "BranchNo": "104", "AccountNo": "753951824", "IBAN": "AT611904400234573201", "Status": "Active", "ScholarshipID": 4},
]

donator_data = [
    {"DonatorID": 1, "Name": "Alpha Corp", "Address": "1 Corporate Dr", "PhoneNumber": "555-0001", "E-mail": "contact@alphacorp.com", "CitizenID": "N/A", "ScholarshipID": 1},
    {"DonatorID": 2, "Name": "Beta Foundation", "Address": "2 Philanthropy Pl", "PhoneNumber": "555-0002", "E-mail": "info@betafoundation.org", "CitizenID": "N/A", "ScholarshipID": 2},
    {"DonatorID": 3, "Name": "Gamma Inc", "Address": "3 Business Blvd", "PhoneNumber": "555-0003", "E-mail": "support@gammainc.net", "CitizenID": "N/A", "ScholarshipID": 1},
    {"DonatorID": 4, "Name": "Delta Trust", "Address": "4 Charity Rd", "PhoneNumber": "555-0004", "E-mail": "admin@deltatrust.org", "CitizenID": "N/A", "ScholarshipID": 4},
    {"DonatorID": 5, "Name": "Epsilon LLC", "Address": "5 Commerce Ct", "PhoneNumber": "555-0005", "E-mail": "contact@epsilonllc.com", "CitizenID": "N/A", "ScholarshipID": 2},
]

donation_data = [
    {"DonationID": 1, "AmountReceived": 10000, "DonatorID": 1, "PaymentDate": "2023-01-15", "ScholarshipID": 1},
    {"DonationID": 2, "AmountReceived": 15000, "DonatorID": 2, "PaymentDate": "2023-02-20", "ScholarshipID": 2},
    {"DonationID": 3, "AmountReceived": 5000, "DonatorID": 3, "PaymentDate": "2023-03-10", "ScholarshipID": 1},
    {"DonationID": 4, "AmountReceived": 20000, "DonatorID": 4, "PaymentDate": "2023-04-05", "ScholarshipID": 4},
    {"DonationID": 5, "AmountReceived": 7500, "DonatorID": 5, "PaymentDate": "2023-05-12", "ScholarshipID": 2},
    {"DonationID": 6, "AmountReceived": 12000, "DonatorID": 1, "PaymentDate": "2023-06-18", "ScholarshipID": 1},
    {"DonationID": 7, "AmountReceived": 8000, "DonatorID": 2, "PaymentDate": "2023-07-22", "ScholarshipID": 2},
    {"DonationID": 8, "AmountReceived": 6000, "DonatorID": 3, "PaymentDate": "2023-08-14", "ScholarshipID": 1},
    {"DonationID": 9, "AmountReceived": 25000, "DonatorID": 4, "PaymentDate": "2023-09-09", "ScholarshipID": 4},
    {"DonationID": 10, "AmountReceived": 9000, "DonatorID": 5, "PaymentDate": "2023-10-25", "ScholarshipID": 2},
    {"DonationID": 11, "AmountReceived": 11000, "DonatorID": 1, "PaymentDate": "2023-11-30", "ScholarshipID": 1},
    {"DonationID": 12, "AmountReceived": 16000, "DonatorID": 2, "PaymentDate": "2023-12-05", "ScholarshipID": 2},
    {"DonationID": 13, "AmountReceived": 5500, "DonatorID": 3, "PaymentDate": "2024-01-19", "ScholarshipID": 1},
    {"DonationID": 14, "AmountReceived": 22000, "DonatorID": 4, "PaymentDate": "2024-02-23", "ScholarshipID": 4},
    {"DonationID": 15, "AmountReceived": 8500, "DonatorID": 5, "PaymentDate": "2024-03-08", "ScholarshipID": 2},
]

payment_data = [
    {"PaymentID": 1, "RecipientID": 1, "PaymentDate": "2023-09-01", "PaymentAmount": 500, "ScholarshipID": 1},
    {"PaymentID": 2, "RecipientID": 2, "PaymentDate": "2023-09-01", "PaymentAmount": 700, "ScholarshipID": 2},
    {"PaymentID": 3, "RecipientID": 1, "PaymentDate": "2023-10-01", "PaymentAmount": 500, "ScholarshipID": 1},
    {"PaymentID": 4, "RecipientID": 4, "PaymentDate": "2023-10-01", "PaymentAmount": 800, "ScholarshipID": 4},
    {"PaymentID": 5, "RecipientID": 2, "PaymentDate": "2023-10-01", "PaymentAmount": 700, "ScholarshipID": 2},
    {"PaymentID": 6, "RecipientID": 6, "PaymentDate": "2023-09-10", "PaymentAmount": 800, "ScholarshipID": 4},
    {"PaymentID": 7, "RecipientID": 1, "PaymentDate": "2023-11-01", "PaymentAmount": 500, "ScholarshipID": 1},
    {"PaymentID": 8, "RecipientID": 2, "PaymentDate": "2023-11-01", "PaymentAmount": 700, "ScholarshipID": 2},
    {"PaymentID": 9, "RecipientID": 4, "PaymentDate": "2023-11-01", "PaymentAmount": 800, "ScholarshipID": 4},
    {"PaymentID": 10, "RecipientID": 8, "PaymentDate": "2023-11-01", "PaymentAmount": 700, "ScholarshipID": 2},
    {"PaymentID": 11, "RecipientID": 10, "PaymentDate": "2023-12-01", "PaymentAmount": 800, "ScholarshipID": 4},
    {"PaymentID": 12, "RecipientID": 1, "PaymentDate": "2023-12-01", "PaymentAmount": 500, "ScholarshipID": 1},
    {"PaymentID": 13, "RecipientID": 2, "PaymentDate": "2023-12-01", "PaymentAmount": 700, "ScholarshipID": 2},
    {"PaymentID": 14, "RecipientID": 3, "PaymentDate": "2024-01-15", "PaymentAmount": 500, "ScholarshipID": 1},
    {"PaymentID": 15, "RecipientID": 9, "PaymentDate": "2024-01-20", "PaymentAmount": 500, "ScholarshipID": 1},
    {"PaymentID": 16, "RecipientID": 5, "PaymentDate": "2024-02-01", "PaymentAmount": 700, "ScholarshipID": 2},
    {"PaymentID": 17, "RecipientID": 1, "PaymentDate": "2024-02-01", "PaymentAmount": 500, "ScholarshipID": 1},
    {"PaymentID": 18, "RecipientID": 4, "PaymentDate": "2024-02-01", "PaymentAmount": 800, "ScholarshipID": 4},
    {"PaymentID": 19, "RecipientID": 7, "PaymentDate": "2024-03-01", "PaymentAmount": 500, "ScholarshipID": 1},
    {"PaymentID": 20, "RecipientID": 2, "PaymentDate": "2024-03-01", "PaymentAmount": 700, "ScholarshipID": 2},
    {"PaymentID": 21, "RecipientID": 6, "PaymentDate": "2023-10-10", "PaymentAmount": 800, "ScholarshipID": 4},
    {"PaymentID": 22, "RecipientID": 10, "PaymentDate": "2024-01-01", "PaymentAmount": 800, "ScholarshipID": 4},
    {"PaymentID": 23, "RecipientID": 5, "PaymentDate": "2024-03-01", "PaymentAmount": 700, "ScholarshipID": 2},
    {"PaymentID": 24, "RecipientID": 9, "PaymentDate": "2024-02-20", "PaymentAmount": 500, "ScholarshipID": 1},
]

member_data = [
    {"MemberID": 1, "Name": "Michael Scott", "Address": "701 Office Park", "PhoneNumber": "555-1001", "E-mail": "mscott@example.com", "CitizenID": "10101010101"},
    {"MemberID": 2, "Name": "Pam Beesly", "Address": "702 Art Studio", "PhoneNumber": "555-1002", "E-mail": "pbeesly@example.com", "CitizenID": "20202020202"},
    {"MemberID": 3, "Name": "Jim Halpert", "Address": "703 Sales Desk", "PhoneNumber": "555-1003", "E-mail": "jhalpert@example.com", "CitizenID": "30303030303"},
    {"MemberID": 4, "Name": "Dwight Schrute", "Address": "704 Beet Farm", "PhoneNumber": "555-1004", "E-mail": "dschrute@example.com", "CitizenID": "40404040404"},
]

# Flask App and MySQL Configuration
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sql123'  # REMINDER: This password might need to be changed by the user.
app.config['MYSQL_DB'] = 'odtu_odd'
mysql = MySQL(app)

# Insertion Functions
def insert_scholarships(mysql):
    try:
        cursor = mysql.connection.cursor()
        for item in scholarship_data:
            sql = "INSERT INTO scholarship (ScholarshipID, Name, MonthlyStipendPayment, Status, DetailedDescription) VALUES (%s, %s, %s, %s, %s)"
            values = (item['ScholarshipID'], item['Name'], item['MonthlyStipendPayment'], item['Status'], item['DetailedDescription'])
            cursor.execute(sql, values)
        mysql.connection.commit()
        print("Scholarships inserted successfully.")
    except Exception as e:
        print(f"Error inserting scholarships: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

def insert_recipients(mysql):
    try:
        cursor = mysql.connection.cursor()
        for item in recipient_data:
            # Note: Using RepicientID as the column name for recipient's primary key
            sql = "INSERT INTO recipient (RepicientID, Name, Address, PhoneNumber, `E-mail`, Department, StudentID, CitizenID, FirstPaymentDate, BranchNo, AccountNo, IBAN, Status, ScholarshipID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (item['RecipientID'], item['Name'], item['Address'], item['PhoneNumber'], item['E-mail'], item['Department'], item['StudentID'], item['CitizenID'], item['FirstPaymentDate'], item['BranchNo'], item['AccountNo'], item['IBAN'], item['Status'], item['ScholarshipID'])
            cursor.execute(sql, values)
        mysql.connection.commit()
        print("Recipients inserted successfully.")
    except Exception as e:
        print(f"Error inserting recipients: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

def insert_donators(mysql):
    try:
        cursor = mysql.connection.cursor()
        for item in donator_data:
            sql = "INSERT INTO donator (DonatorID, Name, Address, PhoneNumber, `E-mail`, CitizenID, ScholarshipID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (item['DonatorID'], item['Name'], item['Address'], item['PhoneNumber'], item['E-mail'], item['CitizenID'], item['ScholarshipID'])
            cursor.execute(sql, values)
        mysql.connection.commit()
        print("Donators inserted successfully.")
    except Exception as e:
        print(f"Error inserting donators: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

def insert_donations(mysql):
    try:
        cursor = mysql.connection.cursor()
        for item in donation_data:
            sql = "INSERT INTO donation (DonationID, AmountReceived, DonatorID, PaymentDate, ScholarshipID) VALUES (%s, %s, %s, %s, %s)"
            values = (item['DonationID'], item['AmountReceived'], item['DonatorID'], item['PaymentDate'], item['ScholarshipID'])
            cursor.execute(sql, values)
        mysql.connection.commit()
        print("Donations inserted successfully.")
    except Exception as e:
        print(f"Error inserting donations: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

def insert_payments(mysql):
    try:
        cursor = mysql.connection.cursor()
        for item in payment_data:
            # Note: Using RecipientID as the FK, which should reference recipient.RepicientID
            sql = "INSERT INTO payment (PaymentID, RecipientID, PaymentDate, PaymentAmount, ScholarshipID) VALUES (%s, %s, %s, %s, %s)"
            values = (item['PaymentID'], item['RecipientID'], item['PaymentDate'], item['PaymentAmount'], item['ScholarshipID'])
            cursor.execute(sql, values)
        mysql.connection.commit()
        print("Payments inserted successfully.")
    except Exception as e:
        print(f"Error inserting payments: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

def insert_members(mysql):
    try:
        cursor = mysql.connection.cursor()
        for item in member_data:
            sql = "INSERT INTO member (MemberID, Name, Address, PhoneNumber, `E-mail`, CitizenID) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (item['MemberID'], item['Name'], item['Address'], item['PhoneNumber'], item['E-mail'], item['CitizenID'])
            cursor.execute(sql, values)
        mysql.connection.commit()
        print("Members inserted successfully.")
    except Exception as e:
        print(f"Error inserting members: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

# Main Execution Block
if __name__ == '__main__':
    with app.app_context():
        # Ensure MySQL service is running and credentials are correct before running.
        # The order of insertion matters due to foreign key constraints.
        print("Attempting to insert mock data into the database...")
        print("Please ensure your MySQL server is running and the database 'odtu_odd' exists.")
        print(f"Using MySQL user: {app.config['MYSQL_USER']} and password: {app.config['MYSQL_PASSWORD']}")
        print("If you encounter connection issues, verify these settings and your MySQL service status.")

        insert_scholarships(mysql)
        insert_recipients(mysql) # Depends on Scholarship
        insert_donators(mysql)   # Depends on Scholarship
        insert_donations(mysql)  # Depends on Donator and Scholarship
        insert_payments(mysql)   # Depends on Recipient and Scholarship
        insert_members(mysql)    # No dependencies on other tables in this mock data

        print("Mock data insertion process completed.")
        print("Please check the console output for success or error messages for each table.")
        print("REMINDER: The MySQL password 'sql123' is a placeholder and might need to be changed by the user to match their local MySQL root password.")
