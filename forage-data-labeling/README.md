# AI Data Annotation Tool

## Overview

This project began as a customer-support data labeling simulation and evolved into a Python-based AI Data Annotation Tool. The application allows human reviewers to classify customer messages by intent, sentiment, and PII indicators while applying validation and quality-review workflows.

The resulting structured dataset can be used for AI training, analytics, and human-in-the-loop machine learning processes.

This project demonstrates practical experience with:

- Python
- Pandas
- Data Annotation
- Data Validation
- CSV Processing
- Data Quality Review
- Human-in-the-Loop AI Workflows

---

## Business Problem

Organizations rely on high-quality labeled data to train AI and machine learning models. Raw customer support messages are often unstructured, inconsistent, and may contain sensitive information.

This project addresses the challenge of transforming unstructured customer communications into structured, machine-learning-ready datasets by:

- Classifying customer requests by intent
- Identifying customer sentiment
- Detecting personally identifiable information (PII)
- Applying quality assurance standards
- Improving annotation consistency

The resulting labeled data can support AI model training, customer support automation, operational reporting, and responsible AI development.

---

## Solution

To address this challenge, I developed a Python-based annotation workflow that converts unstructured customer support messages into structured datasets suitable for AI training and analysis.

The workflow:

1. Loads customer support messages from a CSV dataset
2. Presents messages for annotation
3. Allows classification of Intent, Sentiment, and PII
4. Applies standardized labeling guidelines
5. Validates user inputs
6. Exports annotations into a structured dataset
7. Supports downstream quality assurance review processes

### Run Annotation Tool

```bash
python forage-data-labeling/python_annotation_tool/app.py
```

### Run Review Tool

```bash
python forage-data-labeling/python_annotation_tool/review.py
```

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
├── screenshots/
│   └── v1-1-annotation-workflow.png
│
└── README.md
```

---

## Annotation Schema

### Intent Categories

| Intent | Description |
|----------|-------------|
| Billing | Charges, refunds, invoices, subscriptions |
| Technical | App errors, bugs, login failures |
| Account | Profile updates, account access requests |
| Other | General inquiries |

### Sentiment Categories

- Positive
- Neutral
- Negative

### PII Categories

- Yes
- No

---

## Version 1.1 Enhancements

### Validation Layer

Validation functions were added to improve data quality.

The system validates:

- Intent values
- Sentiment values
- PII values

Invalid entries are automatically replaced with default values, simulating quality controls commonly used in AI training pipelines.

### Review Workflow

A review utility was added to generate annotation summaries.

The review process calculates:

- Intent counts
- Sentiment counts
- PII counts

This allows reviewers to quickly assess label distribution and annotation quality.

---

## Screenshot

### Annotation and Review Workflow

![Annotation Workflow](screenshots/v1-1-annotation-workflow.png)

---

## Example Input

```csv
id,message
1,"My card was charged twice."
2,"Please change my email to john@email.com"
3,"The app keeps crashing."
4,"Thank you, that fixed it!"
```

---

## Example Output

```csv
id,intent,sentiment,pii_flag
1,Billing,Negative,No
2,Account,Neutral,Yes
3,Technical,Negative,No
4,Other,Positive,No
```

---

## Results

Successfully transformed raw customer support messages into structured datasets containing:

- Intent labels
- Sentiment labels
- PII indicators

The resulting data can be used for:

- AI model training
- Customer support automation
- Sentiment analysis
- Operational reporting
- Data quality monitoring
- Human-in-the-loop AI workflows

This project demonstrates how structured annotation workflows improve data quality and create reliable datasets for machine learning applications.

---

## Sample Output

```text
Intent Counts

technical    2
account      2
billing      1

Sentiment Counts

negative     3
neutral      1
positive     1

PII Counts

no           4
yes          1
```

---

## Skills Demonstrated

### AI Operations

- Human-in-the-Loop AI
- Data Annotation
- Dataset Preparation
- Quality Assurance

### Data Quality

- Data Validation
- Process Standardization
- Error Reduction
- Consistency Reviews

### Technical Skills

- Python
- Pandas
- CSV Processing
- Git
- GitHub
- Command-Line Applications

---

## Version History

### Version 1.0

- Built annotation workflow
- Loaded messages from CSV
- Captured intent, sentiment, and PII labels
- Exported labeled dataset to CSV

### Version 1.1

- Added validation functions
- Added review workflow
- Added annotation summary reporting
- Improved data quality controls

---

## Future Enhancements

Planned improvements include:

- Confidence scoring
- Multiple annotator support
- Label agreement analysis
- Dashboard reporting with Power BI
- Machine learning model integration
- Web-based annotation interface

---

## Author
```
**LaQuita Jordan**

Data Analytics Graduate Student | AI, Python, & Data Projects Portfolio
```
GitHub Repository: https://github.com/lajordan09/job-simulations
