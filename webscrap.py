

import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
from mysql.connector import Error

url = 'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=78&Tx_State=MH&Tx_District=14&Tx_Market=0&DateFrom=20-Oct-2021&DateTo=21-Oct-2021&Fr_Date=20-Oct-2021&To_Date=21-Oct-2021&Tx_Trend=0&Tx_CommodityHead=Tomato&Tx_StateHead=Maharashtra&Tx_DistrictHead=Pune&Tx_MarketHead=--Select--'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup

commodity_table = soup.find('table', id='cphBody_GridPriceData')
commodity_table

headers = []
for i in commodity_table.find_all('th'):
    title = i.text
    headers.append(title)

headers[9] = 'price data'

mydata = pd.DataFrame(columns=headers)
for j in commodity_table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

mydata.to_csv('commodity.csv', index=False)
mydata2 = pd.read_csv('commodity.csv')
mydata2.head()

try:
    connection = mysql.connector.connect(host='',
                                         database='Commodities',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        mySql_Create_Table_Query = """CREATE TABLE Commodity ( 
                             SrNo int(10) NOT NULL,
                             Commodity_name varchar(250) NOT NULL,
                             District_Name varchar(250) NOT NULL,
                             Market_Name varchar(250) NOT NULL,
                             Variety varchar(250) NOT NULL,
                             Grade varchar(250) NOT NULL,
                             Min_Price float NOT NULL,
                             Max_Price float NOT NULL,
                             Model_Price float NOT NULL,
                             Price_Date date NOT NULL,
                             PRIMARY KEY (SrNo)) """

        for i in mydata:
            mySql_insert_query = """INSERT INTO Commodity (SrNo, Commodity_name, District_Name, Market_Name, Variety, Grade,
                                  Min_Price, Max_Price, Model_Price, Price_Date
                                ) 
                           VALUES 
                           (i[SrNo], i[Commodity_name] , i[District_Name], i[District_Name], i[Market_Name], i[Variety], i[Grade], i[Min_Price], i[Max_Price], i[Model_Price]
                           , i[Price_Date]) """
            print(i)

        cursor = connection.cursor()
        result = cursor.execute(mySql_Create_Table_Query)

        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")