# PhishDetect: Machine Learning for Phishing URL Detection

This repository contains code and documentation for a phishing detection system that evaluates model performance and feature robustness across different datasets.

## Overview

Phishing is a significant cybersecurity threat where attackers impersonate legitimate entities to obtain sensitive information. With the increasing availability of AI tools, detecting these sophisticated attacks requires advanced techniques. This project implements and compares machine learning models for phishing URL detection using both a Kaggle dataset and a custom-extracted dataset.

## Project Structure

- **Extracting Features.ipynb**: Jupyter notebook for extracting features from URLs
- **feature_extraction.py**: Python module with functions for URL feature extraction
- **Model Training.ipynb**: Main notebook for training and evaluating models

## Features Extracted

The project extracts the following features from URLs:

| Feature | Description |
|---------|-------------|
| Have_IP | Whether URL contains an IP address (1) or not (0) |
| URL_Length | Length of the URL |
| TinyURL | Whether URL is shortened (1) or not (0) |
| Have_At | Whether URL contains @ symbol (1) or not (0) |
| Redirection | Whether URL contains double slash redirection (1) or not (0) |
| Prefix/Suffix | Whether domain has hyphen (1) or not (0) |
| https_Domain | Whether URL has multiple HTTP domains (1) or not (0) |
| URL_Depth | The number of / in the URL |
| DNS_Record | Whether domain exists in DNS (0) or not (1) |
| Whois_Registered | Whether domain is registered (0) or not (1) |
| Domain_Age | Age of domain in days (-1 if error, -2 if no creation date) |
| Page_Rank | OpenPageRank score (0-10) |

## Key Features for Phishing Detection

Based on our analysis, the following features are most significant for phishing detection:

1. **page_rank**: Indicator of website importance on the internet
2. **domain_age**: Time since a domain's record has existed in WHOIS
3. **dns_record**: Whether the URL is recognized in the WHOIS database
4. **length_url**: Length of the URL

These URL and domain-related features can effectively detect phishing without resource-intensive HTML or content parsing.

## Datasets

- **Kaggle Dataset (2021)**: A pre-existing dataset containing labeled phishing and legitimate URLs
- **Custom Extracted Dataset**: URLs collected from PhishTank and processed using our feature extraction pipeline
- **Combined Dataset**: Merged data from both sources for improved model robustness

## Models Implemented

The project implements and compares the following models:

1. **Logistic Regression**: A baseline linear model
2. **Decision Tree**: Tree-based model with max depth of 5
3. **Random Forest**: Ensemble of decision trees
4. **XGBoost**: Gradient boosting algorithm
5. **SVM (Support Vector Machine)**: Works well in high-dimensional spaces
6. **Multilayer Perceptron (MLP)**: Neural network with three hidden layers

## Model Performance

| Model | Kaggle Dataset (2021) | Combined Dataset |
|-------|----------------------|------------------|
| Logistic Regression | 0.820 | 0.816 |
| Decision Tree | 0.893 | 0.933 |
| Random Forest | 0.910 | 0.942 |
| XGBoost | 0.923 | 0.950 |
| SVM | 0.822 | 0.828 |
| Multilayer Perceptron | 0.892 | 0.930 |

XGBoost consistently performed best with 95.0% accuracy on the combined dataset, followed by Random Forest at 94.2%.

## Setup and Usage

### Requirements

```
pandas
numpy
scikit-learn
xgboost
whois
dnspython
requests
```

### Installation

```bash
pip install python-whois dnspython requests pandas numpy scikit-learn xgboost
```

### Feature Extraction

1. Open `Extracting Features.ipynb` in Google Colab
2. Mount your Google Drive when prompted
3. Update the input_file path to point to your CSV containing URLs
4. Run all cells to extract features and save to a CSV file

### Model Training

1. Open `Model Training.ipynb` in Google Colab
2. Mount your Google Drive when prompted
3. Run all cells to:
   - Load the datasets
   - Train models
   - Compare and visualize model performance

## Conclusion

We demonstrated that a smaller, carefully selected feature set focused on URL and domain properties can achieve high accuracy in phishing detection. XGBoost consistently outperformed other models, making it the recommended choice for real-world applications.

