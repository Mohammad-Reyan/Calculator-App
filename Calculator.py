import streamlit as st

# Title of the app
st.title("Simple Calculator App")

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Radio buttons for selecting the operation
operation = st.radio("Select an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            return num1 / num2
        else:
            st.warning("Division by zero is not allowed.")
            return None

# Button to calculate the result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    if result is not None:
        st.success(f"The result is: {result}")
