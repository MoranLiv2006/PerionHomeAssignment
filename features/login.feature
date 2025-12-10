Feature: Login Functionality

  Scenario Outline: Login with valid and invalid users
    Given I am on the login page
    When I login with user "<user_type>"
    Then I should see the "<expected_result>"

    Examples:
      | user_type               | expected_result                                    |
      | standard_user           | inventory page                                     |
      | locked_out_user         | Epic sadface: Sorry, this user has been locked out.|
      | problem_user            | inventory page                                     |
      | performance_glitch_user | inventory page                                     |
      | error_user              | inventory page                                     |
      | visual_user             | inventory page                                     |