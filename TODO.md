git# TODO - Database Migration Project - COMPLETED ✅

## Summary of Changes Made:

### 1. Fixed app.py
- The file was already correct (no duplicate code issue found)

### 2. Added Department model to models.py
- Added `Department` model with:
  - `__tablename__ = 'departments'`
  - `id` (Integer, primary_key)
  - `name` (String, nullable=False)
  - `address` (String)
  - `__repr__` method

### 3. Updated tests
- Replaced placeholder test with comprehensive test suite:
  - `test_employee_model_exists`
  - `test_department_model_exists`
  - `test_employee_table_name`
  - `test_department_table_name`
  - `test_add_employee_to_database`
  - `test_add_department_to_database`
  - `test_employee_repr`
  - `test_department_repr`

### 4. Initialized and ran migrations
- Initialized Flask migrations: `flask db init`
- Created initial migration: `flask db migrate -m "Initial migration."`
- Applied migration: `flask db upgrade head`

## Test Results:
```
8 passed in 1.96s
```

All tests pass successfully!

