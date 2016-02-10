echo "INSTALLING PYTHON"
sudo apt-get install python
echo "INSTALLING g++"
sudo apt-get install g++
echo "INSTALLING python-pip"
sudo apt-get install python-pip
echo "INSTALLING Django"
sudo pip install Django==1.8.1
python manage.py makemigrations
python manage.py migrate
echo "Successfully Installed coding_companion."