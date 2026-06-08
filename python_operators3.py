order_id  = "ORD20250608"
item      = "Laptop"
qty       = 1
price     = 65999.00


receipt = f"""
  ┌──────────────────────────────┐
  │       ORDER CONFIRMATION     │
  ├──────────────────────────────┤
  │ Order ID  : {order_id:<18}│
  │ Item      : {item:<18}│
  │ Quantity  : {qty:<18}│
  │ Amount    : ₹{price:<17,.2f}│
  └──────────────────────────────┘
"""
print(receipt)
