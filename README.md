# gudlift-registration

1.  Why

    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2.  Getting Started

    This project uses the following technologies:

    - Python v3.x+

    - [Flask](https://flask.palletsprojects.com/en/1.1.x/)

      Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need.

    - [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

      This ensures you'll be able to install the correct packages without interfering with Python on your machine.

      Before you begin, please ensure you have this installed globally.

3.  Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4.  Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:

    - competitions.json - list of competitions
    - clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5.  Testing

    To ensure the reliability and efficiency of the application, comprehensive testing for coverage and performance is essential. To test the app's coverage and performance, follow these instructions:

    <ins>**Coverage**</ins>

    We use [Coverage](https://coverage.readthedocs.io/en/7.4.2/) to assess the extent of code coverage by tests.

    At the root of the application, type <code>coverage run -m pytest</code> then <code>coverage report</code> to view the coverage report in the logs. You can generate an HTML page with detailed coverage information by typing <code>coverage html</code> to generate an html page with the coverage details.

    <ins>**Performance**</ins>

    We use [Locust](https://locust.io) for load testing and evaluating the application's performance under various conditions.

    **Please, make sure that the application is already running beforehand!**

    At the root of the application, type <code>locust -f tests/performance_tests/locustfile.py</code> then access the Locust interface to launch the performance test at the following URL <code>http://0.0.0.0:8089</code>. Enter the following configuration:

    ```
    Number of users : 1
    Spawn Rate : 1
    Host : http://127.0.0.1:5000
    ```

    You can then click on "START SWARM" to begin the performance tests.
    Don't forget to click on **STOP** to halt the swarm after testing.
