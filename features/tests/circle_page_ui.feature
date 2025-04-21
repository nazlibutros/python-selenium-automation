# Created by rtbut at 4/20/2025
Feature:  Circle page UI test

  Scenario: Verify there are at least 10 benefit cells
    Given Open target circle page
    Then Verify at least 10 benefit links shown
