Feature: Test Countdown Timer

  @runner.continue_after_failed_step
  Scenario Outline: : Verify that the countdown actually happens and the remaining time decreases in one-second increment
    Given User launch e.ggtimer website in a browser and enter <Time> in "Enter a time" text box
    When User click on start
    Then Countdown timer should start with time decreasing
    And Decrement should be equal to one second increment


    Examples:
      | Time  |
      |  25   |

