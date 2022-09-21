
Feature: Login Feature
  Scenario: Login with valid credentials
    Given Lunch chrome browser
    When Open homepage
    And Enter username "Admin" & password "admin123"
    And Click on login button
    Then user successfully login to the Dashboard page

