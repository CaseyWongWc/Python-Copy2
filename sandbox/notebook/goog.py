from Helpers.helpings import *
'''15.1 Introduction to data science
Data science
Data science is an interdisciplinary field focused on discovering patterns and describing relationships using data. Data science uses techniques from computer science and statistics. Data scientists use computers to write code and store, modify, and visualize large datasets. Data scientists can also build, test, and interpret a data model, a representation of a real-life system that organizes data elements and informs how the elements relate to one another. Ex: The FBI's Most Wanted list is a model that contains data elements such as eye color, hair color, known accomplices, etc. related to each suspect on the list. The data model can be used to make predictions for new data.

participation activity
15.1.1: Comparing data science, computer science, and statistics.

Start
Computer scientistsProtect systems from hackersDevelop softwareAnalyze data with algorithmsDesign websitesBuild data storage toolsStatisticiansDesign experimentsDerive new modelsAnalyze data using modelsModify and format datasetsCreate dynamic plots and graphsInterpret resultsData scientists
Step 1: A circle appears labeled "Computer scientists." Computer science tasks are listed in the circle: design websites, develop software, protect from hackers, analyze data with algorithms, build data storage tools. Step 2: A circle appears labeled "Statisticians." Statistics tasks are listed in the circle: design experiments, derive new models, analyze data using models, and interpret results. Step 3: A circle appears labeled "Data scientists." The circle overlaps with both "Computer scientists" and "Statisticians". Analyze data with algorithms, build data storage tools, analyze data using models, interpret results, are in the data science circle. New tasks appear: modify and format datasets, create dynamic plots and graphs.

Captions
Computer scientists use programming to design new software and websites, protect computer systems from hackers, implement algorithms, and store data.
Statisticians design experiments and apply models to discover trends and patterns in a dataset. Statisticians also derive new models using mathematical techniques.
Data scientists use programming to transform data into meaningful information using graphs, algorithms, and models.

Feedback?
participation activity
15.1.2: Data science.
Many professionals use data, but not all are data scientists. Who is most likely to work on each of the data-related tasks below?

1)
Creating an interactive graph of product sales in the past 18 months
Correct
Data scientists present data in graphs, tables, and interactive visualizations, which help the scientists gather meaningful insights from data.
2)
Building a user interface for a data storage system containing data on product sales
3)
Designing an experiment to compare three marketing strategies in different markets

Feedback?'''
with "myfile.txt":
    '''
    1)creating an interactive graph of product sales in the past 18 months
        -data scientists present data in graphs, tables, and interactive visualizations, which help the scientists gather meaningful insights from data. They would be most likely to create an interactive graph of product sales in the past 18 months.
    2)building a user interface for a data storage system containing data on product sales
        -computer scientists design websites, develop software, and build data storage tools. They would be most likely to build a user interface for a data storage system.
    3)designing an experiment to compare three marketing strategies in different markets
        -statisticians design experiments and apply models to discover trends and patterns in a dataset. They would be most likely to design an experiment to compare three marketing strategies in different markets.
    '''

'''Datasets
Data scientists uncover patterns and make predictions from datasets. A dataset is a collection of information. Datasets consist of features and instances. A feature, or variable, is a characteristic that can be measured or observed on an observational unit. Features are recorded for individual instances, or observational units, in the dataset. Instances are also called data points or observations.

participation activity
15.1.3: Features and instances.


1

2

3

Each characteristic of a penguin, such as bill length, body mass, and sex, is a feature. In the dataset, each column represents a different feature.
AdelieChinstrapGentooAdelieGentooDreamDreamDreamBiscoeBiscoe36.543.548.736.345.318.018.115.719.513.718220220819021031503400535038004300femalefemalefemalemalemalespeciesislandbill_length_mmbill_depth_mmflipper_length_mmbody_mass_gsex
Step 1: The first column of a data table is shown. Step 2: Rows are revealed one by one. Step 3: Column headers are revealed.

Captions
Researchers at the Palmer Archipelago in the Antarctic collected data on three local penguin species: Adelie, Chinstrap, and Gentoo.
Each individual penguin in this dataset is an instance. In the dataset, each row represents a different instance.
Each characteristic of a penguin, such as bill length, body mass, and sex, is a feature. In the dataset, each column represents a different feature.
'''
with Scratch:
    with open("mycsv.csv","w") as f:
        f.write("species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex\n")
        # val: 78
        f.write("Adelie,Dream,36.5,18.0,181,3750,female\n")
        # val: 39
        f.write("Chinstrap,Dream,43.5,18.1,195,3800,female\n")
        # val: 42
        f.write("Gentoo,Dream,48.7,15.7,220,5000,female\n")
        # val: 39
        f.write("Adelie,Biscoe,36.3,19.3,180,3250,male\n")
        # val: 38
        f.write("Gentoo,Biscoe,45.3,14.5,210,4500,male\n")
        # val: 38
        f.write("Dream,Biscoe,18.1,8.5,150,1500,male\n")
        # val: 36
# 
'''participation activity
15.1.4: Features and instances.
A data scientist is developing a model to identify suspicious credit card transactions. Identify each of the following as a feature or instance.

1)
Transactions
2)
Sales amount
3)
Type of store

Feedback?'''

with "myfile.txt":
    '''
    1)transactions
        -transactions are instances, or data points, in the dataset. Each transaction is an individual observation that contains information about a specific credit card transaction.
    2)sales amount
        -sales amount is a feature, or variable, in the dataset. It is a characteristic that can be measured or observed for each transaction.
    3)type of store
        -type of store is a feature, or variable, in the dataset. It is a characteristic that can be measured or observed for each transaction.
    '''
'''ig data
The rise of data science over the last 20 years is partially a result of big data. Big data describes datasets with large volume, created and updated with high velocity, that have variety in structure and format. As more companies and organizations collect and use big data, the demand for people with data science skills grows.

participation activity
15.1.5: Big data at Twitter.


1

2

3

4

Twitter users create approximately 400 billion events per day.
VolumeVarietyVelocityDaily tweets: 12 TBAnnual tweets: 4.3 PB
 2,100Big data is everywhere on Twitter.                    #bigdata

Step 1: The Twitter logo appears. Step 2: The header Volume appears. Daily and annual tweet volume is displayed under the Volume header. Six computer icons are shown next to daily usage. Step 3: The header Variety appears. A sketch of a tweet appears under the Variety header, with each icon revealed one at a time. Step 4: The header Velocity appears. A large number of comment, heart, and retweet icons appear under the Velocity heading.

Captions
In early 2022, Twitter had 200 million active daily users and about 1.3 billion accounts. These accounts generated big data.
Storing new tweets takes about 12 terabytes (TB) per day, or the storage of about six MacBook Pros. Storing all tweets posted in a year takes 4.3 petabytes (PB), or about 2,100 MacBook Pros.
Twitter users do more than tweet. User events on Twitter include tweets, hashtags, images, likes, shares, follows, blocks, re-tweets, and comments.
Twitter users create approximately 400 billion events per day.
Playing step 4: Twitter users create approximately 400 billion events per day. Step finished playing

Feedback?
participation activity
15.1.6: Big data in healthcare.
Big data is used by hospitals and medical researchers to track patient outcomes and suggest possible treatment options. For each application of big data in healthcare, which "V" of big data is described?

How to use this tool
Variety
Volume
Velocity
Electronic health records contain data on patient measurements, test results, medical history, image scans, and other characteristics.
Wearable devices like a smartwatch can track a patient's exercise, heart rate, and sleeping habits. Data from these devices are sent to a patient's doctor or care team in real time.
UnitedHealth Group provides insurance for nearly 50 million customers. As part of providing insurance coverage, UnitedHealth Group manages medical records and claims data for each individual customer.

Reset

Feedback?'''

INFO()
# val: /workspaces/Python-Copy2/sandbox/files
# val: Wed May 13 02:45:55 UTC 2026
# val: ./myfile.txt
# val: ./mycsv.csv
# val: ./ '
# val:  _     ___
# val: #_~`--'__ `===-,
# val: `.`.     `#.,;《
# val: ,_|_|     ## #《
# val: `__.__    `####《
# val:      ~~< ,###'~
# val:         》##'
# val: Wolves
# val: '
