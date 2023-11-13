# quorum_test


## Quorum tasks:


### 1. Discuss your solution’s time complexity. What tradeoffs did you make?

I chose to use pandas since I used to work with data and this is the tool I’m more familiar with. The main challenge was related to merging and organizing data. For larger data frames, it would be a bigger challenge for sure. 

For tradeoffs, I decided to write a more readable code instead of focusing on performance (that’s why I also used Jupyter notebooks).

### 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

Since we’re using pandas, the solution is very flexible, easy to maintain and to adapt, we could easily add those columns to the dataframe;

To access the new columns data: alpha_df[“bill voted on date”] and beta_df[“co-sponsors”];


For the case of processing new columns, we could either extend the existing functions or write new ones to handle specific logic related to these columns.

### 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

Another reason why I used pandas is that it is really easy to maintain, even if the data input format changes, say from CSVs to something else,  we could just modify the data loading section of the script. Once the data is stored on the data frame, we can easily manipulate it, so the core data processing logic would probably remain untouched (assuming the columns and their meanings didn’t change).

### 4. How long did you spend working on the assignment?

As always, I like to break the problem into small and easily manageable pieces, so I started by reading a few times to make sure I understood what was required and planning the solution, then coding, searching, debugging and testing. This whole task took around 1 hour.

***


## How to use:

### 0. Prerequisites

  Install Git: Ensure Git is installed on your computer. If not, download and install it from [Git's website](https://git-scm.com/).

  Install Python: This project likely requires Python. Download and install Python from [Python's official website](https://www.python.org/downloads/).

  Install Visual Studio Code (VSCode): While not strictly necessary, VSCode is a popular IDE for Python development. Download and install it from [Visual Studio Code's website](https://code.visualstudio.com/).

### 1. Clone the repository using git:
  Run the command: ```git clone https://github.com/kevcap/quorum_test.git```

### 2. Navigate to the Project Directory:
  In the terminal, change directory to the project folder:
  ```cd quorum_test```

### 3. Working with the Project
  3.1. Open VSCode.
  3.2. Choose 'Open Folder' and select the quorum_test folder.
  3.3. Now you just have to open any of the two .ipynb files and run the code by clicking on the "Play" button ▶️ of each block; For reference, please check the video below:
   
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/h1sAzPojKMg/0.jpg)](https://www.youtube.com/watch?v=h1sAzPojKMg)

[Official documentation of vscode<>jupyter](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
