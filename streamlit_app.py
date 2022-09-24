# Show text for food choices
import streamlit
streamlit.title('Menu for Loaded')

streamlit.header('Proper Dirty Fries')

streamlit.text('🐖 Pulled Pork, Caramelised Onions, Cayenne Pepper and Tabasco Sauce')
streamlit.text('🍗 Chicken, Chicken Skins, Cheddar Cheese and Barbeque Sauce')
streamlit.text('🥑 Avocado, Free-From Cheese, Lettuce and Vegan Sauce')
streamlit.text('🦆 Duck, Mushrooms, Bean Sprouts and Hoisin Sauce')

streamlit.header('🏗️ Build your own Fruit Smoothie')

# Import Fruit list
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Pick fruit
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Lemon','Kiwifruit'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display list of fruits
streamlit.dataframe(fruits_to_show)

