# Week 03 Lab Quiz - Order Approval Policy

## Test Table (Boundary Cases)

| Test Case | Order Amount | Available Stock | Requested Qty | Is Member | Expected Result |
|-----------|--------------|-----------------|---------------|-----------|-----------------|
| Below 500 | 499 TRY      | 10              | 2             | Yes       | Approved, Final Price: 499 TRY (No Discount) |
| Exact 500 | 500 TRY      | 10              | 2             | Yes       | Approved, Final Price: 450 TRY (10% Discount) |
| Above 500 | 501 TRY      | 10              | 2             | Yes       | Approved, Final Price: 450.9 TRY (10% Discount) |

## Test & Code Change Note
- **Test Run:** Tested boundary case with 500 TRY for a member customer.
- **Change Made:** Adjusted condition to `>= 500` instead of `> 500` to correctly include exactly 500 TRY orders in the discount policy.
