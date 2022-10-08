# project2_VioletPang

This is the repo for Violet's project 2: Build a Bash command-line tool that performs a useful data preparation task 

This project included below features: <br>
5 useful command in python file: 
bash CLI for loading and showing basic information of McDonald's nutrition datasets

In the main.py, it contains six useful commands: loaddata, fetchlist, sortbycalories, seemax, numofitems, seebreakfast <br>
loaddata - Load dataset <br>
fetchlist - fetch items list <br>
sortbycalories - return sorted list by calories<br>
seemax - See max value of each dataset <br>
numofitems - See Number of Menu Items for each Food Category <br>
seebreakfast - See List of Breakfast Items <br>

In process_data.sh, it contains the bash script for preparing the menu.csv for processing. By running bash process_data.sh menu.csv > text.txt, <br>
we can learn the basic information such as number of columns, categories, the items in descending order of calories in McDonald's menu. 

## Getting Started

Plese build up the virtual environment for python to run this project in your own codespace 

### Prerequisites
python, bash


## Running the bash command-line tool
bash process_data.sh menu.csv > text.txt

## Running the python command
python main.py --help
python main.py loaddata
python main.py fetchlist
python main.py sortbycalories
python main.py seemax
python main.py numofitems
python main.py seebreakfast



## Deployment
To deploy this project, please open it with codespace 

## Authors
Violet Pang


## Acknowledgments
The knowledge for making this project is gained from Prof. Noah Gift's lecture.
