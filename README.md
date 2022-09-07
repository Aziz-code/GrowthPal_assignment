# GrowthPal_assignment

STEP 1.INSTALLING LIBRARIES:-<br/>
requests <br/>
BeautifulSoup <br/>
pandas <br/>
mysql.connector <br/>
<br/>
STEP 2. IMPORT REQUIRED LIBRARIES <br/>
 <br/>
STEP 3. SELECT PAGE:-
agmark site for the commodities information
 <br/>  <br/>
STEP 4. REQUEST PERMISSION:
After we select what page we want to scrape, now we can copy the page’s URL and use requests to ask permission from the hosting server that we want to fetch data from their site.
 <br/> <br/>
STEP 5. INSPECT TABLE ELEMENT
Obtain information from tag <table>
table1 = soup.find('table', id='table_id')
 <br/> <br/>
STEP 6. CREATE A COLUMN LIST
 <br/> <br/> 
STEP 7. CREATE A DATA FRAME
 <br/> <br/>
STEP 8. CREATE A FOR LOOP TO FILL DATAFRAME
 <br/> <br/>
STEP 9. EXPORT TO CSV AND TRY TO RUN IT
 <br/> <br/>
//Database connection
 <br/>
step 1. install MySQL Connector Python
pip install mysql-connector-python
 <br/> <br/> 
step 2. import MySQL connector 
 <br/> <br/>
step 3. Use the connect() method
 <br/> <br/>
step 4. Create a table
 <br/> <br/>
step 5. Define a SQL Insert query
 <br/> <br/>
step 6. Use the cursor() method:
Use the cursor() method of a MySQLConnection object to create a cursor object to perform various SQL operations.
 <br/> <br/>
step 7. Execute the insert query using execute() method
 <br/> <br/>
step 8. Close the cursor object and database connection object

//INSTRUTCTIONS HOW TO RUN DATABASE QUERY:-
<br/>
step 1 First download and install any local server such as xampp or wampp
<br/><br/>
step 2 Then start the local server of your system
<br/><br/>
step 3 Now add the localhost as a host
<br/><br/> 
step 4 Now enter your database details in code such as dbname, root and password.
<br/><br/>
step 5 That's it your database will be connected.
