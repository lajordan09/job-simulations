````markdown
# AI Data Annotation Workflow (Version 1.1)

## Project Overview

**Project Name:** AI Data Annotation Workflow

**Objective:**  
Build a Python-based annotation workflow that simulates tasks commonly performed by AI Data Annotators and AI Trainers. The application reads customer support messages from a CSV file, captures human annotations, validates responses, exports labeled data, and generates quality review reports.

---

## Business Problem

AI systems require large amounts of accurately labeled training data.

Manual annotation processes can introduce:

- Inconsistent labels
- Typographical errors
- Missing information
- Data quality issues

This project demonstrates how Python can be used to create a structured annotation workflow that improves consistency and produces training-ready datasets.

---

## Technologies Used

- Python
- Pandas
- CSV Processing
- Git
- GitHub
- VS Code
- GitHub Codespaces

---

# Project Structure

```text
forage-data-labeling/
│
├── data/
│   └── sample_messages.csv
│
├── outputs/
│   └── labeled_data.csv
│
├── python_annotation_tool/
│   ├── app.py
│   ├── review.py
│   ├── utils.py
│   └── requirements.txt
│
└── README.md
```

---

# Version 1.0 Workflow

## Step 1: Load Source Data

The application reads customer messages from:

```text
sample_messages.csv
```

Using:

```python
pd.read_csv()
```

---

## Step 2: Display Messages

Each customer message is displayed one at a time.

Example:

```text
Message ID: 1
Message: My card was charged twice.
```

---

## Step 3: Capture Annotation Inputs

For each message, the annotator provides:

### Intent

Options:

- Billing
- Technical
- Account
- Other

### Sentiment

Options:

- Positive
- Neutral
- Negative

### PII Flag

Options:

- Yes
- No

---

## Step 4: Store Annotations

Annotations are collected into a Python list.

Example:

```python
{
    "id": 1,
    "intent": "billing",
    "sentiment": "negative",
    "pii_flag": "no"
}
```

---

## Step 5: Export Results

The application converts annotations into a DataFrame.

```python
pd.DataFrame()
```

Then exports:

```text
labeled_data.csv
```

---

# Version 1.1 Enhancements

## Enhancement 1: Input Validation

Created:

```text
utils.py
```

Purpose:

Prevent invalid annotation values from entering the dataset.

### Intent Validation

Valid values:

```text
billing
technical
account
other
```

If invalid:

```text
Invalid intent. Defaulting to 'other'.
```

### Sentiment Validation

Valid values:

```text
positive
neutral
negative
```

If invalid:

```text
Invalid sentiment. Defaulting to 'neutral'.
```

### PII Validation

Valid values:

```text
yes
no
```

If invalid:

```text
Invalid value. Defaulting to 'no'.
```

---

## Enhancement 2: Review Workflow

Created:

```text
review.py
```

Purpose:

Provide a quick quality-control summary after annotations are completed.

### Review Metrics

#### Intent Counts

Example:

```text
billing     1
technical   2
account     2
```

#### Sentiment Counts

Example:

```text
negative    3
neutral     1
positive    1
```

#### PII Counts

Example:

```text
no     4
yes    1
```

---

# Git & GitHub Workflow

## Version Control Activities

### Initial Commit

Created Version 1.0 including:

- app.py
- sample_messages.csv
- labeled_data.csv
- README.md

### Git Tag

Created release tag:

```bash
git tag -a v1.0 -m "Version 1: AI Data Annotation Tool"
git push origin v1.0
```

Purpose:

Mark the first working version of the application.

### Version 1.1 Development

Added:

```text
utils.py
review.py
```

Enhanced:

```text
app.py
```

### Repository Maintenance

Created:

```text
.gitignore
```

Contents:

```text
__pycache__/
*.pyc
```

Purpose:

Prevent Python cache files from being tracked in Git.

### Cleanup

Removed:

```text
__pycache__
```

from repository tracking.

---

# Skills Demonstrated

## Python

- Functions
- Loops
- Lists
- Dictionaries
- Imports

## Data Processing

- CSV ingestion
- Data validation
- Data transformation
- Data export

## Pandas

- read_csv()
- DataFrame()
- to_csv()
- value_counts()

## Software Development

- Modular design
- Input validation
- Reporting workflow
- Version control

## Git & GitHub

- Clone
- Commit
- Push
- Pull
- Merge conflict resolution
- Git tags
- Repository cleanup

---

# Key Takeaways

This project demonstrates the complete lifecycle of a small AI data labeling workflow:

1. Load raw data
2. Capture annotations
3. Validate inputs
4. Export structured outputs
5. Review annotation quality
6. Track versions with Git
7. Maintain a clean repository

The workflow mirrors common tasks performed by:

- AI Data Annotators
- AI Trainers
- Data Quality Specialists
- Machine Learning Operations Support Teams

---

# Version History

## Version 1.0

**Released:** June 2026

Features:

- CSV message ingestion
- Intent labeling
- Sentiment labeling
- PII flagging
- CSV export

## Version 1.1

**Released:** June 2026

Features:

- Input validation
- Annotation review reporting
- Repository cleanup
- .gitignore implementation
- Improved data quality controls

---

# Next Planned Release

## Version 2.0

Potential enhancements:

- Confidence scores
- Reviewer notes
- Annotation timestamps
- Dashboard reporting
- Multiple annotator simulation
- Quality scoring metrics
- Analytics visualizations

This version would move the project closer to a production-style AI training data workflow.
````
