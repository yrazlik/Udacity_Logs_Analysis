# Udacity_Logs_Analysis Project
This is a project for Udacity's [Full Stack Web Developer Nanodegree]

## Project Description:
This is a reporting tool that rints out reports (in plain text) 
based on the data in the database. This reporting tool is a Python program 
using the psycopg2 module to connect to the database.

### Questions to Answer:
1. **What are the most popular three articles of all time?** Which articles have been 
accessed the most? Present this information as a sorted list with the most popular 
article at the top.
1. **Who are the most popular article authors of all time?** That is, when you sum up 
all of the articles each author has written, which authors get the most page views? 
Present this as a sorted list with the most popular author at the top.
1. **On which days did more than 1% of requests lead to errors?**  The log table 
includes a column status that indicates the HTTP status code that the news site sent 
to the user's browser. 

## Setting Up The Project Environment:
Here are the steps to set up the project environment to run it:

1. Install Vagrant from https://www.vagrantup.com.
2. Install VirtualBox from https://www.virtualbox.org.
3. Download the vagrant setup files from https://github.com/udacity/fullstack-nanodegree-vm.
4. Download the database from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
5. Put the newsdata.sql file into the vagrant directory.
7. Clone or download my project.
8. Upzip as needed and copy all files into the vagrant directory.
9. Open Terminal and navigate to the project folder.
10. cd into the vagrant directory
11. Run ``` vagrant up ``` to build the VM.
12. After vagrant is up and running, run ``` vagrant ssh ```.
13. cd into the project directory: ``` cd /vagrant ```
14. Load the data using the following command: ``` psql -d news -f newsdata.sql ```
15. Run ``` python newsdata.py ```
