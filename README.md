# Procurement-Bot
finderBuddy :: An ultimate aide for procurement 

Instructions:
1. In the 'Procurement Bot' zip folder, there are two folders namely 'Procurement Bot API' and 'Procurement Bot'

2. Make sure, python is installed already. if not go to below link:
	https://www.tutorialspoint.com/python/python_environment.htm

3. Then install Django using below link:
	https://www.djangoproject.com/download/

4. Paste all the folders of Procurement Bot API folder to below location:
	"C:\Python27\Lib\site-packages"

5. Open 'Procurement Bot' folder, then there open CMD by holding Shift key + Right Click.

5. Type "python manage.py runserver" (without quotes) and press enter. It will start Django server.

6. Open any browser and enter URL "http://127.0.0.1:8000/" (without quotes). Voila !! Web App starts now.

7. Download all necessary packages of python if required by finderBuddy.

Note:
There are some of the required packages present in API folder. Download all the remaining packages using pip install.

For database purpose, we use MongoDB and SQLite.
To setup these database go to below links:

MongoDB : https://www.tutorialspoint.com/mongodb/mongodb_environment.htm

SQLite:
https://www.tutorialspoint.com/sqlite/sqlite_installation.htm

Sample database of SQLite is present in finderBuddy folder.
item_list = List of Items available in inventory
order_list = List of order placed by user
