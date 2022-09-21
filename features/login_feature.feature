Feature: Login Feature

  Scenario: Login with valid credentials
    Given Lunch chrome browser1
    When Open homepage1
    And Enter username "Admin" & password "admin123"
    And Click on login button
    Then user successfully login to the Dashboard page

  Scenario Outline: Login with Multiple valid and invalid credentials
    Given Lunch chrome browser1
    When Open homepage1
    And Enter username <username> & password <password>
    And Click on login button
    Then user successfully login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin1   | admin    |
      | admin1   | admin1   |
      | admin0   | admin123 |