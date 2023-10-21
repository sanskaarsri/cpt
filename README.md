# CLOUD_PERFORMANCE_TUNING
# Health Hub

Welcome to the Health Hub ! This Python code helps you check and predict possible medical conditions based on the symptoms you input.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Features](#Features)
- [Modules used](#modulesused)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Introduction

This code is a simple medical diagnosis system that uses machine learning to analyze symptoms and suggest possible medical conditions. It's designed to assist users in identifying potential health issues based on the symptoms they provide.


## Prerequisites

Before using this system, you'll need:

- A Python environment with the necessary libraries installed.
- Training and testing data in CSV format (provided as 'Training.csv' and 'Testing.csv' here).
- An Azure account if you wish to deploy this code as a web service.

## Features

- Register Screen.
- Sign-in Screen.
- Generates database for user login system.
- Offers you a GUI Based Chatbot for patients for diagnosing. 
- Reccomends an appropriate doctor to you for the following symptom.

## Modules Used

- tkinter
- os
- webbrowser
- numpy
- pandas
- matplotlib


## Usage

1. Load Data: Start by providing training and testing data in CSV format. The code uses this data for analysis.

2. Train Models: The code trains a Decision Tree classifier and a Support Vector Machine (SVM) to make predictions based on the symptoms.

3. Feature Importance: It calculates feature importances to understand which symptoms contribute the most to predictions.

4. Symptom Analysis: The code offers an interactive session where you can input your symptoms and the number of days you've experienced them. It predicts possible diseases and provides descriptions and precautions.


## Deployment

You can deploy this code on Azure as a web application or service for wider accessibility. 

Ensure that you have an Azure account. 
Decide on the deployment approach. You can deploy the code as a web app or create an Azure Function (for serverless deployment) depending on your specific requirements.
You'll need a server to host your code. You can create a virtual machine or use Azure's App Service for web app hosting.
Ensure that the required libraries, including Python and the necessary packages, are installed on the virtual machine or app service.
You will need to upload and deploy your code to the virtual machine or web app

## Contributing

Feel free to contribute to this project! If you have ideas for improvements or new features, submit a pull request. We welcome your contributions.


This README provides a simple and clear introduction to the code, instructions on how to get started, use the system, deploy it on Azure, contribute to the project, and mentions the licensing.


