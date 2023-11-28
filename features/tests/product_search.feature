Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown

#  Scenario: User can see cart is empty message
#    Given Open target main page
#    When Click on cart icon
#    Then Verify cart is empty message shown