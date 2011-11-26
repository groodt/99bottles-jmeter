Code from the [Mind Candy tech blog post](http://tech.mindcandy.com/2011/11/99-bottles-of-jmeter-on-the-wall/) describing JMeter scripting.

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

    ./server.py
* Open the JMeter Test Plan in JMeter. File -> Open -> Test Plan.jmx
* Start the Test Plan in JMeter. Run -> Start
* You should see the "99 Bottles" song printed out on your console.
<pre>
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    9 bottles of mead on the wall. Date=1320485924124 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    8 bottles of cider on the wall. Date=1320485924127 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    7 bottles of wine on the wall. Date=1320485924131 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    6 bottles of beer on the wall. Date=1320485924136 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    5 bottles of cider on the wall. Date=1320485924139 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    4 bottles of mead on the wall. Date=1320485924142 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    3 bottles of beer on the wall. Date=1320485924146 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    2 bottles of wine on the wall. Date=1320485924149 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    1 bottle of wine on the wall. Date=1320485924152 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
    0 bottles of beer on the wall. Date=1320485924156 Thread=3
    127.0.0.1 - - [05/Nov/2011:09:38:44 +0100] "POST /bottle HTTP/1.1" 200 7 "-" "Java/1.6.0_26"
</pre>
