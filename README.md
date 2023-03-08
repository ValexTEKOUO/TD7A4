##How to properly use this image

Hello here is the explanation of how you can use this image to serve your needs.
The goal is to build a simpla flask application with mongoDB and also use volumes for data persistance.

![image](https://user-images.githubusercontent.com/112904885/223761015-3457474c-6592-4e7c-aeb1-b5e584baf1af.png)

Basically we just need four files as you can see on the image above

##app.py
This file is where we build the code of our appliation 

##Dockerfile
This is where we write specifications and the environment variables


##Docker-Compose

This is where we make the description about the application: the type of service we used, the type of network, the services and the database
First we will specifie the version which is 3,
• We specified the network(mynetworkTP5) which is a bridge type,
• After we specified the services mongoDB(our database), flaskapp(the type of application)
• mongoDB uses the network created(mynetworkTP5), the type of the image (mongo) and the
port(27017) to map the connection.
• The flaskapp is use from the origin (‘.’), it uses the same network(mynetworkTP5) as
mongoDB
• When we use depends_on(“mongoDB”) is to say that if the db container is not started the
container app can’t be start.
• We also use port(5000:5000) for mapping connection)

##Requirements
In our project we use Flask and mongoDB, this is where we can mention that

Once you finished you can type Docker Compose up to start building
