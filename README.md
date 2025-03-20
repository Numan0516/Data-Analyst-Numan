# AWS Data Quality ETL Pipeline

## Overview
This project demonstrates an **AWS Glue ETL pipeline** that validates data **uniqueness, completeness, and freshness** before processing it for the City of Vancouver. If the data fails validation, it is moved to a failed-data folder; otherwise, it is processed and stored in a clean dataset.

## Architecture
The pipeline follows this process:
1. **Data is uploaded to Amazon S3**
2. **AWS Glue ETL job runs validation checks**
3. **Data is classified as Passed or Failed**:
   - Passed data is moved to the `processed-data` folder.
   - Failed data is stored in the `failed-data` folder for review.
4. **AWS Athena queries data** for analysis
5. **AWS CloudWatch monitors performance**
6. **AWS SNS sends notifications** for failures or success

## Technologies Used
- **AWS S3** – Storage for input and output data
- **AWS Glue** – ETL and data validation
- **AWS Athena** – SQL querying
- **AWS CloudWatch** – Monitoring
- **AWS SNS** – Notifications
- **AWS KMS** – Data security

## Data Quality Checks
- **Uniqueness Check:** Ensures IDs are unique.
- **Completeness Check:** No missing values in required fields.
- **Freshness Check:** Data is recent and valid.

## File Structure
```
AWS-Data-Quality-ETL/
│── README.md
│── glue_etl_script.py
│── architecture_diagram.png  # Your architecture diagram
│── sample_input_data/  # Example dataset
│── processed_data/  # Folder for cleaned data
│── failed_data/  # Folder for rejected data
```

## How to Run
1. Upload input data to S3 bucket.
2. Trigger AWS Glue ETL job.
3. Monitor results in CloudWatch.
4. Processed data is available in `processed-data/`.
5. Failed data is moved to `failed-data/` for review.

## Notifications
AWS SNS sends alerts for:
- **Success:** Data processing completed.
- **Failure:** Data validation failed.

## Conclusion
This project showcases how AWS Glue automates data validation and ETL processing for a real-world use case. 🎯
