import streamlit as st
#Functionality
def distance_convertor(from_unit,to_unit,value):
    units ={
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_unit] /units[to_unit]
    return result

#tempreture convert function
def tempreture_convertor(from_unit,to_unit,value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result =(value - 32) *5/9
    else:
        result = value
    return result            

#Weight
def weight_convertor (from_unit,to_unit,value):
    units ={
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_unit] /units[to_unit]
    return result

#Pressure
def pressure_convertor (from_unit,to_unit,value):
    units ={
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    result = value * units[from_unit] /units[to_unit]
    return result

#UI

st.title("Unit Convertor")
#select category
category = st.selectbox("Select Category", ["Distance","Tempreture","Weight","Pressure"])

if category == "Distance":
    from_unit= st.selectbox("From", ["Meters","Kilometers", "Feet","Miles"] )

    to_unit= st.selectbox("To", ["Meters","Kilometers", "Feet","Miles"])

    value=st.number_input("Enter value")
    if st.button("Convert"):
        result =distance_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} ={result:.2f} {to_unit}")

elif category == "Tempreture":
    from_unit= st.selectbox("From", ["Celsius", "Fahrenheit"] )

    to_unit= st.selectbox("To", ["Celsius", "Fahrenheit"])

    value=st.number_input("Enter value")
    if st.button("Convert"):
        result =tempreture_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} ={result:.2f} {to_unit}")
     
elif category == "Weight":
    from_unit= st.selectbox("From", ["Kilograms","Grams", "Pounds","Ounces"] )

    to_unit= st.selectbox("To", ["Kilograms","Grams", "Pounds","Ounces"])

    value=st.number_input("Enter value")
    if st.button("Convert"):
        result =weight_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} ={result:.2f} {to_unit}")

elif category == "Pressure":
    from_unit= st.selectbox("From", ["Pascals","Hectopascals","Kilopascals","Bar"] )

    to_unit= st.selectbox("To", ["Pascals","Hectopascals","Kilopascals","Bar"])

    value=st.number_input("Enter value")
    if st.button("Convert"):
        result = pressure_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} ={result:.2f} {to_unit}")
