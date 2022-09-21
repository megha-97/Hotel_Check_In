# Hotel_Check_In

Problem Statement : To predict the customer who is going to check-in into the hotel using the history of customer booking in a hotel.
Approach: The process followed to solve this problem is as follows:

1. Read the train dataset provided and prepare the data by handling missing values.
2. Encode the categorical features using label encoding or one-hot encoding.
3. Trained Logistic regression and XGBoost model on train dataset.
4. Measured the accuracy on test dataset.
5. Found that only 3 features were contributing to the model predictions namely 'LodgingRevenue', 'RoomNights' and 'DaysSinceFirstStay'.
6. Trained another model using these 3 features only on dumped it into pickle file.
7. Created an API using streamlit.
8. Deployed the API on heroku.

Deployed URL Link : https://customer-check-in.herokuapp.com/
