Feature: Product Management

  Background:
    Given I am logged in as "standard_user"

  Scenario: Verify product data integrity
    Then all products should have a name and a price greater than 0

  Scenario: Verify product sorting by Price
    When I sort items by "Price (low to high)"
    Then the products should be sorted by price ascending
    When I sort items by "Price (high to low)"
    Then the products should be sorted by price descending