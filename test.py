import streamlit as st

st.title("Title")
st.header("Header")
st.subheader("subheader")

st.write("Write Something")

if st.button("click button"):
  st.write("Data Loading..")
  # 데이터 로딩 함수는 여기에!

checkbox_btn = st.checkbox('Checktbox Button')
	
if checkbox_btn:
  st.write('Great!')

checkbox_btn2 = st.checkbox('Checktbox Button2', value=True)
	
if checkbox_btn2:
  st.write('Button2')

option = st.selectbox('Please select in selectbox!',
                       ('kyle', 'seongyun', 'zzsza'))
st.write('You selected:', option)
