*** Settings ***
Library	ats.robot.pyATSRobot
Library	genie.libs.robot.GenieRobot
Library	unicon.robot.UniconRobot
Suite setup    Setup


*** Variables ***
${testbed}    testbed.yml
${hostname}   leaf01

*** Test Cases ***
Send net show system
    ${output} =    execute "net show system" on device "cum01"
    Should Contain  ${output}  ${hostname}

*** Keywords ***
Setup
    use genie testbed "${testbed}"
    connect to device "cum01"
