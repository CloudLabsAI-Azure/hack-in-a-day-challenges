# Challenge 02: Create the Translation Agent

## Introduction

In this challenge, you will create your first AI agent directly in the Microsoft Foundry UI. The Translation Agent is responsible for converting Oracle PL/SQL syntax to Azure SQL T-SQL syntax using the GPT-4.1 model you deployed in Challenge 1. You will configure the agent with specialized instructions, set up the deployment, and test it using the playground.

## Challenge Objectives

- Navigate to the Agents section in Microsoft Foundry Studio
- Create a new Translation Agent with a descriptive name
- Configure the agent to use your GPT-4.1 deployment
- Write comprehensive instructions for Oracle to Azure SQL translation
- Test the agent with sample Oracle SQL queries
- Verify translation accuracy and adjust instructions if needed

## Steps to Complete

### Task 1: Navigate to Agents Section

1. Open **Microsoft Foundry Studio** (https://ai.azure.com).

1. Select your project: **sql-modernize-<inject key="DeploymentID" enableCopy="false"/>** (from Challenge 1).

1. In the left navigation menu, under **Build and customize**. Click on **Agents**.

1. You should see a **Defualt Agent** on the *Create and debug your agents* page.

### Task 2: Create Translation Agent

1. Click on the **defualt Agent**.

1. In the **Setup** panel on the right, configure:

   - **Agent name**: Rename it to `SQL-Translation-Agent`
   - **Deployment**: Select **sql-translator** (the deployment from Challenge 1)
   - **Temperature**: 1 (default)
   - **Top P**: 1 (default)

1. The system will auto-generate an **Agent ID** (e.g., asst_xxxxx). Keep this for reference.

<validation step="9a022344-6b1a-48a9-9788-7b5183d1593e" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 3: Write Agent Instructions

1. In the **Instructions** text box, copy and paste the following complete instructions:

      ```
      You are an expert SQL translation specialist. Your role is to convert Oracle PL/SQL code to Azure SQL T-SQL code with 100% accuracy.

      TRANSLATION RULES:

      1. Date Functions:
         - Oracle SYSDATE → Azure SQL GETDATE()
         - Oracle CURRENT_DATE → Azure SQL CAST(GETDATE() AS DATE)
         - Oracle TO_DATE(string, format) → Azure SQL CONVERT(DATETIME, string, style_code)
         - Oracle TRUNC(date) → Azure SQL CAST(date AS DATE)
         - Oracle ADD_MONTHS(date, n) → Azure SQL DATEADD(MONTH, n, date)

      2. String Functions:
         - Oracle NVL(expr1, expr2) → Azure SQL ISNULL(expr1, expr2) or COALESCE(expr1, expr2)
         - Oracle NVL2(expr, val1, val2) → Azure SQL CASE WHEN expr IS NOT NULL THEN val1 ELSE val2 END
         - Oracle SUBSTR(str, start, length) → Azure SQL SUBSTRING(str, start, length)
         - Oracle INSTR(str, substr) → Azure SQL CHARINDEX(substr, str)
         - Oracle LENGTH(str) → Azure SQL LEN(str)
         - Oracle CONCAT(str1, str2) → Azure SQL CONCAT(str1, str2) or str1 + str2

      3. Conditional Logic:
         - Oracle DECODE(expr, search1, result1, search2, result2, default) → Azure SQL CASE WHEN expr = search1 THEN result1 WHEN expr = search2 THEN result2 ELSE default END

      4. Row Limiting:
         - Oracle ROWNUM <= N → Azure SQL TOP N
         - Oracle FETCH FIRST N ROWS ONLY → Azure SQL TOP N
         - Oracle OFFSET n ROWS FETCH NEXT m ROWS ONLY → Azure SQL OFFSET n ROWS FETCH NEXT m ROWS ONLY (same syntax)

      5. Joins:
         - Oracle (+) outer join syntax → Azure SQL LEFT JOIN or RIGHT JOIN
         - Example: WHERE a.id = b.id(+) → FROM a LEFT JOIN b ON a.id = b.id

      6. Hierarchical Queries:
         - Oracle START WITH ... CONNECT BY PRIOR → Azure SQL Recursive Common Table Expressions (CTE)
         - Example pattern:
         Oracle: SELECT * FROM employees START WITH manager_id IS NULL CONNECT BY PRIOR emp_id = manager_id
         Azure SQL: WITH RecursiveCTE AS (SELECT * FROM employees WHERE manager_id IS NULL UNION ALL SELECT e.* FROM employees e INNER JOIN RecursiveCTE r ON e.manager_id = r.emp_id) SELECT * FROM RecursiveCTE

      7. Sequences:
         - Oracle sequence_name.NEXTVAL → Azure SQL NEXT VALUE FOR sequence_name
         - Oracle sequence_name.CURRVAL → Not directly supported (use variables or OUTPUT clause)

      8. Data Types:
         - Oracle VARCHAR2 → Azure SQL VARCHAR or NVARCHAR
         - Oracle NUMBER → Azure SQL INT, BIGINT, DECIMAL, or FLOAT (choose based on precision)
         - Oracle CLOB → Azure SQL VARCHAR(MAX) or NVARCHAR(MAX)
         - Oracle BLOB → Azure SQL VARBINARY(MAX)

      9. Dual Table:
         - Oracle SELECT ... FROM DUAL → Azure SQL SELECT ... (no FROM clause needed for scalar expressions)

      10. PL/SQL to T-SQL:
         - Oracle DECLARE/BEGIN/END blocks → Azure SQL equivalent with proper syntax
         - Oracle CURSOR FOR loops → Azure SQL CURSOR with FETCH NEXT pattern or set-based alternatives
         - Oracle :NEW and :OLD (in triggers) → Azure SQL INSERTED and DELETED tables
         - Oracle RAISE_APPLICATION_ERROR → Azure SQL RAISERROR or THROW

      OUTPUT REQUIREMENTS:
      - Return the translated Azure SQL T-SQL code inside a ```sql code block
      - Do NOT include explanations or commentary about the translation process
      - Preserve the original query logic and structure
      - Ensure proper T-SQL syntax
      - Maintain readability with proper indentation
      ```

1. The agent will auto-save the instructions.

> **Important**: You will add hand-off instructions later in Challenge 3 and Challenge 4 when you connect the other agents.

### Task 4: Configure Agent Description (Optional)

1. Expand the **Agent Description** section.

1. Add a description:

      ```
      Translates Oracle PL/SQL code to Azure SQL T-SQL code using comprehensive syntax conversion rules. This agent handles date functions, string operations, joins, hierarchical queries, and procedural code translation.
      ```

### Task 5: Test the Agent in Playground

1. Click the **Try in playground** button on the top right.

1. In the chat interface, test with this simple Oracle query:

      ```
      SELECT emp_id, emp_name, hire_date
      FROM employees
      WHERE hire_date > SYSDATE - 30
      AND ROWNUM <= 10;
      ```

1. Send the message and wait for the response.

1. Verify the agent returns Azure SQL like:

      ```sql
      SELECT TOP 10 emp_id, emp_name, hire_date
      FROM employees
      WHERE hire_date > DATEADD(DAY, -30, GETDATE());
      ```

### Task 6: Test with More Complex Query

1. Test with an Oracle NVL and DECODE query:

      ```
      SELECT emp_id,
            emp_name,
            NVL(commission, 0) AS commission,
            DECODE(dept_id, 10, 'Sales', 20, 'Marketing', 'Other') AS department
      FROM employees;
      ```

2. Verify the translation uses ISNULL/COALESCE and CASE WHEN.

### Task 7: Test with Cursor-Based Code

1. Test with Oracle PL/SQL procedure:

      ```
      DECLARE
      CURSOR emp_cursor IS
         SELECT emp_id, salary FROM employees WHERE dept_id = 10;
      BEGIN
      FOR emp_rec IN emp_cursor LOOP
         UPDATE employees
         SET bonus = emp_rec.salary * 0.1
         WHERE emp_id = emp_rec.emp_id;
      END LOOP;
      COMMIT;
      END;
      ```

2. Verify the agent converts it to T-SQL cursor syntax or suggests a set-based approach.

### Task 8: Refine Instructions (If Needed)

1. If the translations aren't accurate, go back to the agent configuration.

2. Update the **Instructions** to be more specific about problem areas.

3. Test again in the playground.

4. Repeat until translations are consistently accurate.

### Task 9: Save and Note Agent ID

1. The agent auto-saves as you make changes.

2. In the **Setup** panel on the right, locate the **Agent ID** field.

3. Copy the **Agent ID** (e.g., `asst_4suaVDw2ZsziL9sShpoyeoDM`).

4. Save this ID in a text file - you'll need it in Challenge 6 for the Streamlit app.

## Success Criteria

- Translation Agent created successfully in Microsoft Foundry
- Agent configured with GPT-4 deployment
- Comprehensive Oracle to Azure SQL translation instructions added
- Agent tested with simple SELECT queries and produces correct T-SQL
- Agent handles NVL, DECODE, ROWNUM, and SYSDATE correctly
- Agent can translate PL/SQL cursor code to T-SQL
- Complex queries (hierarchical, outer joins) translate accurately
- Agent ID copied and saved for later use
- Agent consistently provides clean T-SQL output without extra formatting

## Additional Resources

- [Microsoft Foundry Agents Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/develop/agents)
- [Oracle to Azure SQL Migration Guide](https://learn.microsoft.com/azure/azure-sql/migration-guides/database/oracle-to-sql-database-guide)
- [T-SQL Reference](https://learn.microsoft.com/sql/t-sql/language-reference)

Now, click **Next** to continue to **Challenge 03**.
