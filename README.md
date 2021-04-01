# CS229-328Project
Etsy Project

Investigate API
Courtney & Christy							March 16, 2021

Instagram
Goal: Write a simple python program to retrieve & output something using API
Start reading API documentation
What data can you retrieve? 
Etsy’s api lets you retrieve its website's features such as: public profiles, tags, listings, shops, sales data, and favourites!
What format is the data?
JSON
What info about each data item?
You can get shop names, user names, team names, images, and currency! 
FInd a good python library & examples for working with API
Etsy PyPi
Create a Github Repo for Project { CS229/328 Project }
Put this info into the READMe
Email WIlson Repo Link
Commit the initial python program

Example: Twitter
Users, Tweets, …
JSON
Users: ID, Handle, Start Date, ...

Project Overview
Goal: Retrieve daily top 100 trending listings, store in a SQL database, serve information about trending listings (Courtney only)

Step 1: Need to write a program that will retrieve the following info for each of the top 100 trending listings, store in python dictionary with listing_id as key (print info (json) for each day's listing to a file): (Christy & Courtney)
- listing_id
- title
- description
- creation_tsz
- price
- tags
- featured rank
- URL
- views
  
Step 2: Design and an SQL Database for the informatin you retrieve (Christy & Courtney)

Step 3: Modify program to do a) any necessary processing of the data before b) adding each listing to the database (Christy & Courtney)

Step 4: Write simpile program to serve info from database over the web (Courtney only)


