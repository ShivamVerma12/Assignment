Feature: Test Login

    Scenario: user creating a new project
        Given user login with credentials
        When user enter the organization name
        And user clicks on skip
        And user clicks on skip
        And user clicks on skip
        And user clicks on skip
        And user starts a new project, enter the project title and click continue
        Then user verifies project name



    
