# Self-Healing-Code-System
AI-powered system for automatic error detection and code correction.

# Self-Healing Code System

## Overview

The **Self-Healing Code System** is a proof-of-concept project that demonstrates how an AI/LLM can automatically analyze and fix failing unit tests.
The system takes failed test cases as input, uses a language model to suggest corrections, and validates the fixes by rerunning the tests.

This approach helps improve developer productivity by reducing the time spent debugging and correcting test cases.

---

## Key Features

* Automated **unit test failure detection**
* AI-powered **test case correction**
* Validation by **rerunning corrected tests**
* Modular Python structure for easy extension
* Lightweight backend using **Flask**

---

## Project Structure

```
Self-Healing-Code-System
│
├── project/
│   ├── app.py                # Flask application
│   ├── utils.py              # Utility functions for model prediction
│   └── tests/
│       └── test_utils.py     # Unit tests
│
├── static/                   # Frontend assets
│   ├── app.css
│   └── app.js
│
├── template/
│   └── app.html              # Simple UI for testing
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How the Self-Healing Workflow Works

1. A unit test fails during execution.
2. The failed test case and error message are passed to an LLM.
3. The LLM analyzes the failure and generates a corrected version of the test.
4. The corrected test is executed again.
5. If the test passes, the fix is accepted.

---

## Installation

Clone the repository:

```
git clone https://github.com/ajayyy17/Self-Healing-Code-System.git
cd Self-Healing-Code-System
```

Create a virtual environment:

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```
python project/app.py
```

Then open the browser at:

```
http://localhost:5000
```

---

## Running Unit Tests

```
pytest
```

---

## Technologies Used

* Python
* Flask
* PyTest
* NumPy / Pandas
* Scikit-learn
* LLM-based reasoning for automated test correction

---



AI / Machine Learning Engineer with experience in Generative AI, ML pipelines, and data-driven systems.

