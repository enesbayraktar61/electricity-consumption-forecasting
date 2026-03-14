# Electricity Consumption Forecasting (LSTM)

This project builds a time series forecasting model to predict electricity consumption using Long Short-Term Memory (LSTM) networks.

The model was trained on household electricity usage data and deployed with Streamlit.

---

## Project Overview

- **Problem Type:** Time Series Forecasting  
- **Approach:** Deep Learning (LSTM)  
- **Framework:** TensorFlow / Keras  
- **Deployment:** Streamlit  

---

## Dataset

The dataset consists of household electricity consumption measurements, including:

- Date  
- Time  
- Global Active Power  
- Voltage  
- Global Intensity  
- Sub-metering values  

For this project, the main target variable used was:

- **Global_active_power**

---

## Data Preprocessing

### Time Series Preparation

- Combined `Date` and `Time` columns into a single datetime index  
- Selected only the `Global_active_power` variable  
- Removed invalid and missing values  

### Scaling

- Applied **MinMaxScaler** to normalize values between 0 and 1  

### Sequence Generation

- Created input sequences of **60 time steps**  
- Split the dataset chronologically into training and testing sets  

These preprocessing steps ensured proper formatting for LSTM modeling.

---

## Modeling

The forecasting model was built using a stacked LSTM architecture.

### Model Architecture

- LSTM layer with 50 units (`return_sequences=True`)  
- Second LSTM layer with 50 units  
- Dense output layer with 1 unit  

### Training

- Loss function: **Mean Squared Error**  
- Optimizer: **Adam**  
- Epochs: **10**  
- Batch size: **32**

The model was trained to predict the next electricity consumption value based on the previous 60 time steps.

---

## Results

The model achieved strong forecasting performance:

- Successfully captured overall consumption patterns  
- Followed major fluctuations despite high noise  
- Generated realistic predictions aligned with actual values  

The prediction plot shows that the LSTM model learned meaningful temporal dependencies.

---

## Deployment

The trained model was saved in `.keras` format, and the fitted scaler was saved using pickle.

The Streamlit application allows users to:

- Enter the last 60 consumption values  
- Predict the next electricity consumption value  

---

## Conclusion

This project demonstrates how LSTM models can be effectively applied to real-world time series forecasting problems such as electricity consumption prediction.

Despite the noisy nature of real household data, the model successfully captured trends and temporal patterns. This project highlights the importance of scaling, sequence modeling, and careful preprocessing when working with time series datasets.

---

## How to Run Locally

```bash
git clone https://github.com/enesbayraktar61/electricity-consumption-forecasting.git
cd electricity-consumption-forecasting
pip install -r requirements.txt
streamlit run app.py

---

