PES1UG23AM304_LAB5 - Static Code Analysis
Student Details
Name: Sindhu

SRN: PES1UG23AM304

Section: AM

Lab: 5 - Static Code Analysis

Lab Objective
To enhance Python code quality, security, and style by utilizing static analysis tools (Pylint, Bandit, and Flake8) to detect and rectify common programming issues.

Tools Used
Pylint - Code quality and logical errors

Bandit - Security vulnerabilities

Flake8 - PEP 8 style guidelines

Issues Found and Fixed
Issue	Type	Line(s)	Description	Fix Approach
Dangerous eval()	Security	Line 45	Could execute harmful code	Removed entirely
Empty except clause	Bug	Line 18	Hides all errors	Changed to specific exceptions
Mutable default argument	Bug	Line 7	logs=[] shared between calls	Used logs=None with initialization
No input validation	Bug	Multiple	Accepts wrong data types	Added type and value checks
Unsafe file handling	Security	Line 22,28	Files not properly closed	Used with statements
Poor variable names	Style	Multiple	Single letter variables	Used descriptive names
Global variable	Design	Line 5	Hard to test and maintain	Converted to class
Broad except clause	Security	Line 18	Catches all exceptions	Specific exception handling
Hardcoded data	Design	Multiple	No separation of concerns	Implemented class structure
Analysis Reports Summary
Pylint Report
Score: 8.07/10

Status: Good code quality with minor improvements needed

Main Issues: Code structure and documentation

Bandit Report
Status:  No security issues identified

Result: All security vulnerabilities successfully fixed

Confidence: High - no potential security risks found

Flake8 Report
Issues Found: 21 style issues

Main Problems: Whitespace and line length violations

Status: Code follows PEP 8 with minor formatting issues

Files in Repository
inventory_system.py - Original code with issues

clean_inventory_system.py - Refactored and secured code

pylint_report_clean.txt - Pylint analysis report

bandit_report_clean.txt - Bandit security report

flake8_report_clean.txt - Flake8 style report

README.md - This documentation file

Code Improvements Made
Security Enhancements
Removed dangerous eval() function

Implemented proper exception handling

Secured file operations with context managers

Added input validation and type checking

Code Quality Improvements
Converted from procedural to object-oriented design

Added comprehensive docstrings

Improved variable naming conventions

Implemented proper logging

Functionality Improvements
Added input validation for all user-facing functions

Implemented proper error messages

Added inventory persistence with JSON

Created comprehensive inventory management class

Reflection
1. Which issues were the easiest to fix, and which were the hardest? Why?
Easiest: Removing eval() - straightforward deletion of one line with immediate security improvement

Hardest: Converting to class structure - required complete code restructuring and understanding of OOP principles

2. Did the static analysis tools report any false positives? If so, describe one example.
No false positives were reported. All identified issues were genuine problems that needed addressing. The tools accurately detected:

Actual security vulnerabilities (eval usage)

Code quality issues (mutable defaults, broad exceptions)

Style violations (naming conventions, formatting)

3. How would you integrate static analysis tools into your actual software development workflow?
Pre-commit Hooks: Automatically run analysis before each commit

CI/CD Pipeline: Integrate with GitHub Actions for automated checks on pull requests

Quality Gates: Set minimum quality scores (Pylint > 8.0, Bandit zero issues)

Developer Workflow: Run tools locally before pushing code

Code Review: Use reports as objective evidence during reviews

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
Security: Eliminated code injection risks and insecure patterns

Maintainability: Class-based structure allows easier extensions and testing

Readability: Clear method names and comprehensive documentation

Robustness: Proper error handling prevents crashes from invalid inputs

Professionalism: Code now follows industry standards and best practices

How to Run the Code
bash
# Run the original code (for comparison)
python inventory_system.py

# Run the cleaned and secured code
python clean_inventory_system.py

# Generate analysis reports
python -m pylint clean_inventory_system.py > pylint_report_clean.txt
python -m bandit -r clean_inventory_system.py > bandit_report_clean.txt
python -m flake8 clean_inventory_system.py > flake8_report_clean.txt
Learning Outcomes
Understanding static code analysis principles

Identifying and fixing common Python issues

Using industry-standard analysis tools

Interpreting analysis reports and applying fixes

Improving overall code quality and security