# Challenge 03: Create Validation Agent and Connect Pipeline

## Introduction

Now that you have a Translation Agent, you need a Validation Agent to check if the translated SQL is correct. In this challenge, you will create a second agent that validates Azure SQL T-SQL syntax and semantics. More importantly, you will **connect** this agent to your Translation Agent so that translations automatically flow to validation - creating your first multi-agent pipeline!

## Challenge Objectives

- Create a Validation Agent with SQL validation instructions
- Configure the agent to use GPT-4 deployment
- Test validation capabilities with correct and incorrect SQL
- **Connect the Validation Agent to the Translation Agent** using "Connected agents"
- Test the complete pipeline: Translation → Validation
- Verify hand-off works automatically

## Steps to Complete

### Part 1: Create Validation Agent

1. In **Azure AI Foundry Studio**, navigate to **Agents**.

2. Click **+ New agent**.

3. Configure the agent:
   - **Agent name**: `SQL-Validation-Agent`
   - **Deployment**: Select **gpt-4-sql-translator**

### Part 2: Write Validation Instructions

1. In the **Instructions** box, paste:

```
You are an Azure SQL T-SQL validation expert. Your role is to analyze T-SQL code and determine if it is syntactically and semantically correct.

VALIDATION CHECKS:

1. Syntax Validation:
   - Verify all SQL keywords are spelled correctly (SELECT, FROM, WHERE, JOIN, etc.)
   - Check for proper statement termination (semicolons where needed)
   - Validate parentheses, brackets, and quote matching
   - Ensure proper use of commas in column lists
   - Check for invalid SQL keywords or deprecated syntax

2. Semantic Validation:
   - Verify JOIN conditions are present and logical
   - Check that aggregate functions (SUM, COUNT, AVG) are used correctly with GROUP BY
   - Validate WHERE clause conditions make sense
   - Ensure data type compatibility in comparisons
   - Check for potential NULL handling issues

3. Azure SQL Specific:
   - Verify Azure SQL T-SQL functions are used correctly (GETDATE, DATEADD, ISNULL, etc.)
   - Check that deprecated functions are not used
   - Validate TOP N syntax is correct
   - Ensure window functions (ROW_NUMBER, RANK) have proper OVER clauses

4. Best Practices:
   - Flag SELECT * usage (recommend explicit column lists)
   - Identify missing WHERE clauses on UPDATE/DELETE (could affect all rows)
   - Detect potential SQL injection vulnerabilities (dynamic SQL without parameterization)
   - Warn about NOLOCK hints (dirty reads)

OUTPUT FORMAT (JSON):
Return your validation result as a JSON object with this structure:
{
  "valid": true or false,
  "confidence": 0.0 to 1.0,
  "syntax_errors": [
    {"severity": "error", "message": "description", "line": line_number_if_known}
  ],
  "semantic_warnings": [
    {"severity": "warning", "message": "description"}
  ],
  "best_practice_suggestions": [
    "suggestion 1",
    "suggestion 2"
  ],
  "summary": "Brief overall assessment"
}

If the SQL is valid, return valid: true with confidence near 1.0.
If there are errors, return valid: false and list all issues found.
```

2. Save the instructions.

### Part 3: Add Agent Description

1. Expand **Agent Description** and add:
```
Validates Azure SQL T-SQL code for syntax correctness, semantic validity, and best practice compliance. Returns structured JSON with error details and suggestions.
```

### Part 4: Test Validation Agent Independently

1. Click **Try in playground**.

2. Test with VALID SQL:

```sql
SELECT emp_id, emp_name, hire_date
FROM employees
WHERE hire_date > DATEADD(DAY, -30, GETDATE());
```

3. Verify it returns `"valid": true` in JSON format.

4. Test with INVALID SQL (syntax error):

```sql
SELECT emp_id emp_name hire_date
FROM employees
WHERE hire_date > GETDATE()
```

5. Verify it returns `"valid": false` and identifies missing commas.

6. Test with semantic issue:

```sql
SELECT emp_id, SUM(salary)
FROM employees
WHERE dept_id = 10;
```

7. Verify it flags the missing GROUP BY for the aggregate function.

### Part 5: Connect Validation Agent to Translation Agent

Now comes the key part - connecting the agents!

1. Go back to the **Agents** list.

2. Click on your **SQL-Translation-Agent** (the first agent you created).

3. Scroll down to the **Connected agents** section.

4. Click **+ Add**.

5. In the dialog:
   - **Agent**: Select **SQL-Validation-Agent**
   - **Description**: `Validates translated T-SQL for correctness`

6. Click **Add**.

7. You should now see SQL-Validation-Agent listed under Connected agents.

### Part 6: Configure Hand-Off Behavior

1. Still in the Translation Agent configuration, update the **Instructions** to tell it when to hand off.

2. Add this to the END of your Translation Agent instructions:

```
After translating Oracle SQL to Azure SQL T-SQL, automatically hand off the translated code to the SQL-Validation-Agent for validation.
```

3. Save the updated instructions.

### Part 7: Test the Connected Pipeline

1. Go back to **SQL-Translation-Agent**.

2. Click **Try in playground**.

3. Send this Oracle query:

```sql
SELECT emp_id, emp_name, NVL(commission, 0) as comm
FROM employees
WHERE ROWNUM <= 5;
```

4. Observe what happens:
   - Translation Agent translates it to T-SQL
   - Translation Agent automatically hands off to Validation Agent
   - Validation Agent validates the T-SQL
   - You see results from BOTH agents

5. Verify you see:
   - Translated SQL from Agent 1
   - Validation JSON from Agent 2

### Part 8: Test with Complex Query

1. In the same playground, test with hierarchical query:

```sql
SELECT emp_id, emp_name, manager_id, LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR emp_id = manager_id;
```

2. Verify:
   - Agent 1 translates to CTE
   - Agent 2 validates the CTE syntax
   - Both results appear in the conversation

### Part 9: Test Error Handling

1. Intentionally send broken Oracle SQL:

```sql
SELECT emp_id emp_name FROM employees WHERE;
```

2. Observe:
   - Translation Agent attempts translation
   - Validation Agent identifies syntax errors
   - You can see the validation flagged issues

### Part 10: Save Agent IDs

1. Go back to **Agents** list.

2. Note the **Agent ID** for **SQL-Validation-Agent**.

3. Keep both agent IDs (Translation and Validation) saved for Challenge 6.

## Success Criteria

- Validation Agent created successfully
- Agent validates correct SQL with `valid: true` response
- Agent identifies syntax errors in malformed SQL
- Agent flags semantic issues (missing GROUP BY, etc.)
- Agent returns structured JSON format
- Validation Agent successfully connected to Translation Agent
- Pipeline tested: Oracle SQL → Translation → Validation
- Hand-off happens automatically without manual intervention
- Both agent results visible in playground conversation
- Complex queries (CTEs, joins) flow through pipeline correctly

## Additional Resources

- [Azure AI Agents - Connected Agents](https://learn.microsoft.com/azure/ai-studio/how-to/develop/agents#connected-agents)
- [T-SQL Syntax Reference](https://learn.microsoft.com/sql/t-sql/language-reference)
- [Azure SQL Best Practices](https://learn.microsoft.com/azure/azure-sql/database/performance-guidance)

Now, click **Next** to continue to **Challenge 04**.
