# Manual Test Cases

## Module: Login

### TC_LOGIN_001 - Valid Login
- **Precondition:** User is on login page
- **Steps:**
  1. Enter username `standard_user`
  2. Enter password `secret_sauce`
  3. Click Login
- **Expected Result:** User is redirected to inventory page
- **Priority:** High

### TC_LOGIN_002 - Invalid Password
- **Precondition:** User is on login page
- **Steps:**
  1. Enter username `standard_user`
  2. Enter password `wrong_password`
  3. Click Login
- **Expected Result:** Error message displayed; user remains on login page
- **Priority:** High

### TC_LOGIN_003 - Locked User
- **Precondition:** User is on login page
- **Steps:**
  1. Enter username `locked_out_user`
  2. Enter password `secret_sauce`
  3. Click Login
- **Expected Result:** Locked user error message displayed
- **Priority:** High

## Module: Inventory / Cart

### TC_CART_001 - Add Single Item to Cart
- **Precondition:** User is logged in
- **Steps:**
  1. Click `Add to cart` for first inventory item
  2. Open cart
- **Expected Result:** Item appears in cart
- **Priority:** Medium

