import streamlit as st

st.title("unit converter app")
st.markdown("### this app converts units of length, mass, and temperature")
st.write("welcome select category enter value and select unit")

category = st.selectbox("select category", ["weight", "time", "length"])

def converter_unit(category,value,unit):
    if category == "length":
        if unit == "kilometer to miles":
            return value * 0.621371
        elif unit == "miles to feet":
            return value / 0.621371
        

    elif category == "weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462
    elif category == "time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to seconds":
            return value * 3600
        elif unit == "days to hours":
            return value * 24
        elif unit == "hours to days":
            return value / 24
    return "invalide conversation selected"
        

if category == "length":
    unit = st.selectbox("select conversation", ["miles to feet","kilometer to miles"])

elif category == "weight":
    unit = st.selectbox("select conversation", ["kilograms to pounds", "pounds to kilograms"])

elif category == "time":
    unit = st.selectbox("select conversation", ["seconds to minutes", "minutes to hours", "minutes to seconds", "hours to minutes", "hours to seconds", "days to hours", "hours to days"])

value = st.number_input("enter value")

if st.button("convert"):
    result = converter_unit(category, value, unit)
    st.success(f"the result is {result:.2f}")




        
        




    


