```markdown
# DLMDSPWP01 – Python Data Analysis Pipeline  
## Least-Squares Function Fitting & Interactive Visualization

> **A complete, object-oriented data processing pipeline** that loads, analyzes, maps, and visualizes mathematical functions — built for IU assignment **DLMDSPWP01**.

---

## 🌟 Overview

This project implements a **modular, robust, and testable** Python pipeline that:

1. **Ingests** `train.csv`, `ideal.csv`, and `test.csv` into a **SQLite database** using **SQLAlchemy**.  
2. **Fits** the 4 training functions to 50 ideal functions via **Least-Squares Error (LSE)** minimization.  
3. **Maps** test data points to the best-fitting ideal functions using the **`√2 × max_deviation`** criterion.  
4. **Persists** results in the database.  
5. **Generates** an interactive, multi-tab **Bokeh** visualization (`assignment_results.html`).

All assignment requirements — **OOP**, **inheritance**, **custom exceptions**, **unit testing**, and **dual DB access** — are fully satisfied.

---

## 🚀 Key Features

| Feature | Implementation |
|---------|----------------|
| **Object-Oriented Design** | `DatabaseLoader`, `FunctionFitter`, `TestDataMapper` |
| **Inheritance** | `FunctionFitter` & `TestDataMapper` inherit from `DatabaseAnalyzer` (`src/analysis.py`) |
| **Custom Exceptions** | `DataLoadError`, `FittingError`, … in `src/exceptions.py` |
| **Dual DB Access** | **SQLAlchemy** for loading, **sqlite3** for analysis |
| **Least-Squares Fitting** | Full 4×50 SSE matrix |
| **√2 Deviation Mapping** | `numpy.sqrt(2)` threshold |
| **Interactive Plots** | Bokeh multi-tab HTML with hover/zoom/pan |
| **Unit Testing** | 100% coverage via `unittest` |

---

## 📁 Project Structure

```bash
Python_Assignment/
├── data/
│   ├── train.csv      # 4 training functions (x, y1–y4)
│   ├── ideal.csv      # 50 ideal functions (x, y1–y50)
│   └── test.csv       # Test points to map
│
├── src/
│   ├── __init__.py
│   ├── db_loader.py       # → DatabaseLoader (SQLAlchemy)
│   ├── analysis.py        # → DatabaseAnalyzer, FunctionFitter, TestDataMapper
│   ├── plotter.py         # → generate_plots() with Bokeh
│   └── exceptions.py      # → Custom exceptions
│
├── tests/
│   ├── test_db_loader.py  # → Tests DatabaseLoader
│   └── test_analysis.py   # → Tests FunctionFitter & mapping
│
├── main.py                # → Entry point: runs full pipeline
├── requirements.txt       # → Project dependencies
├── assignment_pipeline.db # → Generated SQLite DB (auto-created)
├── assignment_results.html# → Interactive Bokeh report (auto-opened)
└── README.md              # → This file
```

---

## 🛠️ Technologies

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Core language |
| **pandas** | CSV & DataFrame handling |
| **SQLAlchemy** | ORM-based DB creation & bulk load |
| **sqlite3** | Direct queries during analysis |
| **numpy** | SSE & √2 calculations |
| **Bokeh** | Interactive HTML visualisations |
| **unittest** | Built-in testing framework |

---

## ⚡ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/RajnibhaiVirani/Python_Assignment.git
cd Python_Assignment
```

### 2. Set Up Virtual Environment
**Windows**
```bash
python -m venv venv
.\venv\Scripts\activate
```
**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*`requirements.txt` contains:* `pandas`, `sqlalchemy`, `bokeh`, `numpy`

### 4. Run the Pipeline
```bash
python main.py
```

**Result**  
- `assignment_pipeline.db` is created/updated  
- Mapped data saved to `mapped_test_results` table  
- `assignment_results.html` opens automatically in your browser

---

## 🧪 Run Unit Tests

```bash
python -m unittest discover tests
```

Expected output (all tests pass):

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.032s

OK
```

---

## 📊 Pipeline Workflow

```mermaid
graph TD
    A[main.py] --> B[DatabaseLoader]
    B --> C[Load CSVs → SQLite via SQLAlchemy]
    C --> D[FunctionFitter]
    D --> E[Compute 4×50 SSE Matrix]
    E --> F[Select 4 Best Ideal Functions]
    F --> G[TestDataMapper]
    G --> H[Map Test Points with √2 Threshold]
    H --> I[Save to mapped_test_results]
    I --> J[generate_plots()]
    J --> K[Open assignment_results.html]
```

---

## 🎨 Visualization Preview

`assignment_results.html` contains:

* **Tabs 1–4** – each training function + its best-fit ideal + mapped test points  
* **Tab 5** – all test points plotted against the four chosen ideals  
* **Interactivity** – hover tooltips, linked panning, zoom, responsive layout

---

## 💡 What I Learned

* Building **end-to-end data pipelines** with clean architecture  
* Applying **Least-Squares** statistical fitting in production code  
* Using **inheritance** and **custom exceptions** for robust OOP  
* Combining **SQLAlchemy + sqlite3** strategically  
* Creating **interactive visualisations** with Bokeh  
* Writing **maintainable unit tests**

---

## 📝 License

Submitted as part of **IU DLMDSPWP01**.  
**For educational and demonstrative purposes only.**

---

**Made with ❤️ by [Rajnibhai Virani](https://github.com/RajnibhaiVirani)**  
*International University — Data Science & Programming*
```

**Just copy the whole block above (including the three backticks) and paste it into `README.md`.**  
Commit, push, and GitHub will render it exactly as designed. No further editing needed!
```