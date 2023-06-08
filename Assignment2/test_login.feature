Feature: Test Login
  Scenario: User login with login credentials
    Given User login with credentials
    When User enter the organization name
    And User clicks on skip
    And User clicks on skip
    And User clicks on skip
    And User clicks on skip
    And User starts a new project, enter the project title and click continue
    Then User verifies project name