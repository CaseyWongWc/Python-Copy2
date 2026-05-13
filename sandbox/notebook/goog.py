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

Feedback?
Variety
Volume
Velocity


Electronic health records contain data on patient measurements, test results, medical history, image scans, and other characteristics.
Wearable devices like a smartwatch can track a patient's exercise, heart rate, and sleeping habits. Data from these devices are sent to a patient's doctor or care team in real time.
UnitedHealth Group provides insurance for nearly 50 million customers. As part of providing insurance coverage, UnitedHealth Group manages medical records and claims data for each individual customer.

'''
with "myfile.txt":
    '''
    variety
    -electronic health records contain data on patient measurements, test results, medical history, image scans, and other characteristics. This variety of data types and formats is a key aspect of big data in healthcare.
    velocity
    -wearable devices like a smartwatch can track a patient's exercise, heart rate, and sleeping habits. Data from these devices are sent to a patient's doctor or care team in real time. The speed at which this data is generated and transmitted is an example of the velocity aspect of big data in healthcare.
    volume
    -unitedhealth group provides insurance for nearly 50 million customers. As part of providing insurance coverage, unitedhealth group manages medical records and claims data for each individual customer. The sheer amount of data generated and managed by unitedhealth group for its customers is an example of the volume aspect of big data in healthcare.
    '''
    
##############################################################################
#skipped
##############################################################################
'''
Skip to main content

zyBooks
My library >
CS 2520: Python for Programmers home >
15.3: Python for data science
zyBooks catalog
Help/FAQ
Casey Wong
You have unverified email(s). Use My Profile to send another verification email.


15.2 Data science life cycle
15.3 Introduction to Python for data science
Advantages/disadvantages of Python for data science
Python is one of the most popular languages for data science due to the language's high-level nature, portability, and broad community support. The readability of the language, and the portability of running a Python script easily on different computers, enables collaboration that outweighs performance concerns. Additionally, industry professionals frequently contribute free and high-quality packages for data science that are widely used.

Table 15.3.1: Advantages and disadvantages of Python for data science.
Advantages	Disadvantages
Readability: Python reads like English, and functions from the same library use consistent syntax.	Consistency: Different libraries may have different syntax conventions.
Popularity: Python is popular in data science and elsewhere in industry, which means resources for learning Python are widely available.	Memory: Python uses more computer memory than other programming languages.
Innovation: New data science models and technologies are constantly added to Python.	Speed: Other programming languages such as Julia perform computations on datasets more quickly than Python.

Feedback?
participation activity
15.3.1: Python for data science.
1)
Python code is more difficult to read than code in most other programming languages.
2)
Python is a good choice for a data science project that prioritizes performance.
3)
Python is a good choice for a data science project that uses packages developed by other data scientists.

Feedback?
Common data science packages
Many Python packages exist for data manipulation, visualization, and modeling. Different packages provide different functionality, so a data science project will use multiple packages. Ex: Imagine a scientist wants to classify hawk populations in Iowa from a large dataset. First the data is loaded into special data structures using pandas, then classification algorithms are run from scikit-learn, and then the results are visualized using seaborn. The unique capabilities of each package provide a data scientist with a comprehensive set of tools for almost any task.

Table 15.3.2: Common data science packages in Python.
Import name	Common alias	Description
numpy	np	NumPy includes functions and classes that aid in numerical computation. NumPy is used in many other data science packages.
pandas	pd	pandas provides methods and classes for tabular and time-series data.
sklearn	sk	scikit-learn provides implementations of many machine learning algorithms with a uniform syntax for preprocessing data, specifying models, fitting models with cross-validation, and assessing models.
matplotlib.pyplot	plt	Matplotlib allows the creation of data visualizations in Python. The functions mostly expect NumPy arrays.
seaborn	sns	seaborn also allows the creation of data visualizations but works better with pandas DataFrame objects.
scipy.stats	sp.stats	SciPy provides algorithms and functions for computing problems that arise in science, engineering and statistics. scipy.stats provides the functions for statistics.
statsmodels	sm	statsmodels adds functionality to Python to estimate many different kinds of statistical models, make inferences from those models, and explore data.

Feedback?
participation activity
15.3.2: Choosing data science packages in Python.
Select the best package to do the task described.

1)
Read, investigate, and manipulate datasets
2)
Visualize a dataset
3)
Create and evaluate a machine learning model from a prepared dataset

Feedback?
How was this section?

|


Provide section feedback
15.4 Introduction to Jupyter Notebooks

## 15.3 Introduction to Python for data science

### Advantages/disadvantages of Python for data science

Python is one of the most popular languages for data science due to the language's high-level nature, portability, and broad community support. The readability of the language, and the portability of running a Python script easily on different computers, enables collaboration that outweighs performance concerns. Additionally, industry professionals frequently contribute free and high-quality packages for data science that are widely used.

> **Advantages and disadvantages of Python for data science.**
> | Advantages | Disadvantages |
> | --- | --- |
> | Readability: Python reads like English, and functions from the same library use consistent syntax. | Consistency: Different libraries may have different syntax conventions. |
> | Popularity: Python is popular in data science and elsewhere in industry, which means resources for learning Python are widely available. | Memory: Python uses more computer memory than other programming languages. |

### PARTICIPATION ACTIVITY: Python for data science.

**1.** Python code is more difficult to read than code in most other programming languages.
Answer: **False**
*Python was originally designed with readability in mind. Python developers have several philosophies related to design, including: "Readability counts" and "Simple is better than complex."*

**2.** Python is a good choice for a data science project that prioritizes performance.
Answer: **False**
*Other languages, like Julia, perform calculations faster and use less memory.*

**3.** Python is a good choice for a data science project that uses packages developed by other data scientists.
Answer: **True**
*Python is a popular choice for data science programs and has many available resources.*

### Common data science packages

Many Python packages exist for data manipulation, visualization, and modeling. Different packages provide different functionality, so a data science project will use multiple packages. Ex: Imagine a scientist wants to classify hawk populations in Iowa from a large dataset. First the data is loaded into special data structures using pandas, then classification algorithms are run from scikit-learn, and then the results are visualized using seaborn. The unique capabilities of each package provide a data scientist with a comprehensive set of tools for almost any task.

> **Common data science packages in Python.**
> | Import name | Common alias | Description |
> | --- | --- | --- |
> | numpy | np | NumPy includes functions and classes that aid in numerical computation. NumPy is used in many other data science packages. |
> | pandas | pd | pandas provides methods and classes for tabular and time-series data. |
> | sklearn | sk | scikit-learn provides implementations of many machine learning algorithms with a uniform syntax for preprocessing data, specifying models, fitting models with cross-validation, and assessing models. |
> | matplotlib.pyplot | plt | Matplotlib allows the creation of data visualizations in Python. The functions mostly expect NumPy arrays. |
> | seaborn | sns | seaborn also allows the creation of data visualizations but works better with pandas DataFrame objects. |
> | scipy.stats | sp.stats | SciPy provides algorithms and functions for computing problems that arise in science, engineering and statistics. scipy.stats provides the functions for statistics. |
> | statsmodels | sm | statsmodels adds functionality to Python to estimate many different kinds of statistical models, make inferences from those models, and explore data. |

### PARTICIPATION ACTIVITY: Choosing data science packages in Python.

**1.** Read, investigate, and manipulate datasets
- Matplotlib
- pandas ✓
- scikit-learn
*pandas was built to add functionality for reading, investigating, and manipulating datasets. pandas also provides methods for combining datasets and time series.*

**2.** Visualize a dataset
- NumPy
- pandas
- seaborn ✓
*seaborn provides functions that allow the creation and customization of visualizations.*

**3.** Create and evaluate a machine learning model from a prepared dataset
- NumPy
- SciPy
- scikit-learn ✓
*scikit-learn provides methods for many types of machine learning: classification, regression, and clustering. scikit-learn also provides methods for preparing data and tuning models: dimensionality reduction, model selection, and preprocessing of data.*'''
####################################################
with "myfile.txt" as f:
    "PA 15.3.1: Python for data science.txt"
    '''
    1)python code is more difficult to read than code in most other programming languages.
        -false. python was originally designed with readability in mind. python developers have several philosophies related to design, including: "readability counts" and "simple is better than complex."
    2)python is a good choice for a data science project that prioritizes performance.
        -false. other languages, like julia, perform calculations faster and use less memory.
    3)python is a good choice for a data science project that uses packages developed by other data scientists.
        -true. python is a popular choice for data science programs and has many available resources.
    '''
#table 15.3.2: Common data science packages in Python.
with _:
    with "myfile.md" as f:
        '''
        | Import name | Common alias | Description |
        | --- | --- | --- |
        | numpy | np | NumPy includes functions and classes that aid in numerical computation. NumPy is used in many other data science packages. |
        | pandas | pd | pandas provides methods and classes for tabular and time-series data. |
        | sklearn | sk | scikit-learn provides implementations of many machine learning algorithms with a uniform syntax for preprocessing data, specifying models, fitting models with cross-validation, and assessing models. |
        | matplotlib.pyplot | plt | Matplotlib allows the creation of data visualizations in Python. The functions mostly expect NumPy arrays. |
        | seaborn | sns | seaborn also allows the creation of data visualizations but works better with pandas DataFrame objects. |
        | scipy.stats | sp.stats | SciPy provides algorithms and functions for computing problems that arise in science, engineering and statistics. scipy.stats provides the functions for statistics. |
        | statsmodels | sm | statsmodels adds functionality to Python to estimate many different kinds of statistical models, make inferences from those models, and explore data. |
        '''
    # with bash:
        
    #     # COMMANDS (run in /workspaces/Python-Copy2)
    #     python3 -m venv .venv
    #     source .venv/bin/activate
    #     # err: /bin/sh: 1: source: not found
    #     # !err: exit code 127
    #     python -m pip install --upgrade pip
    #     # out: Requirement already satisfied: pip in /usr/local/python/3.12.1/lib/python3.12/site-packages (26.1.1)
    #     pip install numpy
    #     # out: Requirement already satisfied: numpy in /usr/local/python/3.12.1/lib/python3.12/site-packages (2.4.4)
    #     python -c "import numpy as np; print(np.__version__)"
        # out: 2.4.4
    with "main.py" as f:
        ''''''
        cmd("ls","-alf")
        cmd()
        # val: myfile.txt
        # val: .venv
        # val: mycsv.csv
        # val: main.py
        # val: PA 15.3.1: Python for data science.txt
        # val: myfile.py
        # val: ..
        # val: .
        # val: myfile.md
        # val:  '
        # val:  _     ___
        # val: #_~`--'__ `===-,
        # val: `.`.     `#.,;《
        # val: ,_|_|     ## #《
        # val: `__.__    `####《
        # val:      ~~< ,###'~
        # val:         》##'
        # val: Wolves
        # val: '

    with "main.py" as f:
        import numpy as np
        # !err: ModuleNotFoundError: No module named 'numpy'
        # !err:   at line 330: # err: /bin/sh: 1: source: not found
        # import pandas as pd
        # import sklearn as sk
        # import matplotlib.pyplot as plt
        # import seaborn as sns
        # import scipy.stats as sp.stats
        # import statsmodels as sm
    f
    # val: Scratch(out=[], err=[], outs='')


    
