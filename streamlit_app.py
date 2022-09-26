# Import required packages
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# Show the menu
streamlit.title('Menu for Loaded')

streamlit.header('Proper Dirty Fries')

streamlit.text('🐖 Pulled Pork, Caramelised Onions, Cayenne Pepper and Tabasco Sauce')
streamlit.text('🍗 Chicken, Chicken Skins, Cheddar Cheese and Barbeque Sauce')
streamlit.text('🥑 Avocado, Free-From Cheese, Lettuce and Vegan Sauce')
streamlit.text('🦆 Duck, Mushrooms, Bean Sprouts and Hoisin Sauce')

streamlit.header('🏗️ Build your own Fruit Smoothie')

# Import Fruit list
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Pick fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Lemon','Kiwifruit'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display list of fruits
streamlit.dataframe(fruits_to_show)

# Fruit Advice header
streamlit.header('FruityVice Fruit Advice!')

# Create the check fruit function
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# Scrape data about a chosen fruit in a DataFrame
try:
  fruit_entry = streamlit.text_input('What fruit would you like information about?','kiwi')
  if not fruit_entry:
    streamlit.error('Please enter a fruit to get information')
  else:
    back_from_function = get_fruityvice_data(fruit_entry)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

# STOP: Code past this point is not viewable by users
streamlit.stop()

# Snowflake Connector
fruit_wanted = streamlit.text_input('What fruit would you like to add?')
streamlit.text('Thank you for adding ' + fruit_wanted + ' to the list')

# Show table of Fruit list items
streamlit.text("Items in the table Fruit Load List:")

# Function to display the table
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST VALUES")
        return my_cur.fetchall

# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list
    streamlit.dataframe(my_data_rows)
