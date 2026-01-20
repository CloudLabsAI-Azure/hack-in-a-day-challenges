# Challenge 02: Build the Translation Agent

## Introduction

The Translation Agent is the core component of the SQL modernization pipeline. It uses Azure AI Foundry's GPT-4 model to convert Oracle PL/SQL syntax to Azure SQL T-SQL syntax. This challenge focuses on designing effective prompts, handling dialect-specific conversions, and managing common translation scenarios including stored procedures, functions, cursors, and complex queries.

## Challenge Objectives

- Set up Azure AI Foundry development environment with Jupyter notebooks
- Create a Translation Agent using Azure AI Foundry's OpenAI API
- Design prompts for accurate Oracle to Azure SQL translation
- Handle common PL/SQL to T-SQL conversions (data types, functions, syntax)
- Test translations with sample Oracle SQL files
- Implement error handling and retry logic

## Steps to Complete

### Part 1: Set Up AI Foundry Development Environment

1. Navigate to the **Azure Portal** and open your **AI Foundry project**: `sql-modernization-ai-project`

2. Click on **Launch Azure AI Foundry Studio** (or similar button to open the studio interface).

3. In AI Foundry Studio, navigate to **Build** or **Develop** section.

4. Click on **+ New Notebook** to create a Jupyter notebook.

5. Name the notebook: `Translation_Agent`

6. Select **Python 3.10** or later as the kernel.

7. Wait for the notebook environment to initialize (30-60 seconds).

### Part 2: Install Required Libraries

1. In the first cell of your notebook, install necessary Python packages:

```python
# Install required libraries
!pip install openai azure-identity python-dotenv --quiet

print("Libraries installed successfully")
```

2. Run the cell and wait for installation to complete.

### Part 3: Configure AI Foundry Model Connection

1. Add a new cell and configure the AI Foundry OpenAI client (uses same SDK):

```python
import os
from openai import AzureOpenAI

# AI Foundry OpenAI configuration (from Challenge 1)
AZURE_OPENAI_ENDPOINT = "https://your-ai-foundry-endpoint.openai.azure.com/"  # Replace with your AI Foundry endpoint
AZURE_OPENAI_KEY = "your-api-key-here"  # Replace with your key from AI Foundry
AZURE_OPENAI_DEPLOYMENT = "gpt-4-sql-translator"  # Your deployment name from Challenge 1
AZURE_OPENAI_API_VERSION = "2024-02-15-preview"

# Initialize client (uses Azure OpenAI SDK)
client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_API_VERSION
)

print("Azure OpenAI client initialized successfully")
```

3. Replace the placeholder values with your actual Azure OpenAI endpoint and API key from Challenge 1.

4. Run the cell to verify the connection works.

### Part 4: Design the Translation Prompt

1. Add a new cell to create the system prompt for SQL translation:

```python
# System prompt for Oracle to Azure SQL translation
TRANSLATION_SYSTEM_PROMPT = """You are an expert database migration specialist with deep knowledge of Oracle PL/SQL and Azure SQL (T-SQL). 
Your task is to translate Oracle PL/SQL code to Azure SQL T-SQL accurately while preserving the original logic and functionality.

Follow these translation rules:

1. Data Type Conversions:
   - Oracle NUMBER -> SQL Server INT, BIGINT, DECIMAL, or NUMERIC (choose based on precision)
   - Oracle VARCHAR2 -> SQL Server VARCHAR or NVARCHAR
   - Oracle DATE -> SQL Server DATETIME2 or DATE
   - Oracle CLOB -> SQL Server NVARCHAR(MAX) or VARCHAR(MAX)
   - Oracle BLOB -> SQL Server VARBINARY(MAX)

2. Function Conversions:
   - Oracle NVL() -> SQL Server ISNULL() or COALESCE()
   - Oracle SYSDATE -> SQL Server GETDATE() or SYSDATETIME()
   - Oracle DECODE() -> SQL Server CASE WHEN
   - Oracle TO_DATE() -> SQL Server CONVERT() or CAST()
   - Oracle TO_CHAR() -> SQL Server CONVERT() or FORMAT()
   - Oracle SUBSTR() -> SQL Server SUBSTRING()
   - Oracle INSTR() -> SQL Server CHARINDEX()
   - Oracle ROWNUM -> SQL Server ROW_NUMBER() or TOP

3. Syntax Conversions:
   - Oracle sequences -> SQL Server IDENTITY or SEQUENCE
   - Oracle packages -> SQL Server schemas with stored procedures
   - Oracle cursors -> SQL Server cursors (or suggest set-based alternatives)
   - Oracle EXECUTE IMMEDIATE -> SQL Server EXEC sp_executesql
   - Oracle PRAGMA AUTONOMOUS_TRANSACTION -> SQL Server separate transaction handling
   - Oracle RAISE_APPLICATION_ERROR -> SQL Server THROW or RAISERROR

4. Stored Procedure Syntax:
   - Oracle CREATE OR REPLACE PROCEDURE -> SQL Server CREATE PROCEDURE (with DROP IF EXISTS pattern)
   - Oracle IN/OUT/IN OUT parameters -> SQL Server INPUT/OUTPUT parameters
   - Oracle RETURN in functions -> SQL Server RETURNS and RETURN
   - Oracle BEGIN/END blocks remain similar but check exception handling

5. Exception Handling:
   - Oracle EXCEPTION WHEN OTHERS -> SQL Server TRY...CATCH with ERROR_MESSAGE()
   - Oracle SQLCODE and SQLERRM -> SQL Server ERROR_NUMBER() and ERROR_MESSAGE()

6. Best Practices:
   - Add comments explaining significant translations
   - Maintain original formatting and structure where possible
   - Flag any code that requires manual review with /* TODO: Review */ comments
   - Suggest Azure SQL optimizations where applicable

Translate the provided Oracle SQL code to Azure SQL T-SQL. Provide only the translated code without additional explanations unless there are critical warnings."""

print("Translation prompt configured")
```

2. Run the cell.

### Part 5: Create the Translation Agent Function

1. Add a new cell with the core translation function:

```python
def translate_oracle_to_azure_sql(oracle_sql: str, include_explanations: bool = False) -> dict:
    """
    Translates Oracle PL/SQL code to Azure SQL T-SQL using Azure OpenAI.
    
    Args:
        oracle_sql (str): The Oracle SQL code to translate
        include_explanations (bool): Whether to include translation explanations
    
    Returns:
        dict: Contains translated_sql, success status, and any warnings
    """
    try:
        # Prepare user message
        user_message = f"Translate the following Oracle PL/SQL code to Azure SQL T-SQL:\n\n{oracle_sql}"
        
        # Call Azure OpenAI
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": TRANSLATION_SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,  # Lower temperature for more deterministic translations
            max_tokens=4000,
            top_p=0.95
        )
        
        # Extract translated SQL
        translated_sql = response.choices[0].message.content.strip()
        
        # Remove markdown code blocks if present
        if translated_sql.startswith("```sql"):
            translated_sql = translated_sql.replace("```sql", "").replace("```", "").strip()
        elif translated_sql.startswith("```"):
            translated_sql = translated_sql.replace("```", "").strip()
        
        return {
            "success": True,
            "translated_sql": translated_sql,
            "original_sql": oracle_sql,
            "tokens_used": response.usage.total_tokens,
            "warnings": []
        }
        
    except Exception as e:
        return {
            "success": False,
            "translated_sql": None,
            "original_sql": oracle_sql,
            "error": str(e),
            "warnings": [f"Translation failed: {str(e)}"]
        }

print("Translation agent function created")
```

2. Run the cell.

### Part 6: Test with Sample Oracle SQL

1. Add a new cell to test the translation with a simple Oracle query:

```python
# Test 1: Simple SELECT query
oracle_query_1 = """
SELECT employee_id, first_name, last_name, 
       NVL(commission_pct, 0) as commission,
       TO_CHAR(hire_date, 'YYYY-MM-DD') as hire_date_formatted
FROM employees
WHERE hire_date > TO_DATE('2020-01-01', 'YYYY-MM-DD')
ORDER BY hire_date DESC;
"""

print("Original Oracle SQL:")
print(oracle_query_1)
print("\n" + "="*80 + "\n")

result = translate_oracle_to_azure_sql(oracle_query_1)

if result["success"]:
    print("Translated Azure SQL:")
    print(result["translated_sql"])
    print(f"\nTokens used: {result['tokens_used']}")
else:
    print(f"Translation failed: {result['error']}")
```

2. Run the cell and review the translated SQL.

3. Add another test with a stored procedure:

```python
# Test 2: Oracle stored procedure
oracle_procedure = """
CREATE OR REPLACE PROCEDURE update_employee_salary(
    p_employee_id IN NUMBER,
    p_new_salary IN NUMBER,
    p_status OUT VARCHAR2
)
IS
    v_current_salary NUMBER;
BEGIN
    SELECT salary INTO v_current_salary
    FROM employees
    WHERE employee_id = p_employee_id;
    
    IF v_current_salary IS NULL THEN
        p_status := 'Employee not found';
        RETURN;
    END IF;
    
    UPDATE employees
    SET salary = p_new_salary,
        last_updated = SYSDATE
    WHERE employee_id = p_employee_id;
    
    COMMIT;
    p_status := 'Success';
    
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        p_status := 'Error: ' || SQLERRM;
        RAISE_APPLICATION_ERROR(-20001, 'Salary update failed');
END;
"""

print("Original Oracle Procedure:")
print(oracle_procedure)
print("\n" + "="*80 + "\n")

result = translate_oracle_to_azure_sql(oracle_procedure)

if result["success"]:
    print("Translated Azure SQL Procedure:")
    print(result["translated_sql"])
    print(f"\nTokens used: {result['tokens_used']}")
else:
    print(f"Translation failed: {result['error']}")
```

4. Run the cell and verify the stored procedure translation.

### Part 7: Handle Batch Translations

1. Add a new cell to handle multiple SQL files:

```python
def translate_batch(sql_statements: list) -> list:
    """
    Translates a batch of Oracle SQL statements.
    
    Args:
        sql_statements (list): List of Oracle SQL code strings
    
    Returns:
        list: List of translation result dictionaries
    """
    results = []
    
    for idx, sql in enumerate(sql_statements, 1):
        print(f"Translating statement {idx}/{len(sql_statements)}...")
        result = translate_oracle_to_azure_sql(sql)
        results.append(result)
        
        if not result["success"]:
            print(f"  Warning: Translation {idx} failed")
    
    print(f"\nBatch translation complete: {len(results)} statements processed")
    return results

# Example batch translation
sample_queries = [
    "SELECT * FROM employees WHERE ROWNUM <= 10;",
    "SELECT employee_id, DECODE(status, 'A', 'Active', 'I', 'Inactive', 'Unknown') FROM emp_status;",
    "SELECT employee_id, SUBSTR(email, 1, INSTR(email, '@')-1) AS username FROM employees;"
]

batch_results = translate_batch(sample_queries)

# Display results
for idx, result in enumerate(batch_results, 1):
    print(f"\nQuery {idx}:")
    if result["success"]:
        print(result["translated_sql"])
    else:
        print(f"Failed: {result.get('error', 'Unknown error')}")
```

2. Run the cell.

### Part 8: Implement Retry Logic for Failed Translations

1. Add a new cell with retry mechanism:

```python
import time

def translate_with_retry(oracle_sql: str, max_retries: int = 3, delay: int = 2) -> dict:
    """
    Translates Oracle SQL with retry logic for handling transient failures.
    
    Args:
        oracle_sql (str): Oracle SQL code to translate
        max_retries (int): Maximum number of retry attempts
        delay (int): Delay in seconds between retries
    
    Returns:
        dict: Translation result
    """
    for attempt in range(1, max_retries + 1):
        result = translate_oracle_to_azure_sql(oracle_sql)
        
        if result["success"]:
            return result
        
        if attempt < max_retries:
            print(f"Attempt {attempt} failed. Retrying in {delay} seconds...")
            time.sleep(delay)
        else:
            print(f"All {max_retries} attempts failed.")
            return result
    
    return result

# Test retry logic
test_query = "SELECT employee_id, NVL(manager_id, 0) as manager FROM employees;"
result = translate_with_retry(test_query, max_retries=2)

if result["success"]:
    print("Translation successful:")
    print(result["translated_sql"])
```

2. Run the cell.

### Part 9: Save Translations to Files

1. Add a new cell to export translations:

```python
import json
from datetime import datetime

def save_translation_result(result: dict, output_folder: str = "translations"):
    """
    Saves translation result to a JSON file.
    
    Args:
        result (dict): Translation result dictionary
        output_folder (str): Folder to save results
    """
    import os
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_folder}/translation_{timestamp}.json"
    
    # Save to file
    with open(filename, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"Translation saved to: {filename}")
    return filename

# Test saving
if batch_results:
    for idx, result in enumerate(batch_results):
        save_translation_result(result, output_folder="translations")
```

2. Run the cell.

### Part 10: Validate Translation Agent

1. Create a final test cell with complex Oracle SQL:

```python
# Complex test with cursor and exception handling
complex_oracle_sql = """
DECLARE
    CURSOR emp_cursor IS
        SELECT employee_id, salary, department_id
        FROM employees
        WHERE department_id = 50;
    
    v_emp_id NUMBER;
    v_salary NUMBER;
    v_dept_id NUMBER;
    v_total_salary NUMBER := 0;
BEGIN
    OPEN emp_cursor;
    
    LOOP
        FETCH emp_cursor INTO v_emp_id, v_salary, v_dept_id;
        EXIT WHEN emp_cursor%NOTFOUND;
        
        v_total_salary := v_total_salary + NVL(v_salary, 0);
        
        DBMS_OUTPUT.PUT_LINE('Employee: ' || v_emp_id || ', Salary: ' || v_salary);
    END LOOP;
    
    CLOSE emp_cursor;
    
    DBMS_OUTPUT.PUT_LINE('Total Salary: ' || v_total_salary);
    
EXCEPTION
    WHEN OTHERS THEN
        IF emp_cursor%ISOPEN THEN
            CLOSE emp_cursor;
        END IF;
        RAISE;
END;
"""

print("Translating complex Oracle PL/SQL block...\n")
result = translate_oracle_to_azure_sql(complex_oracle_sql)

if result["success"]:
    print("Translated Azure SQL:")
    print(result["translated_sql"])
    print(f"\nTokens used: {result['tokens_used']}")
else:
    print(f"Translation failed: {result['error']}")
```

2. Run the cell and verify the translation handles cursors, loops, and exception handling correctly.

## Success Criteria

- Azure AI Foundry notebook environment set up successfully
- Azure OpenAI client configured and connected
- Translation system prompt designed with comprehensive conversion rules
- Translation agent function created and tested
- Simple SELECT queries translated correctly (NVL, TO_CHAR, TO_DATE functions)
- Stored procedures translated with proper parameter handling
- Batch translation function processes multiple queries
- Retry logic implemented for handling failures
- Translation results saved to JSON files
- Complex PL/SQL blocks (cursors, loops, exceptions) translated successfully
- All tests demonstrate accurate Oracle to Azure SQL conversion

## Additional Resources

- [Azure OpenAI Service API Reference](https://learn.microsoft.com/azure/ai-services/openai/reference)
- [Oracle to SQL Server Migration Guide](https://learn.microsoft.com/sql/sql-server/migrate/guides/oracle-to-sql-server)
- [T-SQL Function Reference](https://learn.microsoft.com/sql/t-sql/functions/functions)
- [Prompt Engineering for Code Translation](https://learn.microsoft.com/azure/ai-services/openai/concepts/advanced-prompt-engineering)

Now, click **Next** to continue to **Challenge 03**.
