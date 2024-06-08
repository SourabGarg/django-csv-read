# CSV Data Analysis Web Application

## Overview
This Django-based web application allows users to upload CSV files, performs data analysis using pandas, and displays the results on the web interface using matplotlib.

## Requirements
### 1. Django Setup
- Create a Django project named 'csv_read'.
- Configure the project with a setup you are comfortable with.

### 2. File Upload Feature
- Implement a form that allows users to upload CSV files.
- Store the uploaded files temporarily for processing.

### 3. Data Processing
- Use pandas to read the uploaded CSV file.
- Perform basic data analysis tasks such as:
  - Displaying the first few rows of the data.
  - Calculating summary statistics (mean, median, standard deviation) for numerical columns.
  - Identifying and handling missing values.

### 4. User Interface
- Use Django templates to create a simple and user-friendly interface.
- Display the data analysis results in a clear and organized manner.

## Deliverables
1. A GitHub repository containing the Django project code.
2. A README file with setup instructions and a brief explanation of the project.
3. A sample CSV(test_data.csv) file for testing purposes.

## Usage
1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the Django server using `python manage.py runserver`.
4. Access the web application in your browser at `http://localhost:8000`.

## Structure
The project consists of a Django project named 'csv_read' with the main functionality implemented using pandas for data analysis.

## Note
- Only CSV files can be uploaded. If a file of another type is uploaded, an error will be displayed.

## Sample CSV File
A sample CSV file named `test_data.csv` is provided in the repository for testing purposes.

# Result

![image](https://github.com/SourabGarg/django-csv-read/assets/112079423/af0c0fa4-b371-4400-98a1-59dbdd671ba2)

![image](https://github.com/SourabGarg/django-csv-read/assets/112079423/8ebd6469-5ecf-4312-8788-d2f4e72776cc)


