## Cr
## eated by rtbut at 3/24/2025
#Feature: Target search test cases
#  # Enter feature description here
#
#  Scenario: User can search a product on Target
#    Given Open Target main page
#    When Search for tea
#    Then Verify correct search results show
#
##  Scenario: 'Your cart is empty' message is shown for empty cart
##    Given Open Target main page
##    When Click on Cart icon
##    Then Verify “Your cart is empty” message is shown
##
##  Scenario: Sign In form opened for logged out user
##    Given Open Target main page
##    When Click Sign In
##    And From right side navigation menu, click Sign In
##    Then Verify Sign In form opened
  Feature: Target search test cases

  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search results shown for <expected_text>
    Examples:
    |search_word  |expected_text  |
    |tea          |tea            |
    |iPhone       |iPhone         |
    |dress        |dress          |


  Scenario: Search and add a product to Target cart
    Given Open target main page
    When Search for "plates"
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open Cart Page
    Then Verify cart has 1 item(s)
    Then Verify cart has correct product
