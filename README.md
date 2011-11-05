# Purpose
A simple example showing how to use scripting inside JMeter for more complex HTTP request generation.

# Setup
* Make sure you have JMeter installed. This example works with JMeter 2.5.

    ```brew install jmeter```
* Make sure you have pip installed on your platform

    ```sudo easy_install pip```
* Create a virtualenv for Python. Optional, but recommended step. See [virtualenv](http://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](http://www.doughellmann.com/docs/virtualenvwrapper/) for info on how to install these tools.
   
    ```mkvirtualenv 99bottles --no-site-packages```
* Install the dependencies

        cd 99bottles-jmeter
        pip install --requirement=requirements.txt

# Running the example
* Start the server

    ```./server.py```
* Open the JMeter Test Plan in JMeter
    File -> Open -> Test Plan.jmx
* Start the Test Plan in JMeter
    Run -> Start
* You should see the "99 Bottles" song printed out on your console
