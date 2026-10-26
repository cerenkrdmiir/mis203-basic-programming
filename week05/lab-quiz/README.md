# Week 5 Lab - Reusable Shipping Quote

## Tests Run and Changes Made
- **Test Run:** Ran `assert` checks for orders below and above the 500 threshold boundary to verify correctness.
- **Change Made:** Refactored the shipping fee logic so that orders of 500 and above qualify for free shipping (0 TL), while lower orders incur a standard shipping fee.

## Difference Between Print and Return
- **`print`**: Displays output directly to the console/screen for the user to see. The program cannot reuse this printed value in subsequent calculations, and its return value is `None`.
- **`return`**: Passes the resulting value back to where the function was called. This allows the value to be stored in variables, passed into other functions, or verified using `assert` statements.
