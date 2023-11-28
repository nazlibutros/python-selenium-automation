# Created by rtbut at 11/9/2023
Feature: Main Page UI Tests

  Scenario: Header has correct amount of links
  Given Open target main page
  Then  Verify header is present
  And Verify header has 5 links

