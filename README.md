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

Root cause matrix

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


![COV](UCW_DAP.png)


![COV](ETL_UCW.png)



## 5. Data Quality Control & Monitoring

**Objective:**

The objective of this project is to design and implement a comprehensive Data Quality Control (DQC) framework tailored for the City of Vancouver's water quality dataset. The goal is to ensure that all data used in downstream analysis—such as exploratory data analysis, reporting, and predictive modeling—is clean, accurate, and trustworthy. By implementing automated data validation and segregation rules, this project aims to enhance the integrity, reliability, and overall value of the dataset while minimizing the manual effort involved in identifying and correcting data issues.

**Background:**

With the increasing volume of environmental data collected through IoT sensors and water monitoring systems, data quality concerns such as missing values, duplicates, outdated records, and inconsistencies have become more frequent. These issues can compromise the validity of insights drawn from the data and mislead critical decisions. As part of our broader data engineering efforts, this project was initiated to automate the detection and handling of low-quality data before it is ingested into data pipelines for analysis. Stakeholders and analysts needed a structured, automated approach to ensure that only high-quality data was made available for analysis and reporting.

**Scope of the Project:**

The DQC framework is built around three critical dimensions of data quality:

Completeness – Ensures that essential fields like Operating Permit Number are adequately populated. Missing values in these critical fields can impact regulatory compliance and operational tracking.

Uniqueness – Verifies that certain columns (like Turbidity) maintain high distinctiveness, helping detect duplicate or copy-paste errors in data collection.

Freshness – Filters out outdated records (older than 1000 days) to ensure that analytical insights reflect current and relevant conditions.

This structured scope allows the data quality framework to be applied across datasets with similar structures and regulatory importance.

**Methodology:**

1. Defining Data Quality Rules:
The first phase involved establishing specific data quality thresholds based on business needs and environmental monitoring standards:

Completeness Rule: The Operating Permit Number must be populated in at least 95% of records. This ensures traceability of the sample origin.

Uniqueness Rule: At least 99% of the Turbidity readings should be unique to confirm proper sensor functioning and prevent data duplication.

Freshness Rule: Records older than 1000 days (approximately 3 years) are considered outdated and are filtered out to maintain the relevance of insights.

These rules were documented and approved by stakeholders before pipeline implementation.

2. Building the Glue ETL Pipeline:

Using AWS Glue, a visual ETL job was designed to automate the validation process. The key components of the workflow include:

Data Ingestion: Raw CSV files were stored in Amazon S3 and catalogued using AWS Glue Crawler.

Data Validation Steps:

Applied completeness checks by counting non-null values in critical columns.

Used custom logic in Glue DynamicFrames to calculate distinct counts for uniqueness.

Applied date-based filters to assess data freshness.

Data Segregation: Based on validation results, records were routed into two separate S3 paths:

/passed/ folder for records that met all quality criteria.

/failed/ folder for records that violated any rules for further inspection or reprocessing.

3. Monitoring and Alerts with AWS CloudWatch:

To ensure real-time visibility and long-term monitoring of data quality performance, AWS CloudWatch was integrated with S3 buckets and Glue ETL jobs. Key metrics and alerts configured:

S3 Bucket Monitoring: Dashboards track the growth of the passed and failed folders over time.

Error Rate Alerts: Notifications are triggered if the size of buckets exceeds the defined threshold, indicating possible data collection issues.

**Tools and Technologies Used:**

AWS Glue (Crawler & ETL): For schema detection, rule-based transformations, and workflow automation.

Amazon S3: For raw, passed, and failed data storage.

Amazon CloudWatch: For pipeline monitoring and alerting.

SQL & PySpark: For writing validation logic and dynamic transformations inside the ETL jobs.

**Deliverables:**

A comprehensive Data Quality Rulebook defining all business logic

Glue ETL job scripts with clearly defined transformation steps

Data segregation into separate S3 folders (passed and failed)

CloudWatch monitoring dashboard with custom metrics and alarms

Validation reports summarizing quality metrics across completeness, uniqueness, and freshness

Documentation of architecture, flow diagrams, and quality logs

**Key Insights and Results:**

Over 98% of the dataset passed all quality checks after the first run, proving the effectiveness of the framework.

The Freshness rule helped filter out nearly 20% of legacy records, leading to more current and actionable analysis in subsequent projects.

Automated separation of failed records saved hours of manual data cleaning and allowed analysts to focus on insights rather than error checking.

CloudWatch alerts enabled early detection of potential issues in upstream data collection, allowing timely corrections before data entered the core analysis environment.

This Data Quality Control initiative not only improved the integrity of the dataset used in the water monitoring system but also established a reusable and scalable framework for future data validation tasks. It significantly boosted confidence in analytical outcomes and ensured that only accurate, complete, and recent data entered the analytics pipeline.


![COV](DataQC.png)

![COV](DataETL.png)

![COV](dashboard.png)





