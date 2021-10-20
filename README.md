# R3serve
A program to reserve one or more lessons in the Roma Tre University [student website](https://gomp.uniroma3.it/Login?ReturnUrl=%2f).


## Installation
* Clone this project (`git clone https://github.com/drew458/PS5-scraper.git`) or [download it](https://github.com/drew458/PS5-scraper/archive/refs/heads/master.zip)
* The script uses ChromeDriver, so [download](https://chromedriver.chromium.org/downloads) and place it into the folder 
* With [Python 3.8](https://www.python.org/downloads/release/python-380/) installed on your computer, install the external
modules by running in Command Line Interface:
  * `pip install -r requirements.txt`

To run the script, `cd` into the folder and `python3 main.py`.

## Options
The program takes the following parameters when launching:

    -h, --help                   Print the parameters list

    -u, -U, --username           The username of your GOMP account

    -p, -P, --password           The password of your GOMP account

    -c, -C, -course, --course [COURSENAME]
                                 The course you want to reserve
    
    -A, -a, -auto, -automatic, --automatic
                                 Run the program only in Automatic Course Reserve mode
    
    -hl, -H, -headless, --headless
                                 Don't open the browser for the whole task(Headless mode)
    
    -heroku, --heroku            Run the program in Heroku mode 
                                 (see for login credentials in the environment variables)

Example of launching:
```
python main.py -u YOURUSERNAME -p YOURPASSWORD -c Fondamenti di Automatica -hl
```


## Cloud deployment

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

The script is ready for deployment on Heroku, which is what I use to run it continuously on the cloud. The free tier on 
Heroku perfectly fits. In this case the username and password must go into the virtual environment variables 
(see the settings page on Heroku's dashboard).