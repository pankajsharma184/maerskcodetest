import math
from behave import *
from main.SeleniumFunctions import SeleniumFunctions
from main.SystemFunction import SystemFunction
from hamcrest import *

@given(u'User launch e.ggtimer website in a browser and enter {Time:d} in "Enter a time" text box')
def step_impl(context, Time):
    context.Time = Time
    if (context.Time >= 21):
        context.selfunc = SeleniumFunctions(context.Time)
        context.selfunc.launch_browser()
    else:
        context.scenario.skip(reason='Incorrect Time Value')
        print("Hey! We are testing countdown timer using Browser Automation tool(which takes time to load) and in "
              "order to get accurate results, Please enter 21 or more")

@when(u'User click on start')
def step_impl(context):
    context.selfunc.browser_actions()

@then(u'Countdown timer should start with time decreasing')
def step_impl(context):
    context.sf = SystemFunction()
    context.selfunc.browser_first_wait()
    context.capture_start = context.sf.start_system_timer()
    context.selfunc.browser_second_wait()
    context.capture_stop = context.sf.stop_system_timer()

@then(u'Decrement should be equal to one second increment')
def step_impl(context):
    context.time_difference = 0
    if context.capture_start > context.capture_stop:
        context.time_difference = ((60 - context.capture_start) + context.capture_stop)
    elif context.capture_stop > context.capture_start:
        context.time_difference = (context.capture_stop - context.capture_start)
    elif context.capture_start == context.capture_stop:
        context.time_difference = 60
    context.time_difference = round(context.time_difference, 3)

    # I have considered 15 seconds window to capture system time from Website UI Timer element 20 Seconds - 5 Seconds.
    # 15 Seconds capture is good time to verify if the countdown timer is working as expected.
    # Hence 15 becomes our expected result.
    context.expected_time = 15

    if (context.time_difference > 14 and context.time_difference < 15):
        context.time_difference = math.ceil(context.time_difference)
        assert_that(context.time_difference, is_(context.expected_time))
    elif (context.time_difference > 15 and context.time_difference < 16):
        context.time_difference = math.floor(context.time_difference)
        assert_that(context.time_difference, is_(context.expected_time))
    else:
        print("Seconds Increment in System time does not match with Seconds decrement on Countdown timer")
    context.selfunc.close_browser()
