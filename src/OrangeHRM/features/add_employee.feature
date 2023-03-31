Feature: OrangeHRM Add employee

Scenario: Add new employee
    Given I launch Chrome browser and login to orangeHRM
    When go to pim page
    And click add 
    And Enter First_name "a" and middle_name "b" and last_name "c" and employee_id "0001"
    Then click save