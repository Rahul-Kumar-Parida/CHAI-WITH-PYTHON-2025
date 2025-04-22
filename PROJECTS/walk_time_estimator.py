import streamlit as st

# Define speeds in km/h
speeds = {
    "slow": 3,
    "avg": 5, 
    "fast": 6
}

# Title
st.title("🚶‍♂️ Walk Time Estimator")

# Input fields
distance = st.number_input("Enter distance (in km):", min_value=0.0)
speed_type = st.selectbox("Select walking speed:", ["slow", "avg", "fast"])

# Calculate and display result
if st.button("Estimate Time"):
    if distance > 0:  # Check if distance is greater than 0
        speed = speeds[speed_type]
        time_hour = distance / speed
        total_minutes = int(time_hour * 60)

        hours = total_minutes // 60
        minutes = total_minutes % 60

        if hours > 0:
            st.success(f"Estimated walking time: {hours} hr {minutes} min")
        else:
            st.success(f"Estimated walking time: {minutes} min")
    else:
        st.error("Please enter a valid distance (greater than 0).")
