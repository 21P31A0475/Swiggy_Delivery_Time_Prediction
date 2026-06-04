import pandas as pd
import pickle
import streamlit as st

df = pd.read_csv(r'swiggy_demographic.csv')
df.dropna(inplace=True)
df.drop(columns=['rider_id','order_date'],inplace=True)

with open(r'model.pkl','rb') as file:
    Model = pickle.load(file)
st.image(r'https://miro.medium.com/v2/resize:fit:2000/1*jz9VEZqxXyriwdWSsuOJQg.png')
st.title("Swiggy Delivery Time Prediction")

AGE = st.number_input("Enter the Age",min_value=float(df["age"].min()),max_value=float(df["age"].max()),format="%.1f")
RATINGS = st.number_input("Enter the Ratings",min_value=float(df["ratings"].min()),max_value=float(df["ratings"].max()),format="%.1f")
RESTAURANT_LATITUDE = st.number_input("Enter the Restaurant Latitude",min_value=float(df["restaurant_latitude"].min()),max_value=float(df["restaurant_latitude"].max()),format="%.6f")
RESTAURANT_LONGITUDE = st.number_input("Enter the Restaurant Longitude",min_value=float(df["restaurant_longitude"].min()),max_value=float(df["restaurant_longitude"].max()),format="%.6f")
DELIVERY_LATITUDE = st.number_input("Enter the Delivery Latitude",min_value=float(df["delivery_latitude"].min()),max_value=float(df["delivery_latitude"].max()),format="%.6f")
DELIVERY_LONGITUDE = st.number_input("Enter the Delivery Longitude",min_value=float(df["delivery_longitude"].min()),max_value=float(df["delivery_longitude"].max()),format="%.6f")
WEATHER = st.selectbox("Enter the Weather",df["weather"].unique())
TRAFFIC = st.selectbox("Enter the Traffic",df["traffic"].unique())
VEHICLE_CONDITION = st.number_input("Enter the Vehicle Condition",min_value=int(df["vehicle_condition"].min()),max_value=int(df["vehicle_condition"].max()),step=1)
TYPE_OF_ORDER = st.selectbox("Enter the Type_of_order",df["type_of_order"].unique())
TYPE_OF_VEHICLE = st.selectbox("Enter the Type_of_vehicle",df['type_of_vehicle'].unique())
MULTIPLE_DELIVERIES = st.number_input("Enter the Multiple Deliveries",min_value=float(df["multiple_deliveries"].min()),max_value=float(df["multiple_deliveries"].max()),format="%.1f")
FESTIVAL = st.selectbox("Enter the Festival time",df["festival"].unique())
CITY_TYPE = st.selectbox("Enter the City Type",df["city_type"].unique())
CITY_NAME = st.selectbox("Enter the City Name",df["city_name"].unique())
ORDER_DAY = st.number_input("Enter the Order Day",min_value=int(df["order_day"].min()),max_value=int(df["order_day"].max()),step=1)
ORDER_MONTH = st.number_input("Enter the Order Month",min_value=int(df["order_month"].min()),max_value=int(df["order_month"].max()),step=1)
ORDER_DAY_OF_WEEK = st.selectbox("Enter the Order Day of the Week",df["order_day_of_week"].unique())
IS_WEEKEND = st.number_input("Is Weekend? (0 = No, 1 = Yes)",min_value=0,max_value=1,step=1)
PICKUP_TIME_MINUTES = st.number_input("Enter the Pickup_Time_Minutes",min_value=float(df["pickup_time_minutes"].min()),max_value=float(df["pickup_time_minutes"].max()),format="%.1f")
ORDER_TIME_HOUR = st.number_input("Enter the Order Time Hour",min_value=float(df["order_time_hour"].min()),max_value=float(df["order_time_hour"].max()),format="%.1f")
ORDER_TIME_OF_DAY = st.selectbox("Enter the Order Time of Day",df["order_time_of_day"].unique())
DISTANCE = st.number_input("Enter the distance",min_value=float(df["distance"].min()),max_value=float(df["distance"].max()),format="%.2f")

input_data = pd.DataFrame({"age":[AGE],"ratings":[RATINGS],"restaurant_latitude":[RESTAURANT_LATITUDE],"restaurant_longitude":[RESTAURANT_LONGITUDE],
                          "delivery_latitude":[DELIVERY_LATITUDE],"delivery_longitude":[DELIVERY_LONGITUDE],"weather":[WEATHER],"traffic":[TRAFFIC],
                          "vehicle_condition":[VEHICLE_CONDITION],"type_of_order":[TYPE_OF_ORDER],"type_of_vehicle":[TYPE_OF_VEHICLE],
                          "multiple_deliveries":[MULTIPLE_DELIVERIES],"festival":[FESTIVAL],"city_type":[CITY_TYPE],"city_name":[CITY_NAME],
                          "order_day":[ORDER_DAY],"order_month":[ORDER_MONTH],"order_day_of_week":[ORDER_DAY_OF_WEEK],"is_weekend":[IS_WEEKEND],
                          "pickup_time_minutes":[PICKUP_TIME_MINUTES],"order_time_hour":[ORDER_TIME_HOUR],"order_time_of_day":[ORDER_TIME_OF_DAY],"distance":[DISTANCE]})

if st.button('Predict'):
      input_data = input_data[Model.feature_names_in_]
      result = Model.predict(input_data)
      st.write(f"Estimated Delivery Time: {result[0]:.2f} minutes")



