# Learning-MongoDB
My first Data App using MongoDB and Streamlit.

[Link to Application](https://evening-plateau-77242.herokuapp.com/)

This is very simple data app that explores a static MongoDB collection.
Building this app was actually very fun and a great opportunity to learn the following technologies:
* **MongoDB:** Although there are no complex queries in the project, it was necessary to create my own instance of a MongoDB database and use **pymongo** to upload and query the dataset. If the dataset was not static, the queries would have to be more elaborate.
* **pandas:** Because the dataset is static and small, it is possible to use pandas to convert the entire data of the MongoDB collection into a pd.DataFrame and easily manipulate the dataset from there.
* **streamlit:** This python module was used to easily create a data visualization app.
* **heroku:** The cloud service that makes this app run is provided by heroku.
