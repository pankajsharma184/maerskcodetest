# Maersk Code Test

# Highlights
As per requirement our focus is to test the countdown timer on the given website and make sure that remaining time decreases in one-second increments.

So as expected behaviour, I have taken system time as point of reference to validate the results.

I have only considered seconds to verify the countdown timer and have changed nano seconds to nearest higher/lower value. This is because in UI automation, we have to consider some nano seconds latency in opening browser, launching website and navigating page.

This is not common in UI automation but since we are testing "Time" here so these considerations are mandatory. 

I have considered 15 seconds window to capture system time and Website UI Countdown Timer.
15 Seconds capture is good time to verify if the countdown timer is working as expected.
Hence 15 becomes our expected result.

Tools used:
1. Selenium for browser automation
2. Python as programming language
3. BEHAVE(python based BDD)

# Improvements
As prototype, I have developed framework with one test scenario as per requirement and the same can be enhanced to work with different test input data.

There are many different type of input data (For ex: New Year Day, etc) which can be added as testsing scenarios.


# Instructions to build and run

1. Install and configure Python version 3+ on the system. Refer: https://realpython.com/installing-python/

2. Install Google Chrome latest version (87).

2. Clone the project and navigate to project folder. Open command prompt on this path (<SOME_PATH>\maerskcodetest>)

3. Create python virtual environment with command : python -m venv <name_of_virtualenv> OR python3 -m venv <name_of_virtualenv> depending on OS configuration. For more information refer: https://www.geeksforgeeks.org/python-virtual-environment/

4. Once created run command to activate python virtual environment using command:  <name_of_virtualenv>\Scripts\activate (Windows) , <name_of_virtualenv>/bin/activate (Linux) or Source <name_of_virtualenv>/bin/activate (MAC). Refer above link for more information.

5. Make sure the once its activated the command prompt should look like "(virtualenv) <SOME_PATH>\maerskcodetest>" 

6. Run Command pip3 install -r requirements.txt to install all the dependency required to run the test.

7. Once all above steps done Run: <SOME_PATH>\maerskcodetest>behave -f plain and it should start executing test case.

Once Sucessfully test execution command prompt should show :

Feature: Test Countdown Timer
  Scenario Outline: : Verify that the countdown actually happens and the remaining time decreases in one-second increment -- @1.1

    Given User launch e.ggtimer website in a browser and enter 25 in "Enter a time" text box ... passed
    When User click on start ... passed
    Then Countdown timer should start with time decreasing ... passed
    And Decrement should be equal to one second increment ... passed

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
4 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m31.658s
 
Note1: If the above steps do not work as expected. Download Pycharm IDE Community edition and import this project. Once it completes all the requirement project can be easily executed with the same "behave" command from Pycharm Terminal.

Note2: There are chances of getting chromedriver.exe missing path error depending on the OS and the same should be fixed by configuring System Environment Variable. Refer: https://chromedriver.chromium.org/getting-started

# Platform limitations

I have made this project in Windows 10 using Pycharm IDE and have not tested on other platforms like Mac or Linux.


# Dependencies Required
All required dependencies are mentioned in the requirements.txt and if they are installed properly there wont be any need of other dependencies.


