import argparse
from configparser import ConfigParser

from main import mainAutomatic, mainManual


def parse():
    # this allows to insert the course full name (even with whitespaces) without need to add ""
    # the course name is inferred from the argument between two options (e.g. -c sistemi operativi -hl)
    class MyAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            setattr(namespace, self.dest, ' '.join(values))

    # COMMAND LINE ARGUMENTS
    parser = argparse.ArgumentParser(description='Your username and password are needed to perform log in')
    parser.add_argument("-U", "-u", "-username", "--username", default=None, type=str, help="The GOMP username")
    parser.add_argument("-P", "-p", "-password", "--password", default=None, type=str, help="The GOMP password")
    parser.add_argument("-C", "-c", "-course", "--course", default=None, type=str,
                        help="The course you want to reserve",
                        nargs="+", action=MyAction)
    parser.add_argument("-A", "-a", "-auto", "-automatic", "--automatic", action="store_true",
                        help="Run the program only in Automatic Course Reserve mode")
    parser.add_argument("-hl", "-headless", "--headless", action="store_true",
                        help="Don't open the browser for the whole task "
                             "(Headless mode)")
    parser.add_argument("-L", "-l", "-logging", "--logging", action="store_true",
                        help="Enable logging")
    parser.add_argument("-heroku", "--heroku", action="store_true",
                        help="Run the program in Heroku mode (see for login credentials in the "
                             "environment variables")
    parser.add_argument("-B", "-b", "-biblio", "-lib", "-library","--library", default=None, type=str,
                        help="The library hour to reserve. Insert only the start hour (ex. if the reservation time "
                             "slot is 14.00-15.00, only insert 14.00 or 14)")

    args = parser.parse_args()

    # CONFIG FILE (config.ini)
    config = ConfigParser(allow_no_value=True)
    config.read('config.ini')

    # If arguments given from console are NOT in their default state, use them for the execution. Otherwise, look for
    # them in the config file
    if args.username is not None:
        tempUsername = args.username
        if tempUsername is not None:
            usernamePassed = tempUsername.upper()
        else:
            usernamePassed = tempUsername
    else:
        tempUsername = config.get('main', 'username')
        if tempUsername is not None:
            usernamePassed = tempUsername.upper()
        else:
            usernamePassed = tempUsername

    if args.password is not None:
        passwordPassed = args.password
    else:
        passwordPassed = config.get('main', 'password')

    if args.course is not None:
        coursePassed = args.course
    else:
        coursePassed = config.get('main', 'course')

    if args.automatic is not False:
        autoModePassed = args.automatic
    else:
        autoModePassed = config.getboolean('main', 'autoMode')

    if args.headless is not False:
        headlessModePassed = args.headless
    else:
        headlessModePassed = config.getboolean('main', 'headless')

    if args.logging is not False:
        loggingModePassed = args.logging
    else:
        loggingModePassed = config.getboolean('main', 'logging')

    if args.heroku is not False:
        herokuModePassed = args.heroku
    else:
        herokuModePassed = config.getboolean('main', 'heroku')

    biblioHourPassed = args.library

    if autoModePassed is True:
        mainAutomatic(usernamePassed, passwordPassed, coursePassed, headlessModePassed,
                      herokuModePassed, loggingModePassed)
    else:
        mainManual(usernamePassed, passwordPassed, coursePassed, biblioHourPassed, headlessModePassed,
                   loggingModePassed, herokuModePassed)