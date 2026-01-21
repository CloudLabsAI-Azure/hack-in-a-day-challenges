-- Simple SELECT query with Oracle-specific functions
SELECT emp_id, 
       emp_name, 
       hire_date,
       salary
FROM employees
WHERE hire_date > SYSDATE - 30
  AND ROWNUM <= 10
ORDER BY salary DESC;
