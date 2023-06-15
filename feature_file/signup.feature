Feature: User Signup
  Scenario: User register new User
    Given User open desired url
    When User enter credentials and click Signup
    Then User verifies signin or not
