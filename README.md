# Pytest
- Added the solutions to the test code
- For report generation, added xml reporting in settings.json
Logging Implementation
  - Using in-built logging function, setting the logging level or severity of the info(Error, Warning, Critical) with the function 
    basicConfig
  - Using RotatingFileHandler, we are storing the log info in app.log file with max memory set to 100 KB and 3 old log files
  - Defining the format of the message (TIME - NAME - INFOLEVEL - MESSAGE)
    
