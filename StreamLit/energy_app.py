import streamlit as st


# main function
def main():
    st.write("""
    	# Energy Generation Prediction Model
    	This app predicts the actual energy generated on a particular day given estimated energy of that day
         """)

    # Side bar for user inputs
    st.sidebar.header("User inputs here")

    st.sidebar.subheader("Eastern Region")

    hydro_east = st.sidebar.slider("Hydro Energy Estimated Value", 2.65, 105.92, 53.04)
    thermal_east = st.sidebar.slider("Thermal Energy Estimated Value", 138.30, 610.79, 474.04)
    st.sidebar.subheader("There is no Nuclear energy in Eastern Region")


    st.sidebar.subheader("Western Region")

    hydro_west = st.sidebar.slider("Hydro Energy Estimated Value", 3.80, 131.80, 35.57)
    thermal_west = st.sidebar.slider("Thermal Energy Estimated Value", 409.17, 1442.38, 1210.71)
    nuclear_west = st.sidebar.slider("Nuclear Energy Estimated Value", 0.00, 44.55, 32.23)


    st.sidebar.subheader("Northern Region")

    hydro_north = st.sidebar.slider("Hydro Energy Estimated Value", 62.09, 397.38, 53.04)
    thermal_north = st.sidebar.slider("Thermal Energy Estimated Value", 209.74, 817.50, 608.86)
    nuclear_north = st.sidebar.slider("Nuclear Energy Estimated Value", 0.00, 37.71, 31.72)


    st.sidebar.subheader("Southern Region")

    hydro_south = st.sidebar.slider("Hydro Energy Estimated Value", 0.00, 195.55, 77.94)
    thermal_south = st.sidebar.slider("Thermal Energy Estimated Value", 191.91, 746.79, 549.87)
    nuclear_south = st.sidebar.slider("Nuclear Energy Estimated Value", 0.00, 76.64, 47.00)


    st.sidebar.subheader("NorthEastern Region")

    hydro_ne = st.sidebar.slider("Hydro Energy Estimated Value", 0.00, 31.01, 14.21)
    thermal_ne = st.sidebar.slider("Thermal Energy Estimated Value", 12.38, 47.23, 33.474)
    st.sidebar.subheader("There is no Nuclear energy in NorthEastern Region")

    if st.button("Predict Hydro Eastern"):
        st.subheader("User Data")
        st.write("Estimated value of Hydro energy", hydro_east)

        y = 0.8478 * hydro_east + 4.2441
        st.write("Predicted Actual value of Hydro energy", y)

    if st.button("Predict Thermal Eastern"):
        st.subheader("User Data")
        st.write("Estimated value of Thermal energy", thermal_east)

        y = 0.2431 * thermal_east + 372.0341
        st.write("Predicted Actual value of Thermal energy", y)

    if st.button("Predict Hydro Western"):
        st.subheader("User Data")
        st.write("Estimated value of Hydro energy", hydro_west)

        y = 0.0487 * hydro_west + 35.0628
        st.write("Predicted Actual value of Hydro energy", y)

    if st.button("Predict Thermal Western"):
        st.subheader("User Data")
        st.write("Estimated value of Thermal energy", thermal_west)

        y = 0.3690 * thermal_west + 772.011
        st.write("Predicted Actual value of Thermal energy", y)

    if st.button("Predict Nuclear Western"):
        st.subheader("User Data")
        st.write("Estimated value of Nuclear energy", nuclear_west)

        y = 0.4502 * nuclear_west + 13.3004
        st.write("Predicted Actual value of Nuclear energy", y)

    if st.button("Predict Hydro Northern"):
        st.subheader("User Data")
        st.write("Estimated value of Hydro energy", hydro_north)

        y = 0.8750 * hydro_north + 12.8911
        st.write("Predicted Actual value of Hydro energy", y)

    if st.button("Predict Thermal Northern"):
        st.subheader("User Data")
        st.write("Estimated value of Thermal energy", thermal_north)

        y = 0.0113 * thermal_north + 655.2021
        st.write("Predicted Actual value of Thermal energy", y)

    if st.button("Predict Nuclear Northern"):
        st.subheader("User Data")
        st.write("Estimated value of Nuclear energy", nuclear_north)

        y = 0.1682 * nuclear_north + 21.9737
        st.write("Predicted Actual value of Nuclear energy", y)

    if st.button("Predict Hydro Southern"):
        st.subheader("User Data")
        st.write("Estimated value of Hydro energy", hydro_south)

        y = 0.2215 * hydro_south + 54.8140
        st.write("Predicted Actual value of Hydro energy", y)

    if st.button("Predict Thermal Southern"):
        st.subheader("User Data")
        st.write("Estimated value of Thermal energy", thermal_south)

        y = 0.2786 * thermal_south + 463.6173
        st.write("Predicted Actual value of Thermal energy", y)

    if st.button("Predict Nuclear Southern"):
        st.subheader("User Data")
        st.write("Estimated value of Nuclear energy", nuclear_south)

        y = (-0.2228) * nuclear_south + 66.9957
        st.write("Predicted Actual value of Nuclear energy", y)

    if st.button("Predict Hydro NorthEastern"):
        st.subheader("User Data")
        st.write("Estimated value of Hydro energy", hydro_ne)

        y = 0.8547 * hydro_ne + 5.6093
        st.write("Predicted Actual value of Hydro energy", y)

    if st.button("Predict Thermal NorthEastern"):
        st.subheader("User Data")
        st.write("Estimated value of Thermal energy", thermal_ne)

        y = 0.2189 * thermal_ne + 25.1635
        st.write("Predicted Actual value of Thermal energy", y)


if __name__ == '__main__':
    main()