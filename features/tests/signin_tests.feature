# Created by rtbut at 11/28/2023
Feature: Target Sign in Page Tests

  Scenario: User can see sign in form
    Given Open target main page
    When Click Sign in
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened


  Scenario: User can open and close Terms and Conditions from sign in page
     Given Open sign in page
     When Store original windows
     Then Click on Target terms and conditions link
     And Switch to the newly opened window
     Then Verify Terms and Conditions page is opened
     And User can close new window and switch back to original