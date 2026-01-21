-- Cursor-based update (needs optimization to set-based approach)
DECLARE
  CURSOR emp_cursor IS
    SELECT emp_id, salary 
    FROM employees 
    WHERE dept_id = 10;
  
  v_bonus NUMBER;
BEGIN
  FOR emp_rec IN emp_cursor LOOP
    v_bonus := emp_rec.salary * 0.1;
    
    UPDATE employees
    SET bonus = v_bonus,
        last_updated = SYSDATE
    WHERE emp_id = emp_rec.emp_id;
  END LOOP;
  
  COMMIT;
END;
