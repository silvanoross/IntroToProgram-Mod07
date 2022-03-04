Name: Silvano Ross
Date: March 04, 2022
Course: IT FDN 110A
GitHub: https://github.com/silvanoross/IntroToProg-Python-Mod07/edit/main/Assignment07Webpage.md

# Assignment 07 - The Pickling Exception

## Introduction: 
This week we are officially on our own. Our job is to demonstrate how pickling and structured error-handling work in python. So far we have used relatively in-efficient forms of storing and accessing data. Through pickling data we are better able to utilize a computer’s memory when reading and writing data. Further, we have only been relying on the built-in error handling that comes with python. Through structured error handling we can create more custom notes for specific kinds of errors to better explain to a user what may have gone wrong. 

## PICKLING - Just Like Pickles
The term pickling in python holds a meaning that is in fact quite close to the same term used in food storage. Much like how one pickles items to preserve them for later use (also somewhat altering the shape and flavor of the item), pickling in python refers to storing data in a different form from its original for later use. Pickling requires that information be stored in binary files rather than text files or other formats. This creates files that better utilize a computer’s working memory.  

This week I decided to turn the code from Assignment 06 that wrote text files into code that did something similar, but wrote pickled binary files instead. This involved a big work-around of many of the variable names and a few of the user-defined functions. Ultimately I was able to successfully re-create the program to write user-inputted data to a binary file. The only trouble I had was getting the program to read from a binary file and store the data into a successful working format. 

![Figure1.1](https://github.com/silvanoross/IntroToProg-Python-Mod07/blob/main/1.1.PNG)
