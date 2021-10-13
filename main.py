import ClassNames, LoginWithCookies, Login
import Worker


def main():
    # Perform the log in
    driver = Login.login()

    # Insert the class
    selected_class = ClassNames.insertClass()

    # Reserve the lesson
    Worker.reserve(driver, selected_class)


# Press the green button on the left side to run the script
if __name__ == '__main__':
    main()
