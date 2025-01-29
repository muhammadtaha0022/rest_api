# what is api
* application programming interface
* API stands for Application Programming Interface. It's a set of instructions that allow different software programs to communicate with each other. 
# Rest api 
* A REST API allows applications to communicate by exchanging data over HTTP using methods like GET, POST, PUT, and DELETE. It adheres to REST principles, focusing on statelessness and resource-based URLs. Data is typically exchanged in formats like JSON or XML.
# next
* install python
* install django
* install mysql
* install mysql wordbench
* pip install mysqlclient 
# lecture #7 
* change data base in setting 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quickstart',
        'HOST': 'localhost',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':'#taha'
    }
}
```
* pip install mysqlclient
* migrate
* createsuperuser
# lecture #8
* pip install djangorestframework