# Challenge 04: Build the Optimization Agent

## Introduction

The Optimization Agent analyzes translated Azure SQL code and provides performance improvement recommendations tailored to Azure SQL Database. This agent identifies missing indexes, suggests query hints, recommends rewriting patterns, and highlights Azure-specific optimization opportunities. The goal is to ensure migrated code performs optimally in the cloud environment.

## Challenge Objectives

- Create an Optimization Agent using Azure OpenAI
- Analyze translated SQL for performance bottlenecks
- Suggest Azure SQL specific optimizations (indexes, hints, statistics)
- Identify query patterns that benefit from rewriting
- Generate optimization reports with priority rankings
- Test optimization suggestions with sample queries

## Steps to Complete

### Part 1: Create Optimization Agent Notebook

1. In **Azure AI Foundry Studio**, create a new notebook named `Optimization_Agent`.

2. In the first cell, import libraries:

```python
from openai import AzureOpenAI
import json
from datetime import datetime

print("Optimization libraries imported")
```

3. Run the cell.

### Part 2: Configure Azure OpenAI Connection

1. Add a new cell with OpenAI configuration:

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

print("Azure OpenAI client initialized for optimization")
```

2. Run the cell.

### Part 3: Design Optimization Prompt

1. Add a new cell with the optimization system prompt:

```python
OPTIMIZATION_SYSTEM_PROMPT = """You are an expert Azure SQL Database performance tuning specialist.
Your task is to analyze T-SQL code and provide actionable optimization recommendations specifically for Azure SQL Database.

Optimization Analysis Areas:

1. Index Recommendations:
   - Identify missing indexes based on WHERE, JOIN, and ORDER BY clauses
   - Suggest covering indexes for frequently accessed columns
   - Recommend columnstore indexes for large analytical queries
   - Flag over-indexing or redundant indexes

2. Query Performance:
   - Identify missing statistics or outdated statistics
   - Suggest query hints (NOLOCK, RECOMPILE, OPTIMIZE FOR, etc.)
   - Recommend SET options (NOCOUNT ON, ARITHABORT, etc.)
   - Flag expensive operations (functions on columns, implicit conversions)

3. Azure SQL Specific Optimizations:
   - Suggest In-Memory OLTP opportunities for hot tables
   - Recommend Intelligent Query Processing features
   - Identify opportunities for Query Store optimization
   - Suggest appropriate service tier based on workload patterns

4. Code Rewriting Suggestions:
   - Replace cursors with set-based operations
   - Optimize subqueries to CTEs or JOINs
   - Suggest batch operations instead of row-by-row updates
   - Recommend temp tables vs table variables based on size

5. Best Practices:
   - Parameterize queries to avoid SQL injection and enable plan reuse
   - Use appropriate transaction isolation levels
   - Minimize locking and blocking with proper indexing
   - Suggest partitioning for very large tables

Output Format:
Provide a JSON response with:
- overall_score (0-100, where 100 is perfectly optimized)
- priority_optimizations (array of high-impact changes)
- index_recommendations (array of index suggestions)
- query_rewrites (array of rewrite suggestions)
- azure_features (array of Azure-specific features to use)
- performance_warnings (array of potential performance issues)

Example response:
{
  "overall_score": 65,
  "priority_optimizations": [
    {
      "priority": "HIGH",
      "category": "Index",
      "recommendation": "Add non-clustered index on Employees(DepartmentID, Salary)",
      "reason": "Frequent filtering and sorting on these columns",
      "estimated_impact": "50-70% query time reduction"
    }
  ],
  "index_recommendations": [...],
  "query_rewrites": [...],
  "azure_features": [...],
  "performance_warnings": [...]
}

Analyze the provided T-SQL code and return only the JSON response."""

print("Optimization prompt configured")
```

2. Run the cell.

### Part 4: Create Optimization Analysis Function

1. Add a new cell with the core optimization function:

```python
def analyze_sql_optimization(sql_code: str, query_context: dict = None) -> dict:
    """
    Analyzes SQL code and provides optimization recommendations.
    
    Args:
        sql_code (str): T-SQL code to optimize
        query_context (dict): Optional context (table sizes, workload patterns, etc.)
    
    Returns:
        dict: Optimization recommendations
    """
    try:
        # Prepare analysis message
        user_message = f"Analyze the following Azure SQL T-SQL code for optimization opportunities:\n\n{sql_code}"
        
        if query_context:
            user_message += f"\n\nQuery Context:\n{json.dumps(query_context, indent=2)}"
        
        # Call Azure OpenAI
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": OPTIMIZATION_SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,
            max_tokens=3000,
            response_format={"type": "json_object"}
        )
        
        # Parse optimization result
        optimization_json = response.choices[0].message.content.strip()
        optimization_result = json.loads(optimization_json)
        
        # Add metadata
        optimization_result["analyzed_sql"] = sql_code
        optimization_result["timestamp"] = datetime.now().isoformat()
        optimization_result["tokens_used"] = response.usage.total_tokens
        
        return optimization_result
        
    except json.JSONDecodeError as e:
        return {
            "overall_score": 0,
            "error": f"Failed to parse optimization response: {str(e)}",
            "priority_optimizations": [],
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "overall_score": 0,
            "error": f"Optimization analysis failed: {str(e)}",
            "priority_optimizations": [],
            "timestamp": datetime.now().isoformat()
        }

print("Optimization analysis function created")
```

2. Run the cell.

### Part 5: Test Optimization with Sample Queries

1. Add a new cell to test with a suboptimal query:

```python
# Test with a query that needs optimization
suboptimal_query = """
SELECT e.EmployeeID, e.FirstName, e.LastName, d.DepartmentName, e.Salary
FROM Employees e, Departments d
WHERE e.DepartmentID = d.DepartmentID
  AND e.Salary > 50000
  AND YEAR(e.HireDate) = 2023
ORDER BY e.Salary DESC;
"""

print("Analyzing suboptimal query...\n")
optimization_result = analyze_sql_optimization(suboptimal_query)

print(f"Overall Optimization Score: {optimization_result.get('overall_score', 0)}/100")
print(f"\nPriority Optimizations: {len(optimization_result.get('priority_optimizations', []))}")

for idx, opt in enumerate(optimization_result.get('priority_optimizations', [])[:5], 1):
    print(f"\n{idx}. [{opt.get('priority', 'MEDIUM')}] {opt.get('category', 'General')}")
    print(f"   Recommendation: {opt.get('recommendation', '')}")
    print(f"   Reason: {opt.get('reason', '')}")
    print(f"   Impact: {opt.get('estimated_impact', 'Unknown')}")
```

2. Run the cell and review the optimization suggestions.

### Part 6: Test with Cursor-Based Code

1. Add a new cell to test with cursor code that should be rewritten:

```python
# Test with cursor-based code (should suggest set-based approach)
cursor_query = """
DECLARE @EmployeeID INT;
DECLARE @Bonus DECIMAL(10,2);

DECLARE employee_cursor CURSOR FOR
    SELECT EmployeeID FROM Employees WHERE DepartmentID = 10;

OPEN employee_cursor;

FETCH NEXT FROM employee_cursor INTO @EmployeeID;

WHILE @@FETCH_STATUS = 0
BEGIN
    SET @Bonus = (SELECT Salary * 0.1 FROM Employees WHERE EmployeeID = @EmployeeID);
    
    UPDATE Employees
    SET Bonus = @Bonus
    WHERE EmployeeID = @EmployeeID;
    
    FETCH NEXT FROM employee_cursor INTO @EmployeeID;
END;

CLOSE employee_cursor;
DEALLOCATE employee_cursor;
"""

print("Analyzing cursor-based code...\n")
cursor_optimization = analyze_sql_optimization(cursor_query)

print(f"Overall Optimization Score: {cursor_optimization.get('overall_score', 0)}/100\n")

# Show rewrite suggestions
rewrites = cursor_optimization.get('query_rewrites', [])
if rewrites:
    print("Query Rewrite Suggestions:")
    for idx, rewrite in enumerate(rewrites, 1):
        print(f"\n{idx}. {rewrite.get('suggestion', '')}")
        print(f"   Reason: {rewrite.get('reason', '')}")
        if 'rewritten_code' in rewrite:
            print(f"   Rewritten Code:\n{rewrite['rewritten_code']}")
else:
    print("No rewrite suggestions found")
```

2. Run the cell.

### Part 7: Add Query Context for Better Recommendations

1. Add a new cell to provide table statistics for more accurate optimization:

```python
# Provide context about table sizes and workload
query_with_context = """
SELECT o.OrderID, c.CustomerName, o.OrderDate, o.TotalAmount
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE o.OrderDate >= '2023-01-01'
  AND o.Status = 'Completed'
ORDER BY o.OrderDate DESC;
"""

context_info = {
    "table_statistics": {
        "Orders": {
            "row_count": 5000000,
            "avg_row_size_kb": 2.5,
            "growth_rate": "10000 rows/day"
        },
        "Customers": {
            "row_count": 500000,
            "avg_row_size_kb": 1.2
        }
    },
    "workload_pattern": "OLTP with frequent reads",
    "query_frequency": "Executed 1000+ times per day",
    "current_performance": "Average execution time: 2.5 seconds"
}

print("Analyzing query with context...\n")
context_optimization = analyze_sql_optimization(query_with_context, context_info)

print(f"Overall Score: {context_optimization.get('overall_score', 0)}/100\n")

# Show index recommendations
indexes = context_optimization.get('index_recommendations', [])
if indexes:
    print("Index Recommendations:")
    for idx, index in enumerate(indexes, 1):
        print(f"\n{idx}. {index.get('index_name', '')}")
        print(f"   Type: {index.get('index_type', '')}")
        print(f"   Columns: {index.get('columns', '')}")
        print(f"   Reason: {index.get('reason', '')}")
```

2. Run the cell.

### Part 8: Identify Azure-Specific Features

1. Add a new cell to highlight Azure SQL features:

```python
# Complex analytical query that could benefit from Azure features
analytical_query = """
SELECT 
    DepartmentID,
    YEAR(HireDate) as HireYear,
    COUNT(*) as EmployeeCount,
    AVG(Salary) as AvgSalary,
    SUM(Salary) as TotalSalary
FROM Employees
WHERE HireDate >= '2020-01-01'
GROUP BY DepartmentID, YEAR(HireDate)
HAVING COUNT(*) > 10
ORDER BY DepartmentID, HireYear;
"""

print("Analyzing for Azure SQL specific features...\n")
azure_optimization = analyze_sql_optimization(analytical_query)

# Show Azure-specific recommendations
azure_features = azure_optimization.get('azure_features', [])
if azure_features:
    print("Azure SQL Features to Consider:")
    for idx, feature in enumerate(azure_features, 1):
        print(f"\n{idx}. {feature.get('feature_name', '')}")
        print(f"   Benefit: {feature.get('benefit', '')}")
        print(f"   Implementation: {feature.get('implementation_notes', '')}")
else:
    print("No Azure-specific features suggested")
```

2. Run the cell.

### Part 9: Generate Optimization Report

1. Add a new cell to create detailed reports:

```python
def generate_optimization_report(optimization_result: dict) -> str:
    """
    Generates a comprehensive optimization report.
    
    Args:
        optimization_result (dict): Optimization analysis results
    
    Returns:
        str: Formatted report
    """
    report = []
    report.append("="*80)
    report.append("SQL OPTIMIZATION REPORT")
    report.append("="*80)
    report.append(f"Timestamp: {optimization_result.get('timestamp', 'N/A')}")
    report.append(f"Overall Optimization Score: {optimization_result.get('overall_score', 0)}/100")
    report.append("")
    
    # Priority optimizations
    priorities = optimization_result.get('priority_optimizations', [])
    if priorities:
        report.append("HIGH PRIORITY OPTIMIZATIONS:")
        for idx, opt in enumerate(priorities, 1):
            report.append(f"\n{idx}. [{opt.get('priority', 'MEDIUM')}] {opt.get('category', '')}")
            report.append(f"   {opt.get('recommendation', '')}")
            report.append(f"   Reason: {opt.get('reason', '')}")
            report.append(f"   Est. Impact: {opt.get('estimated_impact', 'Unknown')}")
        report.append("")
    
    # Index recommendations
    indexes = optimization_result.get('index_recommendations', [])
    if indexes:
        report.append("INDEX RECOMMENDATIONS:")
        for idx, index in enumerate(indexes, 1):
            report.append(f"\n{idx}. {index.get('index_name', 'Recommended Index')}")
            report.append(f"   Type: {index.get('index_type', 'Non-clustered')}")
            report.append(f"   Columns: {index.get('columns', '')}")
        report.append("")
    
    # Performance warnings
    warnings = optimization_result.get('performance_warnings', [])
    if warnings:
        report.append("PERFORMANCE WARNINGS:")
        for idx, warning in enumerate(warnings, 1):
            report.append(f"  {idx}. {warning}")
        report.append("")
    
    report.append("="*80)
    
    return "\n".join(report)

# Generate report for previous optimization
print(generate_optimization_report(azure_optimization))
```

2. Run the cell.

### Part 10: Save Optimization Results

1. Add a final cell to persist optimization results:

```python
def save_optimization_result(optimization_result: dict, output_folder: str = "optimizations"):
    """
    Saves optimization results to JSON file.
    
    Args:
        optimization_result (dict): Optimization analysis results
        output_folder (str): Output directory
    
    Returns:
        str: File path
    """
    import os
    
    os.makedirs(output_folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_folder}/optimization_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(optimization_result, f, indent=2)
    
    # Also save the report
    report_filename = f"{output_folder}/optimization_report_{timestamp}.txt"
    report = generate_optimization_report(optimization_result)
    
    with open(report_filename, 'w') as f:
        f.write(report)
    
    print(f"Optimization results saved to: {filename}")
    print(f"Optimization report saved to: {report_filename}")
    
    return filename

# Save all optimization results
save_optimization_result(cursor_optimization)
save_optimization_result(context_optimization)
save_optimization_result(azure_optimization)
```

2. Run the cell.

## Success Criteria

- Optimization Agent notebook created successfully
- Azure OpenAI client configured for optimization analysis
- Optimization prompt designed with comprehensive performance rules
- Optimization function analyzes SQL and returns JSON recommendations
- Suboptimal queries identified with specific improvement suggestions
- Cursor-based code flagged with set-based rewrite recommendations
- Index recommendations provided based on query patterns
- Azure SQL specific features suggested (columnstore, In-Memory OLTP, etc.)
- Query context (table sizes, workload) considered for accurate recommendations
- Optimization reports generated in readable format
- Results saved to JSON files for audit trail

## Additional Resources

- [Azure SQL Database Performance Best Practices](https://learn.microsoft.com/azure/azure-sql/database/performance-guidance)
- [Index Design Guidelines](https://learn.microsoft.com/sql/relational-databases/sql-server-index-design-guide)
- [Intelligent Query Processing](https://learn.microsoft.com/sql/relational-databases/performance/intelligent-query-processing)
- [Azure SQL In-Memory Technologies](https://learn.microsoft.com/azure/azure-sql/in-memory-oltp-overview)

Now, click **Next** to continue to **Challenge 05**.
