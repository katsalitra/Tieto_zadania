*** Settings ***

Documentation    Log in to user’s email account
Library  SeleniumLibrary
Test Setup    begin web test
Test Teardown    end web test


*** Variables ***

${BROWSER}     chrome
${URL}    https://poczta.wp.pl

${validUsername} =    1anna1_zi@wp.pl
${validPassword} =    Jamnik123!

${invalidUsername} =    xxxxx@wp.pl
${invalidPassword} =    Jajko123!

${emptyUserName}=
${emptyUserPassword}=

${validUsernameUpper} =     1ANNA1_ZI@WP.PL
${validPasswordUpper} =    JAMNIK123!


*** Test Cases ***

User log in with valid Credentials
    Assert wp Mail - login site
    input valid username/email
    input valid password
    click on 'zaloguj się' button
    assert valid - check if user is on proper site


User try to log in with invalid username
    Assert wp Mail - login site
    input invalid username/email
    input valid password
    click on 'zaloguj się' button
    assert invalid


User try to log in with invalid password
    assert wp Mail - login site
    input valid username/email
    input invalid password
    click on 'zaloguj się' button
    assert invalid


User try to log in with invalid password and invalid username
    assert wp Mail - login site
    input invalid username/email
    input invalid password
    click on 'zaloguj się' button
    assert invalid


User try to log in with leaving username field empty
    assert wp Mail - login site
    input empty username/email field
    input valid password
    click on 'zaloguj się' button
    assert wp Mail - login site


User try to log in with leaving password field empty
    assert wp Mail - login site
    input valid username/email
    input empty password field
    click on 'zaloguj się' button
    assert wp Mail - login site


User try to log in with leaving both fields-username and password- empty
    assert wp Mail - login site
    input empty username/email field
    input empty password field
    click on 'zaloguj się' button
    assert wp Mail - login site


User try to log in with valid username written in capital letters
    Assert wp Mail - login site
    input valid username/email uppercase
    input valid password
    click on 'zaloguj się' button
    assert valid - check if user is on proper site

User try to log in with valid password written in capital letters
    assert wp Mail - login site
    input valid username/email
    input valid password uppercase
    click on 'zaloguj się' button
    assert invalid


*** Keywords ***
begin web test
    open browser    ${URL}   ${BROWSER}
assert wp Mail - login site
    title should be    Poczta - Najlepsza Poczta, największe załączniki - WP
input valid username/email
    input text    xpath = //*[@id="login"]    ${validUsername}


input valid username/email uppercase
    input text    xpath = //*[@id="login"]    ${validUsernameUpper}

input valid password uppercase
    input password    xpath = //*[@id="password"]     ${validPasswordUpper}


input valid password
    input password    xpath = //*[@id="password"]     ${validPassword}
assert valid - check if user is on proper site
    page should contain    Odebrane
input invalid username/email
    input text    xpath = //*[@id="login"]    ${invalidUsername}
input invalid password
    input password    xpath = //*[@id="password"]     ${invalidPassword}
input empty username/email field
    input text    xpath = //*[@id="login"]    ${emptyUserName}
input empty password field
    input password    xpath = //*[@id="password"]     ${emptyUserPassword}
click on 'zaloguj się' button
    click button     xpath=//*[@id="stgMain"]/div/div/div[1]/form/button
assert invalid
    page should contain     Podany login i/lub hasło są nieprawidłowe.
end web test
    close browser