import streamlit
import pandas

# Streamlit Headings
streamlit.title('Proper Good Filth Food')
streamlit.header('Takeaway Menu')
streamlit.text('🐖🌶️🍟Pulled Pork and Jalapeno Fries')
streamlit.text('🦆♨️🍟Crispy Duck and Smoky BBQ Fries')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
