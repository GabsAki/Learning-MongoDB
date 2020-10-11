from pymongo import MongoClient
import pandas as pd
import streamlit as st
from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

# Get the DB config
client = config_object["DBCONFIG"]

# The streamlit output starts here
st.title('MongoDB Data Visualization App')
st.write("This app is my first try using streamlit and MongoDB :sweat_smile:")
st.write("The dataset is composed of some information about playable characters of a well known game called League of Legends.")

# Get the data and convert it into a pandas DataFrame
cluster =  MongoClient('{}'.format(client['client']))
db = cluster['test']
collection = db['champions']
data = pd.DataFrame(collection.find())

# Preparing the dataframe for the "Explore the simpliflied dataset" section
data_show = data.copy()
data_show = pd.concat([data_show.drop(['stats'], axis= 1), data['stats'].apply(pd.Series)], axis= 1)

data_show.drop(['_id', 'id', 'key', 'icon', 'sprite', 'description', 'hpperlevel', 'mpperlevel', 'armorperlevel', 'spellblockperlevel', 'hpregenperlevel', 'mpregenperlevel',
                'critperlevel', 'attackdamageperlevel', 'attackspeedperlevel'
                ],
               axis= 1,
               inplace= True
               )

st.header("Explore simplified dataset:")
data_show

# Answering a simple aggregation question: "How many champions are in the dataset?"
st.header("How many champions are in the dataset?")
st.markdown(":small_blue_diamond: **{}** champions".format(len(data['_id'])))

# Making a simple barchart with the column 'tags'.
# A champion can have more than one tag, so this column contains a various lists.
# Because of this, we use DataFrame.explode() method to create a new dataframe where each row contains only the champion name and one of its tags.
data_tags = data[['name', 'tags']]
data_tags = data_tags.explode('tags')
st.header("How many champions by tag?")
st.bar_chart(data_tags.groupby(['tags']).count())
st.markdown(":small_blue_diamond: The most common tag is **Figther**")
st.markdown(":small_blue_diamond: The less common tag is **Marksman**")

# Here whe create a selectbox in which the user can select a champion and get a more detailed description.
st.header("Champion descriptions:")
champions = list(data['name'])
champions.sort()
selected_champ = st.selectbox("Select a champion:", champions)
selected_data = data[data['name']==selected_champ]
st.subheader(selected_data['name'].iloc[0])
st.markdown(selected_data['title'].iloc[0])
st.image(selected_data['icon'].iloc[0])
st.markdown(selected_data['description'].iloc[0])