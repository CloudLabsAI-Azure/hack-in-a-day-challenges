# Challenge 04: Create Optimization Agent and Complete Pipeline

## Introduction

Your SQL translation and validation pipeline is working! Now you'll add the final agent: the Optimization Agent. This agent analyzes translated Azure SQL code and provides performance recommendations including indexes, query hints, and Azure-specific features. You'll connect it to complete the three-agent pipeline where data flows automatically through translation → validation → optimization.

## Challenge Objectives

- Create an Optimization Agent with performance analysis instructions
- Configure the agent to provide actionable Azure SQL recommendations
- Test optimization capabilities with sample queries
- **Connect the Optimization Agent to the Validation Agent**
- Test the complete three-agent pipeline
- Verify all results flow through automatically

## Steps to Complete

### Part 1: Create Optimization Agent

1. In **Microsoft Foundry Studio**, navigate to **Agents**.

2. Click **+ New agent**.

3. Configure:
   - **Agent name**: `SQL-Optimization-Agent`
   - **Deployment**: **sql-translator**

### Part 2: Write Optimization Instructions

1. In the **Instructions** box, paste:

   ```
   You are an Azure SQL Database performance optimization expert. Your role is to analyze T-SQL code and provide specific, actionable optimization recommendations.

   OPTIMIZATION ANALYSIS:

   1. Index Recommendations:
      - Identify columns used in WHERE clauses → suggest non-clustered indexes
      - Identify columns in JOIN conditions → suggest covering indexes
      - Identify columns in ORDER BY → suggest index with INCLUDE columns
      - Flag frequently filtered columns for indexing
      - Recommend columnstore indexes for large analytical queries (> 1M rows)

   2. Query Performance:
      - Identify functions on columns in WHERE (e.g., WHERE YEAR(date) = 2023) → suggest computed columns or index views
      - Flag SELECT * → recommend explicit column lists
      - Identify implicit type conversions → suggest explicit CAST/CONVERT
      - Flag cursors → suggest set-based alternatives
      - Identify nested subqueries → suggest CTEs or JOINs

   3. Azure SQL Specific Features:
      - Suggest In-Memory OLTP for hot tables with high read/write activity
      - Recommend Intelligent Query Processing for complex analytics
      - Suggest Query Store for tracking performance over time
      - Recommend Automatic Tuning for index management
      - Suggest partitioning for very large tables (> 100GB)

   4. Query Hints and Settings:
      - Recommend NOLOCK only when dirty reads acceptable
      - Suggest RECOMPILE for queries with parameter sniffing issues
      - Recommend SET NOCOUNT ON for procedures
      - Suggest appropriate transaction isolation levels

   5. Rewrite Suggestions:
      - Cursor-based updates → SET-based UPDATE with JOIN
      - Multiple separate queries → Batch with CTEs
      - Scalar functions in SELECT → Inline calculations or table-valued functions
      - Row-by-row processing → Set-based operations

   OUTPUT FORMAT (JSON):
   {
   "optimization_score": 0 to 100,
   "priority_recommendations": [
      {
         "priority": "HIGH" | "MEDIUM" | "LOW",
         "category": "Index" | "Query Rewrite" | "Azure Feature" | "Performance",
         "recommendation": "Specific action to take",
         "reason": "Why this helps",
         "estimated_impact": "Expected improvement (e.g., 30-50% faster)",
         "implementation": "SQL code or steps to implement"
      }
   ],
   "index_recommendations": [
      {
         "table": "table_name",
         "index_name": "IX_TableName_Column",
         "columns": "column_list",
         "index_type": "Non-clustered" | "Clustered" | "Columnstore",
         "include_columns": "optional_columns",
         "create_statement": "CREATE INDEX statement"
      }
   ],
   "azure_features": [
      {
         "feature": "Feature name",
         "benefit": "Performance or functionality benefit",
         "how_to_enable": "Implementation steps"
      }
   ],
   "rewrite_examples": [
      {
         "current_code": "Existing inefficient pattern",
         "optimized_code": "Improved version",
         "improvement": "What this achieves"
      }
   ]
   }

   Score Guidelines:
   - 90-100: Excellent, already well-optimized
   - 70-89: Good, minor improvements possible
   - 50-69: Moderate, significant optimizations available
   - Below 50: Poor, needs major restructuring
   ```

2. Save the instructions.

### Part 3: Add Agent Description

1. Expand **Agent Description**:

   ```
   Analyzes Azure SQL T-SQL code and provides performance optimization recommendations including indexes, query rewrites, and Azure-specific features. Returns structured JSON with prioritized suggestions.
   ```

### Part 4: Test Optimization Agent Independently

1. Click **Try in playground**.

2. Test with a simple query:

   ```sql
   SELECT emp_id, emp_name, hire_date, salary
   FROM employees
   WHERE hire_date > DATEADD(DAY, -30, GETDATE())
   ORDER BY salary DESC;
   ```

3. Verify it suggests:
   - Index on `hire_date` column
   - Possibly covering index with `salary`

4. Test with a cursor-based query:

   ```sql
   DECLARE @emp_id INT, @bonus DECIMAL(10,2);
   DECLARE emp_cursor CURSOR FOR SELECT emp_id FROM employees WHERE dept_id = 10;
   OPEN emp_cursor;
   FETCH NEXT FROM emp_cursor INTO @emp_id;
   WHILE @@FETCH_STATUS = 0
   BEGIN
      SET @bonus = (SELECT salary * 0.1 FROM employees WHERE emp_id = @emp_id);
      UPDATE employees SET bonus = @bonus WHERE emp_id = @emp_id;
      FETCH NEXT FROM emp_cursor INTO @emp_id;
   END;
   CLOSE emp_cursor;
   DEALLOCATE emp_cursor;
   ```

5. Verify it suggests a set-based rewrite:

   ```sql
   UPDATE employees
   SET bonus = salary * 0.1
   WHERE dept_id = 10;
   ```

### Part 5: Connect Optimization Agent to Translation Agent

> **Note**: Due to Microsoft Foundry limitations, an agent that is already connected (like Validation Agent) cannot have its own connected agents. Therefore, we'll connect the Optimization Agent directly to the Translation Agent as a second connected agent.

1. Go to **Agents** list.

2. Click on **SQL-Translation-Agent** (the first agent).

3. In the **Setup** panel on the right, scroll to **Connected agents** section.

4. You should already see **validation_agent** listed. Click **+ Add** to add a second connected agent.

5. In the **Adding a connected agent** dialog, configure:
   - **Agent**: Select **SQL-Optimization-Agent** from dropdown
   - **Unique name**: Enter `optimization_agent`
   - **Tools**: (Shows agent tools if any - leave as is)
   - **Detail the steps to activate the agent**: Enter:

      ```
      After the translation is complete and validation has passed, automatically transfer the translated SQL to the SQL-Optimization-Agent for performance analysis and optimization recommendations.
      ```

6. Click **Add**.

7. You should now see both connected agents listed:
   - validation_agent
   - optimization_agent

### Part 6: Update Translation Agent Instructions

1. Still in **SQL-Translation-Agent**, scroll to the **Instructions** text box.

2. Find the `PIPELINE INSTRUCTIONS` section you added in Challenge 3 and **replace it** with this updated version:

   ```
   PIPELINE INSTRUCTIONS (MANDATORY):
   After translating the Oracle SQL to Azure SQL T-SQL, you MUST execute these steps in order:
   1. Hand off the translated T-SQL code to validation_agent for syntax and semantic validation
   2. After validation completes, hand off the translated T-SQL code to optimization_agent for performance analysis and optimization recommendations
   3. Include the results from all three stages (translation, validation, optimization) in your final response
   ```

3. Your complete Translation Agent instructions should now end with:

   ```
   OUTPUT REQUIREMENTS:
   - Return the translated Azure SQL T-SQL code inside a ```sql code block
   - Do NOT include explanations or commentary about the translation process
   - Preserve the original query logic and structure
   - Ensure proper T-SQL syntax
   - Maintain readability with proper indentation

   PIPELINE INSTRUCTIONS (MANDATORY):
   After translating the Oracle SQL to Azure SQL T-SQL, you MUST execute these steps in order:
   1. Hand off the translated T-SQL code to validation_agent for syntax and semantic validation
   2. After validation completes, hand off the translated T-SQL code to optimization_agent for performance analysis and optimization recommendations
   3. Include the results from all three stages (translation, validation, optimization) in your final response
   ```

4. The agent will auto-save.

### Part 7: Test the Complete Three-Agent Pipeline

1. Go back to **SQL-Translation-Agent** (the first agent).

2. Click **Try in playground**.

3. Send this Oracle query:

   ```sql
   SELECT emp_id, emp_name, NVL(commission, 0) as commission
   FROM employees
   WHERE hire_date > SYSDATE - 90
   AND ROWNUM <= 20
   ORDER BY commission DESC;
   ```

4. Watch the magic happen:

   - **Agent 1 (Translation)**: Translates to T-SQL
   - **Agent 2 (Validation)**: Validates syntax (should be valid)
   - **Agent 3 (Optimization)**: Analyzes and suggests optimizations

5. Verify you see results from ALL THREE agents in sequence.

### Part 8: Test with Complex Query

1. Test with Oracle hierarchical query:

   ```sql
   SELECT emp_id, emp_name, manager_id, LEVEL as emp_level
   FROM employees
   START WITH manager_id IS NULL
   CONNECT BY PRIOR emp_id = manager_id;
   ```

2. Verify the pipeline:
   - Translates to recursive CTE
   - Validates the CTE syntax
   - Suggests optimization (maybe index on manager_id and emp_id)

### Part 9: Test Error Handling in Pipeline

1. Send malformed Oracle SQL:

   ```sql
   SELECT emp_id, emp_name FROM employees WHERE dept_id =;
   ```

2. Observe:
   - Translation Agent tries to translate
   - Validation Agent finds error and STOPS (doesn't hand off)
   - Optimization Agent is NOT called
   - You only see Translation and Validation results

3. This confirms the pipeline properly handles failures!

### Part 10: Test Performance Scenario

1. Send a query that needs optimization:

   ```sql
   SELECT o.OrderID, c.CustomerName, o.OrderDate, o.TotalAmount
   FROM Orders o, Customers c
   WHERE o.CustomerID = c.CustomerID
   AND YEAR(o.OrderDate) = 2023
   ORDER BY o.OrderDate DESC;
   ```

2. Verify Optimization Agent suggests:
   - Change old-style join to INNER JOIN
   - Add index or computed column for `YEAR(OrderDate)`
   - Possibly rewrite to avoid function on column

### Part 11: Document Agent IDs

1. Go to **Agents** list.

2. Copy all three Agent IDs:
   - **SQL-Translation-Agent**: `asst_xxxxx`
   - **SQL-Validation-Agent**: `asst_yyyyy`
   - **SQL-Optimization-Agent**: `asst_zzzzz`

3. Save these - you'll need them in Challenge 6 for API calls.

## Success Criteria

- Optimization Agent created successfully
- Agent analyzes queries and provides optimization score
- Agent suggests specific index recommendations
- Agent identifies cursor-based code and suggests set-based rewrites
- Agent recommends Azure SQL specific features
- Optimization Agent connected to Validation Agent
- Three-agent pipeline works end-to-end: Translation → Validation → Optimization
- Valid SQL flows through all three agents
- Invalid SQL stops at Validation (doesn't reach Optimization)
- Complex queries (CTEs, joins) get meaningful optimization suggestions
- All agent IDs documented for API integration

## Additional Resources

- [Azure SQL Performance Best Practices](https://learn.microsoft.com/azure/azure-sql/database/performance-guidance)
- [Index Design Guidelines](https://learn.microsoft.com/sql/relational-databases/sql-server-index-design-guide)
- [Intelligent Query Processing](https://learn.microsoft.com/sql/relational-databases/performance/intelligent-query-processing)

Now, click **Next** to continue to **Challenge 05**.
