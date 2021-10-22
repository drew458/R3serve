# R3serve
A program to reserve one or more lesson in the  [student website (GOMP)](https://gomp.uniroma3.it/Login?ReturnUrl=%2f).


## Installation
* Clone this project via command line (`git clone https://github.com/drew458/PS5-scraper.git`) or [download it](https://github.com/drew458/PS5-scraper/archive/refs/heads/master.zip).
* With [Python 3.8](https://www.python.org/downloads/release/python-380/) (or higher) installed on your computer, install the external
modules by running in Command Line Interface:
  * `pip install -r requirements.txt`

To run the script, open Command Line Interface in the folder you downloaded or cloned and run `python main.py`.

## Options
The program accepts the following parameters when launching:

    -h, --help                   
                                 Print the parameters list

    -U, -u, --username           
                                 The username of your GOMP account                                      [default: None]

    -P, -p, --password           
                                 The password of your GOMP account                                      [default: None]

    -C, -c, -course, --course [COURSENAME]
                                 The course you want to reserve                                         [default: None]
    
    -A, -a, -auto, -automatic, --automatic
                                 Run the program only in Automatic Course Reserve mode                  [default: False]
    
    -hl, -headless, --headless   
                                 Don't open the browser for the whole task(Headless mode)               [default: False]

    -L, -l, -logging, --logging
                                 Enable logging                                                         [default: False]
    
    -heroku, --heroku            
                                 Run the program in Heroku mode 
                                 (see for login credentials in the environment variables)               [default: False]

Example of launching:
```
python main.py -u YOURUSERNAME -p YOURPASSWORD -c Fondamenti di Automatica -hl
```


## Cloud deployment

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

The script is ready for deployment on Heroku, which is what I use to run it continuously on the cloud. The free tier perfectly fits. In this case the username and password must go into the virtual environment variables (see the settings page on Heroku's dashboard).
