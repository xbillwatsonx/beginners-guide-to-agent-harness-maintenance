# Maintenance Report Template

Use this template for the output of any report-only maintenance job.

```text
========================================
<Job Name> Report
Date: <YYYY-MM-DD HH:MM>
Harness: <harness name>
Version: <current version>
========================================

## Results

[PASS] <check 1 name>
[PASS] <check 2 name>
[WARN] <check 3 name>: <warning details>
[FAIL] <check 4 name>: <failure details>
[PASS] <check 5 name>

## Summary

Passed: X/Y
Warnings: Z
Failed: W

## Details

### Warnings
- <warning 1>: <explanation and recommended action>
- <warning 2>: <explanation and recommended action>

### Failures
- <failure 1>: <explanation and recommended action>
- <failure 2>: <explanation and recommended action>

## Action Items

- [ ] <action 1>
- [ ] <action 2>
- [ ] <action 3>

## Notes

<Any additional context, trends, or observations>

========================================
End of Report
========================================
```
