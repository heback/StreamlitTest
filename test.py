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

multi_select = st.multiselect('Please select somethings in multi selectbox!',
                                ['A', 'B', 'C', 'D'])
st.write('You selected:', multi_select)

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

start_color, end_color = st.select_slider(
  'Select a range of color wavelength',
  options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
  value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)


st.text_input("비밀번호 입력", '1234', type="password")

st.text_area("여러 줄 입력")
