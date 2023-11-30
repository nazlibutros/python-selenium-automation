# Created by rtbut at 11/28/2023
Feature: Target Sign in Page Tests

  Scenario: User can see sign in form
    Given Open target main page
    When Click Sign in
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened