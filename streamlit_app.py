import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# Define FruityVice Function
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# Define Get Fruit Load List
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        streamlit.header("The Fruit List contains:")
        my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
        return my_cur.fetchall()

# Define Function for Adding New Rows
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('" + new_fruit + "')")
        return streamlit.write("Thanks for adding " + add_my_fruit)

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
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    streamlit.write('The user entered ', fruit_choice)
except URLError as e:
  streamlit.error()

# Add a button to load the Fruit Data
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

# Add a button to enter a fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add Fruit to List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text_input(back_from_function)


