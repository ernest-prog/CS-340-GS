# CS-340-GS

CS 340 README Template


About the Austin Animal Center
Grazioso Salvare’s project consists of the database and client-facing web application that will use existing data from Austin animal shelters.  The software application will serve to identify and categorize available dogs for search and rescue training. It will also allow users to create, read, update, and remove from the database. 

Motivation
When databases and API are used correctly they increase the ability to search larger data sets quickly based off either specific information or general. In our case for Grazioso Salvare’s we created a query that organizes their database by breed, age, and sex allowing the staff to locate their guest more easily.

Getting Started
To get started you’ll need to add our database to your Linux shell. You can do this by importing Austin Animal Center (AAC). You can then use our client facing application to conduct searches of animals currently at our shelter. Note: Be sure to use database animals once imported.

•	Install the MongoDB and Python drivers needed. 
•	Download the following files into your Mongo Directory: 
o	aac_shelter_outcomes.csv
o	CRUD.PY
o	CRUD_test.py

Installation
To install our application please visit the appropriate app store. For developers you can access our installation instructions found below. 


1.	Login using authentication
2.	Once logged in import Austin Animals Database. 
3.	After installation of our database, you can use our query functions to do controlled searches. 


Usage
Our application works a few different ways. As a provider or employee of Austin Animal Center you can easily add animals into the database. If you’re a developer, you can create queries that call our database to gather information. You will need to be an authorized user, however. 



Code Example
 


Tests
To run a test, you can write a test script to call our database to gather information about a specific animal or group of animals. Your test should return results if it matches any of the criteria contained within our database. 

 


Screenshots
 
 



Roadmap/Features (Optional)

Contact
Ernest Enriquez
Ernest.enriquez@snhu.edu 


How do you write programs that are maintainable, readable, and adaptable? 
To write programs that are maintanable, readable, and adaptable you must ensure you code is commented and all documentation is up to date.

Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
When using widgets it allows us to segment our code. Enabling flexibility for those widgets to be used across numerous dashboards and our code not turning into spaghetti code.I can leverage my learnings from this CRUD module in my career path later on as an sql database engineer. 

How do you approach a problem as a computer scientist? 
As a computer scientist were trained to evaluate our problem and break it down into smaller sub task. I'd first start with a white board drawing to ensure I completly understand the task and the order of which I will begin to code. This will allow me to implement agile methods which enables me to have a maintainable, readable, and adaptable project in the furture. 
Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses?
It differed because the end point tasks was given to us by Grazioso Salvare. We were then to break it down similiar to how each module assignment already had done for us. I first identified all my imports that needed to be created in my dataset. Then once imported ran search queries to ensure datasets were proper. This also enabled me to see what stored values were for making queries. 

What techniques or strategies would you use in the future to create databases to meet other client requests?
Some techniques I found super valuable were aggregating my pipeline and the $unwind ability. Understanding how to also make a call to a local host is super important for remote work. 

What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
Computer scientists use technology to solve a range of different problems. My role as a computer scientist would help Grazioso Salvare because I have the knowledge to create an structure of data that makes it simple for their employees but we can also create applications that are consumer facing which enables their consumers to create accounts and manaage authorized datasets. 
