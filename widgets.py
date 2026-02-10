import streamlit as st

st.text_input("Enter your Name")

if st.button('click'):
    st.write(name)

address =   st.text_area('Address')
st.write(address)

st.date_input('select a time ')

if st.checkbox('Accepts Terms and Conditions'):
    st.write('thankyou')

r =st.radio('COLORS',["R","Y","B","G"])
st.write(r)


sb = st.selectbox('COLORS',["R","Y","B","G"],index=2)
st.write(sb)


msb = st.selectbox('COLORS',["R","Y","B","G"])
st.write(msb)

sl = st.slider("age",min_value=18,max_value=60,step=5)
st.write(sl)


nu = st.number_input("salary",min_value=15000.0,max_value=50000.0,step=500.0)
st.write(nu) 

f = st.file_uploader("UPLOAD FILE")
if f:
    st.image(f)

# a = st.camera_input('take a picture')
# if a:
#     st.image(a)

clr = st.color_picker('pick Any Color : ')
if clr:
    st.write(clr)