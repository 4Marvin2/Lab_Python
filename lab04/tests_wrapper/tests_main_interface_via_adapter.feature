Feature: Compatibility check via wrapper

    Scenario: Checking a square detail of suitable size
        Given size of square detail - width "20" and size of round hole - "10"
        Then detail and hole compatible after conversion via wrapper

    Scenario: Checking a square detail if unsuitable size
        Given size of square detail - width "10" and size of round hole - "10"
        Then detail and hole incompatible after conversion via wrapper
