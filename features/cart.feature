Feature: Cart Functionality

  Background:
    Given I am logged in as "standard_user"

  Scenario: Add and remove items from the cart
    When I add the first "3" items to the cart
    Then the cart badge should display "3"
    When I remove the first item from the cart
    Then the cart badge should display "2"