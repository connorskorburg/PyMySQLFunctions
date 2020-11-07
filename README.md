(for Mac/Linux)

1. Set Up MySQL Workbench and make sure you have a server initialized connection to MySQL
  server: https://dev.mysql.com/downloads/mysql/
  workbench: https://dev.mysql.com/downloads/workbench/
2. Create a new virtual environment (python3 -m venv venv)
3. Activate the Environment (source venv/bin/activate)
4. Install Flask and PyMySQL with PIP (pip3 install flask pymysql)
5. updated the calling of MySQLConnection('SSDB') to your databse schema name
6. update the mysqlconnection.py file with your database password
7. run python3 app.py to start server and go to http://localhost:5000 in your browser
8. refresh the browser and check your terminal for queries and data from MySQL Database 