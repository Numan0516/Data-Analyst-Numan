**Data-Analyst-Numan**
# AWS Data Projects Portfolio

Welcome to my portfolio! This repository contains **five key data projects** illustrating how I used **AWS services**—like **S3**, **AWS Glue DataBrew**, **AWS Glue ETL**, **Amazon Athena**, and **CloudWatch** and various other tools—to perform data ingestion, profiling, cleaning, transformation, analysis, and monitoring.

> **Table of Contents**
> 1. [Exploratory Data Analysis](#1-exploratory-data-analysis)
> 2. [Descriptive Analysis](#2-descriptive-analysis)
> 3. [Diagnostic Analysis](#3-diagnostic-analysis)
> 4. [Data Wrangling](#4-data-wrangling)
> 5. [Data Quality Control & Monitoring](#5-data-quality-control--monitoring)



## 1. Exploratory Data Analysis

**Project Title: Exploring Temperature-Turbidity Correlation in Vancouver's Water Quality Data**

**Objective**:
The objective of this project is to perform an in-depth Exploratory Data Analysis (EDA) using the City of Vancouver’s water quality dataset. This analysis focuses on investigating the relationship between temperature and turbidity levels in drinking water systems, with the ultimate aim of understanding if temperature fluctuations can act as a predictor for changes in water clarity. This insight can assist in identifying seasonal or environmental influences on water quality.

**Dataset:**
The dataset includes real-world water quality readings collected by the City of Vancouver.

Key attributes include:

Temperature: The recorded water temperature at various monitoring points

Turbidity: A measure of water clarity, where higher values indicate more particles or cloudiness

Operating Permit Number, Facility ID, Sample Date, and other operational metadata

**Methodology:**

Data Storage & Collection: Data was initially stored in Amazon S3 for centralized access and versioning.

Data Profiling: AWS Glue DataBrew was used to profile the data, identify missing values, check column formats, and inspect outliers.

Data Cleaning: A cleaning recipe was created in DataBrew, which included dropping irrelevant columns (e.g., mechanical, permit status), fixing data types, and removing duplicates.

**Analysis:** 
Cleaned data was queried using Amazon Athena to explore:

Correlation between temperature and turbidity

Seasonal trends or time-based changes in turbidity

Distribution and variance of turbidity values across different months and temperature ranges

**Tools and Technologies**:

AWS S3, AWS Glue DataBrew, Amazon Athena

**Deliverables**:

Cleaned dataset in S3

SQL queries and outputs via Athena

**Key Findings:**

The analysis indicated a moderate correlation between increased water temperature and elevated turbidity levels during the summer months. It also uncovered recurring seasonal spikes in turbidity, emphasizing the need for preventive water system maintenance during warm periods.
![COV](COV_Drawio.png)

![COV](profiling.png)

![COV](profiling1.png)

![BQ](BQ_Example.png)

---

## 2. Descriptive Analysis

**Project Title**: Summarizing Vancouver Water Quality Patterns for Annual Review

**Objective:**
This project provides a descriptive statistical summary of water quality metrics collected from the City of Vancouver. The purpose is to gain a foundational understanding of the data, identify usage trends over time, and help stakeholders recognize recurring behaviors in environmental measurements.

**Dataset:**
The dataset includes:

Time-series water quality measurements (temperature, turbidity)

Sampling details from multiple locations

Permit and facility information

Data captured over multiple years and seasons


**Methodology:**

Data Collection: The dataset was loaded from AWS S3 into AWS Glue.

Schema Detection: AWS Glue Crawler was used to automatically identify field types and build a catalog.

ETL Process: AWS Glue ETL transformed the dataset by standardizing formats and calculating:

Monthly averages

Year-over-year variations

Total number of records per location or season

**Tools and Technologies:**

AWS Glue Crawler, AWS Glue ETL, Amazon S3

**Deliverables:**

Data catalog in AWS Glue

Summary tables and basic stats (e.g., average turbidity per month)

Time-series charts for reports

**Key Findings:**

The data revealed predictable seasonal fluctuations, with higher turbidity levels recorded in warmer months. Some locations consistently showed higher values than others, indicating possible environmental or infrastructure-based differences.

![COV](catalog.png)

![COV](summarization.png)

## 3. Diagnostic Analysis

**Project Title**: Investigating Anomalies in Vancouver Water Quality Data

**Objective:**

The objective is to conduct a diagnostic analysis to identify the underlying causes of abnormal turbidity spikes or missing data trends in Vancouver’s water quality monitoring. The goal is to inform city water departments about potential operational or environmental concerns.

**Background:**
City departments raised concerns about sudden spikes in turbidity in particular months. Understanding whether these are due to real-world events or system/sensor issues is critical for taking corrective actions.

**Dataset:**

Combines multiple sources:

Sensor logs with timestamps

Turbidity and temperature readings

Location IDs and facility details

**Methodology:**

Data Integration: Combined datasets from various sensors via AWS Glue.

Anomaly Detection: Used DataBrew to check for:

Irregular timestamp gaps

Sudden outlier readings

Invalid or duplicated records

Root Cause Analysis: Evaluated possible issues such as:

Sensor recalibration periods

Sampling errors

Unreported weather events

Segmentation: Analyzed anomalies across different facility IDs and sampling regions

**Tools and Technologies:**

AWS Glue, DataBrew, Amazon S3, Excel (for cross-checking outlier clusters)

**Deliverables:**

Anomaly detection report

Charts highlighting abnormal readings

Root cause matrix (e.g., fishbone diagram or 5-whys)

**Key Findings:**

Most anomalies coincided with sensor maintenance periods or data entry gaps. This highlighted the need for better documentation of sensor servicing schedules and automated anomaly flagging.


## 4. Data Wrangling

**Project Title:** Data Wrangling for Academic Standing Analysis at UCW

**Objective:**

To clean, merge, and restructure student academic data to prepare it for academic standing evaluations at the University Canada West. The project ensures that data from various student information systems is consolidated, reliable, and analytics-ready.

**Background:**

UCW needs accurate and timely academic standing reports for administrative and student services. However, data is often scattered across systems, lacking consistency.

**Dataset:**

Includes:

Student demographic data

Course grades, GPA, and credits

Program and department codes

Enrolment records

**Methodology:**

Data Profiling: Used AWS Glue DataBrew to assess field quality.

Cleaning: Dropped irrelevant columns, converted strings to proper data types (e.g., dates, numeric grades).

Transformation: Added calculated fields like cumulative GPA, course completion ratio.

Data Organization: Categorized data into three buckets in S3:

Raw: untouched input

Transformed: cleaned and structured

Curated: final dataset for academic standing logic

**Tools and Technologies:**

AWS Glue DataBrew, Glue ETL, Amazon S3

**Deliverables:**

Three-layered S3 storage

Cleaned and labeled dataset

Wrangling documentation (recipes, transformations)

**Key Achievements:**

Reduced data processing time by 50%. Enabled UCW to generate academic standing reports with more accuracy and less manual effort.

**Project Description**: Data Wrangling for Academic Standing Procedure (UCW)  
**Objective**: Create a **Data Analysis Pipeline (DAP)** for UCW’s academic standing data.

![COV](UCW_DAP.png)

**What I Did**  
- **AWS Glue DataBrew**: Cleaned and standardized student data (dropped irrelevant columns, fixed data types)  
- **Glue Crawler & ETL**: Stored data in raw, transformed, and curated buckets in **S3**

![COV](ETL_UCW.png)

- **Consolidation**: Ensured consistent IDs and metrics to enable accurate academic standing checks

**Key Takeaways**  
- Streamlined the data preparation workflow  
- Organized data into distinct layers (raw, transformed, curated) for clarity

<!-- Insert a screenshot or diagram for Data Wrangling:
![Data Wrangling Flow](images/data_wrangling_flow.png)
-->

---

## 5. Data Quality Control & Monitoring

### 5.1 Data Quality Control
**Project Description**: Implementing data governance checks for City of Vancouver  
**Objective**: Verify completeness, uniqueness, and freshness of water data before further analysis.

1. **Completeness**: `operating permit number` must be at least 95% populated  
2. **Uniqueness**: Turbidity values must be at least 99% unique  
3. **Freshness**: Exclude data older than 1000 days

![COV](DataQC.png)

- **AWS Glue Visual ETL** pipeline splits data into “passed” or “failed” S3 buckets based on rules

![COV](DataETL.png)

### 5.2 Monitoring with AWS CloudWatch
- **Dashboards**: Track S3 bucket size (raw vs. transformed)  
- **Alarms**: Trigger if usage exceeds 40,000 bytes

![COV](dashboard.png)

**Key Takeaways**  
- Automated data quality checks improve dataset reliability  
- Real-time monitoring allows rapid detection of anomalies




