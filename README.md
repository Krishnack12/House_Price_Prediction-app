 # House_Price_Prediction-app
The  House Price Prediction project focuses on estimating house prices in Bangalore using machine learning techniques. The project is built using Python and popular libraries such as NumPy, Pandas, Scikit-learn, Joblib, and Streamlit. It provides an end-to-end solution that includes data processing, model training, and a web-based interface for real-time predictions.

# *Project Overview*
The “**House Price Prediction**” project aims to develop a machine learning model that can accurately predict house prices based on various features. This project is particularly useful in the real estate domain, where price estimation plays an important role in decision-making for buyers and sellers.
The model is trained using the Bangalore House Price dataset, which contains essential attributes such as **total square feet, number of bathrooms, balconies,** and **bedrooms (BHK)**. By employing machine learning algorithms and a curated dataset, this project provides a powerful tool for estimating house prices.
 The trained model is then deployed using Streamlit, allowing users to interact with the system through a simple and user-friendly web application.

# *Key Features*

## Data Collection and Processing
The project uses the Bangalore House Price dataset, which includes important property details such as total square feet, number of bathrooms, balconies, and bedrooms (BHK). The dataset is processed using Pandas to remove irrelevant columns, handle missing values, and prepare the data in a format suitable for training the machine learning model.
## Feature Selection
Only the most relevant features affecting house prices are selected to improve model performance. These features include Total Square Feet, Bathrooms, Balconies, and Bedrooms (BHK). Proper feature selection helps in reducing noise and improving prediction accuracy.
## Train-Test Split
To evaluate the effectiveness of the model, the dataset is divided into training and testing sets. The model is trained on the training data and tested on unseen data to ensure that it generalizes well and does not overfit.
## Regression Model using Linear Regression
The project uses Linear Regression to build the house price prediction model. Linear Regression is a simple yet effective algorithm for understanding the relationship between independent variables and house prices. The model is implemented using the Scikit-learn library.
## Model Evaluation
The performance of the model is evaluated using the R-squared (R²) score, which measures how well the model explains the variance in house prices. The trained model achieves satisfactory prediction accuracy for real-world estimation.
## Web Application using Streamlit
A Streamlit-based web interface is developed to allow users to input property details and instantly receive predicted house prices. The application provides a clean and interactive user experience, making the model easy to use even for non-technical users.
## Model Deployment
The trained model is saved using Joblib and integrated into the Streamlit application. This allows the application to load the model and generate predictions in real time, simulating a real-world machine learning deployment scenario.


## *Getting Started*
To run this project locally, follow these steps:
1.	Download the project as a ZIP file from the GitHub repository and extract the ZIP file to your system
2.	Open the project folder in VS Code or any code editor.
3.	Install the required libraries: pip install -r requirements.txt
4.	Run the Streamlit application: python -m streamlit run app.py
5.	Open the browser and use the House Price Prediction web application.

----
## *Tech Stack*
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## *Conclusion*
The House Price Prediction project provides a simple and practical solution for estimating Bangalore house prices based on key property features such as square feet, bathrooms, balconies, and bedrooms. The project uses Linear Regression to model the relationship between these features and house prices.
By integrating the trained model into a Streamlit web application, users can easily input property details and receive real-time price predictions. This project demonstrates the complete machine learning workflow, including data preprocessing, model training, evaluation, and deployment, making it an effective learning project in applied machine learning
# *License*
This project is licensed under the MIT license. See the **LICENSE** file for more information.

## *Acknowledgement*
This project was made possible with the help of the open-source community and widely used Python libraries. I would like to express my gratitude to the developers and contributors of NumPy, Pandas, Scikit-learn, Streamlit, and Joblib for providing reliable tools that enabled data processing, model development, and web application deployment. Their continuous efforts make learning and implementing machine learning projects more accessible and effective


