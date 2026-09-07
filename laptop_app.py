import streamlit as st
import pickle
df=pickle.load('df.pkl','rb')
pipe= pickle.load('pipe.pkl','rb')
st.title("Laptop Price Predictor App")
st.text("This app is using a select few laptop(around 1200 laptop models), so may not align with the real world data")
company = st.selectbox("Manufacturer of the laptop",df['Company'].unique(),index=4)
typename = st.radio("Type of the laptop",df['TypeName'].unique(),index=1,horizontal=True)
cpu = st.selectbox("Processor",df['Cpu'].unique(),index=0)
ram = st.pills("RAM on the system(in GB)",[4,8,12,16,24,32,64,128])
gpu = st.radio("Graphics Card",df['Gpu'].unique(),index=1)
os = st.selectbox("Operating System",df['OpSys'].unique(),index=2)
weight = st.slider("Weight of the laptop(in kg)",min_value=0.7,max_value=5.0,step=0.1,value=2.0)
touchscreen = st.radio("Does the laptop have touchscreen",[0,1])
ips = st.radio("Does the laptop have IPS display",[0,1])
cpu_speed = st.slider("Clock Speed of CPU(in GHz)",min_value=0.9,max_value=4.0,step=0.1,value=2.3)
ppi = st.slider("PPI(Pixel Density)",min_value=90,max_value=350,step=5,value=140)

if st.button("PREDICT PRICE"):
    query = [[company,typename,cpu,ram,gpu,os,weight,touchscreen,ips, cpu_speed, ppi]]
    op = pipe.predict(query)
    st.subheader(f"The estimated price of the laptop with the above mentioned specifications is ₹{int(round(op[0],-2))}")
