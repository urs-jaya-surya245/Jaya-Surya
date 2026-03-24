# Test Plan - SauceDemo Login and Inventory

## 1. Objective
Validate the core user journey:
- Login
- Product inventory visibility
- Add-to-cart behavior
- Logout

## 2. In Scope
- Functional testing of login page
- Positive and negative login scenarios
- Basic cart flow for one product

## 3. Out of Scope
- Performance testing
- Security testing
- Mobile app testing

## 4. Test Environment
- URL: https://www.saucedemo.com/
- Browsers: Chrome (latest), Firefox (latest)
- Test Data:
  - Valid user: `standard_user`
  - Locked user: `locked_out_user`
  - Password: `secret_sauce`

## 5. Entry Criteria
- Application URL reachable
- Test credentials available

## 6. Exit Criteria
- All high-priority test cases executed
- Critical defects logged and triaged

## 7. Risks
- Environment downtime may block testing
- Shared test account data may change during execution

