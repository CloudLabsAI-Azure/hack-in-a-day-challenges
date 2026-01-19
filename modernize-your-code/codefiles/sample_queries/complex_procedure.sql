-- Complex stored procedure with multiple Oracle-specific features
CREATE OR REPLACE PROCEDURE process_employee_bonuses(
  p_dept_id IN NUMBER,
  p_bonus_pct IN NUMBER,
  p_result OUT VARCHAR2
)
IS
  v_total_employees NUMBER := 0;
  v_total_bonus NUMBER := 0;
  v_emp_count NUMBER;
BEGIN
  -- Check if department exists
  SELECT COUNT(*)
  INTO v_emp_count
  FROM employees
  WHERE dept_id = p_dept_id;
  
  IF v_emp_count = 0 THEN
    p_result := 'Department not found';
    RETURN;
  END IF;
  
  -- Update bonuses using cursor
  FOR emp_rec IN (
    SELECT emp_id, salary, NVL(commission, 0) AS commission
    FROM employees
    WHERE dept_id = p_dept_id
      AND hire_date < SYSDATE - 180
  ) LOOP
    DECLARE
      v_bonus NUMBER;
    BEGIN
      v_bonus := (emp_rec.salary + emp_rec.commission) * (p_bonus_pct / 100);
      
      UPDATE employees
      SET bonus = v_bonus,
          last_updated = SYSDATE
      WHERE emp_id = emp_rec.emp_id;
      
      v_total_employees := v_total_employees + 1;
      v_total_bonus := v_total_bonus + v_bonus;
    END;
  END LOOP;
  
  COMMIT;
  
  p_result := 'Processed ' || v_total_employees || ' employees, total bonus: ' || v_total_bonus;
  
EXCEPTION
  WHEN OTHERS THEN
    ROLLBACK;
    p_result := 'Error: ' || SQLERRM;
END process_employee_bonuses;
