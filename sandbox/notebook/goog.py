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
with "myfile.txt":
    '''
    1)which is a selectable type of cell in the menu bar?
        -markdown. a markdown cell contains descriptive text that can be formatted. the three types of cells are labeled code, markdown, and raw.
    2)what does the double right triangle button do in a Jupyter notebook?
        -restart the kernel and run all cells. the double right triangle button restarts the Python kernel and runs all cells in the Jupyter notebook. restarting the kernel ensures that all code runs from top to bottom.
    3)what does the + button do in a Jupyter notebook?
        -add a new cell directly below the current cell. the plus button adds a new cell
        directly below the current or active cell. adding a new cell is useful for splitting code cells into smaller chunks, or adding text explanations within the notebook.
    '''
####################################################Try 15.4.1: Getting started with Jupyter notebooks.
with _:
    with "myfile.txt" as f:
        '''
        the Jupyter notebook loads the miles per gallon dataset and creates a scatter plot of miles per gallon against weight and engine size (number of cylinders) for each car. the notebook also calculates summary statistics for weight.
        
        - click the double right arrow icon to restart the kernel and run all cells. 
        - examine the code and text below. 
        - add a new heading and text inside the first text cell.
        - copy code cell `In[3]`. in the new cell, change the `"weight"` feature to `"horsepower"`.
        - click "file", then "download as". download the Jupyter notebook as a notebook or HTML file.
        '''
    with "myfile.md" as f:
        '''
        the Jupyter notebook loads the miles per gallon dataset and creates a scatter plot of miles per gallon against weight and engine size (number of cylinders) for each car. the notebook also calculates summary statistics for weight.
        
        - click the double right arrow icon to restart the kernel and run all cells. 
        - examine the code and text below. 
        - add a new heading and text inside the first text cell.
        - copy code cell `In[3]`. in the new cell, change the `"weight"` feature to `"horsepower"`.
        - click "file", then "download as". download the Jupyter notebook as a notebook or HTML file.
        '''
    with bash:
        # cat myfile.txt
        cat First\ Jupyter\ notebook.ipynb | head -n 10
        # out: {
        # out:  "cells": [
        # out:   {
        # out:    "cell_type": "markdown",
        # out:    "id": "c175a6bd",
        # out:    "metadata": {},
        # out:    "source": [
        # out:     "# This is a heading\n",
        # out:     "\n",
        # out:     "This is a text cell. Data scientists use text cells in a Jupyter notebook to write comments about a dataset or notes about  findings. Double click this Markdown cell to change the text, and click Run to format the text.\n",
        #cat First\ Jupyter\ notebook.ipynb
        
        #waht now?
    with _:
        print("You've completed sections 15.1-15.4 of the data science course!")
        # out: You've completed sections 15.1-15.4 of the data science course!
        print("\nNext steps:")
        # out: 
        # out: Next steps:
        print("1. Continue to section 15.5: NumPy - learn array operations")
        # out: 1. Continue to section 15.5: NumPy - learn array operations
        print("2. Practice with pandas DataFrames for data manipulation")
        # out: 2. Practice with pandas DataFrames for data manipulation
        print("3. Build a small data analysis project combining these concepts")
        # out: 3. Build a small data analysis project combining these concepts
        print("\nYes, it's worth it! Data science skills are in high demand.")
        # out: 
        # out: Yes, it's worth it! Data science skills are in high demand.
##############################################################################
'''## 15.5 NumPy

### Introduction to NumPy

The NumPy (pronounced "Num-pie") package provides tools for mathematical computations in Python. Ex: NumPy includes functions to perform common linear algebra operations, fast fourier transforms, and statistics. NumPy is used frequently in data science and statistical analysis. NumPy is also frequently used with other data science packages, such as pandas and Matplotlib. NumPy can be downloaded and installed from
https://numpy.org/install/.

NumPy provides a multidimensional array object, conceptually similar to a list, consisting of an ordered set of elements of the same type. NumPy arrays benefit from having more mathematical support than lists and also perform mathematical operations faster than lists, because a NumPy array is a wrapper around fast native code that is compiled to run on a specific processor instead of in the Python interpreter. 

To use NumPy in a program, the package is often imported with the alias `np`.

> **Summing arrays vs summing lists.**
> ```python
> import numpy as np
> 
> list1 = [15.5, 25.11, 19.0]
> list2 = [12.2, 1.3, 6.38] 
> 
> # Create two 1-dimensional (1D) arrays
> # with the elements of the above lists
> array1 = np.array(list1)
> array2 = np.array(list2)
> 
> # Concatenate two lists
> print("Concatenation of list1 and list2 =", end=" ")
> print(list1 + list2)
> print()
> 
> # Sum two lists
> print("Sum of list1 and list2 =", end=" ")
> for i in range(len(list1)):
>     print(list1[i] + list2[i], end=" ")  
> print("\n")
> 
> # Sum two 1D arrays
> print("Sum of array1 and array2 =", end=" ")
> print(array1 + array2)
> ```
> ```
> Concatenation of list1 and list2 = [15.5, 25.11, 19.0, 12.2, 1.3, 6.38]
> 
> Sum of list1 and list2 = 27.7 26.41 25.38 
> 
> Sum of array1 and array2 = [27.7  26.41 25.38]
> ```

### PARTICIPATION ACTIVITY: NumPy.

**1.** What is a benefit of using NumPy over list operations?
- Faster mathematical operations ✓
- More built-in list functions
- Easier access of array elements
*NumPy has more support for math operations and is able to complete math operations much faster than performing similar operations with lists. In the above example, multiple constructs and operations (a for loop, range() function, len() function, access operations) are used to sum 2 lists, whereas 2 NumPy arrays are just added together to achieve the same result.*

**2.** What operation is not done with NumPy?
- Array subtraction
- List concatenation ✓
- Array multiplication
*NumPy's primary object is an array, not a list. NumPy is used for mathematical computations, whereas list concatenation can be done in Python without NumPy.*

**3.** ```
import numpy as np
```

Which term is an alias?
- numpy
- as
- np ✓
*"np" is the common alias term used when importing NumPy. The alias term is defined by the programmer and can be any term of the programmer's choosing.*

**4.** NumPy is often used for which field?
- Statistical analysis ✓
- Mobile application development
- Web programming
*Statistical analysis requires complex mathematical computations, which is why NumPy's mathematical operations are often used.*

### NumPy arrays

The NumPy array data type is called ndarray, where "nd" stands for N-dimensional and N can be any number of dimensions.

 
- A zero-dimensional array consists of a scalar object. Ex: 2.
- A one-dimensional array consists of a container of scalars. Ex: [2, 4, 6, 8].
- A two-dimensional array consists of a container of containers of scalars. 2D arrays have rows and columns. Ex: [ [2, 4, 6, 8], [12, 14, 16, 18] ], which appears as

```
[[2 4 6 8]
 [12 14 16 18]]
```

when output to the screen.

An N-dimensional array has N levels of nested containers. At each level, all containers must have the same number of elements. The shape of an array is a tuple of the lengths of each of the array's dimensions. The size of an array is the total number of elements in an array. Ex: The shape of the 2D array [ [2, 4, 6, 8], [12, 14, 16, 18] ] is (2, 4) and the size of the array is 8.

An array is created using NumPy's array() function.

### LAB ACTIVITY: Array shape and size attributes.

Click Run to execute the code and see the shape and size of the array. Modify the array and click Run to see the modified shape and size.

### PARTICIPATION ACTIVITY: Array shape.

### Array axes

A NumPy array axis is a direction along each array dimension. 1D arrays have 1 axis, 2D arrays have 2 axes, etc. Discussion of axes occurs most frequently when dealing with 2D arrays. In a 2D array, axis 0 is the first axis that runs down the array's rows and axis 1 is the second axis that runs across the array's columns.

Many NumPy functions and methods take an axis argument which determines along which axis the function should operate.

### PARTICIPATION ACTIVITY: Array axes.

Step 1: Caption: In a 2D array, axis 0 indicates the direction along the array's rows and axis 1 indicates the direction along the array's columns. 
Animation: Displays a 2-dimensional array with 4 rows and 3 columns. The array values are: 
row 0, col 0: 12
row 0, col 1: 57
row 0, col 2: 89
row 1, col 0: 94
row 1, col 1: 23
row 1, col 2: 68
row 2, col 0: 72
row 2, col 1: 10
row 2, col 2: 45
row 3, col 0: 26
row 3, col 1: 41
row 3, col 2: 32
An arrow runs vertically from row 0 to row 3 with the label "axis 0". An arrow runs horizontally from column 0 to column 2 with the label "axis 1". 

Step 2: Caption: Many NumPy array functions and methods, such as numpy.delete() and ndarray.sort(), take an axis argument to indicate which axis to work along.
Animation: Two function calls appear: np.delete(ndarray, obj=1, axis=1) and ndarray.sort(axis=0).

Step 3: Caption: The delete() function removes the row (axis 0) or column (axis 1) indicated by the index. When index is 1 and axis is 1, the second column is removed. The returned array has a (4, 2) shape.
Animation: A copy of the original array is made and moves to be under the np.delete(ndarray, obj=1, axis=1) function call. A red strikeout line is placed over the second column of the copied array and then the second column is deleted. The new array has 4 rows and 2 columns with the following values:
row 0, col 0: 12
row 0, col 1: 89
row 1, col 0: 94
row 1, col 1: 68
row 2, col 0: 72
row 2, col 1: 45
row 3, col 0: 26
row 3, col 1: 32

Step 4: Caption: The array sort() method can take an axis argument to indicate which axis to sort along. If axis is 0, sorting happens ascending order in each column downwards along the rows.
Animation: A copy of the original array is made and moves to be under the ndarray.sort(axis=0) function call. Each column of the copied array is sorted in ascending order. The new array has 4 rows and 3 columns with the following values:
row 0, col 0: 12
row 0, col 1: 10
row 0, col 2: 32
row 1, col 0: 26
row 1, col 1: 23
row 1, col 2: 45
row 2, col 0: 72
row 2, col 1: 41
row 2, col 2: 68
row 3, col 0: 94
row 3, col 1: 57
row 3, col 2: 89

### PARTICIPATION ACTIVITY: Array axes.

**1.** How many axes does a 3D array have?
- 1
- 2
- 3 ✓
*An array has an axis for each dimension.*

**2.** In a 2D array, which axis is the second or last axis?
- 0
- 1 ✓
*The axes are counted like indexes, so the second or last axis of a 2D array is axis 1.*

**3.** In a 2D array, the 0 axis runs along the array's _____.
- rows ✓
- columns
*The 0 axis indicates the direction along the array's rows.*

### Creating and modifying arrays

A NumPy array is an ordered, indexed, and mutable container. NumPy provides many functions to create and modify arrays. Though mutable, NumPy arrays have a fixed shape, so any operation to change an array's shape actually creates a new version (a new Python object) of the array with the intended modification, leaving the original unchanged.

If the elements in the array are unknown before creation, certain NumPy functions create placeholder values that can be changed during a program's run. Ex: `np.zeros((1, 3))` creates a (1, 3) shape array filled with 0s and `np.ones((1, 3))` creates a (1, 3) shape array filled with 1s.

Some NumPy operations are instance methods of the object, Ex: array.sort(), while other NumPy operations are functions of the NumPy module, Ex: np.delete(). This material takes an object-oriented approach and uses array methods. NumPy functions are used where array methods don't exist.

> **Array functions.**
> | Function/Method | Description | Example |
> | --- | --- | --- |
> | array(object) | Returns an ndarray based on a given object, like a list. | # Creates a 1D (4,) array based off of a list array1D = np.array([1, 2, 3, 4])  # Creates a 2D (2, 2) array based off of 2 lists array2D = np.array([ [1, 2], [3, 4] ]) |
> | zeros(arrShape) ones(arrayShape) full(arrayShape, value) | Returns an ndarray of a specified shape filled with zeros, ones, or a specified value. | # Creates a 2D (2, 2) array filled with 6s # [ [6, 6], [6, 6] ] array_6fill = np.full((2, 2), 6) |
> | array[row_index, col_index] | Returns the element located at indices [row_index, col_index]. | array2D = np.array([ [1, 2], [3, 4] ])  # Returns 3: Element located at second row (index 1), first column (index 0) elem_1_0 = array2D[1, 0] |
> | delete(ndarray, obj, axis) | Returns a new ndarray with a row or column deleted from the given ndarray. Deletes the row or column indicated by obj. If axis = 0, delete row. If axis = 1, delete column. | array2D = np.array([ [1, 2], [3, 4] ])  # Returns a new 1D (1x2) array with the second row (obj 1, axis 0) ([3,4]) removed # [1, 2] new_a1D = np.delete(array2D, 1, axis=0) |
> | ndarray.sort(axis) | Sorts an ndarray in place in ascending order along an axis. If axis=None, the array is flattened into a 1D array, and then sorted. If no argument is passed, sorting occurs along the last axis (axis 1 for a 2D array). | my_array = np.array([2, 4, 1, 3])  # Sorts a 1D array in place # [1, 2, 3, 4] my_array.sort() |
> | ndarray.ravel() | Returns a flattened (1D) version of the given ndarray. | array_7 = np.array([ [7, 7], [7, 7] ])  # Returns a new flattened 1D (4,) version of a 2D (2, 2) array # [7, 7, 7, 7] array_7flat = array_7.ravel() |
> | ndarray.reshape(new_shape) | Returns a new ndarray containing the elements of the given ndarray with a new shape. | array1D = np.array([1, 2, 3, 4])  # Returns a new reshaped 2D (2, 2) version of a 1D (4,) array # [ [1, 2], [3, 4] ] a_reshaped = array1D.reshape((2,2)) |
> | ndarray.transpose() | Returns the transpose of an ndarray. | # Returns a new transposed version of a_reshaped # [[1, 3], [2, 4]] array1_transposed = a_reshaped.transpose() |

### PARTICIPATION ACTIVITY: Array functions.

**1.**
```
my_array2 = np.______(my_array, 1, axis=0)
print(my_array2)
```
Answer: delete
*Hint: `d____e`*
*The delete() function returns a new version of a given array with a specified row or column deleted. `axis=0` indicates a row is deleted, and the second argument, 1, indicates that the deleted row is at index 1 (the second row).*

**2.**
```
my_array2 = np._____(my_array)
print(my_array2)
```
Answer: ravel
*Hint: The array is flattened from a 2D array to a 1D array.*
*The ravel() function returns a flattened version of the given array, meaning all elements appear in a single row.*

**3.**
```
my_array._____(axis=0)
print(my_array)
```
Answer: sort
*Hint: Each column is in ascending order.*
*The sort() method sorts an array in place (in ascending order) along an axis. When sorting a 2D array, if axis=0, each column is sorted along the direction of the rows.*

**4.**
```
my_array.sort(axis=____)
print(my_array)
```
Answer: 1 or -1
*Hint: Each row is in ascending order.*
*When sorting a 2D array, if axis=1, each row is sorted along the direction of the columns. For each row of the array, each character in the first column was already a lesser value than the character in the second column, so sorting along axis 1 did not change the original array.*

### Mathematical operations

The NumPy package contains many mathematical operations and functions to be performed on arrays. Mathematical operations between arrays are performed between the matching elements of each array. Ex: [5 5 5] + [1 2 3] computes [5+1 5+2 5+3], or [6 7 8].

> **Math operators and functions.**
> | Expression | Description |
> | --- | --- |
> | array1 + array2 | Element-wise addition |
> | array1 - array2 | Element-wise subtraction |
> | array1 * array2 | Element-wise multiplication |
> | array1 / array2 | Element-wise division |
> | np.sqrt(array1) | Square root of array elements |
> | np.log(array1) | Logarithm of array elements |
> | np.sin(array1) | Sine of array elements |
> | np.max(array1) | Maximum of array elements |
> | np.median(array1) | Median of array elements |
> | np.std(array1) | Standard deviation of array elements |
> | np.var(array1) | Variance of array elements |
> | np.dot(array1, array2) | Dot product of   array1 and array2 |
> | np.matmul(array1, array2) | Also the dot product of array1 and array2 but with subtle differences from dot() when either array has dimension >= 3 |
> | np.cross(array1, array2) | Cross product of array1 and array2 |

> **Common NumPy math operations and functions.**
> ```python
> import numpy as np
> 
> array1 = np.array([10, 20, 30, 40])
> array2 = np.array([1, 2, 3, 4])
> 
> # Some common array operations
> 
> print("Adding arrays (array1 + array2)")
> print(array1 + array2)
> 
> print("\nSubtracting arrays (array1 - array2)")
> print(array1 - array2)
> 
> print("\nMultiplying arrays (array1 * array2)")
> print(array1 * array2)
> 
> print("\nCalculating dot product of arrays")
> print(np.dot(array1, array2))
> 
> print("\nFinding square root of each element in array1")
> print(np.sqrt(array1))
> 
> print("\nFinding minimum element in array1")
> print(array1.min())
> 
> print("\nFinding maximum element in array1")
> print(array1.max())
> ```
> ```
> Adding arrays (array1 + array2)
> [11 22 33 44]
> 
> Subtracting arrays (array1 - array2)
> [ 9 18 27 36]
> 
> Multiplying arrays (array1 * array2)
> [10  40  90 160]
> 
> Calculating dot product of arrays
> 300
> 
> Finding square root of each element in array1
> [3.16227766 4.47213595 5.47722558 6.32455532]
> 
> Finding minimum element in array1
> 10
> 
> Finding maximum element in array1
> 40
> ```

### PARTICIPATION ACTIVITY: Math operators and functions.

**1.** All NumPy mathematical functions can take a scalar argument.
Answer: **True**
*A scalar is a zero-dimensional array, so any function that takes an array argument can also take a scalar argument.*

**2.** Operators such as , and == can compare arrays.
Answer: **True**
*Like arithmetic operators, comparison operations are performed between the matching elements of each array. Ex:

```
array1 = numpy.array( [23, 68] )
array2 = numpy.array( [42, -5] )
array1 < array2
```

returns `[True, False]`*

**3.** The min() method returns a 1D array.
Answer: **False**
*ndarray's min() method returns the smallest value in an array, which is  a scalar, or a 0-dimensional array. Ex: 
```
my_array = np.array([12, 6, 2, 8])
print(my_array.min())
```

outputs array's minimum value, 2.*

### CHALLENGE ACTIVITY: Using NumPy. (5 Levels)

**Level 1:**

**Task:**
Create a 2-dimensional array containing the arrays [...].

**Explanation pattern:**
A 2-dimensional NumPy array is created using `np.array()`, where the argument is an array that contains multiple arrays of the same length.

**Code structure:**
```python
# Load the necessary package
import numpy as np

# Create an array
my_array =
# Your code goes here
# Print the array
print(my_array)
```

**Level 2:**

**Task:**
In [...], sort each [...] along the direction of the [...]s in ascending order.

**Explanation pattern:**
`[...].sort()` takes an axis argument that determines along which axis the array should be sorted. axis=[...] sorts each [...] along the direction of the [...]s.

**Code structure:**
```python
# Load necessary package
import numpy as np

# Create array
___ = np.array([___])

# Sort array
# Your code goes here
# Print the array
print(___)
```

**Level 3:**

**Task:**
Delete the [...] of [...].

**Explanation pattern:**
`np.delete()` takes in three positional arguments: array, index, and axis. axis=[...] indicates a [...] is deleted, and the second argument, [...], indicates that the deleted [...] is at index [...] (the [...]).

**Code structure:**
```python
# Load necessary package
import numpy as np

# Create array
___ = np.array([___])

# Delete the ___ ___ of array
___ =
# Your code goes here
# Print the array
print(___)
```

**Level 4:**

**Task:**
Flatten [...].

**Explanation pattern:**
`np.ravel()` returns a flattened (1D) version of the given array.

**Code structure:**
```python
# Load necessary package
import numpy as np

# Create array
___ = np.array([___])

# Flatten array
___ =
# Your code goes here
# Print the array
print(___)
```

**Level 5:**

**Task:**
Return the [...] of elements in [...].

**Explanation pattern:**
Simple functions can have an array or scalar argument, so finding the [...] of elements in [...] is done using `np.[...]([...])`.

**Code structure:**
```python
# Load necessary package
import numpy as np

# Create array
___ = np.array([___])

# Find ___ of array elements
___ =
# Your code goes here
# Print the array
print(___)
```

Exploring further:

-  NumPy documentation
- NumPy tutorial'''
'''Introduction to NumPy
The NumPy (pronounced "Num-pie") package provides tools for mathematical computations in Python. Ex: NumPy includes functions to perform common linear algebra operations, fast fourier transforms, and statistics. NumPy is used frequently in data science and statistical analysis. NumPy is also frequently used with other data science packages, such as pandas and Matplotlib. NumPy can be downloaded and installed from https://numpy.org/install/.

NumPy provides a multidimensional array object, conceptually similar to a list, consisting of an ordered set of elements of the same type. NumPy arrays benefit from having more mathematical support than lists and also perform mathematical operations faster than lists, because a NumPy array is a wrapper around fast native code that is compiled to run on a specific processor instead of in the Python interpreter.

To use NumPy in a program, the package is often imported with the alias np.

Figure 15.5.1: Summing arrays vs summing lists.
import numpy as np

list1 = [15.5, 25.11, 19.0]
list2 = [12.2, 1.3, 6.38] 

# Create two 1-dimensional (1D) arrays
# with the elements of the above lists
array1 = np.array(list1)
array2 = np.array(list2)

# Concatenate two lists
print("Concatenation of list1 and list2 =", end=" ")
print(list1 + list2)
print()

# Sum two lists
print("Sum of list1 and list2 =", end=" ")
for i in range(len(list1)):
    print(list1[i] + list2[i], end=" ")  
print("\n")

# Sum two 1D arrays
print("Sum of array1 and array2 =", end=" ")
print(array1 + array2)
Concatenation of list1 and list2 = [15.5, 25.11, 19.0, 12.2, 1.3, 6.38]

Sum of list1 and list2 = 27.7 26.41 25.38 

Sum of array1 and array2 = [27.7  26.41 25.38]

Feedback?
participation activity
15.5.1: NumPy.
1)
What is a benefit of using NumPy over list operations?
2)
What operation is not done with NumPy?
3)
import numpy as np
Which term is an alias?

4)
NumPy is often used for which field?

Feedback?
NumPy arrays
The NumPy array data type is called ndarray, where "nd" stands for N-dimensional and N can be any number of dimensions.

A zero-dimensional array consists of a scalar object. Ex: 2.
A one-dimensional array consists of a container of scalars. Ex: [2, 4, 6, 8].
A two-dimensional array consists of a container of containers of scalars. 2D arrays have rows and columns. Ex: [ [2, 4, 6, 8], [12, 14, 16, 18] ], which appears as
[[2 4 6 8]
 [12 14 16 18]]
when output to the screen.
An N-dimensional array has N levels of nested containers. At each level, all containers must have the same number of elements. The shape of an array is a tuple of the lengths of each of the array's dimensions. The size of an array is the total number of elements in an array. Ex: The shape of the 2D array [ [2, 4, 6, 8], [12, 14, 16, 18] ] is (2, 4) and the size of the array is 8.
An array is created using NumPy's array() function.

Try 15.5.1: Array shape and size attributes.

Full screen
Click Run to execute the code and see the shape and size of the array. Modify the array and click Run to see the modified shape and size.



Feedback?
participation activity
15.5.2: Array shape.
Match the shape to the array.

Select the definition that matches each term
How to use this tool
(4,)
(2, 2, 3)
(1,)
( )
invalid array
(2, 4)
(4, 2)
["a", "b", "c", "d"]
[ [ [1, 2, 9], [3, 2, 6] ], [ [8, 8, 4], [9, 8, 7] ] ]
[ [1, 2], [3, 4], [5, 6], [7, 8] ]
3.1415
[ [10, 20, 30, 40], [50, 60, 70] ]
[ [10, 20, 30, 40], [50, 60, 70, 80] ]
[3.1415]

Reset

Feedback?
Array axes
A NumPy array axis is a direction along each array dimension. 1D arrays have 1 axis, 2D arrays have 2 axes, etc. Discussion of axes occurs most frequently when dealing with 2D arrays. In a 2D array, axis 0 is the first axis that runs down the array's rows and axis 1 is the second axis that runs across the array's columns.

Many NumPy functions and methods take an axis argument which determines along which axis the function should operate.

participation activity
15.5.3: Array axes.

Start
row 0row 0row 0row 1row 2row 3row 1row 2row 3row 1row 2row 3col 0col 1col 2col 0col 1col 2col 0col 1col 22D Array(4, 3) shapeaxis 0axis 1np.delete(ndarray, obj=1, axis=1)ndarray.sort(axis=0)121212232323101010575757454545949494686868323232898989727272262626414141122672942341106845893257
Step 1: Caption: In a 2D array, axis 0 indicates the direction along the array's rows and axis 1 indicates the direction along the array's columns. Animation: Displays a 2-dimensional array with 4 rows and 3 columns. The array values are: row 0, col 0: 12 row 0, col 1: 57 row 0, col 2: 89 row 1, col 0: 94 row 1, col 1: 23 row 1, col 2: 68 row 2, col 0: 72 row 2, col 1: 10 row 2, col 2: 45 row 3, col 0: 26 row 3, col 1: 41 row 3, col 2: 32 An arrow runs vertically from row 0 to row 3 with the label "axis 0". An arrow runs horizontally from column 0 to column 2 with the label "axis 1". Step 2: Caption: Many NumPy array functions and methods, such as numpy.delete() and ndarray.sort(), take an axis argument to indicate which axis to work along. Animation: Two function calls appear: np.delete(ndarray, obj=1, axis=1) and ndarray.sort(axis=0). Step 3: Caption: The delete() function removes the row (axis 0) or column (axis 1) indicated by the index. When index is 1 and axis is 1, the second column is removed. The returned array has a (4, 2) shape. Animation: A copy of the original array is made and moves to be under the np.delete(ndarray, obj=1, axis=1) function call. A red strikeout line is placed over the second column of the copied array and then the second column is deleted. The new array has 4 rows and 2 columns with the following values: row 0, col 0: 12 row 0, col 1: 89 row 1, col 0: 94 row 1, col 1: 68 row 2, col 0: 72 row 2, col 1: 45 row 3, col 0: 26 row 3, col 1: 32 Step 4: Caption: The array sort() method can take an axis argument to indicate which axis to sort along. If axis is 0, sorting happens ascending order in each column downwards along the rows. Animation: A copy of the original array is made and moves to be under the ndarray.sort(axis=0) function call. Each column of the copied array is sorted in ascending order. The new array has 4 rows and 3 columns with the following values: row 0, col 0: 12 row 0, col 1: 10 row 0, col 2: 32 row 1, col 0: 26 row 1, col 1: 23 row 1, col 2: 45 row 2, col 0: 72 row 2, col 1: 41 row 2, col 2: 68 row 3, col 0: 94 row 3, col 1: 57 row 3, col 2: 89

Captions

Feedback?
participation activity
15.5.4: Array axes.
1)
How many axes does a 3D array have?
2)
In a 2D array, which axis is the second or last axis?
3)
In a 2D array, the 0 axis runs along the array's _____.

Feedback?
Creating and modifying arrays
A NumPy array is an ordered, indexed, and mutable container. NumPy provides many functions to create and modify arrays. Though mutable, NumPy arrays have a fixed shape, so any operation to change an array's shape actually creates a new version (a new Python object) of the array with the intended modification, leaving the original unchanged.

If the elements in the array are unknown before creation, certain NumPy functions create placeholder values that can be changed during a program's run. Ex: np.zeros((1, 3)) creates a (1, 3) shape array filled with 0s and np.ones((1, 3)) creates a (1, 3) shape array filled with 1s.

Some NumPy operations are instance methods of the object, Ex: array.sort(), while other NumPy operations are functions of the NumPy module, Ex: np.delete(). This material takes an object-oriented approach and uses array methods. NumPy functions are used where array methods don't exist.

Table 15.5.1: Array functions.
Function/Method	Description	Example
array(object)	Returns an ndarray based on a given object, like a list.	
# Creates a 1D (4,) array based off of a list
array1D = np.array([1, 2, 3, 4])

# Creates a 2D (2, 2) array based off of 2 lists
array2D = np.array([ [1, 2], [3, 4] ])
zeros(arrShape)
ones(arrayShape)
full(arrayShape, value)	Returns an ndarray of a specified shape filled with zeros, ones, or a specified value.	
# Creates a 2D (2, 2) array filled with 6s
# [ [6, 6], [6, 6] ]
array_6fill = np.full((2, 2), 6)
array[row_index, col_index]	Returns the element located at indices [row_index, col_index].	
array2D = np.array([ [1, 2], [3, 4] ])

# Returns 3: Element located at second row (index 1), first column (index 0)
elem_1_0 = array2D[1, 0]
delete(ndarray, obj, axis)	Returns a new ndarray with a row or column deleted from the given ndarray. Deletes the row or column indicated by obj. If axis = 0, delete row. If axis = 1, delete column.	
array2D = np.array([ [1, 2], [3, 4] ])

# Returns a new 1D (1x2) array with the second row (obj 1, axis 0) ([3,4]) removed
# [1, 2]
new_a1D = np.delete(array2D, 1, axis=0)
ndarray.sort(axis)	Sorts an ndarray in place in ascending order along an axis. If axis=None, the array is flattened into a 1D array, and then sorted. If no argument is passed, sorting occurs along the last axis (axis 1 for a 2D array).	
my_array = np.array([2, 4, 1, 3])

# Sorts a 1D array in place
# [1, 2, 3, 4]
my_array.sort()
ndarray.ravel()	Returns a flattened (1D) version of the given ndarray.	
array_7 = np.array([ [7, 7], [7, 7] ])

# Returns a new flattened 1D (4,) version of a 2D (2, 2) array
# [7, 7, 7, 7]
array_7flat = array_7.ravel()
ndarray.reshape(new_shape)	Returns a new ndarray containing the elements of the given ndarray with a new shape.	
array1D = np.array([1, 2, 3, 4])

# Returns a new reshaped 2D (2, 2) version of a 1D (4,) array
# [ [1, 2], [3, 4] ]
a_reshaped = array1D.reshape((2,2))
ndarray.transpose()	Returns the transpose of an ndarray.	
# Returns a new transposed version of a_reshaped
# [[1, 3], [2, 4]]
array1_transposed = a_reshaped.transpose()

Feedback?
participation activity
15.5.5: Array functions.
Given the initialized array and console output, fill in the blanks.

import numpy as np

my_array = np.array( [  ["c", "d"], ["e", "f"], ["a", "b"], ["g", "h"] ] )
print(my_array)

[["c" "d"]
 ["e" "f"]
 ["a" "b"]
 ["g" "h"]]


1)
my_array2 = np.______(my_array, 1, axis=0)
print(my_array2)

[["c" "d"]
 ["a" "b"]
 ["g" "h"]]

Check

Show answer
2)
my_array2 = np._____(my_array)
print(my_array2)

["c" "d" "e" "f" "a" "b" "g" "h"]

Check

Show answer
3)
my_array._____(axis=0)
print(my_array)

[["a" "b"]
 ["c" "d"]
 ["e" "f"]
 ["g" "h"]]

Check

Show answer
4)
my_array.sort(axis=____)
print(my_array)

[["c" "d"]
 ["e" "f"]
 ["a" "b"]
 ["g" "h"]]

Check

Show answer

Feedback?
Mathematical operations
The NumPy package contains many mathematical operations and functions to be performed on arrays. Mathematical operations between arrays are performed between the matching elements of each array. Ex: [5 5 5] + [1 2 3] computes [5+1 5+2 5+3], or [6 7 8].

Table 15.5.2: Math operators and functions.
Expression	Description
array1 + array2	Element-wise addition
array1 - array2	Element-wise subtraction
array1 * array2	Element-wise multiplication
array1 / array2	Element-wise division
np.sqrt(array1)	Square root of array elements
np.log(array1)	Logarithm of array elements
np.sin(array1)	Sine of array elements
np.max(array1)	Maximum of array elements
np.median(array1)	Median of array elements
np.std(array1)	Standard deviation of array elements
np.var(array1)	Variance of array elements
np.dot(array1, array2)	Dot product of array1 and array2
np.matmul(array1, array2)	Also the dot product of array1 and array2 but with subtle differences from dot() when either array has dimension >= 3
np.cross(array1, array2)	Cross product of array1 and array2

Feedback?
Figure 15.5.2: Common NumPy math operations and functions.
import numpy as np

array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Some common array operations

print("Adding arrays (array1 + array2)")
print(array1 + array2)

print("\nSubtracting arrays (array1 - array2)")
print(array1 - array2)

print("\nMultiplying arrays (array1 * array2)")
print(array1 * array2)

print("\nCalculating dot product of arrays")
print(np.dot(array1, array2))

print("\nFinding square root of each element in array1")
print(np.sqrt(array1))

print("\nFinding minimum element in array1")
print(array1.min())

print("\nFinding maximum element in array1")
print(array1.max())
Adding arrays (array1 + array2)
[11 22 33 44]

Subtracting arrays (array1 - array2)
[ 9 18 27 36]

Multiplying arrays (array1 * array2)
[10  40  90 160]

Calculating dot product of arrays
300

Finding square root of each element in array1
[3.16227766 4.47213595 5.47722558 6.32455532]

Finding minimum element in array1
10

Finding maximum element in array1
40

Feedback?
participation activity
15.5.6: Math operators and functions.
1)
All NumPy mathematical functions can take a scalar argument.
2)
Operators such as <, >, and == can compare arrays.
3)
The min() method returns a 1D array.

Feedback?
challenge activity
15.5.1: Using NumPy.
712910.5105864.qx3zqy7

Start
Create a 2-dimensional array containing the arrays [19, 7], [3, 16], [8, 12].

# Load the necessary package
import numpy as np

# Create an array
my_array =
 # Your code goes here


# Print the array
print(my_array)

1

2

3

4

5

Check

Next level
1
2
3
4
5

Feedback?
Exploring further:
NumPy documentation
NumPy tutorial
How was this section?

|


Provide section feedback
'''
####################################################Figure 15.5.1: Summing arrays vs summing lists.
with "main.py" as RUN:
    import numpy as np

    list1 = [15.5, 25.11, 19.0]
    list2 = [12.2, 1.3, 6.38] 

    # Create two 1-dimensional (1D) arrays
    # with the elements of the above lists
    array1 = np.array(list1)
    array2 = np.array(list2)

    # Concatenate two lists
    print("Concatenation of list1 and list2 =", end=" ")
    print(list1 + list2)
    print()

    # Sum two lists
    print("Sum of list1 and list2 =", end=" ")
    for i in range(len(list1)):
        print(list1[i] + list2[i], end=" ")  
    print("\n")

    # Sum two 1D arrays
    print("Sum of array1 and array2 =", end=" ")
    print(array1 + array2)  
    # out: Concatenation of list1 and list2 = [15.5, 25.11, 19.0, 12.2, 1.3, 6.38]
    # out: 
    # out: Sum of list1 and list2 = 27.7 26.41 25.38 
    # out: 
    # out: Sum of array1 and array2 = [27.7  26.41 25.38]
####################################################Participation activity 15.5.1: NumPy.
with "main.py" as RUN:
    

INFO()
# val: /workspaces/Python-Copy2/sandbox/files
# val: Wed May 13 04:00:45 UTC 2026
# val: ./myfile.txt
# val: ./.venv/pyvenv.cfg
# val: ./mycsv.csv
# val: ./main.py
# val: ./PA 15.3.1: Python for data science.txt
# val: ./myfile.py
# val: ./myfile.md
# val: ./First Jupyter notebook.ipynb
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
