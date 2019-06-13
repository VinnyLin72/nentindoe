x1# Nentindoe
### Vincent Lin(PM), Yin On Chan, Mohtasim Howlader, Zane Wang

## Description
A website where users will be able to log in using their emails to create images, from scratch or drawing on existing images, and post them publicly. Users will be able draw on a canvas using a variety of “tools” and colors, users will be able to import images they wish to edit onto the web app, draw on it, and save or upload the new image. Users will be able to create groups to privately share images amongst friends.

## Video Demo
https://youtu.be/GE45Qb4TNws

## Dependencies
- Flask==1.0.2
  Framework
- Jinja2==2.10.1
  Templating

## Launch Codes
### Local Host
1. Open a terminal session.
2. Create your own environment by typing (name is a placeholder for the name of the virtual environment of your choosing):
```
$ python3 -m venv <name>
```
3. Activate the virtual environment by typing ```$ . <name>/bin/activate``` in the terminal and make sure it is running python3 by typing ```(venv)$ python --version``` in the terminal.
4. Clone this repository. If you have already cloned this repository, skip this step. To clone this repo, open a terminal session and navigate to the directory you want for this repository to located in. Then clone using SSH by typing ```(venv)$ git clone git@github.com:VinnyLin72/nentindoe.git``` or clone using HTTPS by typing ```(venv)$ git clone https://github.com/VinnyLin72/nentindoe.git``` in the terminal.
5. Install all necessary requirements to the virtual environment by typing ```pip install -r requirements.txt``` in the terminal.
6. Navigate to our repository by typing ```$ cd nentindoe/``` in the terminal.
7. Run the python file by typing ```(venv)$ python <path>/__init__.py``` in the terminal. This should appear in the terminal after running the python file.   
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 248-748-502
```
8. Open a web browser and navigate to the link http://127.0.0.1:5000/.

### Apache2
1. ssh into your droplet through a user using `$ ssh <user>@<ip address>`
2. Go to the directory /var/www through `$ cd /var/www/`
3. Clone the repo and name the directory your chosen appname by running
  `$ sudo git clone https://github.com/VinnyLin72/nentindoe.git `
4. Move the .conf file to the /etc/apache2/sites-available directory by running the command
  `$ sudo mv /var/www/nentindoe/nentindoe.conf /etc/apache2/sites-available`
5. Go into the first directory named scribble and run both
    1. `$ sudo chgrp -R www-data nentindoe`
    2. `$ sudo chmod -R g+w nentindoe`
6. Install virtualenv by running `$ pip3 install virtualenv`
   * Make a venv by running `$ python3 -m venv VENV_NAME`
   * Activate it by running `$ . ~/path_to_venv/VENV_NAME/bin/activate`
   * Deactivate it by running `$ deactivate`
7. Activate your virtual environment
8. Go into the second directory named scribble and run `$ pip install -r requirements.txt`
9. After running everything above, run `$ sudo service apache2 restart`
   * Run this anytime you make changes as well
10. Go to your ip address to view your app
