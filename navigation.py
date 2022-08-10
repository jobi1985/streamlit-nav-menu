import streamlit as st
from streamlit_option_menu import option_menu

def funaws():
    st.markdown('Streamlit is **_really_ cool**.')


with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Instances'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0)
    
if selected =="Home":
    #st.title(f"You have selected {selected}")
    st.button('Process', key='next', on_click=funaws)
      
if selected =="Instances":
    import boto3
    client = boto3.client('ec2')
    Myec2=client.describe_instances()
    for pythonins in Myec2['Reservations']:
      for printout in pythonins['Instances']:
         st.text(printout['InstanceId'])
         st.text(printout['InstanceType'])
         st.text(printout['State']['Name'])
         st.text("-----------------------")
