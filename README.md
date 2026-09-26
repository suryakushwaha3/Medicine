# 💊 Medicine Shop API

> 🚀 A simple and practical **Medicine Shop Backend API** built with **Python, Flask & SQLite**.

A backend system for managing **users, medicines, products, orders, sales and available stock** through REST APIs.

---

## ✨ Features

| 🧩 Feature | 📝 Description |
|---|---|
| 👤 **User Management** | Create, login, read and update users |
| 💊 **Product Management** | Add, view, update and delete products |
| 📦 **Order Management** | Create, view, update and delete orders |
| 💰 **Sell History** | Store and manage selling records |
| 📊 **Stock Management** | Manage available medicine stock |
| 🗄️ **SQLite Database** | Store application data locally |
| 🌐 **REST API** | Communicate with Android and other clients |
| ☁️ **Cloud Hosted** | Backend hosted on PythonAnywhere |

---

## 🛠️ Tech Stack

```text
🐍 Python
🌶️ Flask
🗄️ SQLite
🔗 REST API
☁️ PythonAnywhere
📱 Android Client Support
```

---

## 📁 Project Structure

```text
Medicine/
│
├── 📄 main.py
├── 🗄️ my_medicalshop.db
│
├── 📂 operations/
│   ├── createTableOperation.py
│   ├── addOperation.py
│   ├── authUser.py
│   ├── readOperation.py
│   ├── updatesOperation.py
│   ├── product_operation.py
│   ├── order_operation.py
│   ├── sell_operation.py
│   └── available_stock_operation.py
│
└── 📂 routes/
    ├── user_routes.py
    ├── product_routes.py
    ├── order_routes.py
    ├── sell_routes.py
    └── available_stock_routes.py
```

---

## 📂 Project Files

| 📄 File / Folder | 🎯 Purpose |
|---|---|
| `main.py` | 🚀 Starts the Flask application |
| `operations/` | 🗄️ Handles database operations |
| `routes/` | 🔗 Handles API routes |
| `my_medicalshop.db` | 💾 SQLite database |

---

# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/suryakushwaha3/Medicine.git
```

## 2️⃣ Open Project

```bash
cd Medicine
```

## 3️⃣ Install Flask

```bash
pip install flask
```

## 4️⃣ Run Server

```bash
python main.py
```

### 🌐 Local Server

```text
http://127.0.0.1:5000
```

> ✅ Now the Flask backend is ready to receive API requests.

---

# 🔗 API Documentation

## 👤 User APIs

| 🔧 Method | 🔗 Endpoint | 📝 Description |
|---|---|---|
| 🟢 `GET` | `/user` | Test User API |
| 🟡 `POST` | `/createUser` | Create a new user |
| 🟡 `POST` | `/login` | Login user |
| 🟢 `GET` | `/getAllUsers` | Get all users |
| 🟡 `POST` | `/getSpacificUser` | Get specific user |
| 🔵 `PATCH` | `/updateUser` | Update user |

---

## 💊 Product APIs

| 🔧 Method | 🔗 Endpoint | 📝 Description |
|---|---|---|
| 🟡 `POST` | `/addProduct` | Add a product |
| 🟢 `GET` | `/productsDetails` | Get all products |
| 🔵 `PATCH` | `/updateProduct` | Update product |
| 🔴 `DELETE` | `/deleteProduct` | Delete product |

---

## 📦 Order APIs

| 🔧 Method | 🔗 Endpoint | 📝 Description |
|---|---|---|
| 🟡 `POST` | `/addOrder` | Create a new order |
| 🟢 `GET` | `/orders` | Get all orders |
| 🟢 `GET` | `/userOrders/<user_id>` | Get user's orders |
| 🔵 `PATCH` | `/updateOrder` | Update order |
| 🔴 `DELETE` | `/deleteOrder` | Delete order |

### 💡 Example

```http
GET /userOrders/USER001
```

---

## 💰 Sell History APIs

| 🔧 Method | 🔗 Endpoint | 📝 Description |
|---|---|---|
| 🟡 `POST` | `/addSell` | Add sell record |
| 🟢 `GET` | `/sellHistory` | Get all sell history |
| 🟢 `GET` | `/userSellHistory/<user_id>` | Get user's sell history |
| 🔴 `DELETE` | `/deleteSell` | Delete sell record |

### 💡 Example

```http
GET /userSellHistory/USER001
```

---

## 📊 Available Stock APIs

| 🔧 Method | 🔗 Endpoint | 📝 Description |
|---|---|---|
| 🟡 `POST` | `/addAvailableStock` | Add available stock |
| 🟢 `GET` | `/availableStock` | Get all available stock |
| 🟢 `GET` | `/userAvailableStock/<user_id>` | Get user's stock |
| 🔵 `PATCH` | `/updateAvailableStock` | Update stock |
| 🔴 `DELETE` | `/deleteAvailableStock` | Delete stock |

### 💡 Example

```http
GET /userAvailableStock/USER001
```

---

# 🌐 Live API

> ☁️ **Medicine Shop API is hosted on PythonAnywhere.**

### 🔗 Live Server

```text
https://suryakush.pythonanywhere.com
```

### 🧪 Test API

```text
https://suryakush.pythonanywhere.com/productsDetails
```

> 💡 `GET` APIs can be opened directly in your browser.

---

# 🗄️ Database

> 💾 This project uses **SQLite** as its database.

### 📄 Database File

```text
my_medicalshop.db
```

### 📋 Main Tables

```text
👤 Users
│
├── 💊 Products
│
├── 📦 Orders_Details
│
├── 💰 Sell_History
│
└── 📊 Available_Stock
```

---

# 🔄 How It Works

```text
                    📱 Android App
                          │
                          │ HTTP Request
                          ▼
                 🌐 Flask REST API
                          │
                          ▼
                  🐍 Python Backend
                          │
                          ▼
                   🗄️ SQLite Database
```

> 🔗 The Android application communicates with the Flask backend using HTTP requests.

---

# 📱 Android Integration

This backend can be connected with an Android application using:

```text
📱 Android App
      │
      ▼
🌐 HTTP / REST API
      │
      ▼
🐍 Flask Backend
      │
      ▼
🗄️ SQLite
```

The API can be consumed from Android using libraries such as **Retrofit** or other HTTP clients.

---

# 🎯 Project Purpose

> 📚 This project was created to learn and practice **Python backend development and REST API development**.

| 📚 Topic | 🎯 Purpose |
|---|---|
| 🐍 Python | Backend programming |
| 🌶️ Flask | Web framework |
| 🔗 REST API | Client-server communication |
| 🗄️ SQLite | Database management |
| ✏️ CRUD | Create, Read, Update & Delete |
| 🧪 API Testing | Test backend endpoints |
| ☁️ Hosting | Deploy backend online |
| 📱 Android | Connect mobile application with backend |

---

# 👨‍💻 Developer

## Surya Kushwaha

> 💻 **Android Developer | Python Flask Backend Learner**

### 🔗 GitHub

```text
https://github.com/suryakushwaha3
```

---

# ⭐ Support

> ❤️ If you find this project useful, please consider giving it a **⭐ Star** on GitHub.

```text
⭐ Star the Repository
🚀 Follow the Project
💡 Build Something Awesome
```

---

# 📌 Note

> 📝 This project is mainly created for **learning, practice and backend development**.

Future improvements can include:

```text
🔐 Better API Security
🔑 Authentication & Authorization
🛡️ Input Validation
📈 Better Database Management
🚀 More Backend Features
```

---

# 🙌 Thank You

> Thanks for checking out **Medicine Shop API**! 💊🚀
