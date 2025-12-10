Feature: Checkout Process

  Background:
    Given I am logged in as "standard_user"

  Scenario: Successful Checkout with data from CSV
    Given I have "2" items in my cart
    And I proceed to the checkout page
    When I fill checkout information from "checkout_data.csv"
    Then the Item total plus Tax should equal the Total amount
    When I finish the order
    Then I should see the order completion message "Thank you for your order!"

#  Scenario: Negative Test - Checkout with empty cart
#    Given my cart is empty
#    When I try to navigate to checkout
#    Then the system should prevent checkout or show an error