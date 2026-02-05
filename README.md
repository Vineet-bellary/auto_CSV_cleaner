# Automatic CSV Data Cleaner

## Overview

Automatic CSV Data Cleaner is a web-based application that simplifies **data preprocessing for Machine Learning workflows**.It provides a no-code interface to **analyze, clean, and validate CSV datasets**, making them ready for downstream ML tasks.

The project focuses on implementing an **industry-style data preprocessing pipeline** with clear separation of concerns, robust state management, and user-driven actions.

## Problem Statement

In real-world Machine Learning projects, a significant portion of development time is spent on **cleaning and preparing datasets**.This process often requires programming expertise and repetitive preprocessing code, creating a barrier for beginners and non-technical users.

## Proposed Solution

This project provides a **user-friendly web interface** that automates common data preprocessing steps while maintaining transparency and control.Users can upload a CSV file, analyze its quality, perform automatic cleaning using safe defaults, and verify improvements through re-profiling.

## Key Features (Implemented)

### 1 CSV Dataset Ingestion

* Upload CSV files through the UI

* Dataset loaded using Pandas

* Preview of uploaded data

* Automatic session reset on new uploads to avoid stale state

### 2 Dataset Profiling (Pre-Cleaning)

A profiling layer analyzes the dataset before any transformations:

* Total rows and columns

* Duplicate row count

* Column-wise data types

* Unique value counts per column

* Missing value counts per column

Profiling results are displayed using a structured tab-based UI for clarity.

### 3 Automatic Data Cleaning (MVP)

A one-click auto-cleaning mechanism is implemented using industry-safe defaults:

* Removal of duplicate rows

* Trimming whitespace from column names

* Missing value handling:

  * Numerical columns → filled using **median**

  * Categorical columns → filled using **mode**

* Trimming whitespace in string columns

These defaults are commonly used in production ML pipelines to minimize bias and reduce preprocessing errors.

### 4 Dataset Profiling (Post-Cleaning)

After cleaning, profiling is re-run on the processed dataset to:

* Validate the impact of cleaning

* Confirm reduction in missing values and duplicates

* Ensure dataset consistency before ML usage

Post-cleaning profiling is displayed **only after explicit user action**, ensuring correct UI behavior.

### 5 Robust State Management

* Uses Streamlit session state safely

* Prevents unintended UI rendering during app reruns

* Cleaning results are shown strictly based on user-triggered actions

* Previous cleaning state is cleared when a new dataset is uploaded

## Project Architecture

```txt
├── app
│   ├── config
│   │   └── settings.py
│   ├── core
│   │   ├── cleaner.py
│   │   ├── loader.py
│   │   ├── profiler.py
│   │   ├── utils.py
│   │   └── validator.py
│   ├── ui
│   │   ├── cleaning.py
│   │   ├── export.py
│   │   ├── profiling.py
│   │   └── upload.py
│   └── main.py
├── data
│   ├── processed
│   └── raw
├── .gitignore
├── README.md
└── requirements.txt
```

## Technology Stack

* **Python**

* **Streamlit** – Web application framework

* **Pandas** – Data manipulation and analysis

* **NumPy** – Numerical operations

## Application Workflow

Upload CSV
   ↓
Dataset Profiling (Before Cleaning)
   ↓
Auto Clean Dataset (User Action)
   ↓
Dataset Profiling (After Cleaning)

## MVP Scope

The current implementation focuses on delivering a stable and usable **Minimum Viable Product (MVP)**:

* CSV upload

* Dataset profiling

* Automatic cleaning

* Post-cleaning validation

Advanced preprocessing and ML-specific features are intentionally excluded at this stage.

## Future Enhancements

* User-configurable missing value strategies

* Download cleaned dataset

* Train–test split export

* Feature encoding and scaling

* ML task type detection (classification/regression)

* Dataset versioning

* Preprocessing pipeline export

## Key Learnings

* Importance of profiling datasets before and after preprocessing

* Practical Streamlit session state management

* Separation of UI and core logic in data applications

* Designing data tools with an MVP-first approach

## Author

**Vineet** - <vineet.bellary@gmail.com>
