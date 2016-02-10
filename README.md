# coding_companion
An offline IDE for C++, although similar to ideone.com, but ensures that your code doesn't fall into wrong hands :p

###Installing
1. Clone the repository on your PC `git clone https://github.com/nikhil96sher/coding_companion/`
2. Install Django (https://docs.djangoproject.com/en/1.9/topics/install/)
3. Make Migrations `python manage.py makemigrations`
4. Apply Migrations `python manage.py migrate`
3. Run server using `python manage.py runserver`
4. Go to the Url `127.0.0.1:8000/ccr/` and enjoy

**Note** : If the run server command results in an error - "The port is already in use", try running the server on another port using `python manage.py runserver <Port-Number>` . For example : `python manage.py runserver 5000`

###Features Completed
1. Compile and Run C++ code.
2. Create a template, so you need not type your #defines again and again.
3. Save code on your PC. (Although a temporary copy is always saved as a backup)

###Screenshots
![Alt text](https://github.com/nikhil96sher/coding_companion/blob/master/screenshots/compile_error.png "Screenshot")

###Resources
1. Django (https://www.djangoproject.com/)
2. Ace Editor (https://github.com/ajaxorg/ace)
3. Bootstrap CSS (http://getbootstrap.com/css/)
4. jQuery (https://jquery.com/)

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/nikhil96sher/coding_companion/trend.png)](https://bitdeli.com/free "Bitdeli Badge")