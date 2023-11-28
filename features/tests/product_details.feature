
  Feature: Tests for product page

  Scenario: User can select colors
    Given Open target product A-88062531 page
    Then Verify user can click through ['Black', 'Brown', 'Green', 'Cream - Out of Stock', 'Dark Gray - Out of Stock']


# product = A-89191279
#expected_colors = ['Black', 'Green', 'Oatmeal', 'Red']