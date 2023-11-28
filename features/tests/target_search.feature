Feature: Search tests

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee
    And Verify coffee in search result url

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea
    And Verify tea in search result url

  Scenario: User can see cart is empty message
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty message shown

  Scenario: User can see sign in form
    Given Open target main page
    When Click Sign in
    Then From right side navigation menu, click Sign In
    Then Verify Sign In form opened

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search worked for <expected_product>
    And Verify <expected_url> in search result url
    Examples:
    |product            |expected_product           |expected_url     |
    |coffee             |coffee                     |coffee           |
    |tea                |tea                        |tea              |
    |mug                |mug                        |mug              |
    |christmas lights   |christmas lights           |christmas+lights |

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for AirPods (3rd Generation)
    And Click on Add to Cart button
    And Store product name
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify every product has a name and an image
