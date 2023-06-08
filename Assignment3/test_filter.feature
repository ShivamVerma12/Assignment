Feature: Test Filter Script
  Scenario: user search on url and click on first result
    Given user open url
    When user search the product, apply filter and click on first result
    Then user validate with filter