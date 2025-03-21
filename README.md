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
**Project Description**: EDA of City of Vancouver data  
**Objective**: Analyze and understand how changes in temperature might affect turbidity levels.

**What I Did**  
- **Data Storage**: Placed the raw data in **Amazon S3**.  
- **Profiling**: Used **AWS Glue DataBrew** to identify missing values, invalid data types, and duplicate records.  
- **Cleaning**: Created a **DataBrew recipe** to drop unnecessary columns (e.g., permit status, mechanical).  
- **Analysis**: Employed **Amazon Athena** to query the cleaned data and answer three business questions:
  1. Correlation between temperature changes and turbidity levels  
  2. Trends in turbidity over specific time periods  
  3. Identification of outlier temperature or turbidity readings

**Key Takeaways**  
- Insight into temperature–turbidity correlations  
- Simplified queries by removing irrelevant columns  
- Demonstrated speed of AWS Glue DataBrew for data profiling and recipe-based cleaning

![COV](images/COV_Drawio.png)
(main/COV_Drawio.png)
-->

---

## 2. Descriptive Analysis
**Project Description**: Summarizing Vancouver data using AWS Glue ETL  
**Objective**: Provide a descriptive summary (data cataloging & summarization) **without** deep business queries.

**What I Did**  
- **Data Cataloging**: Created a **Glue Crawler** to automatically detect schemas and populate the **AWS Glue Data Catalog**.  
- **Data Summarization**: Built an **AWS Glue ETL** pipeline to transform the dataset (generating aggregated stats like mean, median, count).  
- **Analysis**: This time, *did not* run business questions via Athena; focus was on stable summaries.

**Key Takeaways**  
- Established a robust data catalog for quick data discovery  
- Collected aggregated stats to track high-level trends

<!-- Insert a screenshot or diagram related to Descriptive Analysis:
![Descriptive Analysis Diagram](images/descriptive_analysis.png)
-->

---

## 3. Diagnostic Analysis
**Project Description**: Investigating underlying issues or anomalies in the Vancouver dataset  
**Objective**: Diagnose potential factors contributing to unusual data patterns (e.g., sudden spikes in turbidity).

**What I Did**  
- **Data Collection & Preparation**: Continued using **AWS Glue** (Crawler + ETL) to unify data.  
- **Trend & Correlation Checks**: Used **DataBrew** to verify data integrity before analyzing.  
- **Root-Cause Insights**: Explored sensor calibration times, missing data segments, etc., for potential anomalies.  
- **Analysis Tools**: Focused on basic descriptive statistics, with minimal or no Athena usage here.

**Key Takeaways**  
- Identified sensor calibration issues or data gaps causing spikes/dips  
- Reinforced the value of thorough data cleaning and consistent data cataloging

<!-- Insert a screenshot or diagram for Diagnostic Analysis:
![Diagnostic Analysis Screenshot](images/diagnostic_analysis.png)
-->

---

## 4. Data Wrangling
**Project Description**: Data Wrangling for Academic Standing Procedure (UCW)  
**Objective**: Create a **Data Analysis Pipeline (DAP)** for UCW’s academic standing data.

**What I Did**  
- **AWS Glue DataBrew**: Cleaned and standardized student data (dropped irrelevant columns, fixed data types)  
- **Glue Crawler & ETL**: Stored data in raw, transformed, and curated buckets in **S3**  
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

- **AWS Glue Visual ETL** pipeline splits data into “passed” or “failed” S3 buckets based on rules

### 5.2 Monitoring with AWS CloudWatch
- **Dashboards**: Track S3 bucket size (raw vs. transformed)  
- **Alarms**: Trigger if usage exceeds 40,000 bytes

**Key Takeaways**  
- Automated data quality checks improve dataset reliability  
- Real-time monitoring allows rapid detection of anomalies

<!-- Insert a screenshot or diagram showing Data Quality checks or CloudWatch metrics:
![Data Quality & Monitoring Dashboard](images/data_quality_monitoring.png)
-->



