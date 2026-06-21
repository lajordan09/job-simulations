# AI Data Annotation Workflow

A Python-based data annotation tool that simulates real-world AI training data workflows. This project allows users to classify customer support messages by intent, sentiment, and PII indicators, then export structured labeled data for machine learning and analytics use cases.

---

## Project Overview

This project began as a data labeling and quality assurance simulation focused on preparing training data for AI and machine learning systems.

The original simulation involved manually reviewing customer support messages and applying standardized labels for:

- Intent Classification
- Sentiment Analysis
- Personally Identifiable Information (PII) Detection
- Data Quality Review

After completing the simulation, I expanded the project by developing a Python-based annotation workflow to automate and standardize portions of the labeling process.

The resulting application allows users to:

- Load customer messages from a CSV file
- Classify messages by intent
- Label sentiment
- Flag potential PII
- Validate annotation inputs
- Export structured training datasets
- Generate annotation review summaries

This project demonstrates how a manual AI data labeling workflow can evolve into a repeatable software solution that supports data quality and AI training operations.

---

## Features

### Version 1.0

- Load customer messages from CSV
- Capture intent classifications
- Capture sentiment labels
- Flag potential PII indicators
- Export labeled data to CSV

### Version 1.1

- Input validation for annotation fields
- Modular utility functions
- Annotation review workflow
- Summary reporting
- Git version control improvements
- Repository cleanup using `.gitignore`

---
## Project Evolution

### Phase 1: Data Labeling Simulation

Completed a simulated AI Data Labeling and Quality Assurance project involving:

- Intent classification
- Sentiment analysis
- PII identification
- Quality assurance reviews

### Phase 2: Python Workflow Development

Designed and built a Python application that transforms the manual annotation process into a repeatable workflow.

Enhancements included:

- CSV-based data ingestion
- Annotation capture
- Input validation
- Automated dataset generation
- Annotation reporting
- Version-controlled development using Git and GitHub

### Current Status

Version 1.1

Features:

- Annotation workflow
- Validation utilities
- Review reporting
- Structured CSV outputs
- Git versioning

### Next Phase

Version 2.0 will focus on introducing automation features such as:

- Automatic PII detection
- Annotation confidence scoring
- Reviewer workflows
- Analytics and dashboard reporting
---

## Project Structure

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
├── docs/
│   └── Version-1.1-Workflow.md
│
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- CSV Processing
- Git
- GitHub
- VS Code

---

## How It Works

### Step 1: Load Data

The application reads customer support messages from:

```text
sample_messages.csv
```

### Step 2: Annotate Messages

For each message, the user provides:

- Intent
  - Billing
  - Technical
  - Account
  - Other

- Sentiment
  - Positive
  - Neutral
  - Negative

- PII Flag
  - Yes
  - No

### Step 3: Validate Inputs

The application validates entries before saving them to the dataset.

### Step 4: Export Results

Annotations are exported to:

```text
outputs/labeled_data.csv
```

### Step 5: Review Results

Run the review workflow to generate annotation summaries and quality checks.

---

## Running the Application

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Annotation Workflow

```bash
python forage-data-labeling/python_annotation_tool/app.py
```

### Run Annotation Review

```bash
python forage-data-labeling/python_annotation_tool/review.py
```

---

## Sample Output

### Intent Summary

```text
billing     1
technical   2
account     2
```

### Sentiment Summary

```text
negative    3
neutral     1
positive    1
```

### PII Summary

```text
no     4
yes    1
```

---

## Skills Demonstrated

### Python Development

- Functions
- Loops
- Lists
- Dictionaries
- Imports

### Data Processing

- CSV ingestion
- Data validation
- Data transformation
- Data export

### Data Analysis

- Pandas
- DataFrames
- Summary statistics

### Software Development

- Modular code design
- Input validation
- Reporting workflows
- Version control

### Git & GitHub

- Repository management
- Branch synchronization
- Merge conflict resolution
- Git tags
- Repository maintenance

---

## Version History

### Version 1.0

- CSV message ingestion
- Intent labeling
- Sentiment labeling
- PII detection
- CSV export

### Version 1.1

- Input validation
- Annotation review workflow
- Summary reporting
- .gitignore implementation
- Repository cleanup

---

## Future Enhancements (Version 2.0)

Planned improvements include:

- Confidence scores
- Reviewer comments
- Annotation timestamps
- Dashboard reporting
- Multi-label classification
- Analytics visualizations
- Quality scoring metrics

---

## Author

**LaQuita Jordan**
Data Analytics Graduate Student | AI & Data Projects Portfolio

GitHub Repository: job-simulations
