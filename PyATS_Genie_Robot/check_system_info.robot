# robot check_system_info.robot
*** Settings ***
Library	ats.robot.pyATSRobot
Library	genie.libs.robot.GenieRobot
Library	unicon.robot.UniconRobot
Suite setup    Setup


*** Variables ***
${testbed}    testbed.yml

*** Test Cases ***
Send show version
    ${output}=    execute "net show system" on device "cum01"

*** Keywords ***
Setup
    use genie testbed "${testbed}"
    connect to device "cum01"
