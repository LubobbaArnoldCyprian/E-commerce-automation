# DealX-Automation-Assesment


 # **Page Object Model using Selenium (POM)**

Page Object model is an object design pattern in Selenium, where web pages are represented as classes, and the various elements on the page are defined as variables in the class and all possible user interactions can then be implemented as methods in the class. 

  

 ## **Why Page Object model?**

* It is useful in reducing code duplication and improves test case maintenance. 

* Helps with reusing code 

* It eases readability and reliability of scripts 

 ### **Initial Setup:**
To test the project locally:
* Clone the project on your local machine - git clone 

* open IDE >File >Open(directory of the project).

* Install the requirements.txt file by going to the terminal and run command pip install -r requirements.txt


 ### **Running Tests:**
 To run TC1, TC2 & TC3 run the command below.
 * python -m pytest -v -s .\test_cases\test_search.py --browser chrome
 
To run TC4
* python -m pytest -v -s .\test_cases\test_signin.py --browser chrome

To run TC5
* python -m pytest -v -s .\test_cases\test_cart.py --browser chrome


To run TC6
 * python -m pytest -v -s .\test_cases\test_categories.py --browser chrome



