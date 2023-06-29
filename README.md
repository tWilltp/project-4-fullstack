# Project 4 Full Stack Framework

* This site showcases an example of a website utilizing frontend and backend development, in the form of an online store selling makeup.
* This project is designed as a training excersize, to consolidate my knowledge of frontend, backend, libraries and frameworks in software development.  
[Project-4 view](https://project-4-fst.herokuapp.com/)

---

# Table of contents

- [UX](#UX)
   - [Site creator aim](#Site-creator-aim)
   - [User aim](#User-aim)
   - [Site structure](#Site-structure)
- [Technology](#Technology)
- [Testing](#Testing)
   - [Is the programme functional](#Is-the-programme-functional)
   - [Main Bugs and Fixes](#Main-Bugs-and-Fixes)
   - [Performance Testing](#Performance-Testing)
   - [Code Validation](#Code-Validation)
   - [Development Issues](#Development-Issues)
- [Deployment](#Deployment)
- [Credits](#Credits)

# UX

## Site Creator Aim

In this Project I aimed to display various products for a user to select, then provide the functionality for that user to leave reviews for their chosen project and in turn allow others to comment on eachothers reviews. providing a sufficient example of user interactivity with databses that I have created.

## User Aim

The User should have all the necessary functionality that would allow them to interact with a database (insert data, pull required data, edit data and delete data) presented to them in a consise, easy to understand manor. The user should also have the ability to pull a product from one database into another (basket) completeing the required e-commerce functionality.

## Site Structure

The Site consists of several pages displaying products, product reviews, products on individual pages as selected, reviews on individual pages as selected, the basket with checkout page, and a user authentification system that allows customers to sign up to the website and interact with it accordingly

## features

* 
*
*
*
*
*
*
*

---

# Technology

## Python

* The programming language I used to develop the code for this project.

## Git-hub

* The software hosting platform I used for this project.

## Git-pod

* The development hosting platform I used for this project. [link to gitpod workspace](https://twilltp-project3python-iy5rktxmppv.ws-eu96b.gitpod.io)

## Heroku

* The back end hosting platform used to deploy this app. [link to heroku dashboard](https://dashboard.heroku.com/apps/project-3-python)

---

# Testing

## Is the programme funtional

The progamme runs as I expect it to, with the information coming in an order that is easy to follow and gameplay that properly relates to the player, their position and options as they move through to the end.

## Main Bugs and Fixes

* Bug: due to the different ways the game can end, the relevant information was not accurately displayed.
* Fix: differnet endgame functions were created so after the different types of losses/wins the code was directed properly.

* Bug: the number of shots a player has left is always registered as 19.
* Fix: I used a global value since the local value was always reset with each shot meaning 20 would go down to 19 repeatedly.

* Bug: if the player hits a sunken enemy ship it is registered as 'shot missed'.
* Fix: I added a condition to the shots fired function so that if the player hits 'S' 'Area clear' is printed.

* Bug: if the computer hits an unnacceptable target e.g. '-', 'L', 'S' the board is printed and it guesses again instead of guessing again and printing the board with the acceptable target.
* Fix: I changed the structure of the computer shot function so that displayboard() was printed after the computer found an acceptable target.

## Performance Testing

The final tests I ran on my code were as follows:

Test | Desired result yes | Desired result no | Fail
---|---|---|---
can the player input the same coordinates twice | | X |
can the player fire on their own ships | | X |
can the computer fire on an unacceptable coordinate ('-','L','S') | | X |
can the player fire on the enemy ships | X | |
if the computer sinks all of the players ships, is the proper end game function called | X | |
if the player sinks all of the enemy ships, is the proper end game function called | X | |
if the player turns expire, is the proper end game function called | X | |
is the amount of shots taken for the player to win displayed at the end of the game | X | |

## Python Linter

The python code passes through the pep8 linter (version 22.3.1) installed in gitpod, with no significant issues. [link to gitpod workspace](https://twilltp-project3python-iy5rktxmppv.ws-eu96b.gitpod.io)

## Development Issues

The largest and most time consuming issue I encountered while developing the game was to clear the board of all previous ships and shots. I tried many different tactics in order to get through this problem such as: using multiple if statements to change every symbol on the board back to a blank area; employing a while loop to loop through every square on the board changing them individually; placing the variable that generated the board in many different positions so that it would be built anew in a comprehensible way for the flow of the code. Some variant of the last attempt was correct as I had to set the board fresh in a new function using a global variable, then call that function in each of the respective endGame() functions.

---

# Deployment

## Github Deployment

The website was delpoyed using GitHub. To do this I did the following;

* When on the websites GitHub repository, click on the settings tab
* Now on the settings page, on the left hand side of the page, click on the pages tab
* Under the Source section, click on the drop down menu titled Branch and select main
* The page is now published with a link available to use.

 Veiw repository: [Project-3-python](https://github.com/tWilltp/project-3-python)

## Creating a Fork or Copying

To clone/fork/copy the repository you click on the fork tab which is situated next to unwatch tab in the top right corner of the page

## Clone

To create a clone you do the following;

* Click on the code tab, left of the Gitpod tab
* To the right of the repository name, click the clipboard icon
* In the IED open GitBash
* Change the working directory to the location you prefer
* Add Git Clone with the copy of the repositroy name
* Clone has been created

## Repositroy deployment via Heroku

* On the https://dashboard.heroku.com/apps page, click New and then select Create New App from the drop-down menu.
* When the next page loads insert the App name and Choose a region. The click Create app
* In the settings tab click on Reveal Config Vars and add the key Port and the value 8000. There were no credentials required for this app.
* Below this click Add buildpack and choose python and nodejs in that order.

## Deployment of the app

* Click on the Deploy tab and select Github-Connect to Github.
* Enter the repository name and click Search.
* Choose the repository that holds the correct files and click Connect.
* A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub.
* Once the deployment method has been chosen the app will be built and can be launched by clicking the Open app button at the top of the page.

---

# Credits

These are the examples and resources I used as inspiration for my code and to better understand what mistakes where being made and how to rectify them.

* [Github battleships example](https://gist.github.com/w0300133/7f3e3e6f836e519f64272150ca34080c)
* [Pythondex battleship example](https://pythondex.com/python-battleship-game)
* [Stack overflow](https://stackoverflow.com/questions/36695039/python-battleships-game)