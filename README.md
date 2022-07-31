# name-generator
This is a project similar to my [previous](https://github.com/santitomatis/rememberable-password-generator) (just a password generator) but instead of a password now generates a name that could hypothetically be used to create a bot's name maybe for a videogame or similar.

## Disclaimer
**Please be aware that as [mentioned later on](https://github.com/santitomatis/name-generator#what-i-learned), this is just a project made to help me learn some python, even doe it does work, it could have some mistakes and also it may be noticeable *specially if you generate a lot of names* that a many of the names have the same start-finish pattern**

## Demo
When you run this script you are going to be asked wether you like to configure advanced settings or just go by default

```
Welcome to Bot Name Generator Project
Do you want to do some advanced configuration? Just type y/n (yes or no)
```

If you type n, a random bot name is going to be generated for you

```
Do you want to do some advanced configuration? Just type y/n (yes or no) n
Your bot name is:
xXMacazagaHelenaXx
```

In the other hand if you type y, the amount of names generated and language among other details are going to be custom

```
Do you want to do some advanced configuration? Just type y/n (yes or no) y
From which country do you want your name to be? (type mx for Mexico or us for United States)us
Do you want your name to be more credible or more likely to be available (for registration in 3rd party apps)? | (type cr for credible and av for available)cr
How many bot names do you want to generate? (just type an int number (eg: 5))10
Do you want to generate names with a separator between them? (type y for yes and n for no)n
Your bots names are:
HamlinCrystallynn
TheSENTINELLAJACKALYN45
xXSaidiLasandraXx
XxSnearlyVernonxX
Kyrstenpro
TheHELMINKMAYUR
TheKush
MednickAminda
Thechiante
TheMyrckLetecia51
```
> In this demo we are asking the script to generate 10 names based on United States common names lists, that are credible and don't have a separator between them

### Explaining costumization settings
- From which country do you want your name to be? ***Makes the names generated to pick names, surnames and nouns from a certain language***
- Do you want your name to be more credible or more likely to be available (for registration in 3rd party apps)? ***The names generated can be more "realistic" or if you want to, more likely to be available for registration, the second option adds a number at the end of the name and makes it overall longer***
- How many bot names do you want to generate? ***pretty straightforward, allows you to generate more than 1 bot name with the same config at once***
- Do you want to generate names with a separator between them? ***Adds a ----- between every name, making it more readable***

*That's pretty much all there is to its functionality*

## What I learned
I've learned a lot with this project, *mostly basic things but those things had to be learn a way or another*

- Correct some mistakes using pandas to convert .txt files to arrays
- Use of docstrings to document functions
- Functions of the random module
- Use random functions to bias probabilities (in a very basic way, I'm sure that there are better practices for this)
- Using .split() to manipulate strings
- print statement to debug

There are also some things I already knew but this project gave me a deeper understanding
- pandas (conversion of .txt file into array)
- git and github 
- markdown language (to write this readme)

To build this I used two Platzi's courses: [Basic python](https://platzi.com/cursos/python/) and [Introduction to computational thinking with python](https://platzi.com/cursos/python-cs/) and of course my own research

![certificadoCursoBasicoPython](https://user-images.githubusercontent.com/86212669/182045981-08d77f7e-2847-4f82-8ef6-d2f4609e0e0d.png)

![diplomaPensamientoCompPython](https://user-images.githubusercontent.com/86212669/182046012-a1d4ad9d-033a-400d-94aa-5f55854e87c5.png)


