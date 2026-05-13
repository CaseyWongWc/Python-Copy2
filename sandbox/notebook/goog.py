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
    # with "main.py" as f:
    #     '''
    #     python3 -m venv .venv
    #     source .venv/bin/activate
    #     python -m pip install --upgrade pip
    #     pip install numpy
    #     python -c "import numpy as np; print(np.__version__)'''
    #     #cmd("ls","-alf")
    #     cmd("python3", "-m", "venv", ".venv")
    #     # val: 
    #     cmd(".venv/bin/activate")
    #     cmd("python", "-m", "pip", "install", "--upgrade", "pip")
    #     cmd("pip", "install", "numpy")
    #     cmd("python", "-c", "import numpy as np; print(np.__version__)")
    #     import numpy as np
    #     # !err: PermissionError: [Errno 13] Permission denied: '.venv/bin/activate'
    #     # !err:   at line 339: python3 -m venv .venv

    # with "main.py" as f:
    #     import numpy as np
    #     # !err: ModuleNotFoundError: No module named 'numpy'
    #     # !err:   at line 345: # val: myfile.txt
    #     # import pandas as pd
    #     # import sklearn as sk
    #     # import matplotlib.pyplot as plt
    #     # import seaborn as sns
    #     # import scipy.stats as sp.stats
    #     # import statsmodels as sm
    # f
    # # val: Scratch(out=[], err=[], outs='')

    with "main.py" as f:
        import numpy as np
        import pandas as pd
        import sklearn as sk
        import matplotlib.pyplot as plt
        import seaborn as sns
        import scipy.stats as sp_stats
        import statsmodels as sm
    f
    # val: Scratch(np=<module 'numpy' from '/workspaces/Python-Copy2/.venv/lib/python3.12/site-packages/numpy/__init__.py'>, pd=<module 'pandas' from '/workspaces/Python-Copy2/.venv/lib/python3.12/site-packages/pandas/__init__.py'>, sk=<module 'sklearn' from '/workspaces/Python-Copy2/.venv/lib/python3.12/site-packages/sklearn/__init__.py'>, plt=<module 'matplotlib.pyplot' from '/workspaces/Python-Copy2/.venv/lib/python3.12/site-packages/matplotlib/pyplot.py'>, sns=<module 'seaborn' from '/workspaces/Python-Copy2/.venv/lib/python3.12/site-packages/seaborn/__init__.py'>, sp_stats=<module 'scipy.stats' from '/workspaces/Python-Copy2/.venv/lib/python3.12/site-packages/scipy/stats/__init__.py'>, sm=<module 'statsmodels' from '/workspaces/Python-Copy2/.venv/lib/python3.12/site-packages/statsmodels/__init__.py'>, out=[], err=[], outs='')
    
with "myfile.txt":
    '''
    1)read, investigate, and manipulate datasets
        -pandas was built to add functionality for reading, investigating, and manipulating datasets. pandas also provides methods for combining datasets and time series.
    2)visualize a dataset
        -seaborn provides functions that allow the creation and customization of visualizations.
    3)create and evaluate a machine learning model from a prepared dataset
        -scikit-learn provides methods for many types of machine learning: classification, regression, and clustering. scikit-learn also provides methods for preparing data and tuning models: dimensionality reduction, model selection, and preprocessing of data.
    '''
##############################################################################
'''## 15.4 Introduction to Jupyter Notebooks

### Jupyter

Jupyter is an interactive development environment (IDE) for writing and testing code in data science and scientific computing. In Jupyter, code is written in an interactive document called a Jupyter notebook. A notebook contains cells, which organize code, text, and output all in one place for testing, presenting, and sharing.  The three types of cells are code cells, markdown (text) cells, and raw (output) cells. Each cell can be run independently.

### PARTICIPATION ACTIVITY: Jupyter notebooks.

Step 1: A screenshot of the Jupyter notebook interface appears. The notebook interface has a markdown cell with the text "What is the relationship between a car's weight and miles per gallon?", then a code cell. Step 2: The first code cell contains the Python program:
from seaborn import scatterplot, load_dataset
car_data = load_dataset('mpg')
scatterplot(data=car_data, x='weight', y='mpg')
Step 3: The "Run" button is highlighted on the menu bar.
Step 4: The scatter plot appears in a raw cell labeled Out[1] below the code cell.

### PARTICIPATION ACTIVITY: Jupyter notebook.

**1.** Small segments of code and output in Jupyter notebooks are called _____.
- blocks
- cells ✓
- chunks
*Each cell should contain a small segment of code or output, with a specific purpose. Ex: Creating a scatter plot and fitting a model are often done in separate cells.*

**2.** The Run button executes ________ contained in a Jupyter notebook.
- all code
- selected code ✓
*The Run button executes code only from one cell at a time. The Restart and Run All button executes all code after restarting the kernel.*

**3.** Jupyter can be used to write and execute code in _________.
- Python
- multiple languages ✓
*Jupyter was originally developed to support three programming languages: Julia, Python, and R. Together, these three programming languages inspired the name: Ju (Julia) + pyt (Python) + er (R). Today, Jupyter supports over 100 programming languages.*

### Using Jupyter notebooks

Jupyter notebooks are used throughout this zyBook to illustrate data science applications. 
For information about installing and using Jupyter Notebook on a personal computer, check out the Jupyter installation guide. 

Note: Sample notebooks contain code to run a short analysis and can be modified to test new parameter values or different modeling functions. Clicking the "File" menu and "Download as" saves a notebook into a local working directory to save progress.

### PARTICIPATION ACTIVITY: Jupyter menu icons.

Step 1: The Jupyter notebook menu bar appears. Step 2-7: Arrows appear pointing to each button on the menu bar.

### PARTICIPATION ACTIVITY: Jupyter notebooks in the zyBook.

**1.** Which is a selectable type of cell in the menu bar?
- Input
- Kernel
- Markdown ✓
*A markdown cell contains descriptive text that can be formatted. The three types of cells are labeled code, markdown, and raw.*

**2.** What does the double right triangle button do in a Jupyter notebook?
- Run current cell only
- Run all cells
- Restart the kernel and run all cells ✓
*The double right triangle button restarts the Python kernel and runs all cells in the Jupyter notebook. Restarting the kernel ensures that all code runs from top to bottom.*

**3.** What does the + button do in a Jupyter notebook?
- Add a new cell directly below the current cell ✓
- Add a new cell at the end of the notebook
- Create a new notebook
*The plus button adds a new cell directly below the current or active cell. Adding a new cell is useful for splitting code cells into smaller chunks, or adding text explanations within the notebook.*

### LAB ACTIVITY: Getting started with Jupyter notebooks.

The Jupyter notebook loads the miles per gallon dataset and creates a scatter plot of miles per gallon against weight and engine size (number of cylinders) for each car. The notebook also calculates summary statistics for weight.

-  Click the double right arrow icon to restart the kernel and run all cells. 
-  Examine the code and text below. 
-  Add a new heading and text inside the first text cell.
-  Copy code cell `In[3]`. In the new cell, change the `"weight"` feature to `"horsepower"`.
-  Click "File", then "Download as". Download the Jupyter notebook as a notebook or HTML file.

Skip to main content

zyBooks
My library >
CS 2520: Python for Programmers home >
15.4: Intro to Jupyter Notebooks
zyBooks catalog
Help/FAQ
Casey Wong
You have unverified email(s). Use My Profile to send another verification email.


15.3 Introduction to Python for data science
15.4 Introduction to Jupyter Notebooks
Jupyter
Jupyter is an interactive development environment (IDE) for writing and testing code in data science and scientific computing. In Jupyter, code is written in an interactive document called a Jupyter notebook. A notebook contains cells, which organize code, text, and output all in one place for testing, presenting, and sharing. The three types of cells are code cells, markdown (text) cells, and raw (output) cells. Each cell can be run independently.

participation activity
15.4.1: Jupyter notebooks.


1

2

3

4

Running the code generates a scatter plot in a raw cell below the code cell. Raw cells contain output and are labeled with "Out" and the matching code cell number. Ex: Out[1]
Markdown cellCode cellRaw cell
Step 1: A screenshot of the Jupyter notebook interface appears. The notebook interface has a markdown cell with the text "What is the relationship between a car's weight and miles per gallon?", then a code cell. Step 2: The first code cell contains the Python program: from seaborn import scatterplot, load_dataset car_data = load_dataset('mpg') scatterplot(data=car_data, x='weight', y='mpg') Step 3: The "Run" button is highlighted on the menu bar. Step 4: The scatter plot appears in a raw cell labeled Out[1] below the code cell.

Captions
Jupyter notebooks have code cells, markdown cells, and raw cells. This notebook's first cell is a markdown cell: "What is the relationship... ?" Markdown cells are not labeled.
Code cells are numbered and labeled with "In". Ex: Code cell In[1] contains code to load the dataset and produce a scatter plot.
Clicking the "Run" button executes Python functions contained in a single code cell.
Running the code generates a scatter plot in a raw cell below the code cell. Raw cells contain output and are labeled with "Out" and the matching code cell number. Ex: Out[1]
Playing step 4: Running the code generates a scatter plot in a raw cell below the code cell. Raw cells contain output and are labeled with "Out" and the matching code cell number. Ex: Out[1] Step finished playing

Feedback?
participation activity
15.4.2: Jupyter notebook.
1)
Small segments of code and output in Jupyter notebooks are called _____.
2)
The Run button executes ________ contained in a Jupyter notebook.
3)
Jupyter can be used to write and execute code in _________.

Feedback?
Using Jupyter notebooks
Jupyter notebooks are used throughout this zyBook to illustrate data science applications. For information about installing and using Jupyter Notebook on a personal computer, check out the Jupyter installation guide.

Note: Sample notebooks contain code to run a short analysis and can be modified to test new parameter values or different modeling functions. Clicking the "File" menu and "Download as" saves a notebook into a local working directory to save progress.

participation activity
15.4.3: Jupyter menu icons.

Start
New code cellRearrange code cellsRestart kernelCopyRun current cellRestart kernel
and run all cellsChange cell typePaste
Step 1: The Jupyter notebook menu bar appears. Step 2-7: Arrows appear pointing to each button on the menu bar.

Captions

Feedback?
participation activity
15.4.4: Jupyter notebooks in the zyBook.
1)
Which is a selectable type of cell in the menu bar?
2)
What does the double right triangle button do in a Jupyter notebook?
3)
What does the + button do in a Jupyter notebook?

Feedback?
Try 15.4.1: Getting started with Jupyter notebooks.

Full screen
The Jupyter notebook loads the miles per gallon dataset and creates a scatter plot of miles per gallon against weight and engine size (number of cylinders) for each car. The notebook also calculates summary statistics for weight.

Click the double right arrow icon to restart the kernel and run all cells.
Examine the code and text below.
Add a new heading and text inside the first text cell.
Copy code cell In[3]. In the new cell, change the "weight" feature to "horsepower".
Click "File", then "Download as". Download the Jupyter notebook as a notebook or HTML file.


Feedback?
How was this section?

|


Provide section feedback
15.5 NumPy
'''
##############################################################################
####################################################Participation activity 15.4.2: Jupyter notebook.
with "myfile.txt":
    '''
    1)small segments of code and output in Jupyter notebooks are called _____.
        -cells. each cell should contain a small segment of code or output, with a specific purpose. ex: creating a scatter plot and fitting a model are often done in separate cells.
    2)the run button executes ________ contained in a Jupyter notebook.
        -selected code. the run button executes code only from one cell at a time. the restart and run all button executes all code after restarting the kernel.
    3)Jupyter can be used to write and execute code in _________.
        -multiple languages. Jupyter was originally developed to support three programming languages: Julia, Python, and R. together, these three programming languages inspired the name: Ju (Julia) + pyt (Python) + er (R). today, Jupyter supports over 100 programming languages.
    '''
####################################################Participation activity 15.4.4: Jupyter notebooks in the zyBook.

# INFO()
