# Created by rtbut at 11/14/2023
Feature: Circle Page UI Tests

  Scenario: User can verify circle page box count
    Given Open target main page
    When Click Circle
    Then Verify there are 5 benefit boxes
