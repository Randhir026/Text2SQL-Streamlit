# Text2SQL-Streamlit

## 📌 About the Project

**Text2SQL-Streamlit** is a Natural Language to SQL (NL2SQL) search application that allows users to query a PostgreSQL database using plain English instead of writing SQL queries manually. The system interprets user input, converts it into valid SQL, executes it securely, and displays the results through an interactive Streamlit interface.

This project is designed as a practical prototype for intelligent database querying systems and demonstrates how natural language interfaces can simplify data access for non-technical users. It also includes support for **hybrid search** using `pgvector`, enabling semantic similarity search alongside traditional SQL queries.

---

## 🎯 Objective

* Enable users to query structured databases using natural language
* Convert text queries into SQL safely and efficiently
* Demonstrate hybrid search (SQL + vector similarity)
* Provide a simple and intuitive UI using Streamlit
* Showcase a production-style project structure suitable for real-world use

---

## 🧱 Database Schema

### 1️⃣ Employees

Stores employee details

* `id` (Primary Key)
* `name`
* `department_id` (Foreign Key)
* `email`
* `salary`

### 2️⃣ Departments

Stores department information

* `id` (Primary Key)
* `name`

### 3️⃣ Orders

Stores customer order data

* `id` (Primary Key)
* `customer_name`
* `employee_id` (Foreign Key)
* `order_total`
* `order_date`

### 4️⃣ Products

Stores product catalog

* `id` (Primary Key)
* `name`
* `price`
* `embedding` (vector for semantic search)

---

## 🧠 Key Features

* Natural language query input
* Rule-based text-to-SQL generation
* Secure SQL execution (no raw user SQL)
* PostgreSQL relational querying
* Vector similarity search using pgvector
* Dockerized database setup
* Streamlit-based interactive UI

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **Database**: PostgreSQL
* **Vector Search**: pgvector
* **Containerization**: Docker & Docker Compose

---

## 📁 Project Structure

```
Text2SQL-Streamlit/
│
├── app.py                    # Streamlit application
├── docker-compose.yml        # PostgreSQL + pgvector setup
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
│
├── db/
│   ├── 01_schema.sql         # Database schema
│   └── 02_sample_data.sql   # Sample data
│
├── embeddings/
│   └── generate_embeddings.py
│
├── utils/
│   └── sql_generator.py     # Natural language to SQL logic
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Text2SQL-Streamlit.git
cd Text2SQL-Streamlit
```

### 2️⃣ Start PostgreSQL with Docker

```bash
docker-compose up
```

This will:

* Start PostgreSQL
* Enable pgvector extension
* Create tables
* Insert sample data

---

### 3️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Generate Vector Embeddings

```bash
python embeddings/generate_embeddings.py
```

---

### 5️⃣ Run Streamlit App

```bash
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

## 🧪 Example Queries

* "Show all employees"
* "Employees in engineering department"
* "Who has the highest salary?"
* "List all products"
* "Show orders handled by employees"
* "Total sales"

---

## 🔒 Security Considerations

* No raw SQL execution from user input
* Query generation is controlled and validated
* Safe parameter handling

---

## 🔮 Future Improvements

* Replace rule-based SQL generation with LLM-based NL2SQL
* Add authentication & role-based access
* Improve semantic search accuracy
* Add query history and caching
* Support complex joins and aggregations

---

## 📽️ Demo

A screen recording demonstrating the working application is included as part of the project submission.

---

## 📄 License

This project is created for educational and demonstration purposes.

---

## 🙌 Author

**Randhir Kumar**

MCA Graduate | Data Science & AI Enthusiast

---

⭐ If you find this project useful, feel free to star the repository!
