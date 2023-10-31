Feature: Search tests

  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
    Then Verify search worked
    And Verify search result url

  Scenario: User can see cart is empty message
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty message shown

  Scenario: User can see sign in form
    Given Open target main page
    When Click Sign in
    Then From right side navigation menu, click Sign In
    Then Verify Sign In form opened
