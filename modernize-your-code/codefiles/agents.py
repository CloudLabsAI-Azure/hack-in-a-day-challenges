"""
SQL Modernization Agent Module
Provides Translation, Validation, and Optimization agents for Oracle to Azure SQL migration.
"""

from openai import AzureOpenAI
import json
from datetime import datetime
import sqlparse


class SQLModernizationAgent:
    """Multi-agent system for SQL modernization"""
    
    def __init__(self, openai_endpoint: str, openai_key: str, deployment: str, api_version: str):
        """
        Initialize the SQL Modernization Agent.
        
        Args:
            openai_endpoint: Azure OpenAI endpoint URL
            openai_key: Azure OpenAI API key
            deployment: Deployment name (e.g., 'gpt-4-sql-translator')
            api_version: API version (e.g., '2024-02-15-preview')
        """
        self.client = AzureOpenAI(
            azure_endpoint=openai_endpoint,
            api_key=openai_key,
            api_version=api_version
        )
        self.deployment = deployment
    
    def translate_oracle_to_azure_sql(self, oracle_sql: str) -> dict:
        """
        Translates Oracle SQL to Azure SQL T-SQL.
        
        Args:
            oracle_sql: Oracle SQL code to translate
            
        Returns:
            dict: Translation result with success status, translated SQL, and metadata
        """
        
        system_prompt = """You are an expert SQL translator specializing in Oracle to Azure SQL conversions.

Translation Rules:
1. Oracle SYSDATE -> Azure SQL GETDATE()
2. Oracle NVL(expr1, expr2) -> Azure SQL ISNULL(expr1, expr2) or COALESCE(expr1, expr2)
3. Oracle ROWNUM -> Azure SQL ROW_NUMBER() OVER (ORDER BY column) or TOP N
4. Oracle sequence.NEXTVAL -> Azure SQL NEXT VALUE FOR sequence
5. Oracle DECODE(expr, search, result, ..., default) -> Azure SQL CASE WHEN expr = search THEN result ... ELSE default END
6. Oracle (+) outer join syntax -> Azure SQL LEFT JOIN or RIGHT JOIN
7. Oracle CONNECT BY hierarchical queries -> Azure SQL recursive Common Table Expressions (CTE)
8. Oracle TO_DATE(string, format) -> Azure SQL CONVERT(datetime, string, style) or CAST(string AS datetime)
9. Oracle DUAL table -> Not needed in Azure SQL (remove FROM DUAL)
10. Oracle packages/procedures -> Azure SQL stored procedures with T-SQL syntax modifications
11. Oracle VARCHAR2 -> Azure SQL VARCHAR or NVARCHAR
12. Oracle NUMBER -> Azure SQL INT, BIGINT, DECIMAL, or FLOAT
13. Oracle SUBSTR(str, start, length) -> Azure SQL SUBSTRING(str, start, length)
14. Oracle INSTR(str, substr) -> Azure SQL CHARINDEX(substr, str)
15. Oracle TRUNC(date) -> Azure SQL CAST(date AS DATE) or DATEADD(dd, 0, DATEDIFF(dd, 0, date))

Return ONLY valid Azure SQL T-SQL code without explanations, code block markers, or comments."""

        try:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Translate this Oracle SQL to Azure SQL:\n\n{oracle_sql}"}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            translated_sql = response.choices[0].message.content.strip()
            
            # Remove code block markers if present
            if translated_sql.startswith("```sql"):
                translated_sql = translated_sql[6:]
            if translated_sql.startswith("```"):
                translated_sql = translated_sql[3:]
            if translated_sql.endswith("```"):
                translated_sql = translated_sql[:-3]
            
            return {
                "success": True,
                "translated_sql": translated_sql.strip(),
                "tokens_used": response.usage.total_tokens,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "translated_sql": "",
                "timestamp": datetime.now().isoformat()
            }
    
    def validate_sql(self, sql_code: str, use_ai: bool = True, use_parser: bool = True) -> dict:
        """
        Validates SQL code using AI and/or parser-based validation.
        
        Args:
            sql_code: T-SQL code to validate
            use_ai: Whether to use AI-based validation
            use_parser: Whether to use parser-based validation
            
        Returns:
            dict: Validation results with overall validity and detailed findings
        """
        
        validation_prompt = """You are a SQL validation expert for Azure SQL Database. Analyze the provided T-SQL code for:

1. Syntax correctness (proper SQL grammar and structure)
2. Semantic validity (logical consistency and table/column references)
3. Best practice compliance (naming conventions, proper joins, indexing hints)
4. Potential runtime errors (division by zero, type mismatches, NULL handling)
5. Security issues (SQL injection vulnerabilities, improper permissions)

Return ONLY a JSON object with this exact structure:
{
  "valid": true or false,
  "confidence": 0.0 to 1.0,
  "issues": [
    {
      "severity": "error" or "warning" or "info",
      "message": "detailed description of the issue",
      "line": line_number (if applicable, otherwise null)
    }
  ],
  "suggestions": [
    "specific improvement suggestion 1",
    "specific improvement suggestion 2"
  ]
}"""

        results = {
            "overall_valid": False,
            "validations": {},
            "timestamp": datetime.now().isoformat()
        }
        
        # AI-based validation
        if use_ai:
            try:
                response = self.client.chat.completions.create(
                    model=self.deployment,
                    messages=[
                        {"role": "system", "content": validation_prompt},
                        {"role": "user", "content": f"Validate this Azure SQL T-SQL code:\n\n{sql_code}"}
                    ],
                    temperature=0.3,
                    max_tokens=1500,
                    response_format={"type": "json_object"}
                )
                
                ai_result = json.loads(response.choices[0].message.content)
                results["validations"]["ai"] = ai_result
            except Exception as e:
                results["validations"]["ai"] = {
                    "valid": False, 
                    "error": str(e),
                    "confidence": 0.0
                }
        
        # Parser-based validation
        if use_parser:
            try:
                parsed = sqlparse.parse(sql_code)
                
                # Check for parse errors
                has_errors = False
                error_count = 0
                
                for stmt in parsed:
                    tokens = list(stmt.flatten())
                    for token in tokens:
                        if token.ttype is sqlparse.tokens.Error:
                            has_errors = True
                            error_count += 1
                
                parser_valid = len(parsed) > 0 and not has_errors
                
                results["validations"]["parser"] = {
                    "valid": parser_valid,
                    "statement_count": len(parsed),
                    "error_count": error_count,
                    "formatted": sqlparse.format(sql_code, reindent=True, keyword_case='upper')
                }
            except Exception as e:
                results["validations"]["parser"] = {
                    "valid": False, 
                    "error": str(e)
                }
        
        # Determine overall validity
        ai_valid = results["validations"].get("ai", {}).get("valid", False) if use_ai else True
        parser_valid = results["validations"].get("parser", {}).get("valid", False) if use_parser else True
        
        results["overall_valid"] = ai_valid and parser_valid
        
        return results
    
    def optimize_sql(self, sql_code: str, table_context: dict = None) -> dict:
        """
        Provides optimization recommendations for Azure SQL code.
        
        Args:
            sql_code: T-SQL code to optimize
            table_context: Optional dict with table statistics (row counts, sizes, etc.)
            
        Returns:
            dict: Optimization recommendations with score and actionable suggestions
        """
        
        optimization_prompt = """You are an Azure SQL Database performance tuning expert. Analyze the provided T-SQL code and provide optimization recommendations.

Focus Areas:
1. Index Recommendations - Suggest missing indexes based on WHERE, JOIN, ORDER BY clauses
2. Query Performance - Identify expensive operations, implicit conversions, functions on columns
3. Azure SQL Features - Recommend In-Memory OLTP, columnstore indexes, Intelligent Query Processing
4. Code Rewriting - Suggest set-based alternatives to cursors, CTE optimization, subquery improvements
5. Best Practices - Parameterization, proper transaction isolation, minimal locking

Return ONLY a JSON object with this exact structure:
{
  "overall_score": 0 to 100 (integer representing current optimization level),
  "priority_optimizations": [
    {
      "priority": "HIGH" or "MEDIUM" or "LOW",
      "category": "Index" or "Query" or "Azure Feature" or "Code Rewrite",
      "recommendation": "specific actionable recommendation",
      "reason": "why this optimization is needed",
      "estimated_impact": "expected performance improvement (e.g., '30-50% faster')"
    }
  ],
  "index_recommendations": [
    {
      "index_name": "suggested index name (e.g., IX_TableName_Column)",
      "table": "table name",
      "columns": "comma-separated column list",
      "index_type": "Non-clustered" or "Clustered" or "Columnstore",
      "reason": "why this index is recommended"
    }
  ],
  "azure_features": [
    {
      "feature_name": "Azure SQL feature name",
      "benefit": "performance or functionality benefit",
      "implementation_notes": "how to enable or use this feature"
    }
  ],
  "query_rewrites": [
    {
      "current_pattern": "description of current inefficient pattern",
      "suggested_rewrite": "description of better approach",
      "example": "example code snippet (optional)"
    }
  ]
}"""

        try:
            user_content = f"Analyze this Azure SQL T-SQL code for optimization opportunities:\n\n{sql_code}"
            
            if table_context:
                user_content += f"\n\nTable Context:\n{json.dumps(table_context, indent=2)}"
            
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": optimization_prompt},
                    {"role": "user", "content": user_content}
                ],
                temperature=0.3,
                max_tokens=2500,
                response_format={"type": "json_object"}
            )
            
            optimization_result = json.loads(response.choices[0].message.content)
            optimization_result["timestamp"] = datetime.now().isoformat()
            optimization_result["success"] = True
            
            return optimization_result
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "overall_score": 0,
                "priority_optimizations": [],
                "timestamp": datetime.now().isoformat()
            }


if __name__ == "__main__":
    print("SQL Modernization Agent module loaded successfully.")
    print("This module provides Translation, Validation, and Optimization capabilities.")
