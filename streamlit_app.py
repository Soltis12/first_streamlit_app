import streamlit
import pandas
import requests


# Streamlit Headings
streamlit.title('Proper Good Filth Food')
streamlit.header('Takeaway Menu')
streamlit.text('🐖🌶️🍟Pulled Pork and Jalapeno Fries')
streamlit.text('🦆♨️🍟Crispy Duck and Smoky BBQ Fries')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Import the fruit data from the S3 Bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# API Requests
streamlit.header("Fruityvice Fruit Advice")

# Enter a Fruit name to get information about it
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# Normalize the JSON data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Display the Normalized JSON data
streamlit.dataframe(fruityvice_normalized)
