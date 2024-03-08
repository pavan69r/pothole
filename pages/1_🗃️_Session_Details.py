import streamlit as st
import pandas as pd
import folium
import geocoder
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

# Function to get geolocation asynchronously
def get_geolocation_async():
    # Use IP geolocation asynchronously
    g = geocoder.ip('me', future=True)
    if g.ok:
        return g.latlng  # Return latitude and longitude as [latitude, longitude] list
    else:
        return None

# Read session data from Excel file
session_file_path = r"pages\sessions.xlsx"
session_data = read_session_data_from_excel(session_file_path)
data = mapdataF(session_data)
orderedColumn = ['sid', 'number_of_pothole', 'latitude', 'longitude', 'date&time']
session_data = session_data[orderedColumn].sort_values(by='sid', ascending=True)

# Read geolocation data from Excel file
geolocation_file_path = r"pages\geolocation.xlsx"
latitude, longitude = read_geolocation_from_excel(geolocation_file_path)

# Get geolocation asynchronously
latitude_async, longitude_async = get_geolocation_async()

# Set the center of the map around the first coordinate
map_center = (latitude[0], longitude[0])
map = folium.Map(location=map_center, zoom_start=10)

# Add markers for session data
for i, (lat, lon) in enumerate(zip(latitude, longitude)):
    popup_text = f"Session ID: {session_data['sid'][i]}, Number of potholes: {session_data['number_of_pothole'][i]}, Date & Time: {session_data['date&time'][i]}"
    folium.Marker([lat, lon], popup=popup_text).add_to(map)

# Add marker for async geolocation
if latitude_async is not None and longitude_async is not None:
    folium.Marker([latitude_async, longitude_async], popup="Async Geolocation").add_to(map)

# Display the map in Streamlit
st_folium(map, width=700)

# Streamlit app layout
st.title('Current Sessions Data')

# Display current session data in a table
st.table(session_data)

# Button to simulate sending data to the cloud and write to Excel sheet
if st.button('Send Data to Cloud and Write to Excel'):
    # Append new row with async geolocation data to session data
    new_data = pd.DataFrame({'sid': [len(session_data) + 1],
                             'latitude': [latitude_async],
                             'longitude': [longitude_async],
                             'date&time': [pd.Timestamp.now()]})
    session_data = pd.concat([session_data, new_data], ignore_index=True)
    
    # Write session data to Excel sheet
    session_data.to_excel(session_file_path, index=False)

    # Placeholder function to send data to the cloud (replace with your actual function)
    def send_data_to_cloud(data):
        st.success('Data has been sent to the cloud.')
    
    # Call the cloud function with session_data as argument
    send_data_to_cloud(session_data)
