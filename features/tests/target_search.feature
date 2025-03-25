# Cr
# eated by rtbut at 3/24/2025
Feature: Target search test cases
  # Enter feature description here

  Scenario: User can search a product on Target
    Given Open Target main page
    When Search for tea
    Then Verify correct search results show

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: Sign In form opened for logged out user
    Given Open Target main page
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened