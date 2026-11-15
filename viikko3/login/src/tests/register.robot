*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Character
    Set Username  kalle
    Set Password  kalle#abc
    Confirm Password  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Only Lowercase Letters
    Set Username  kalle
    Set Password  kallekalle
    Confirm Password  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one number or special character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  kalle
    Set Password  KalleKalle
    Confirm Password  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one number or special character

Register With Different Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Confirm Password  kalle456
    Click  button >> text=Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Too Short Username And Valid Password
    Set Username  ok
    Set Password  kalle123
    Confirm Password  kalle123
    Click  button >> text=Register
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  Kalle
    Set Password  ok
    Confirm Password  ok
    Click  button >> text=Register
    Register Should Fail With Message  Password is too short

Register With Username That Is Already In Use
    Set Username  test
    Set Password  test1234
    Confirm Password  test1234
    Click  button >> text=Register
    Register Should Fail With Message  User with username test already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  test  test1234
    Go To Register Page
