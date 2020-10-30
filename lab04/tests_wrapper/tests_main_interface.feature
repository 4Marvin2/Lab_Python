Feature: Compatibility check

    Scenario:  Checking a round detail of suitable size
        Given size of round detail - radius "10" and size of round hole - "10"
        Then detail and hole compatible

    Scenario:  Checking a round detail of unsuitable size
        Given size of round detail - radius "20" and size of round hole - "10"
        Then detail and hole incompatible

    Scenario:  Checking a square detail
        Given size of square detail - width "10" and size of round hole - "10"
        Then the square detail is not comparable to the round hole
