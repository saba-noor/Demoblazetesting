# 🛒 Demoblaze Website Testing

This repository contains test cases and bug reports for the [Demoblaze](https://www.demoblaze.com/) demo e-commerce website.  
The site is used for practicing **manual** and **automated testing** using tools like **Selenium** and **Pytest**.

---

## 📌 Website Overview

- **Name:** Demoblaze
- **URL:** [https://www.demoblaze.com](https://www.demoblaze.com)
- **Type:** Demo E-commerce Web Application
- **Technology Used (Frontend):** HTML, CSS, JavaScript
- **Purpose:** QA and automation practice

---

## ✅ Features to Test

| Feature         | Description                          |
|----------------|--------------------------------------|
| User Signup     | Register new users                   |
| User Login      | Login with credentials               |
| Add to Cart     | Add products to shopping cart        |
| Cart Page       | View, remove items, and place order  |
| Contact Form    | Send message to admin                |
| About Us        | Watch company video                  |
| Product Listing | View and navigate between categories |

---

## 🐞 Known Bugs (as of June 2025)

| Bug ID | Title | Severity | Description |
|--------|-------|----------|-------------|
| BUG001 | Enter key not working in Signup/Order form | Medium | Pressing Enter does nothing; only button works |
| BUG002 | About Us video fails to load | High | Shows error: "Media could not be loaded" |
| BUG003 | No alert on invalid login | Medium | No error feedback when wrong credentials are entered |

---

## 🧪 How to Run Automated Tests (If using Selenium + Pytest)

```bash
pip install selenium pytest
pytest test_demoblaze.py
