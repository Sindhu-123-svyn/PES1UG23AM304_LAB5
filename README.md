# PES1UG23AM304_LAB5 - Static Code Analysis

## Student Details
- Name: sindhu d h
- SRN: PES1UG23AM304
- Section: F

## Issues Found and Fixed

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|-------------|
| Dangerous eval() | Security | Line 45 | Could execute harmful code | Removed entirely |
| Empty except clause | Bug | Line 18 | Hides all errors | Changed to specific exceptions |
| Mutable default argument | Bug | Line 7 | logs=[] shared between calls | Used logs=None with initialization |
| No input validation | Bug | Multiple | Accepts wrong data types | Added type and value checks |
| Unsafe file handling | Security | Line 22,28 | Files not properly closed | Used with statements |
| Poor variable names | Style | Multiple | Single letter variables | Used descriptive names |
| Global variable | Design | Line 5 | Hard to test and maintain | Converted to class |

## Reflection

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
- **Easiest**: Removing eval() - just deleted one dangerous line
- **Hardest**: Converting to class - had to restructure the entire code architecture

### 2. Did the static analysis tools report any false positives? If so, describe one example.
No false positives in this case - all reported issues were genuine problems that needed fixing.

### 3. How would you integrate static analysis tools into your actual software development workflow?
- **Local Development**: Run tools before each commit
- **CI/CD Pipeline**: Integrate with GitHub Actions
- **Code Review**: Use reports as objective evidence

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- **Security**: Eliminated dangerous functions
- **Reliability**: Proper error handling
- **Maintainability**: Better structure with class
- **Readability**: Clear variable names and documentation