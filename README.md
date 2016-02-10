# coding_companion
An offline IDE for C++, although similar to ideone.com, but ensures that your code doesn't fall into wrong hands :p

###Installing
1. Clone the repository on your PC `git clone https://github.com/nikhil96sher/coding_companion/`
2. Go to coding_companion `cd coding_companion`
3. Run `./install.sh`

**Note** : If the `install.sh` command results in permission denied error, then first run `chmod 777 install.sh` and then try running `install.sh` again.

###Using
1. Go to the `coding_companion` directory
2. Run `./run.sh`

**Note** : If the `run.sh` command results in permission denied error, then first run `chmod 777 run.sh` and then try running `run.sh` again.

**Note** : If the `run.sh` command results in "The port is already in use", try running the server on another port by using `python manage.py runserver <Port-Number>`. For example : `python manage.py runserver 60002`

###Features
1. Compile and Run C++ code.
2. Create a template, so you need not type your #defines again and again.

  **How To** : Write your code, and save it in a file named `template`. You can modify it by overwriting it anytime.
3. Save code on your PC. (Although a temporary copy is always saved as a backup)

  **How To** : Clicking on `save` saves the code in the directory `codes/saved` in the app's directory. The temporary codes are saved in the directory `codes/tmp`

###Screenshots
![Alt text](https://github.com/nikhil96sher/coding_companion/blob/master/screenshots/run.png "Screenshot")

###Resources
1. Django (https://www.djangoproject.com/)
2. Ace Editor (https://github.com/ajaxorg/ace)
3. Bootstrap CSS (http://getbootstrap.com/css/)
4. jQuery (https://jquery.com/)

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/nikhil96sher/coding_companion/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
