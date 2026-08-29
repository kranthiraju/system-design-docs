### Output:
```
============================================================
        NOTIFICATION SYSTEM DEMO
============================================================

Notification channels registered:
- Email
- SMS
- Push

Users created:
- Apple
- Google

============================================================
TEST CASE 1: ORDER PLACED
============================================================
User: Apple
Type: ORDER_PLACED
Message: Your order has been successfully placed.
[EMAIL] To: apple@app.com, Message: Your order has been successfully placed.
[SMS] To: 9402, Message: Your order has been successfully placed.
[PUSH] To: tk_090, Message: Your order has been successfully placed.

============================================================
TEST CASE 2: ORDER SHIPPED
============================================================
User: Google
Type: ORDER_SHIPPED
Message: Your order has been shipped.
[EMAIL] To: google@app.com, Message: Your order has been shipped.
[PUSH] To: tk_017, Message: Your order has been shipped.

============================================================
TEST CASE 3: ORDER DELIVERED
============================================================
User: Apple
Type: ORDER_DELIVERED
Message: Your order has been delivered successfully.
[EMAIL] To: apple@app.com, Message: Your order has been delivered successfully.
[SMS] To: 9402, Message: Your order has been delivered successfully.
[PUSH] To: tk_090, Message: Your order has been delivered successfully.

============================================================
             DEMO COMPLETED
============================================================
```