## 🧠 Fraud Detection Django Project

### 📋 Overview
This project is a **Fraud Detection Web Application** built with **Django** and **MySQL**.  
It detects potentially fraudulent transactions using data-driven logic and provides an interactive dashboard to monitor results.  

---

### 🚀 Features
- 🗃️ **MySQL Database Integration** — secure and scalable data storage  
- ⚙️ **ETL Pipeline** support for data preprocessing and model integration  
- 🔍 **Real-Time Fraud Detection** — prediction interface for new transactions  
- 📊 **Interactive Dashboard** — visualize fraud statistics dynamically  
- 🌐 **Django Admin Panel** for user and data management  

---

### 🛠️ Tech Stack
| Component | Technology |
|------------|-------------|
| Backend | Django (Python) |
| Frontend | HTML, CSS, Bootstrap |
| Database | MySQL |
| Data Processing | Pandas, Scikit-learn, PySpark *(if applicable)* |
| Hosting *(optional)* | Localhost / Cloud Server |

---

### ⚙️ Setup Instructions

#### 1️⃣ Clone the repository
```bash
git clone https://github.com/JP21409/fraud_detection_django.git
cd fraud_detection_django
```

#### 2️⃣ Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

#### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure MySQL
- Make sure MySQL service is running.
- Create a database (example):
  ```sql
  CREATE DATABASE fraud_detection;
  ```
- Update your database credentials in `settings.py`.

#### 5️⃣ Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6️⃣ Run the server
```bash
python manage.py runserver
```
Then open your browser and go to 👉 `http://127.0.0.1:8000/`

---

### 📈 Future Enhancements
- Integrate a Machine Learning model for automated fraud prediction  
- Deploy the project on Google Cloud or AWS  
- Add role-based authentication for better data access control  

---

### 🧑‍💻 Author
**Sourav Kumar Sahoo**  
_Data Analyst | Django Developer_  
📧 sourav.sahoo68@gmail.com  
🌐 [www.linkedin.com/in/sourav-kumar-sahoo-640170382]  

---


