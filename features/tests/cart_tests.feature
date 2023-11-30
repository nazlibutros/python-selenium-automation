# Created by rtbut at 11/27/2023
Feature: Target Cart Page Tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for AirPods (3rd Generation)
    And Click on Add to Cart button
    And Store product name
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product