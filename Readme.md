# DLMDSPWP01 Assignment - Function Analysis in Python

# 📈 Data Analysis Pipeline with Python
## Applying Least-Squares & Data Mapping for Function Analysis

### 🔍 Overview

This project is a complete, object-oriented Python pipeline built for the IU DLMDSPWP01 assignment. It demonstrates a full data workflow:

-   Loads training, ideal, and test datasets from CSVs into a **SQLite database** using SQLAlchemy.
-   Applies **least-squares error minimization** to find the 4 best-fitting ideal functions for the 4 training functions.
-   Matches **test data** points to the chosen functions based on the **√2 deviation criterion**.
-   Visualizes all results in a multi-tab, interactive **Bokeh** report.
-   Fulfills key OOP requirements like **inheritance** and **custom exception handling**.

---

### 📁 Project Structure

<pre>
Python_Assignment/
├── src/                       # Core application source code
│   ├── db_loader.py           # Class: DatabaseLoader (SQLAlchemy)
│   ├── analysis.py            # Classes: DatabaseAnalyzer, FunctionFitter, TestDataMapper
│   ├── plotter.py             # Function: generate_plots (Bokeh)
│   └── exceptions.py          # Custom user-defined exceptions
├── tests/                     # All unit tests
│   ├── test_analysis.py       # Tests for FunctionFitter logic
│   └── test_db_loader.py      # Tests for DatabaseLoader logic
├── data/                      # Raw CSV data files
│   ├── train.csv
│   ├── ideal.csv
│   └── test.csv
├── assignment_pipeline.db     # Generated SQLite database
├── assignment_results.html    # Generated Bokeh visualization
├── requirements.txt           # Python dependencies
├── main.py                    # Main entry point to run the full pipeline
└── README.md                  # This file
</pre>

---

### 📌 Technologies Used

-   **Python 3.10+**
-   **pandas**: For all data manipulation and analysis.
-   **SQLAlchemy**: For robust database creation and initial data loading.
-   **Bokeh**: For creating the final interactive HTML visualizations.
-   **numpy**: For numerical calculations (LSE, sqrt(2)).
-   **unittest**: Python's built-in library for all unit testing.
-   **Git** + **GitHub**: For version control.

---

### 🧠 Core Workflow

1.  **Data Load** `DatabaseLoader` (using SQLAlchemy) reads `train.csv`, `ideal.csv`, and `test.csv` and loads them into tables in `assignment_pipeline.db`.

2.  **Function Fitting** `FunctionFitter` reads the data and calculates the Sum of Squared Errors (SSE) for all 4x50 combinations to find the 4 best ideal function matches.

3.  **Test Data Mapping** `TestDataMapper` uses the results (and the `sqrt(2) * max_deviation` threshold) to map each test point to one of the 4 chosen functions.

4.  **Save & Visualize** The mapped results are saved to a new table. `generate_plots` then reads all data and creates the `assignment_results.html` report.

---

### 🔧 How to Run the Project

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/RajnibhaiVirani/Python_Assignment.git](https://github.com/RajnibhaiVirani/Python_Assignment.git)
    cd Python_Assignment
    ```

2.  **Create and activate a virtual environment**
    *On Windows:*
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    *On macOS/Linux:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Create `requirements.txt`** Create a new file named `requirements.txt` and paste this inside:
    ```
    pandas
    sqlalchemy
    bokeh
    numpy
    ```

4.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the project** Execute the main script from the root folder:
    ```bash
    python main.py
    ```

6.  **View the visualization** The script will automatically create and open `assignment_results.html` in your default web browser.

---

### ✅ Unit Testing

Run all tests using Python's built-in `unittest` module:

```bash
python -m unittest discover tests

Got it. You want a README.md file that has the same professional style, emojis, and sections as your friend's, but is 100% tailored to your project's specific files, classes, and repository.

Here is a ready-to-use version. Just copy the entire text block below, paste it into your README.md file, and you're all set.

(Copy everything below this line)

Markdown

# DLMDSPWP01 Assignment - Function Analysis in Python

# 📈 Data Analysis Pipeline with Python
## Applying Least-Squares & Data Mapping for Function Analysis

### 🔍 Overview

This project is a complete, object-oriented Python pipeline built for the IU DLMDSPWP01 assignment. It demonstrates a full data workflow:

-   Loads training, ideal, and test datasets from CSVs into a **SQLite database** using SQLAlchemy.
-   Applies **least-squares error minimization** to find the 4 best-fitting ideal functions for the 4 training functions.
-   Matches **test data** points to the chosen functions based on the **√2 deviation criterion**.
-   Visualizes all results in a multi-tab, interactive **Bokeh** report.
-   Fulfills key OOP requirements like **inheritance** and **custom exception handling**.

---

### 📁 Project Structure

<pre>
Python_Assignment/
├── src/                       # Core application source code
│   ├── db_loader.py           # Class: DatabaseLoader (SQLAlchemy)
│   ├── analysis.py            # Classes: DatabaseAnalyzer, FunctionFitter, TestDataMapper
│   ├── plotter.py             # Function: generate_plots (Bokeh)
│   └── exceptions.py          # Custom user-defined exceptions
├── tests/                     # All unit tests
│   ├── test_analysis.py       # Tests for FunctionFitter logic
│   └── test_db_loader.py      # Tests for DatabaseLoader logic
├── data/                      # Raw CSV data files
│   ├── train.csv
│   ├── ideal.csv
│   └── test.csv
├── assignment_pipeline.db     # Generated SQLite database
├── assignment_results.html    # Generated Bokeh visualization
├── requirements.txt           # Python dependencies
├── main.py                    # Main entry point to run the full pipeline
└── README.md                  # This file
</pre>

---

### 📌 Technologies Used

-   **Python 3.10+**
-   **pandas**: For all data manipulation and analysis.
-   **SQLAlchemy**: For robust database creation and initial data loading.
-   **Bokeh**: For creating the final interactive HTML visualizations.
-   **numpy**: For numerical calculations (LSE, sqrt(2)).
-   **unittest**: Python's built-in library for all unit testing.
-   **Git** + **GitHub**: For version control.

---

### 🧠 Core Workflow

1.  **Data Load** `DatabaseLoader` (using SQLAlchemy) reads `train.csv`, `ideal.csv`, and `test.csv` and loads them into tables in `assignment_pipeline.db`.

2.  **Function Fitting** `FunctionFitter` reads the data and calculates the Sum of Squared Errors (SSE) for all 4x50 combinations to find the 4 best ideal function matches.

3.  **Test Data Mapping** `TestDataMapper` uses the results (and the `sqrt(2) * max_deviation` threshold) to map each test point to one of the 4 chosen functions.

4.  **Save & Visualize** The mapped results are saved to a new table. `generate_plots` then reads all data and creates the `assignment_results.html` report.

---

### 🔧 How to Run the Project

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/RajnibhaiVirani/Python_Assignment.git](https://github.com/RajnibhaiVirani/Python_Assignment.git)
    cd Python_Assignment
    ```

2.  **Create and activate a virtual environment**
    *On Windows:*
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    *On macOS/Linux:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Create `requirements.txt`** Create a new file named `requirements.txt` and paste this inside:
    ```
    pandas
    sqlalchemy
    bokeh
    numpy
    ```

4.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the project** Execute the main script from the root folder:
    ```bash
    python main.py
    ```

6.  **View the visualization** The script will automatically create and open `assignment_results.html` in your default web browser.

---

### ✅ Unit Testing

Run all tests using Python's built-in `unittest` module:

```bash
python -m unittest discover tests
```
⚙️ Features Implemented
<pre> 🗂️ Database Management: Uses SQLAlchemy to create a DB and pandas to load CSVs. 
📉 Least-Squares Analysis: FunctionFitter class correctly identifies best-fit functions. 📊 Interactive Visualization: Multi-tab Bokeh report with linked panning and hover tools. ✅ Test Data Mapping: TestDataMapper class implements the √2 deviation criterion. ⚙️ Object-Oriented Design: Clean, modular code separated into logical classes. 🏛️ Inheritance: FunctionFitter and TestDataMapper inherit from a DatabaseAnalyzer base class. 🧪 Unit Testing: Clear, isolated tests for core analysis and database logic. 💡 Custom Exceptions: src/exceptions.py provides robust, user-defined error handling. </pre>

📝 What I Learned
This project was a great opportunity to build a complete data pipeline from scratch. I gained practical experience in:

Combining different libraries (pandas, SQLAlchemy, Bokeh) to work together.

Applying statistical methods (like Least Squares) to a real-world problem.

Designing a clean, object-oriented program using principles like inheritance.

Writing meaningful unit tests to validate my logic.

Managing the full project workflow from data loading to final visualization.

📋 License
This project is submitted as part of the IU assignment DLMDSPWP01. It is intended for educational and demonstrative purposes only.