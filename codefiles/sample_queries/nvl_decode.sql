-- Query using NVL and DECODE functions
SELECT emp_id,
       emp_name,
       NVL(commission, 0) AS commission,
       DECODE(dept_id, 
              10, 'Sales', 
              20, 'Marketing', 
              30, 'IT',
              'Other') AS department_name,
       NVL(manager_id, 0) AS manager_id
FROM employees
WHERE status = 'ACTIVE';
