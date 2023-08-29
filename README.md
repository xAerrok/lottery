# lottery

The lottery is in the opinion of this developer, a game for people who are bad at math. That doesn't mean it can't be a little fun to question the randomness of a process involving physical ping pong balls getting flopped around an airflow machine, right? 

## ticketer.py
- Reads your top14.csv file (Note, this is just the numbers 1-14, so you want to use the other programs to build your own heuristic or statistical indicators that could actually be useful.)
- Gives you 40 sets of numbers to play based on the aprioris

## megaball.py
- A simple example of occurence count from a set of numbers
- Those numbers are hard coded into the program

## megamillions-from-apriori.py
- Reads `megamillions.csv`, which is a listing through July, 2023 of the historic occurence of balls. 
- Outputs each ball number's occurrence rate from 2002-July, 2023. Take note that balls 57-75 were added at some point, so their 21 year historical probabilities are heavily skewed low if you examine the entire dataset. 
- One image pops up for the first ball number, then
- It generates a trend graph for each ball number
- It generates a poor, useless set of graphs of the most common ball numbers by week/month/quarter/year. This needs some work

# Installation
1. Have python3 installed with devtools, usually some version of python3-full is the package name for each operating system. 
2. `git clone https://github.com/angrynarwhal/lottery` 
3. `cd lottery`
4. `python3 -m venv ../../virtualenvs/lottery`
5. `source ../../virtualenvs/lottery/bin/activate`
6. `pip install -r requirements.txt`
7. `python <program name>` to run!

# Future execution requires fewer steps
1. Go to the root of your repository clone/fork directory
2. `source ../../virtualenvs/lottery/bin/activate`
3. `pip install -r requirements.txt`
4. `python <program name>` to run!

# Data
Data used in this toy program were obtained from : https://catalog.data.gov/dataset/lottery-mega-millions-winning-numbers-beginning-2002 

There are other datasets for the various lotteries and other, perhaps more useful questions, available at https://data.gov This is a link to a search for winning numbers I performed on the site in August, 2023: https://catalog.data.gov/dataset/?tags=winning

Copyright 2023, Sean P. Goggins