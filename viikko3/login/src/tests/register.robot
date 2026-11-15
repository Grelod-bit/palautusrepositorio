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
