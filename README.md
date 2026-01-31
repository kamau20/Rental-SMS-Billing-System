# 📲 Rental SMS Billing System

A Django-based rental management system that enables landlords to generate monthly rent bills and send automated SMS notifications to tenants instead of issuing printed receipts.

This system was built to solve a real-world problem where landlords manually prepare and distribute rent statements and arrears notices every month.

---

## 🚀 Features

- Tenant management (name, house number, phone number, rent)
- Monthly billing with:
  - Rent
  - Garbage fee
  - Water bill
  - Automatic total and balance calculation
- Payment tracking
- SMS notifications to tenants
- Bulk SMS sending from Django Admin
- SMS delivery logging
- PostgreSQL database backend
- Simple and reliable admin dashboard

---

## 🧠 How It Works

1. Landlord adds tenants via Django Admin
2. Monthly bills are created per tenant
3. The system automatically calculates:
   - Total payable amount
   - Outstanding balance (arrears)
4. Landlord selects bills and sends SMS notifications
5. Tenants receive clear rent statements via SMS
6. All messages are logged for tracking and reference

---


---

## 🛠️ Tech Stack

- Backend: Python, Django
- Database: PostgreSQL
- SMS Gateway: Africa’s Talking
- Admin Interface: Django Admin
- Version Control: Git & GitHub

---

