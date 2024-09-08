# Speed-Dash Data Pipeline

## 🏗️ Architecture Diagram

![Speed Dash Data Pipeline Architecture](https://github.com/desininja/Speed-Dash-Data-Pipeline/blob/main/Project%20Screenshots/Speed%20Dash%20Data%20Pipeline%20Architecture.png)

This project demonstrates an automated ETL (Extract, Transform, Load) pipeline using AWS services to process daily delivery data for a hypothetical company called SpeedDash. The goal is to provide a simple, scalable, and efficient solution for real-time data processing.

## 🌟 Project Overview

The Speed-Dash Data Pipeline is a serverless data processing solution that leverages AWS services to automate the extraction, transformation, and loading of daily delivery data. When a JSON file containing delivery records is uploaded to a designated S3 bucket, an AWS Lambda function is triggered. The function filters the records based on delivery status and stores the processed data in a different S3 bucket. Additionally, Amazon SNS is used to send notifications regarding the status of data processing, ensuring stakeholders are informed in real-time.

## 🚀 Motivation

While Data Engineering projects can often seem complex and daunting, this project showcases a straightforward approach to building a functional data pipeline. By leveraging managed AWS services, the focus remains on solving the problem rather than dealing with infrastructure management. The project is inspired by similar real-world scenarios and is designed to be both educational and practical.

## 🛠️ AWS Services Used

1. **Amazon S3**: Used for storing both raw input files and processed output files. It serves as the data lake for this project.  
   [Learn More About Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

2. **AWS Lambda**: A serverless compute service that runs the data processing logic whenever a new file is uploaded to the S3 bucket. It is configured to filter records based on delivery status and save the filtered data to another S3 bucket.  
   [Learn More About AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

3. **Amazon SNS (Simple Notification Service)**: Used to send notifications about the processing status to subscribed users via email.  
   [Learn More About Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)

4. **AWS CodeBuild**: A fully managed build service used to automate the deployment process of the Lambda function and its dependencies from a GitHub repository.  
   [Learn More About AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)

## 📝 Requirements

- **AWS Account**  
- **Amazon S3 Buckets**: `speed-dash-landing-zone` (for raw files) and `speed-dash-target-zone` (for processed files)  
- **AWS Lambda**  
- **Amazon SNS**  
- **AWS IAM Roles** (for managing permissions)  
- **AWS CodeBuild** (for CI/CD)  
- **GitHub** (for version control)  
- **Python**, including the `pandas` library  
- **Email Subscription** for SNS notifications  

## 🔄 Steps to Implement the Pipeline

1. **Set Up S3 Buckets**:  
   - Create two S3 buckets: `speed-dash-landing-zone` (for incoming raw JSON files) and `speed-dash-target-zone` (for processed files).

2. **Create Sample JSON File**:  
   - Prepare a sample JSON file (e.g., `2024-03-09-raw_input.json`) containing delivery records with various statuses (e.g., "cancelled," "delivered," "order placed").  
   - Upload daily JSON files to the `speed-dash-landing-zone` bucket in the format `yyyy-mm-dd-raw_input.json`.

3. **Set Up Amazon SNS Topic**:  
   - Create an SNS topic to send notifications about the processing status.  
   - Subscribe an email address to the topic to receive notifications.

4. **Create IAM Role for Lambda**:  
   - Define an IAM role with the necessary permissions to read from `speed-dash-landing-zone`, write to `speed-dash-target-zone`, and publish messages to the SNS topic.

5. **Create and Configure AWS Lambda Function**:  
   - Develop a Lambda function using Python. Include the `pandas` library by either packaging it with the function code or using a Lambda Layer.  
   - Configure the function to trigger when files are uploaded to `speed-dash-landing-zone`. The function should:  
     - Read the JSON file into a `pandas` DataFrame.  
     - Filter records where `status` is "delivered."  
     - Write the filtered data to a new JSON file in `speed-dash-target-zone`.  
     - Send a success or failure notification via SNS.

6. **Set Up AWS CodeBuild for CI/CD**:  
   - Host the Lambda function code on GitHub.  
   - Create an AWS CodeBuild project linked to the GitHub repository.  
   - Use the `buildspec.yml` file to automate the deployment of Lambda function code updates.

7. **Testing and Verification**:  
   - Upload a sample JSON file to `speed-dash-landing-zone` and ensure the Lambda function is triggered automatically.  
   - Verify that the processed file is correctly stored in `speed-dash-target-zone`.  
   - Check for email notifications to confirm the processing status.



## 📂 Folder Structure

- **Project Screenshots**: Contains snapshots of the architecture diagram and other relevant screenshots.
- **scripts**: Contains scripts used for AWS Lambda functions and other processing logic.
- **buildspec.yml**: Configuration file for AWS CodeBuild to automate deployment.
- **requirements.txt**: Contains Python dependencies for the Lambda function, such as `pandas`.
