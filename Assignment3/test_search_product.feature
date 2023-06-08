Feature: Test Search Script
  Scenario: user search on url and click on first result
    Given user open url
    When user search the product and click on first result
    Then user validate with product name
