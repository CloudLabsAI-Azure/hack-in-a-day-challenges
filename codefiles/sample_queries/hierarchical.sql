-- Hierarchical query using CONNECT BY
SELECT emp_id,
       emp_name,
       manager_id,
       LEVEL AS emp_level,
       SYS_CONNECT_BY_PATH(emp_name, ' > ') AS hierarchy_path
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR emp_id = manager_id
ORDER SIBLINGS BY emp_name;
