# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:47:54 2018

@author: ADITYA
"""

import sqlite3
conn = sqlite3.connect('onlineCourses.db')

c = conn.cursor()

# Insert into courses
#Coursera
c.execute('''INSERT INTO course VALUES (001,"App Development","Development")''')
c.execute('''INSERT INTO course VALUES (002,"Algorithms","Development")''')
c.execute('''INSERT INTO course VALUES (003,"Java","Development")''')
c.execute('''INSERT INTO course VALUES (004,"Swift","Development")''')
c.execute('''INSERT INTO course VALUES (005,"Python","Development")''')

c.execute('''INSERT INTO course VALUES (006,"Machine Learning","Data Science")''')
c.execute('''INSERT INTO course VALUES (007,"Python Machine Learning","Data Science")''')
c.execute('''INSERT INTO course VALUES (008,"Deep Learning","Data Science")''')
c.execute('''INSERT INTO course VALUES (009,"Big Data","Data Science")''')

c.execute('''INSERT INTO course VALUES (010,"Blockchain","Blockchain")''')
c.execute('''INSERT INTO course VALUES (011,"IBM Blockchain","Blockchain")''')
c.execute('''INSERT INTO course VALUES (012,"Cryptocurrency","Blockchain")''')

#Udemy
c.execute('''INSERT INTO course VALUES (013,"Meteor React","Development")''')
c.execute('''INSERT INTO course VALUES (014,"C Programming","Development")''')
c.execute('''INSERT INTO course VALUES (015,"Eclipse","Development")''')
c.execute('''INSERT INTO course VALUES (016,"Python","Development")''')

c.execute('''INSERT INTO course VALUES (017,"Machine Learning","Data Science")''')
c.execute('''INSERT INTO course VALUES (018,"Data Science & Machine Learning","Data Science")''')
c.execute('''INSERT INTO course VALUES (019,"Deep Learning","Data Science")''')
c.execute('''INSERT INTO course VALUES (020,"Artificial Intelligence","Data Science")''')

c.execute('''INSERT INTO course VALUES (021,"Blockchain & Bitcoin","Blockchain")''')
c.execute('''INSERT INTO course VALUES (022,"Build your Blockchain","Blockchain")''')
c.execute('''INSERT INTO course VALUES (023,"Ethereum & Solidity","Blockchain")''')

#Udacity
c.execute('''INSERT INTO course VALUES (024,"Android","Development")''')
c.execute('''INSERT INTO course VALUES (025,"IOS","Development")''')
c.execute('''INSERT INTO course VALUES (026,"Full stacks web development","Development")''')
c.execute('''INSERT INTO course VALUES (027,"Python Foundation","Development")''')

c.execute('''INSERT INTO course VALUES (028,"Machine Learning","Data Science")''')
c.execute('''INSERT INTO course VALUES (029,"Deep Learning","Data Science")''')
c.execute('''INSERT INTO course VALUES (030,"Artificial Intelligence","Data Science")''')
c.execute('''INSERT INTO course VALUES (031,"Blockchain Developer","Blockchain")''')

#Insert into details
c.execute('''INSERT INTO details VALUES (101,"Coursera","https://www.coursera.org/specializations/full-stack-mobile-app-development",150,001)''')
c.execute('''INSERT INTO details VALUES (102,"Coursera","https://www.coursera.org/learn/algorithmic-toolbox",150,002)''')
c.execute('''INSERT INTO details VALUES (103,"Coursera","https://www.coursera.org/specializations/java-programming",150,003)''')
c.execute('''INSERT INTO details VALUES (104,"Coursera","https://www.coursera.org/learn/swift-programming",150,004)''')
c.execute('''INSERT INTO details VALUES (105,"Coursera","https://www.coursera.org/learn/python-programming-introduction",150,005)''')

c.execute('''INSERT INTO details VALUES (106,"Coursera"," https://www.coursera.org/learn/machine-learning",150,006)''')
c.execute('''INSERT INTO details VALUES (107,"Coursera","https://www.coursera.org/learn/python-machine-learning",150,007)''')
c.execute('''INSERT INTO details VALUES (108,"Coursera","https://www.coursera.org/specializations/deep-learning",150,008)''')
c.execute('''INSERT INTO details VALUES (109,"Coursera","https://www.coursera.org/specializations/big-data",150,009)''')

c.execute('''INSERT INTO details VALUES (110,"Coursera","https://www.coursera.org/specializations/blockchain",150,010)''')
c.execute('''INSERT INTO details VALUES (111,"Coursera","https://www.coursera.org/learn/ibm-blockchain-essentials-for-developers",150,011)''')
c.execute('''INSERT INTO details VALUES (112,"Coursera","https://www.coursera.org/learn/cryptocurrency",150,012)''')

c.execute('''INSERT INTO details VALUES (113,"Udemy","https://www.udemy.com/meteor-react/",150,013)''')
c.execute('''INSERT INTO details VALUES (114,"Udemy","https://www.udemy.com/c-programming-for-beginners-/",150,014)''')
c.execute('''INSERT INTO details VALUES (115,"Udemy","https://www.udemy.com/eclipse-the-basic-java-programming-course/",150,015)''')
c.execute('''INSERT INTO details VALUES (116,"Udemy"," https://www.udemy.com/python-the-complete-python-developer-course/",150,016)''')

c.execute('''INSERT INTO details VALUES (117,"Udemy","https://www.udemy.com/machinelearning/",150,017)''')
c.execute('''INSERT INTO details VALUES (118,"Udemy","https://www.udemy.com/data-science-and-machine-learning-with-python-hands-on/",150,018)''')
c.execute('''INSERT INTO details VALUES (119,"Udemy","https://www.udemy.com/deeplearning/",150,019)''')
c.execute('''INSERT INTO details VALUES (120,"Udemy","https://www.udemy.com/artificial-intelligence-az/",150,020)''')

c.execute('''INSERT INTO details VALUES (121,"Udemy","https://www.udemy.com/blockchain-and-bitcoin-fundamentals/",150,021)''')
c.execute('''INSERT INTO details VALUES (122,"Udemy","https://www.udemy.com/build-your-blockchain-az/",150,022)''')
c.execute('''INSERT INTO details VALUES (123,"Udemy","https://www.udemy.com/ethereum-and-solidity-the-complete-developers-guide/",150,023)''')

c.execute('''INSERT INTO details VALUES (124,"Udacity","https://in.udacity.com/course/android-developer-nanodegree-by-google--nd801",150,024)''')
c.execute('''INSERT INTO details VALUES (125,"Udacity","https://in.udacity.com/course/ios-developer-nanodegree--nd003",150,025)''')
c.execute('''INSERT INTO details VALUES (126,"Udacity","https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004",150,026)''')
c.execute('''INSERT INTO details VALUES (127,"Udacity","https://in.udacity.com/course/python-foundation-nanodegree--nd002-inpy",150,027)''')

c.execute('''INSERT INTO details VALUES (128,"Udacity","https://in.udacity.com/course/machine-learning-engineer-nanodegree--nd009t",150,028)''')
c.execute('''INSERT INTO details VALUES (129,"Udacity","https://in.udacity.com/course/deep-learning-nanodegree--nd101",150,029)''')
c.execute('''INSERT INTO details VALUES (130,"Udacity","https://in.udacity.com/course/ai-programming-python-nanodegree--nd089",150,030)''')

c.execute('''INSERT INTO details VALUES (131,"Udacity","https://in.udacity.com/course/blockchain-developer-nanodegree--nd1309",150,031)''')

#insert into resources
#Dev
c.execute('''INSERT INTO resources VALUES (201,"Hackerearth","https://www.hackerearth.com/blog/", NULL,"Optional",001)''')
c.execute('''INSERT INTO resources VALUES (202,"Linux Foundation","https://www.linuxfoundation.org/newsroom/blog/",NULL,"Optional",013)''')
c.execute('''INSERT INTO resources VALUES (203,"Odin Project","https://www.theodinproject.com/", NULL,"Optional",024)''')

#DataScience
c.execute('''INSERT INTO resources VALUES (204,"Super Data Science","https://www.superdatascience.com/", NULL,"Optional",006)''')
c.execute('''INSERT INTO resources VALUES (205,"No Free Hunch","http://blog.kaggle.com/ ", NULL,"Optional",017)''')
c.execute('''INSERT INTO resources VALUES (206,"Fastml","http://fastml.com/", NULL,"Optional",028)''')

#Blockchain
c.execute('''INSERT INTO resources VALUES (207,"Ethereum","https://ethereumdev.io/", NULL,"Optional",023)''')
c.execute('''INSERT INTO resources VALUES (208,"Coin Desk","https://www.coindesk.com/", NULL,"Optional",012)''')
c.execute('''INSERT INTO resources VALUES (209,"IBM","https://www.ibm.com/blogs/blockchain/", NULL,"Optional",011)''')
c.execute('''INSERT INTO resources VALUES (210,"Berkeley","https://blockchainatberkeley.blog/?gi=2dff7bdf134a", NULL,"Optional",031)''')


# Save (commit) the changes
conn.commit()
conn.close()
