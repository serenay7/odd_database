from flask import Flask, render_template, request, redirect, url_for, session, send_file
from flask_ngrok import run_with_ngrok
from flask_mysqldb import MySQL
from unidecode import unidecode
import datetime
import csv
import re

app = Flask(__name__)
run_with_ngrok(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sql123'
app.config['MYSQL_DB'] = 'odtu_odd'
  
mysql = MySQL(app)

js2sql = {'jid': 'RepicientID',
          'name': 'Name',
          'address': 'Address',
          'phone': 'PhoneNumber',
          'email': 'E-mail',
          'department': 'Department',
          'studentid': 'StudentID',
          'citizenid': 'CitizenID',
          'fpd': 'FirstPaymentDate',
          'branchno': 'BranchNo',
          'accountno': 'AccountNo',
          'iban': 'IBAN',
          'status': 'Status',
          'scholarshipid': 'ScholarshipID',
          'monthlystipendpayment': 'MonthlyStipendPayment',
          'status': 'Status',
          'detaileddescription': 'DetailedDescription',
          'paymentid':'PaymentID',
          'paymentdate':'PaymentDate',
          'paymentamount':'PaymentAmount',
          'recipientid': 'RecipientID',
          'donationid': 'DonationID',
          'amountreceived': 'AmountReceived',
          'donatorid':'DonatorID',
          'memberid': 'MemberID'
          }

@app.route('/')
def index():
    return render_template("homepage.html")
    
@app.route('/newrecipient.html', methods =['GET', 'POST'])
def newrecipient():
    msg = ''
    if request.method == 'POST' and 'Name' in request.form and 'Address' in request.form and 'PhoneNumber' in request.form and 'Email' in request.form and 'Department' in request.form and 'StudentID' in request.form and 'CitizenID' in request.form and 'FirstPaymentDate' in request.form and 'BranchNo' in request.form and 'AccountNo' in request.form and 'IBAN' in request.form and 'Status' in request.form and 'ScholarshipID' in request.form:
        # RecipientID = request.form['RecipientID']
        Name = request.form['Name']
        Address = request.form['Address']
        PhoneNumber = request.form['PhoneNumber']
        Email = request.form['Email']
        Department = request.form['Department']
        StudentID = request.form['StudentID']
        CitizenID = request.form['CitizenID']    
        FirstPaymentDate = request.form['FirstPaymentDate'] 
        BranchNo = request.form['BranchNo']
        AccountNo = request.form['AccountNo']
        IBAN = request.form['IBAN']
        Status = request.form['Status']
        ScholarshipID = request.form['ScholarshipID']
        
        try:
            cursor = mysql.connection.cursor()
            #elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            #    msg = 'Invalid email address !'
            cursor.execute("""INSERT INTO recipient (Name, Address, PhoneNumber, `E-mail`, Department, StudentID, CitizenID, FirstPaymentDate, BranchNo, AccountNo, IBAN, Status, ScholarshipID) VALUES ('{}', '{}', '{}', '{}', '{}', {}, {}, '{}', {}, {}, '{}', '{}', {})""".format(Name, Address, PhoneNumber, Email, Department, StudentID, CitizenID, FirstPaymentDate, BranchNo, AccountNo, IBAN, Status, ScholarshipID))
            mysql.connection.commit()
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    return render_template('newrecipient.html', msg = msg)

@app.route('/newscholarship.html', methods =['GET', 'POST'])
def newscholarship():
    msg = ''
    if request.method == 'POST' and 'Name' in request.form and 'MonthlyStipendPayment' in request.form and 'Status' in request.form and 'DetailedDescription' in request.form:
        #ScholarshipID = ("""SELECT MAX(ScholarshipID)+1 FROM scholarship""")
        #print(ScholarshipID)
        Name = request.form['Name']
        MonthlyStipendPayment = request.form['MonthlyStipendPayment']
        Status = request.form['Status']  
        DetailedDescription = request.form['DetailedDescription']

        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""INSERT INTO scholarship (Name, MonthlyStipendPayment, Status, DetailedDescription) VALUES ('{}', {}, '{}', '{}')""".format(Name, MonthlyStipendPayment, Status, DetailedDescription))
            mysql.connection.commit()
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)   
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    return render_template('newscholarship.html', msg = msg)
    
@app.route('/newstipendpayment.html', methods =['GET', 'POST'])
def newstipendpayment():
    msg = ''
    if request.method == 'POST' and 'RecipientID' in request.form and 'PaymentDate' in request.form and 'PaymentAmount' in request.form and 'ScholarshipID' in request.form:
        RecipientID = request.form['RecipientID']
        PaymentDate = request.form['PaymentDate']
        PaymentAmount = request.form['PaymentAmount']  
        ScholarshipID = request.form['ScholarshipID']
        cursor = mysql.connection.cursor()
        
        try:
            cursor.execute("""INSERT INTO payment (RecipientID, PaymentDate, PaymentAmount, ScholarshipID) VALUES ({}, '{}', {}, {})""".format(RecipientID, PaymentDate, PaymentAmount, ScholarshipID))
            mysql.connection.commit()
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    return render_template('newstipendpayment.html', msg = msg)
    
@app.route('/newdonation.html', methods =['GET', 'POST'])
def newdonation():
    msg = ''
    if request.method == 'POST' and 'AmountReceived' in request.form and 'DonatorID' in request.form and 'PaymentDate' in request.form and 'ScholarshipID' in request.form:
        AmountReceived = request.form['AmountReceived']
        DonatorID = request.form['DonatorID']
        PaymentDate = request.form['PaymentDate']  
        ScholarshipID = request.form['ScholarshipID']
        
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""INSERT INTO donation (AmountReceived, DonatorID, PaymentDate, ScholarshipID) VALUES ({}, {}, '{}', {})""".format(AmountReceived, DonatorID, PaymentDate, ScholarshipID))
            mysql.connection.commit()
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    return render_template('newdonation.html', msg = msg)
    
@app.route('/newdonator.html', methods =['GET', 'POST'])
def newdonator():
    msg = ''
    if request.method == 'POST' and 'Name' in request.form and 'Address' in request.form and 'PhoneNumber' in request.form and 'Email' in request.form and 'CitizenID' in request.form and 'ScholarshipID' in request.form:
        Name = request.form['Name']
        Address = request.form['Address']
        PhoneNumber = request.form['PhoneNumber']  
        Email = request.form['Email']
        CitizenID = request.form['CitizenID']
        ScholarshipID = request.form['ScholarshipID']
        
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""INSERT INTO donator (Name, Address, PhoneNumber, `E-mail`, CitizenID, ScholarshipID) VALUES ('{}', '{}', '{}', '{}', {}, {})""".format(Name, Address, PhoneNumber, Email, CitizenID, ScholarshipID))
            mysql.connection.commit()
            msg = 'Success !'

        except Exception as e:
            msg = 'Failure: ' + str(e)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    return render_template('newdonator.html', msg = msg)

@app.route('/newmember.html', methods =['GET', 'POST'])
def newmember():
    msg = ''
    if request.method == 'POST' and 'Name' in request.form and 'Address' in request.form and 'PhoneNumber' in request.form and 'Email' in request.form and 'CitizenID' in request.form:
        Name = request.form['Name']
        Address = request.form['Address']
        PhoneNumber = request.form['PhoneNumber']  
        Email = request.form['Email']
        CitizenID = request.form['CitizenID']
        
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""INSERT INTO member (Name, Address, PhoneNumber, `E-mail`, CitizenID) VALUES ('{}', '{}', '{}', '{}', {})""".format(Name, Address, PhoneNumber, Email, CitizenID))
            mysql.connection.commit()
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    return render_template('newmember.html', msg = msg)
    
@app.route('/paymentordergeneration.html', methods =['GET', 'POST'])
def paymentordergeneration():

    def unwrap(sql_object):
        res = []
        total = 0
        for i in list(sql_object):
            individual = [str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), ' ' * (25 - len(i[4])), str(i[5]), ' ' * (30 - len(i[5])), str(i[6]), str(i[7]), ' ' * (50 - len(i[7])), str(i[8]), '\n']
            res.append(individual)
            total += i[3]
        return res, total
        
    msg = ''
    if request.method == 'POST' and 'TransactionDate' in request.form and 'TransactionTime' in request.form:
    
        x = datetime.datetime.now()
        
        TransactionDate = request.form['TransactionDate']
        TransactionTime = request.form['TransactionTime']
        
        if request.form['Month']:
            Month = request.form['Month']
        else:
            Month = x.month
        
        if request.form['BankCustomerNumber']:
            BankCustomerNumber = request.form['BankCustomerNumber']
        else:
            BankCustomerNumber = '4816479'
        
        if request.form['CustomerTitle']:
            CustomerTitle = request.form['CustomerTitle']
        else:
            CustomerTitle = 'ODTÜ Öğrenci Destekleme Derneği'
        if request.form['CustomerIBAN']:
            CustomerIBAN = request.form['CustomerIBAN']
        else:
            CustomerIBAN = 'TR880006400000142290431827'
        if request.form['Currency']:
            Currency = request.form['Currency']
        else:
            Currency = 'TRY'
        if request.form['TransactionType']:
            TransactionType = request.form['TransactionType']
        else:
            TransactionType = 'HAVALE'
        if request.form['CustomerAddress']:
            CustomerAddress = request.form['CustomerAddress']
        else:
            CustomerAddress = 'ODTÜ Endüstri Mühendisliği Bölümü'
        if request.form['CityCode']:
            CityCode = request.form['CityCode']
        else:
            CityCode = '006'
        if request.form['PaymentOrderFileFolder']:
            PaymentOrderFileFolder = request.form['PaymentOrderFileFolder']
        else:
            PaymentOrderFileFolder = 'C:\\Users\\Sinan\\Desktop'
                
        try:
            cursor = mysql.connection.cursor()
            
            cursor.execute("""SELECT CONCAT('D0',recipient.BranchNo), recipient.AccountNo, recipient.IBAN, scholarship.MonthlyStipendPayment*FLOOR(DATEDIFF('{}-{}-01',MAX(PaymentDate))/30) AS PaymentAmount, LEFT(recipient.Name,25), LEFT(scholarship.Name,30), recipient.CitizenID, CONCAT('C','Öğrenci'), DATE_FORMAT(recipient.FirstPaymentDate, '%d%m%y')
FROM recipient INNER JOIN scholarship ON(recipient.ScholarshipID=scholarship.ScholarshipID) INNER JOIN payment ON(payment.RecipientID=recipient.RepicientID)
WHERE (recipient.Status='Active') AND (recipient.IBAN IS NOT NULL OR recipient.AccountNo IS NOT NULL OR recipient.BranchNo IS NOT NULL)
GROUP BY recipient.RepicientID;""".format(x.year, Month)) 
            
            mysql.connection.commit()
            rv = cursor.fetchall()
            data, total = unwrap(rv)    
            header = """B{IBAN}{Cur}{Date}{Time}H{Title}00000{Number}{City}{Addr}\n""".format(IBAN=CustomerIBAN, Cur=Currency, Date=(str(TransactionDate[-2:]) + str(TransactionDate[-3:-5]) + str(TransactionDate[:4])), Time=(str(TransactionTime[:2]) +  str(TransactionTime[3:])), Title=CustomerTitle[:25], Number=BankCustomerNumber, City=CityCode, Addr=CustomerAddress[:200])
            last = """T00043{:014.2f}""".format(total)                
            with open('csv\\payments.txt', mode='w', newline='', encoding="utf-8") as file:
                file.write(header)
                for i in data:
                    file.write(''.join(i))
                file.write(last)
            
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
            
        
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    return render_template('paymentordergeneration.html', msg = msg)
 
@app.route('/csv/payments.txt', methods =['GET', 'POST'])
def paymentstxt():
	try:
		return send_file('csv\\payments.txt', download_name='payments.txt')
	except Exception as e:
		return str(e)
  
@app.route('/scholarshipreport.html', methods =['GET', 'POST'])
def scholarshipreport():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = [i[0], i[1], float(i[2])]
            res.append(individual)
        return res

    data = []
    msg = ''
    avss = []
    space_dict = {}

    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT Name FROM Scholarship""")
    mysql.connection.commit()
    rv = cursor.fetchall()
    selected_scholarships = []
    for i in rv:
        avss.append([i[0], unidecode(i[0].replace(' ', ''))])
        space_dict[unidecode(i[0].replace(' ', ''))] = i[0]
    
    if request.method == 'POST' and 'beginningdate' in request.form and 'enddate':
        beginningdate = request.form['beginningdate']
        enddate = request.form['enddate']

        try:
            sqlscholarship = 'SELECT Name FROM scholarship WHERE'
            for i in request.form:
                if i in [x[1] for x in avss]:
                    sqlscholarship += """ NAME = '""" + space_dict[i] + """' OR"""
                    selected_scholarships.append(space_dict[i])
                           
            cursor = mysql.connection.cursor()         
            cursor.execute("""SELECT YEAR(PaymentDate) AS Year, MONTH(PaymentDate) AS Month, SUM(PaymentAmount) AS MonthlyScholarshipPayment FROM payment INNER JOIN scholarship ON (payment.ScholarshipID = scholarship.ScholarshipID) WHERE scholarship.Name IN ({}) AND payment.PaymentDate BETWEEN '{}' AND '{}' GROUP BY YEAR(PaymentDate), MONTH(PaymentDate);""".format(sqlscholarship[:-3], beginningdate, enddate)) 
            mysql.connection.commit() 
            rv = cursor.fetchall()
            data = unwrap(rv)
            
            with open('csv\\scholarshipreport.csv', mode='w', newline='') as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                employee_writer.writerow(['Year', 'Month', 'Payment'])
                for i in data:
                    employee_writer.writerow(i)
            
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    
    return render_template('scholarshipreport.html', msg = msg, avss = avss, data1 = data, selected_scholarships=' '.join(selected_scholarships))
    
@app.route('/csv/scholarshipreport.csv', methods =['GET', 'POST'])
def scholarshipreportcsv():
	try:
		return send_file('csv\\scholarshipreport.csv', download_name='scholarshipreport.csv')
	except Exception as e:
		return str(e)

@app.route('/donationsreport.html', methods =['GET', 'POST'])
def donationsreport():
    def unwrap1(sql_object):
        res = []
        for i in list(sql_object):
            individual = [i[0], i[1], i[2], float(i[3])]
            res.append(individual)
        return res

    def unwrap2(sql_object):
        res = []
        for i in list(sql_object):
            individual = [float(i[0])]
            res.append(individual)
        return res
    
    table_data1 = []
    table_data2 = []
    msg = ''
    avss = []
    space_dict = {}

    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT Name FROM Scholarship""")
    mysql.connection.commit()
    rv = cursor.fetchall()
    for i in rv:
        avss.append([i[0], unidecode(i[0].replace(' ', ''))])
        space_dict[unidecode(i[0].replace(' ', ''))] = i[0]
        
    
    if request.method == 'POST' and 'beginningdate' in request.form and 'enddate' in request.form:
        beginningdate = request.form['beginningdate']
        enddate = request.form['enddate']
             
        try:
            sqlscholarship = 'SELECT Name FROM scholarship WHERE'
            for i in request.form:
                if i in [x[1] for x in avss]:
                    sqlscholarship += """ NAME = '""" + space_dict[i] + """' OR"""
                    
              
            cursor = mysql.connection.cursor()         
            cursor.execute("""SELECT YEAR(PaymentDate) AS Year, MONTH(PaymentDate) AS Month, scholarship.Name, (AmountReceived) AS MonthlyDonation FROM donation INNER JOIN scholarship ON(donation.ScholarshipID = scholarship.ScholarshipID) WHERE scholarship.Name IN ({}) AND (donation.PaymentDate BETWEEN '{}' AND '{}') GROUP BY scholarship.ScholarshipID, MONTH(PaymentDate), YEAR(PaymentDate)""".format(sqlscholarship[:-3], beginningdate, enddate)) 
            mysql.connection.commit() 
            rv = cursor.fetchall()
            table_data1 = unwrap1(rv)
            
            with open('csv\\donationsreport1.csv', mode='w', newline='', encoding="utf-8") as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                employee_writer.writerow(['Year', 'Month', 'Name', 'Payment'])
                for i in table_data1:
                    employee_writer.writerow(i)
            
            msg = 'Success 1!'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
         
        try:
            sqlscholarship = 'SELECT Name FROM scholarship WHERE'
            for i in request.form:
                if i in [x[1] for x in avss]:
                    sqlscholarship += """ NAME = '""" + space_dict[i] + """' OR"""
                           
            cursor = mysql.connection.cursor()         
            cursor.execute("""SELECT SUM(AmountReceived) AS TotalDonation FROM donation INNER JOIN scholarship ON(donation.ScholarshipID = scholarship.ScholarshipID) WHERE scholarship.Name IN ({}) AND (donation.PaymentDate BETWEEN '{}' AND '{}')""".format(sqlscholarship[:-3], beginningdate, enddate)) 
            mysql.connection.commit() 
            rv = cursor.fetchall()
            table_data2 = unwrap2(rv)
            
            with open('csv\\donationsreport2.csv', mode='w', newline='', encoding="utf-8") as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                employee_writer.writerow(['Total Payment'])
                for i in table_data2:
                    employee_writer.writerow(i)
            
            msg = 'Success 2!'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
        
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
        
    
    return render_template('donationsreport.html', msg = msg, avss = avss, table_data1 = table_data1, table_data2 = table_data2 )

@app.route('/csv/donationsreport1.csv', methods =['GET', 'POST'])
def donationsreport1csv():
	try:
		return send_file('csv\\donationsreport1.csv', download_name='donationsreport1.csv')
	except Exception as e:
		return str(e)
        
@app.route('/csv/donationsreport2.csv', methods =['GET', 'POST'])
def donationsreport2csv():
	try:
		return send_file('csv\\donationsreport2.csv', download_name='donationsreport2.csv')
	except Exception as e:
		return str(e)


@app.route('/numofrecipients.html', methods =['GET', 'POST'])
def numofrecipients():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = [i[0], i[1], i[2]]
            res.append(individual)
        return res

    # Scholarship isimleri list etme
    data = []
    msg = ''
    avss = 'Current Scholarships: | '

    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT Name FROM Scholarship""")
    mysql.connection.commit()
    rv = cursor.fetchall()
    for i in rv:
        avss += str(i[0]) + ' | '
    ####
    
    if request.method == 'POST' and 'beginningdate' in request.form and 'enddate' in request.form:
        beginningdate = request.form['beginningdate']
        enddate = request.form['enddate']
       
        try:
                           
            cursor = mysql.connection.cursor()         
            cursor.execute("""SELECT YEAR(PaymentDate) AS Year, MONTH(PaymentDate) AS Month, COUNT(RecipientID) AS NumofRecip FROM payment WHERE PaymentDate BETWEEN '{}' AND '{}' GROUP BY YEAR(PaymentDate), MONTH(PaymentDate);""".format(beginningdate, enddate)) 
            mysql.connection.commit() 
            rv = cursor.fetchall()
            data = unwrap(rv)
            
            with open('csv\\numofrecipients.csv', newline='', mode='w') as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                employee_writer.writerow(['Year', 'Month', 'Count'])
                for i in data:
                    employee_writer.writerow(i)
            
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    
    return render_template('numofrecipients.html', msg = msg, avss = avss, data1 = data)

@app.route('/csv/numofrecipients.csv', methods =['GET', 'POST'])
def numofrecipientscsv():
	try:
		return send_file('csv\\numofrecipients.csv', download_name='numofrecipients.csv')
	except Exception as e:
		return str(e)

@app.route('/totalnumofrecipients.html', methods =['GET', 'POST'])
def totalnumofrecipients():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = [i[0], i[1]]
            res.append(individual)
        return res

    # Scholarship isimleri list etme
    data = []
    msg = ''
    
    if request.method == 'POST':       
        try:
                           
            cursor = mysql.connection.cursor()         
            cursor.execute("""SELECT Department, COUNT(StudentID) FROM recipient WHERE Status = 'Active' GROUP BY Department;""")
            mysql.connection.commit() 
            rv = cursor.fetchall()
            data = unwrap(rv)
            
            with open('csv\\totalnumofrecipients.csv', mode='w', newline='') as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                employee_writer.writerow(['Department', 'Count'])
                for i in data:
                    employee_writer.writerow(i)
            
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    
    return render_template('totalnumofrecipients.html', msg = msg, data1 = data)

@app.route('/csv/totalnumofrecipients.csv', methods =['GET', 'POST'])
def totalnumofrecipientsscsv():
	try:
		return send_file('csv\\totalnumofrecipients.csv', download_name='totalnumofrecipients.csv')
	except Exception as e:
		return str(e)

##RAPOR 5
@app.route('/donatorspaid.html', methods =['GET', 'POST'])
def donatorspaid():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = [i[0], float(i[1])]
            res.append(individual)
        return res

    data = []
    msg = ''
    avss = []
    space_dict = {}
    
    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT Name FROM Scholarship""")
    mysql.connection.commit()
    rv = cursor.fetchall()
    for i in rv:
        avss.append([i[0], unidecode(i[0].replace(' ', ''))])
        space_dict[unidecode(i[0].replace(' ', ''))] = i[0]
    
    if request.method == 'POST' and 'beginningdate' in request.form and 'enddate' in request.form:
        beginningdate = request.form['beginningdate']
        enddate = request.form['enddate']
       
        try:
            sqlscholarship = 'SELECT Name FROM scholarship WHERE'
            sqlscholarship += """ NAME = '""" + space_dict[request.form['radio']] + """' OR"""
                           
            cursor = mysql.connection.cursor()     
            print("""SELECT donator.Name AS ad, SUM(AmountReceived) AS DonatorPaid FROM donation INNER JOIN donator ON (donation.DonatorID=donator.DonatorID) INNER JOIN scholarship ON (donation.ScholarshipID=scholarship.ScholarshipID) WHERE (scholarship.Name = ({}) AND (donation.PaymentDate BETWEEN '{}' AND '{}')) GROUP BY (ad) ORDER BY (ad);""".format(sqlscholarship[:-3], beginningdate, enddate))
            cursor.execute("""SELECT donator.Name AS ad, SUM(AmountReceived) AS DonatorPaid FROM donation INNER JOIN donator ON (donation.DonatorID=donator.DonatorID) INNER JOIN scholarship ON (donation.ScholarshipID=scholarship.ScholarshipID) WHERE (scholarship.Name = ({}) AND (donation.PaymentDate BETWEEN '{}' AND '{}')) GROUP BY (ad) ORDER BY (ad);""".format(sqlscholarship[:-3], beginningdate, enddate)) 
            mysql.connection.commit() 
            rv = cursor.fetchall()
            data = unwrap(rv)
            
            with open('csv\\donatorspaid.csv', mode='w', newline='', encoding="utf-8") as employee_file:
                employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                employee_writer.writerow(['Name', 'Paid'])
                for i in data:
                    employee_writer.writerow(i)
            
            msg = 'Success !'
            
        except Exception as e:
            msg = 'Failure: ' + str(e)
            
    elif request.method == 'POST':
        msg = 'Please fill out the form completely!'
    
    return render_template('donatorspaid.html', msg = msg, avss = avss, data1 = data)

@app.route('/csv/donatorspaid.csv', methods =['GET', 'POST'])
def donatorspaidcsv():
	try:
		return send_file('csv\\donatorspaid.csv', download_name='donatorspaid.csv')
	except Exception as e:
		return str(e)

@app.route('/reportmenu.html')
def reportmenu():
    return render_template("reportmenu.html")
  
@app.route('/recipient.html')
def recipienthtml():
    return render_template('recipient.html')
    
@app.route('/scholarship.html')
def scholarshipthtml():
    return render_template('scholarship.html')

@app.route('/payment.html')
def paymenthtml():
    return render_template('payment.html')
    
@app.route('/donation.html')
def donationhtml():
    return render_template('donation.html')
    
@app.route('/donator.html')
def donatorhtml():
    return render_template('donator.html')
    
@app.route('/member.html')
def memberhtml():
    return render_template('member.html')
    
@app.route("/homepage.html")
def homepage():
    return render_template("homepage.html")
   
    
@app.route('/api/recipient')
def recipient():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = {'jid': i[0],
                          'name': i[1],
                          'address': i[2],
                          'phone': i[3],
                          'email': i[4],
                          'department': i[5],
                          'studentid': i[6],
                          'citizenid': i[7],
                          'fpd': i[8],
                          'branchno': i[9],
                          'accountno': i[10],
                          'iban': i[11],
                          'status': i[12],
                          'scholarshipid': i[13],
                          'delete': 'x'}
            res.append(individual)
        return res

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM recipient"
    
    
    # search filter
    search = request.args.get('search')
    keys = ['Name', 'RepicientID', 'Address', 'PhoneNumber', '`E-mail`', 'Department', 'StudentID', 'CitizenID',  'FirstPaymentDate', 'BranchNo', 'AccountNo', 'IBAN', 'ScholarshipID']
    if search:
        query += ' WHERE'
        for i in keys:
            query += ' {} LIKE \'%{}%\' OR'.format(i, search)
        query = query[:-3]
        
    cursor.execute(query)
    rv = cursor.fetchall()
    
    total = len(unwrap(rv))        
    
    
    # sorting
    sort = request.args.get('sort')
    if sort:
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if direction == '-':
                query = query + ' ORDER BY {} DESC'.format(js2sql[name])
            else:
                query = query + ' ORDER BY {} ASC'.format(js2sql[name])
            
            
    
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query + ' LIMIT {} OFFSET {}'.format(length, start)
     
    cursor.execute(query)
    rv = cursor.fetchall()
    
    records = unwrap(rv)
    
    return {
        'data': records,
        'total': total,
    }
    


@app.route('/api/recipient', methods=['POST'])
def update_recipient():
    data = request.get_json()
    if 'id' not in data:
        abort(400)
        
    cursor = mysql.connection.cursor()
    
    for field in ['name', 'address', 'phone', 'email', 'department', 'studentid', 'citizenid', 'fpd', 'branchno', 'accountno', 'iban', 'status', 'scholarshipid', 'delete']:
        if field in data:
            if 'delete' in data.keys():
                if data['delete'] == '':
                    query = 'DELETE FROM recipient WHERE RepicientID = {}'.format(data['id'])
                    cursor.execute(query)
                    mysql.connection.commit()    
               
            else:
                query = 'UPDATE recipient SET {}=\"{}\" WHERE RepicientID = {}'.format(str(js2sql[field]), str(data[field]), data['id'])
                cursor.execute(query)
                mysql.connection.commit()
            
            
    return '', 204
    
    
 
@app.route('/api/scholarship')
def scholarship():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = {'scholarshipid': i[0],
                          'name': i[1],
                          'monthlystipendpayment': i[2],
                          'status': i[3],
                          'detaileddescription': i[4],
                          'delete': 'x'}
            res.append(individual)
        return res

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM scholarship"
    
    
    # search filter
    search = request.args.get('search')
    keys = ['ScholarshipID', 'Name', 'MonthlyStipendPayment', 'Status', 'DetailedDescription']
    if search:
        query += ' WHERE'
        for i in keys:
            query += ' {} LIKE \'%{}%\' OR'.format(i, search)
        query = query[:-3]

    cursor.execute(query)
    rv = cursor.fetchall()
    
    total = len(unwrap(rv))        
    
    
    # sorting
    sort = request.args.get('sort')
    if sort:
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if direction == '-':
                query = query + ' ORDER BY {} DESC'.format(js2sql[name])
            else:
                query = query + ' ORDER BY {} ASC'.format(js2sql[name])
            
            
    
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query + ' LIMIT {} OFFSET {}'.format(length, start)
        
    cursor.execute(query)
    rv = cursor.fetchall()
    
    records = unwrap(rv)
    
    return {
        'data': records,
        'total': total,
    }
    


@app.route('/api/scholarship', methods=['POST'])
def update_scholarship():
    data = request.get_json()
    if 'id' not in data:
        abort(400)
        
    cursor = mysql.connection.cursor()
    
    for field in ['name', 'monthlystipendpayment', 'status', 'detaileddescription', 'delete']:
        if field in data:
            if 'delete' in data.keys():
                if data['delete'] == '':
                    query = 'DELETE FROM scholarship WHERE ScholarshipID = {}'.format(data['id'])
                    cursor.execute(query)
                    mysql.connection.commit()    
               
            else:
                query = 'UPDATE scholarship SET {}=\"{}\" WHERE ScholarshipID = {}'.format(str(js2sql[field]), str(data[field]), data['id'])
                cursor.execute(query)
                mysql.connection.commit()
            
            
    return '', 204
    
@app.route('/api/payment')
def payment():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = {'paymentid': i[0],
                          'recipientid': i[1],
                          'paymentdate': i[2],
                          'paymentamount': i[3],
                          'scholarshipid': i[4],
                          'delete': 'x'}
            res.append(individual)
        return res

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM payment"
    
    
    # search filter
    search = request.args.get('search')
    keys = ['PaymentID', 'RecipientID', 'PaymentDate', 'PaymentAmount', 'ScholarshipID']
    if search:
        query += ' WHERE'
        for i in keys:
            query += ' {} LIKE \'%{}%\' OR'.format(i, search)
        query = query[:-3]

    cursor.execute(query)
    rv = cursor.fetchall()
    
    total = len(unwrap(rv))        
    
    
    # sorting
    sort = request.args.get('sort')
    if sort:
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if direction == '-':
                query = query + ' ORDER BY {} DESC'.format(js2sql[name])
            else:
                query = query + ' ORDER BY {} ASC'.format(js2sql[name])
            
            
    
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query + ' LIMIT {} OFFSET {}'.format(length, start)
        
    cursor.execute(query)
    rv = cursor.fetchall()
    
    records = unwrap(rv)
    
    return {
        'data': records,
        'total': total,
    }
    


@app.route('/api/payment', methods=['POST'])
def update_payment():
    data = request.get_json()
    print(data)
    if 'id' not in data:
        abort(400)
        
    cursor = mysql.connection.cursor()
    
    for field in ['recipientid', 'paymentdate', 'paymentamount', 'scholarshipid', 'delete']:
        if field in data:
            if 'delete' in data.keys():
                if data['delete'] == '':
                    query = 'DELETE FROM payment WHERE PaymentID = {}'.format(data['id'])
                    cursor.execute(query)
                    mysql.connection.commit()    
               
            else:
                query = 'UPDATE payment SET {}=\"{}\" WHERE PaymentID = {}'.format(str(js2sql[field]), str(data[field]), data['id'])
                cursor.execute(query)
                mysql.connection.commit()
            
            
    return '', 204
    
@app.route('/api/donation')
def donation():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = {'donationid': i[0],
                          'amountreceived': i[1],
                          'donatorid': i[2],
                          'paymentdate': i[3],
                          'scholarshipid': i[4],
                          'delete': 'x'}
            res.append(individual)
        return res

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM donation"
    
    
    # search filter
    search = request.args.get('search')
    keys = ['DonationID', 'AmountReceived', 'DonatorID', 'PaymentDate', 'ScholarshipID']
    if search:
        query += ' WHERE'
        for i in keys:
            query += ' {} LIKE \'%{}%\' OR'.format(i, search)
        query = query[:-3]

    cursor.execute(query)
    rv = cursor.fetchall()
    
    total = len(unwrap(rv))        
    
    
    # sorting
    sort = request.args.get('sort')
    if sort:
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if direction == '-':
                query = query + ' ORDER BY {} DESC'.format(js2sql[name])
            else:
                query = query + ' ORDER BY {} ASC'.format(js2sql[name])
            
            
    
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query + ' LIMIT {} OFFSET {}'.format(length, start)
        
    cursor.execute(query)
    rv = cursor.fetchall()
    
    records = unwrap(rv)
    
    return {
        'data': records,
        'total': total,
    }
    


@app.route('/api/donation', methods=['POST'])
def update_donation():
    data = request.get_json()
    if 'id' not in data:
        abort(400)
        
    cursor = mysql.connection.cursor()
    
    for field in ['amountreceived', 'donatorid', 'paymentdate', 'scholarshipid', 'delete']:
        if field in data:
            if 'delete' in data.keys():
                if data['delete'] == '':
                    query = 'DELETE FROM donation WHERE DonationID = {}'.format(data['id'])
                    cursor.execute(query)
                    mysql.connection.commit()    
               
            else:
                query = 'UPDATE donation SET {}=\"{}\" WHERE DonationID = {}'.format(str(js2sql[field]), str(data[field]), data['id'])
                cursor.execute(query)
                mysql.connection.commit()
            
            
    return '', 204
    
@app.route('/api/donator')
def donator():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = {'donatorid': i[0],
                          'name': i[1],
                          'address': i[2],
                          'phone': i[3],
                          'email': i[4],
						  'citizenid': i[5],
						  'scholarshipid': i[6],
                          'delete': 'x'}
            res.append(individual)
        return res

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM donator"
    
    
    # search filter
    search = request.args.get('search')
    keys = ['DonatorID', 'Name', 'Address', '`E-mail`', 'CitizenID', 'ScholarshipID']
    if search:
        query += ' WHERE'
        for i in keys:
            query += ' {} LIKE \'%{}%\' OR'.format(i, search)
        query = query[:-3]

    cursor.execute(query)
    rv = cursor.fetchall()
    
    total = len(unwrap(rv))        
    
    
    # sorting
    sort = request.args.get('sort')
    if sort:
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if direction == '-':
                query = query + ' ORDER BY {} DESC'.format(js2sql[name])
            else:
                query = query + ' ORDER BY {} ASC'.format(js2sql[name])
            
            
    
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query + ' LIMIT {} OFFSET {}'.format(length, start)
        
    cursor.execute(query)
    rv = cursor.fetchall()
    
    records = unwrap(rv)
    
    return {
        'data': records,
        'total': total,
    }
    


@app.route('/api/donator', methods=['POST'])
def update_donator():
    data = request.get_json()
    if 'id' not in data:
        abort(400)
        
    cursor = mysql.connection.cursor()
    
    for field in ['name', 'address', 'phone', 'email', 'citizenid', 'scholarshipid', 'delete']:
        if field in data:
            if 'delete' in data.keys():
                if data['delete'] == '':
                    query = 'DELETE FROM donator WHERE DonatorID = {}'.format(data['id'])
                    cursor.execute(query)
                    mysql.connection.commit()    
               
            else:
                query = 'UPDATE donator SET {}=\"{}\" WHERE DonatorID = {}'.format(str(js2sql[field]), str(data[field]), data['id'])
                cursor.execute(query)
                mysql.connection.commit()
            
            
    return '', 204

@app.route('/api/member')
def member():
    def unwrap(sql_object):
        res = []
        for i in list(sql_object):
            individual = {'memberid': i[0],
                          'name': i[1],
                          'address': i[2],
                          'phone': i[3],
                          'email': i[4],
						  'citizenid': i[5],
                          'delete': 'x'}
            res.append(individual)
        return res

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM member"
    
    
    # search filter
    search = request.args.get('search')
    keys = ['MemberID', 'Name', 'Address', '`E-mail`', 'CitizenID']
    if search:
        query += ' WHERE'
        for i in keys:
            query += ' {} LIKE \'%{}%\' OR'.format(i, search)
        query = query[:-3]

    cursor.execute(query)
    rv = cursor.fetchall()
    
    total = len(unwrap(rv))        
    
    
    # sorting
    sort = request.args.get('sort')
    if sort:
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if direction == '-':
                query = query + ' ORDER BY {} DESC'.format(js2sql[name])
            else:
                query = query + ' ORDER BY {} ASC'.format(js2sql[name])
            
            
    
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query + ' LIMIT {} OFFSET {}'.format(length, start)
        
    cursor.execute(query)
    rv = cursor.fetchall()
    
    records = unwrap(rv)
    
    return {
        'data': records,
        'total': total,
    }
    


@app.route('/api/member', methods=['POST'])
def update_member():
    data = request.get_json()
    if 'id' not in data:
        abort(400)
        
    cursor = mysql.connection.cursor()
    
    for field in ['name', 'address', 'phone', 'email', 'citizenid', 'delete']:
        if field in data:
            if 'delete' in data.keys():
                if data['delete'] == '':
                    query = 'DELETE FROM member WHERE MemberID = {}'.format(data['id'])
                    cursor.execute(query)
                    mysql.connection.commit()    
               
            else:
                query = 'UPDATE member SET {}=\"{}\" WHERE MemberID = {}'.format(str(js2sql[field]), str(data[field]), data['id'])
                cursor.execute(query)
                mysql.connection.commit()
            
            
    return '', 204
    
if __name__ == "__main__":
    app.run()