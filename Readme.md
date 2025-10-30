# 🧠 DLMDSPWP01 – Python Data Analysis Pipeline  
## Least-Squares Function Fitting & Interactive Visualization

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: Educational](https://img.shields.io/badge/license-Educational-lightgrey)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/RajnibhaiVirani/Python_Assignment)](https://github.com/RajnibhaiVirani/Python_Assignment/commits/main)

> A complete, **object-oriented Python pipeline** that loads, analyzes, maps, and visualizes mathematical functions using **Least-Squares fitting** — built for IU assignment **DLMDSPWP01**.

---

## 📖 Overview

This project implements a **modular, testable, and fully automated** data analysis workflow:

1. **Load Data** – Reads `train.csv`, `ideal.csv`, and `test.csv` into a **SQLite** database using **SQLAlchemy**.  
2. **Analyze** – Uses **Least-Squares Error (LSE)** minimization to find the 4 ideal functions that best fit the 4 training functions.  
3. **Map Test Points** – Matches each test data point to one of the 4 ideal functions based on the **√2 × max_deviation** rule.  
4. **Visualize** – Generates an interactive multi-tab **Bokeh** graph (`assignment_results.html`).  
5. **Validate** – Includes **unit tests**, **OOP design**, **inheritance**, and **custom exceptions**.

---

## ✨ Key Features

| Feature | Description |
|----------|-------------|
| **Object-Oriented Design** | Clean modular classes (`DatabaseLoader`, `FunctionFitter`, `TestDataMapper`) |
| **Inheritance** | `FunctionFitter` & `TestDataMapper` extend a common base `DatabaseAnalyzer` |
| **Custom Exceptions** | Defined in `src/exceptions.py` for clean error handling |
| **Dual DB Access** | Uses **SQLAlchemy** for loading and **sqlite3** for analysis |
| **Least-Squares Fitting** | Computes 4×50 SSE matrix to find best matches |
| **√2 Deviation Mapping** | Follows IU assignment rule for valid test mapping |
| **Interactive Visualization** | Multi-tab **Bokeh** plots with hover, zoom, and pan |
| **Unit Testing** | Ensures correctness of all major components using `unittest` |

---

## 🗂️ Project Structure

```bash
Python_Assignment/
├── data/
│   ├── train.csv
│   ├── ideal.csv
│   └── test.csv
│
├── src/
│   ├── __init__.py
│   ├── db_loader.py       # → DatabaseLoader (SQLAlchemy)
│   ├── analysis.py        # → DatabaseAnalyzer, FunctionFitter, TestDataMapper
│   ├── plotter.py         # → generate_plots() with Bokeh
│   └── exceptions.py      # → Custom Exceptions
│
├── tests/
│   ├── test_db_loader.py  # → Tests DatabaseLoader
│   └── test_analysis.py   # → Tests FunctionFitter & mapping logic
│
├── main.py                # → Runs the complete pipeline
├── requirements.txt       # → Dependencies (pandas, sqlalchemy, bokeh, numpy)
├── assignment_pipeline.db # → Generated SQLite DB
├── assignment_results.html# → Generated Bokeh visualization
└── README.md              # → This file!
```

---

## ⚙️ Technologies Used

| Tool | Purpose |
|------|----------|
| **Python 3.10+** | Core programming language |
| **pandas** | Data manipulation and CSV handling |
| **SQLAlchemy** | ORM-based database loading |
| **sqlite3** | Direct DB queries during analysis |
| **numpy** | Numerical operations and deviation calculations |
| **Bokeh** | Interactive data visualization |
| **unittest** | Automated testing framework |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/RajnibhaiVirani/Python_Assignment.git
cd Python_Assignment
```

### 2. Create a Virtual Environment
**Windows:**
```bash
python -m venv venv
.
env\Scripts ctivate
```
**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, create one and add:
> ```
> pandas
> sqlalchemy
> bokeh
> numpy
> ```

### 4. Run the Project
```bash
python main.py
```

**Output:**
- Creates `assignment_pipeline.db`
- Maps test data to best-fit ideal functions
- Generates and **auto-opens** `assignment_results.html` in your browser

---

## 🧪 Run Tests
```bash
python -m unittest discover tests
```

Expected output:
```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.03s

OK
```

---

## 🔄 Workflow Diagram

```mermaid
graph TD
    A[main.py] --> B[DatabaseLoader]
    B --> C[Load CSVs → SQLite via SQLAlchemy]
    C --> D[FunctionFitter]
    D --> E[Compute 4×50 SSE Matrix]
    E --> F[Select 4 Best Ideal Functions]
    F --> G[TestDataMapper]
    G --> H[Map Test Points (√2 rule)]
    H --> I[Save Results to DB]
    I --> J[generate_plots()]
    J --> K[Open assignment_results.html]
```

---

## 📊 Visualization Details

The generated HTML report includes:
- **Tabs 1–4**: Each training function, its best-fit ideal, and mapped test points  
- **Tab 5**: Combined overview of all mapped data  
- **Features:** Hover tooltips, zoom, pan, responsive layout  

---

## 🧠 What I Learned

- Building an **end-to-end data pipeline** with modular OOP architecture  
- Implementing **Least-Squares fitting** for real data  
- Managing data in **SQLite** via **SQLAlchemy**  
- Creating **interactive visualizations** with Bokeh  
- Writing **unit tests** for data-driven applications  
- Designing for clarity, modularity, and scalability  

---

## 📜 License

This project is submitted as part of **IU DLMDSPWP01**.  
**For educational and demonstrative purposes only.**

---

**Made with ❤️ by [Rajnibhai Virani](https://github.com/RajnibhaiVirani)**  
*International University – Data Science & Programming*
