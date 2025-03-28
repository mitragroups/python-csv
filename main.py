import pandas as pd
import streamlit as st

st.title("CSV Operation")

user_id = st.text_input("User ID")
name = st.text_input("Name")
job = st.text_input("Job")
salary = st.number_input("Salary", step = 100)

submit_btn = st.button("Add Employee")

with open("data.csv", "r") as file:
    csv = pd.read_csv(file)
    #print(csv) # cetak data di terminal biar lebih rapih
    st.write("### Data")
    st.dataframe(csv) 
    
    st.bar_chart(csv.set_index("name")["salary"])
    
    if submit_btn:
        new_data = pd.DataFrame([[user_id, name, job, salary]], columns=["id", "name", "job", "salary"])
        
        csv = pd.concat([csv, new_data], ignore_index=True)
        
        csv.to_csv("data.csv", index=False)
        
        st.rerun()