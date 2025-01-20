# Top50_Crypto
The objective of this project is to fetch live cryptocurrency data for the top 50 cryptocurrencies, store it in a MySQL database, and analyze it by connecting the database to Power BI. 
The data will be dynamically updated and visualized in Power BI to present live cryptocurrency prices, market capitalization, 24-hour price changes, and trading volumes.

**Follow these steps to get the data:**

 **Step 1: Prepare Your MySQL Database**
 1. Ensure the MySQL Server is Running
   - Test your connection by querying the database through a client like MySQL Workbench.
 2. Note Connection Details:
   - **Host**: (e.g., `localhost` or an IP address)
   - **Port**: Default is `3306`
   - **Database Name**: 'Provided in python script'
   - **Username**: (e.g., `root`)
   - **Password**: (your database password)
     
**step 2:Download and Install MySQL ODBC Driver**:
 1. Go to the official MySQL website: [MySQL ODBC Connector](https://dev.mysql.com/downloads/connector/odbc/).
 2. Download the driver that matches your system architecture:
   - **32-bit** or **64-bit**, depending on your Power BI installation.

**Step 3: Open Power BI**
 1. Launch Power BI Desktop.

**Step 4: Connect to MySQL**
 1.Enter the Server Details
 2.Refresh Data:
   - Power BI service can be configured to automatically refresh the data periodically to fetch the latest updates from your MySQL database.
     (In our case, a).we run the python script in jupyter notebook.
                   b).Once refresh the data in Power BI to get the live and updated data.)
     
     


 

