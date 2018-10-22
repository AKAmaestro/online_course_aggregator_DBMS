# -*- coding: utf-8 -*-
"""
Spyder Editor

This file creates the tables in database named 'onlineCourses.db'.
"""

import sqlite3


conn = sqlite3.connect('onlineCourses.db')
c = conn.cursor()

# Create course table
c.execute('''CREATE TABLE course(c_code int primary key, c_name string, category string)''')

#create details table
c.execute('''CREATE TABLE details(d_id int primary key, provider string, d_link string, 
                                  duration int,c_code int,foreign key(c_code) references 
                                  course(c_code) on delete cascade on update cascade)''')

#Create resources table
c.execute('''CREATE TABLE resources(sl_no int primary key, r_name string ,r_link string, tags int, 
                                    compulsion string,c_code int,foreign key(c_code) references course(c_code) on delete
                                  cascade on update cascade)''')

#To view tables in database
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())
    
# Save (commit) the changes
conn.commit()
conn.close()