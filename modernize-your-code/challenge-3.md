# Challenge 03: Build the Validation Agent

## Introduction

The Validation Agent ensures that translated SQL code is syntactically correct and semantically equivalent to the original Oracle SQL. This challenge implements a hybrid validation approach: AI-based syntax and semantic checking combined with optional real database execution for verification. The agent identifies potential errors, flags risky translations, and provides confidence scores.

## Challenge Objectives

- Create a Validation Agent using Azure OpenAI
- Implement AI-based syntax validation for T-SQL
- Perform semantic equivalence checking between Oracle and Azure SQL
- (Optional) Execute translated queries against Azure SQL Database
- Generate validation reports with error details and confidence scores
- Handle validation failures and retry logic

## Steps to Complete

### Part 1: Create Validation Agent Notebook

1. In **Azure AI Foundry Studio**, create a new notebook named `Validation_Agent`.

2. In the first cell, import required libraries:

```python
# Install additional libraries for SQL parsing
!pip install sqlparse pyodbc --quiet

import os
import re
import sqlparse
from openai import AzureOpenAI
import json
from datetime import datetime

print("Validation libraries imported successfully")
```

3. Run the cell.

### Part 2: Configure Azure OpenAI for Validation

1. Add a new cell to set up the OpenAI client (use same credentials from Challenge 2):

```python
# Azure OpenAI configuration
AZURE_OPENAI_ENDPOINT = "https://sql-modernization-openai-xxxxx.openai.azure.com/"  # Replace
AZURE_OPENAI_KEY = "your-api-key-here"  # Replace
AZURE_OPENAI_DEPLOYMENT = "gpt-4-sql-translator"
AZURE_OPENAI_API_VERSION = "2024-02-15-preview"

# Initialize client
client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_API_VERSION
)

print("Azure OpenAI client initialized for validation")
```

2. Run the cell.

### Part 3: Design Validation Prompt

1. Add a new cell with the validation system prompt:

```python
VALIDATION_SYSTEM_PROMPT = """You are an expert SQL validator specializing in Azure SQL (T-SQL) syntax and semantics. 
Your task is to validate translated SQL code and identify potential errors, syntax issues, or semantic mismatches.

Validation Checklist:

1. Syntax Validation:
   - Verify all T-SQL keywords are correct
   - Check proper use of BEGIN...END blocks
   - Validate data type declarations
   - Ensure proper semicolon usage
   - Verify function signatures match T-SQL standards

2. Semantic Validation:
   - Compare original Oracle logic with translated T-SQL logic
   - Identify potential logic changes or data loss
   - Flag deprecated functions or risky conversions
   - Check for missing error handling
   - Verify transaction management is equivalent

3. Common Issues to Check:
   - Implicit data type conversions that may cause data loss
   - NULL handling differences between Oracle and SQL Server
   - Date/time function behavior differences
   - String comparison case sensitivity differences
   - ROWNUM vs ROW_NUMBER() or TOP equivalence
   - Exception handling completeness

4. Output Format:
   Provide a JSON response with:
   - is_valid (boolean)
   - confidence_score (0.0 to 1.0)
   - syntax_errors (array of error messages)
   - semantic_warnings (array of warning messages)
   - critical_issues (array of critical problems)
   - suggestions (array of improvement suggestions)

Example response:
{
  "is_valid": true,
  "confidence_score": 0.95,
  "syntax_errors": [],
  "semantic_warnings": ["Date comparison may behave differently due to timezone handling"],
  "critical_issues": [],
  "suggestions": ["Consider adding NOCOUNT ON for performance"]
}

Validate the provided T-SQL code and return only the JSON response."""

print("Validation prompt configured")
```

2. Run the cell.

### Part 4: Create AI-Based Syntax Validator

1. Add a new cell with the syntax validation function:

```python
def validate_sql_syntax_ai(translated_sql: str, original_sql: str = None) -> dict:
    """
    Validates T-SQL syntax using Azure OpenAI.
    
    Args:
        translated_sql (str): The translated T-SQL code
        original_sql (str): The original Oracle SQL for semantic comparison
    
    Returns:
        dict: Validation results including errors and warnings
    """
    try:
        # Prepare validation message
        user_message = f"Validate the following Azure SQL (T-SQL) code:\n\n{translated_sql}"
        
        if original_sql:
            user_message += f"\n\nOriginal Oracle SQL for semantic comparison:\n\n{original_sql}"
        
        # Call Azure OpenAI
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": VALIDATION_SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.2,  # Lower temperature for consistent validation
            max_tokens=2000,
            response_format={"type": "json_object"}  # Request JSON response
        )
        
        # Parse validation result
        validation_json = response.choices[0].message.content.strip()
        validation_result = json.loads(validation_json)
        
        # Add metadata
        validation_result["validation_method"] = "AI-based"
        validation_result["timestamp"] = datetime.now().isoformat()
        validation_result["tokens_used"] = response.usage.total_tokens
        
        return validation_result
        
    except json.JSONDecodeError as e:
        # Fallback if JSON parsing fails
        return {
            "is_valid": False,
            "confidence_score": 0.0,
            "syntax_errors": [f"Validation response parsing failed: {str(e)}"],
            "semantic_warnings": [],
            "critical_issues": ["Could not parse validation response"],
            "suggestions": [],
            "validation_method": "AI-based (error)",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "is_valid": False,
            "confidence_score": 0.0,
            "syntax_errors": [str(e)],
            "semantic_warnings": [],
            "critical_issues": [f"Validation failed: {str(e)}"],
            "suggestions": [],
            "validation_method": "AI-based (error)",
            "timestamp": datetime.now().isoformat()
        }

print("AI syntax validator created")
```

2. Run the cell.

### Part 5: Create Basic Syntax Parser

1. Add a new cell with a simple syntax checker using sqlparse:

```python
def validate_sql_syntax_parser(sql: str) -> dict:
    """
    Performs basic syntax validation using SQL parser.
    
    Args:
        sql (str): SQL code to validate
    
    Returns:
        dict: Basic validation results
    """
    try:
        # Format and parse SQL
        formatted = sqlparse.format(sql, reindent=True, keyword_case='upper')
        parsed = sqlparse.parse(sql)
        
        issues = []
        
        # Check if SQL could be parsed
        if not parsed:
            issues.append("SQL could not be parsed - likely syntax error")
        
        # Check for basic T-SQL keywords
        sql_upper = sql.upper()
        tsql_keywords = ['SELECT', 'FROM', 'WHERE', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'DROP']
        has_valid_keyword = any(keyword in sql_upper for keyword in tsql_keywords)
        
        if not has_valid_keyword:
            issues.append("No valid SQL keywords detected")
        
        # Check for unmatched parentheses
        if sql.count('(') != sql.count(')'):
            issues.append("Unmatched parentheses detected")
        
        # Check for unmatched BEGIN/END
        begin_count = len(re.findall(r'\bBEGIN\b', sql_upper))
        end_count = len(re.findall(r'\bEND\b', sql_upper))
        if begin_count != end_count:
            issues.append(f"Unmatched BEGIN/END blocks (BEGIN: {begin_count}, END: {end_count})")
        
        is_valid = len(issues) == 0
        
        return {
            "is_valid": is_valid,
            "syntax_errors": issues,
            "validation_method": "Parser-based",
            "formatted_sql": formatted
        }
        
    except Exception as e:
        return {
            "is_valid": False,
            "syntax_errors": [f"Parser error: {str(e)}"],
            "validation_method": "Parser-based (error)"
        }

print("Parser-based syntax validator created")
```

2. Run the cell.

### Part 6: (Optional) Database Execution Validator

1. Add a new cell for real database validation:

```python
import pyodbc

# Azure SQL Database configuration (from Challenge 1)
SQL_SERVER = "sql-validation-xxxxx.database.windows.net"  # Replace
SQL_DATABASE = "ValidationTestDB"
SQL_USERNAME = "sqladmin"
SQL_PASSWORD = "P@ssw0rd123!"  # Replace

def validate_sql_execution(sql: str, dry_run: bool = True) -> dict:
    """
    Validates SQL by attempting execution against Azure SQL Database.
    
    Args:
        sql (str): T-SQL code to validate
        dry_run (bool): If True, only checks syntax without executing
    
    Returns:
        dict: Execution validation results
    """
    try:
        # Build connection string
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SQL_SERVER};DATABASE={SQL_DATABASE};UID={SQL_USERNAME};PWD={SQL_PASSWORD}"
        
        # Connect to database
        conn = pyodbc.connect(conn_str, timeout=10)
        cursor = conn.cursor()
        
        if dry_run:
            # Use SET PARSEONLY to check syntax without executing
            cursor.execute("SET PARSEONLY ON")
            cursor.execute(sql)
            cursor.execute("SET PARSEONLY OFF")
            
            result = {
                "is_valid": True,
                "execution_successful": False,
                "execution_mode": "syntax-only",
                "message": "Syntax validation passed (no execution)",
                "validation_method": "Database (parse-only)"
            }
        else:
            # Actually execute the query (be careful with this!)
            cursor.execute(sql)
            rows = cursor.fetchall() if cursor.description else []
            
            result = {
                "is_valid": True,
                "execution_successful": True,
                "execution_mode": "full-execution",
                "rows_returned": len(rows),
                "message": "Query executed successfully",
                "validation_method": "Database (full-execution)"
            }
        
        cursor.close()
        conn.close()
        
        return result
        
    except pyodbc.Error as e:
        error_message = str(e)
        
        return {
            "is_valid": False,
            "execution_successful": False,
            "syntax_errors": [error_message],
            "message": f"Database validation failed: {error_message}",
            "validation_method": "Database (error)"
        }
    except Exception as e:
        return {
            "is_valid": False,
            "execution_successful": False,
            "syntax_errors": [str(e)],
            "message": f"Validation error: {str(e)}",
            "validation_method": "Database (error)"
        }

print("Database execution validator created")
print("Note: Database validation is optional and requires Azure SQL Database from Challenge 1")
```

2. Run the cell.

### Part 7: Create Hybrid Validation Function

1. Add a new cell to combine all validation methods:

```python
def validate_translation(translated_sql: str, original_sql: str = None, 
                        use_db_validation: bool = False, db_dry_run: bool = True) -> dict:
    """
    Performs comprehensive validation using multiple methods.
    
    Args:
        translated_sql (str): Translated T-SQL code
        original_sql (str): Original Oracle SQL
        use_db_validation (bool): Whether to validate against real database
        db_dry_run (bool): If True, only syntax check in DB (no execution)
    
    Returns:
        dict: Comprehensive validation results
    """
    validation_results = {
        "translated_sql": translated_sql,
        "original_sql": original_sql,
        "timestamp": datetime.now().isoformat(),
        "validation_methods": []
    }
    
    # Method 1: AI-based validation
    print("Running AI-based validation...")
    ai_validation = validate_sql_syntax_ai(translated_sql, original_sql)
    validation_results["ai_validation"] = ai_validation
    validation_results["validation_methods"].append("AI-based")
    
    # Method 2: Parser-based validation
    print("Running parser-based validation...")
    parser_validation = validate_sql_syntax_parser(translated_sql)
    validation_results["parser_validation"] = parser_validation
    validation_results["validation_methods"].append("Parser-based")
    
    # Method 3: Database validation (optional)
    if use_db_validation:
        print("Running database validation...")
        try:
            db_validation = validate_sql_execution(translated_sql, dry_run=db_dry_run)
            validation_results["database_validation"] = db_validation
            validation_results["validation_methods"].append("Database")
        except Exception as e:
            validation_results["database_validation"] = {
                "is_valid": False,
                "message": f"Database validation unavailable: {str(e)}"
            }
    
    # Determine overall validity
    overall_valid = (
        ai_validation.get("is_valid", False) and 
        parser_validation.get("is_valid", False)
    )
    
    if use_db_validation:
        overall_valid = overall_valid and validation_results.get("database_validation", {}).get("is_valid", False)
    
    validation_results["overall_valid"] = overall_valid
    validation_results["confidence_score"] = ai_validation.get("confidence_score", 0.0)
    
    # Collect all errors and warnings
    all_errors = []
    all_warnings = []
    
    all_errors.extend(ai_validation.get("syntax_errors", []))
    all_errors.extend(ai_validation.get("critical_issues", []))
    all_errors.extend(parser_validation.get("syntax_errors", []))
    
    all_warnings.extend(ai_validation.get("semantic_warnings", []))
    all_warnings.extend(ai_validation.get("suggestions", []))
    
    if use_db_validation and "database_validation" in validation_results:
        all_errors.extend(validation_results["database_validation"].get("syntax_errors", []))
    
    validation_results["all_errors"] = list(set(all_errors))  # Remove duplicates
    validation_results["all_warnings"] = list(set(all_warnings))
    
    return validation_results

print("Hybrid validation function created")
```

2. Run the cell.

### Part 8: Test Validation with Sample Translations

1. Add a new cell to test the validator:

```python
# Test with a correct translation
correct_sql = """
CREATE PROCEDURE UpdateEmployeeSalary
    @EmployeeID INT,
    @NewSalary DECIMAL(10,2),
    @Status NVARCHAR(100) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @CurrentSalary DECIMAL(10,2);
    
    SELECT @CurrentSalary = Salary
    FROM Employees
    WHERE EmployeeID = @EmployeeID;
    
    IF @CurrentSalary IS NULL
    BEGIN
        SET @Status = 'Employee not found';
        RETURN;
    END
    
    UPDATE Employees
    SET Salary = @NewSalary,
        LastUpdated = GETDATE()
    WHERE EmployeeID = @EmployeeID;
    
    SET @Status = 'Success';
END
"""

print("Testing validation with correct SQL...\n")
result = validate_translation(correct_sql, use_db_validation=False)

print(f"Overall Valid: {result['overall_valid']}")
print(f"Confidence Score: {result['confidence_score']}")
print(f"Validation Methods: {', '.join(result['validation_methods'])}")

if result['all_errors']:
    print(f"\nErrors Found: {len(result['all_errors'])}")
    for error in result['all_errors']:
        print(f"  - {error}")
else:
    print("\nNo errors found")

if result['all_warnings']:
    print(f"\nWarnings: {len(result['all_warnings'])}")
    for warning in result['all_warnings'][:3]:  # Show first 3
        print(f"  - {warning}")
```

2. Run the cell.

3. Add another test with intentional errors:

```python
# Test with incorrect SQL
incorrect_sql = """
CREATE PROCEDURE BrokenProcedure
    @Param1 INT
AS
BEGIN
    SELECT * FROM NonExistentTable
    WHERE Column1 = @Param1
    -- Missing END statement intentionally
"""

print("Testing validation with incorrect SQL...\n")
result = validate_translation(incorrect_sql, use_db_validation=False)

print(f"Overall Valid: {result['overall_valid']}")
print(f"Confidence Score: {result['confidence_score']}")

print(f"\nErrors Found: {len(result['all_errors'])}")
for error in result['all_errors']:
    print(f"  - {error}")
```

4. Run the cell.

### Part 9: Create Validation Report Generator

1. Add a new cell to generate validation reports:

```python
def generate_validation_report(validation_result: dict) -> str:
    """
    Generates a human-readable validation report.
    
    Args:
        validation_result (dict): Validation results from validate_translation()
    
    Returns:
        str: Formatted validation report
    """
    report = []
    report.append("="*80)
    report.append("SQL VALIDATION REPORT")
    report.append("="*80)
    report.append(f"Timestamp: {validation_result['timestamp']}")
    report.append(f"Validation Methods: {', '.join(validation_result['validation_methods'])}")
    report.append(f"Overall Status: {'VALID' if validation_result['overall_valid'] else 'INVALID'}")
    report.append(f"Confidence Score: {validation_result['confidence_score']:.2f}")
    report.append("")
    
    # Errors section
    if validation_result['all_errors']:
        report.append("ERRORS:")
        for idx, error in enumerate(validation_result['all_errors'], 1):
            report.append(f"  {idx}. {error}")
        report.append("")
    else:
        report.append("ERRORS: None")
        report.append("")
    
    # Warnings section
    if validation_result['all_warnings']:
        report.append("WARNINGS & SUGGESTIONS:")
        for idx, warning in enumerate(validation_result['all_warnings'], 1):
            report.append(f"  {idx}. {warning}")
        report.append("")
    else:
        report.append("WARNINGS: None")
        report.append("")
    
    report.append("="*80)
    
    return "\n".join(report)

# Test report generation
print(generate_validation_report(result))
```

2. Run the cell.

### Part 10: Save Validation Results

1. Add a final cell to persist validation results:

```python
def save_validation_result(validation_result: dict, output_folder: str = "validations"):
    """
    Saves validation results to JSON file.
    
    Args:
        validation_result (dict): Validation results
        output_folder (str): Output directory
    
    Returns:
        str: File path
    """
    import os
    
    os.makedirs(output_folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_folder}/validation_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(validation_result, f, indent=2)
    
    print(f"Validation result saved to: {filename}")
    return filename

# Save the validation result
save_validation_result(result)
```

2. Run the cell.

## Success Criteria

- Validation Agent notebook created in Azure AI Foundry
- AI-based syntax validation implemented using Azure OpenAI
- Parser-based validation functional with sqlparse
- (Optional) Database validation configured with Azure SQL connection
- Hybrid validation combines multiple methods successfully
- Validation correctly identifies syntax errors in malformed SQL
- Validation passes for correctly translated T-SQL code
- Confidence scores and error messages generated accurately
- Validation reports created in human-readable format
- Validation results saved to JSON files for audit trail

## Additional Resources

- [T-SQL Syntax Reference](https://learn.microsoft.com/sql/t-sql/language-reference)
- [SQL Parser Libraries](https://pypi.org/project/sqlparse/)
- [Azure SQL Database Connection](https://learn.microsoft.com/sql/connect/python/pyodbc/python-sql-driver-pyodbc)
- [Semantic Code Analysis with AI](https://learn.microsoft.com/azure/ai-services/openai/concepts/advanced-prompt-engineering)

Now, click **Next** to continue to **Challenge 04**.
