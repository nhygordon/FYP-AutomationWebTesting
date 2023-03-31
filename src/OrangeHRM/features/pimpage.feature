Feature: PIM page add emplyees

Scenario Outline: Add new employee
    Given I launch Chrome browser and login to orangeHRM
    When go to pim page
    And click add 
    And Enter First_name "<first_name>" and middle_name "<middle_name>" and last_name "<last_name>" and employee_id "<id>"
    Then click save

    Examples:
        
        | first_name    | middle_name   | last_name | id    |
        |y              | h             | n         | 0001  |
        |l              |               | f         | 0002  |
        |c              | y             | c         | 0003  |
