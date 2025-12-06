import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Simple Map")

# Two simple locations
place1 = ["India Gate, Delhi", 28.6129, 77.2295]
place2 = ["Gateway of India, Mumbai", 18.9219, 72.8347]

# Create a map
m = folium.Map(location=[23.0, 80.0], zoom_start=5)

# Add marker 1
folium.Marker(
    location=[place1[1], place1[2]],
    popup=f"{place1[0]} | Lat: {place1[1]} | Lon: {place1[2]}"
).add_to(m)

# Add marker 2
folium.Marker(
    location=[place2[1], place2[2]],
    popup=f"{place2[0]} | Lat: {place2[1]} | Lon: {place2[2]}"
).add_to(m)

# Show map
st_folium(m, width=700, height=500)
