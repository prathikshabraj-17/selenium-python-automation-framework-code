*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    Chrome
${URL}        https://www.google.com
${SEARCH_TERM}    Robot Framework

*** Test Cases ***
Search In Google
    Open Browser    ${URL}    ${BROWSER}
    Input Text      name=q    ${SEARCH_TERM}
    Press Keys      name=q    \\13
    Wait Until Page Contains    ${SEARCH_TERM}
    Title Should Contain        Robot
    Close Browser
