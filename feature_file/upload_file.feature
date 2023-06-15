Feature: Test Upload File
  Scenario: User signup and login with credentials, create a new project and upload a file
    Given User signup a new user
    When User enter the organization name
    And User clicks on skip
    And User clicks on skip
    And User clicks on skip
    And User clicks on skip
    And User starts a new project, enter the project title, select upload file and click continue
    And User select the file, click on upload and sync
    Then User verifies file name