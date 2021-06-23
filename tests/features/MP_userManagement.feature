@multitenant_platform @user_management @login_page
Feature: User Management
  Mark Smart User Management

  @login_test
  Scenario: User logs into the application with valid credentials
    Given User is on Mark Smart login page
    When User wants to log in
    And Enters email and password
    Then Clicks on Sign in button
    And Is directed to the IA Smart Platform Page of the application

  @login_test
  Scenario: User try to log into the application using invalid credentials
    Given User is on Mark Smart login page
    When User wants to log in
    And Enters invalid email and password
    Then Clicks on Sign in button
    And User validates if "Username or password is incorrect" error message pops up

  @login_test
  Scenario: User checks if Sign in button is disabled/enabled when the useremail and password are not entered and entered respectively
    Given User is on Mark Smart login page
    When User does not enter the email and password
    Then User checks that the Sign in Button is disabled
    When Enters email and password
    Then checks that the Sign in Button is enabled

  @login_test
  Scenario: User checks the functionality of forgot your password link when entering valid useremail
    Given User is on Mark Smart login page
    When User does not enter the email and password
    Then User checks that the forgot your password link is disabled
    When User enters only the email which is valid and forgets the password
    Then User checks that the forgot your password link is enabled
    And User clicks on Forgot your password link and sends verification email
    Then User validates if "Password reset link sent to the registered email successfully!" success message pops up

  @login_test
  Scenario: User checks the functionality of forgot your password link when entering invalid useremail
    Given User is on Mark Smart login page
    When User does not enter the email and password
    Then User checks that the forgot your password link is disabled
    When User enters only the email which is invalid and forgets the password
    Then User checks that the forgot your password link is enabled
    And User clicks on Forgot your password link and sends verification email
    Then User validates if "There is no user record corresponding to this identifier. The user may have been deleted." error message pops up














    #Given User checks the table
     # | InputFields | ValueToBeEntered |
     # | UserName    | admin            |
     # | Password    | Abcd123          |
     # | Result      | Pass             |