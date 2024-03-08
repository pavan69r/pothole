import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Function to read session data from Excel file
def read_session_data_from_excel(file_path):
    return pd.read_excel(file_path)

# Function to read geolocation data from local Excel file
def read_geolocation_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df['latitude'].tolist(), df['longitude'].tolist()

# Function to convert session data to list of dictionaries
def mapdataF(session_data):
    li = []
    for session in session_data.itertuples(index=False):
        li.append({'latitude': session.latitude, 'longitude': session.longitude})
    return li

# Read session data from Excel file
session_file_path = "F:\Major\Netra\pages\sessions.xlsx"
session_data = read_session_data_from_excel(session_file_path)
data = mapdataF(session_data)
orderedColumn = ['sid', 'number_of_pothole', 'latitude', 'longitude', 'date&time']
session_data = session_data[orderedColumn].sort_values(by='sid', ascending=True)

# Read geolocation data from Excel file
geolocation_file_path = "F:\\Major\\Netra\\pages\\geolocation.xlsx"
latitude, longitude = read_geolocation_from_excel(geolocation_file_path)

# Set the center of the map around the first coordinate
map_center = (latitude[0], longitude[0])
map = folium.Map(location=map_center, zoom_start=10)

# Add markers for each coordinate
for lat, lon in zip(latitude, longitude):
    folium.Marker([lat, lon]).add_to(map)

# Display the map in Streamlit
st_folium(map, width=700)

# Streamlit app layout
st.title('Current Sessions Data')

# Display current session data in a table
st.table(session_data)

# Button to simulate sending data to the cloud (dummy function)
if st.button('Send Data to Cloud'):
    # Placeholder function to send data to the cloud (replace with your actual function)
    def send_data_to_cloud(data):
        st.success('Data has been sent to the cloud.')
    
    # Call the cloud function with session_data as argument
    send_data_to_cloud(session_data)
