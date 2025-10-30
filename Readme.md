```markdown
# Python Data Analysis Pipeline (DLMDSPWP01)

Hello! This is my project for the IU (DLMDSPWP01) assignment.

I built a complete program that automatically loads, processes, and analyzes a bunch of data. Here's what it does, step-by-step:

1.  It loads the `train.csv`, `ideal.csv`, and `test.csv` files into a new SQLite database using **SQLAlchemy**.
2.  It analyzes the training data against 50 "ideal" functions to find the four best fits. (It uses a **Least-Squares Error** method for this).
3.  It then maps the test data points to those four best functions, based on the **`sqrt(2)` deviation rule** from the assignment.
4.  It saves all these new mapped results back into the database.
5.  Finally, it creates a cool, interactive **Bokeh** graph (as an HTML file) with multiple tabs so you can see all the results.

---

## 🚀 Key Project Features

I built this project to specifically include a few key requirements from the course:

* **Object-Oriented Design:** I split the code into different classes to keep it clean:
    * `DatabaseLoader`: Handles all the initial data loading.
    * `FunctionFitter`: Manages the least-squares analysis.
    * `TestDataMapper`: Handles the test data mapping logic.
* **Inheritance:** To be more efficient, both `FunctionFitter` and `TestDataMapper` *inherit* from a shared `DatabaseAnalyzer` base class. This lets them share the code for connecting to and reading from the database.
* **Custom Exceptions:** I created my own error types (like `DataLoadError`) in `src/exceptions.py`. This makes handling errors way cleaner and more specific.
* **Dual Database Libraries:** I used **SQLAcademy** (in `db_loader.py`) to create the database and load the data, but then used the standard **sqlite3** library (in `analysis.py`) for reading and analyzing.
* **Unit Testing:** I wrote unit tests in the `tests/` folder to check and make sure my database loader and analysis logic were working correctly.

---

## 🔧 Tools I Used

* **Python 3.10+**
* **pandas:** For all the data handling.
* **SQLAlchemy:** For creating the database and loading the CSVs.
* **Bokeh:** For making the final interactive graphs.
* **numpy:** For the math operations (like LSE and `sqrt(2)`).
* **unittest:** For all the unit testing (it's built into Python!).

---

## 📁 Project Structure

Here's how all the files are organized:

```

DLMDSPWP01\_Assignment/
├── data/
│   ├── train.csv         \# 4 training functions
│   ├── ideal.csv         \# 50 ideal functions
│   └── test.csv          \# Test data points
│
├── src/
│   ├── **init**.py
│   ├── db\_loader.py      \# Class: DatabaseLoader (uses SQLAlchemy)
│   ├── analysis.py       \# Classes: DatabaseAnalyzer, FunctionFitter, TestDataMapper
│   ├── plotter.py        \# Function: generate\_plots (uses Bokeh)
│   └── exceptions.py     \# My custom exception classes
│
├── tests/
│   ├── **init**.py
│   ├── test\_analysis.py  \# Unit tests for FunctionFitter
│   └── test\_db\_loader.py \# Unit tests for DatabaseLoader
│
├── main.py               \# The main script you run
├── .gitignore            \# Standard Python .gitignore
├── requirements.txt      \# The list of packages to install
└── README.md             (This file)

````

---

## ⚙️ How to Run the Project

### 1. What You Need
* Python 3.10 or newer
* `git` installed on your computer

### 2. Setup Instructions

1.  **Get the code:**
    ```bash
    git clone [https://github.com/RajnibhaiVirani/Python_Assignment.git](https://github.com/RajnibhaiVirani/Python_Assignment.git)
    cd Python_Assignment
    ```

2.  **Create and activate a virtual environment:**
    * **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Create the `requirements.txt` file:**
    Create a new file named `requirements.txt` in the project folder and paste these four lines into it:
    ```
    pandas
    sqlalchemy
    bokeh
    numpy
    ```

4.  **Install the packages:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Run the Pipeline!

Now you're all set. Just run the `main.py` script:

```bash
python main.py
````

This will:

1.  Print the pipeline's progress right in your terminal.
2.  Create a new file named `assignment_pipeline.db` (your database).
3.  Create and automatically open the `assignment_results.html` file in your browser.

-----

## 🧪 Running Tests

To run the unit tests I wrote, just make sure your virtual environment is active and run:

```bash
python -m unittest discover tests
```

You should see a message letting you know that all the tests passed.

-----

## 🗺️ How it Works (The Details)

Here's the step-by-step flow that `main.py` follows when you run it:

1.  **(Step 1: Load)** It starts the `DatabaseLoader`, which uses **SQLAlchemy** to load `train.csv`, `ideal.csv`, and `test.csv` into tables inside the `assignment_pipeline.db` file.
2.  **(Step 2: Fit)** It starts the `FunctionFitter`, which connects to the database (using `sqlite3`) and reads the `train_data` and `ideal_data` tables.
3.  It runs the `find_best_functions()` method to calculate the Sum of Squared Errors (SSE) for all 4x50 combinations and find the 4 best-fitting ideal functions.
4.  **(Step 3: Map)** It starts the `TestDataMapper`, giving it the results from the fitter.
5.  It runs the `map_test_points()` method, which checks every single test point to see if it fits one of the 4 chosen functions (using the `max_deviation * sqrt(2)` rule).
6.  **(Step 4: Save)** The final list of mapped points is saved to a new table called `mapped_test_results` in the database.
7.  **(Step 5: Plot)** Finally, it calls the `generate_plots` function. This function reads all the data (training, ideal, and the new mapped results) and uses **Bokeh** to create the final tabbed HTML report.

-----

## License

This project was submitted for a university assignment. It's meant for educational and demonstrative purposes only.

```
```