# Color Detection Application
A python application through which you can automatically get the name and R,G,B values of a color in an image by clicking on the color with your mouse.


## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)
* [License](#license)
* [Contributing](#contributing)


## General info

Color detection is the process of identifying the name of any color.  Color detection is important in identifying objects. Various image editing and drawing apps also use it as a tool.

In this project, I built an application which accepts an image path and automatically get the name of the colors in the image when the user presses his/her left or right mouse buttons on them.
The application has a data file that contains the color name and its values, it then calculate the distance from each color and find the shortest one.



## Screenshots

 Running program
:-------------------------:

![cmd](https://user-images.githubusercontent.com/19711677/108757364-5e2e8b80-750f-11eb-957e-c301f5c6990d.PNG)


 Sample Output 1
:-------------------------:

![output1](https://user-images.githubusercontent.com/19711677/108757367-5ec72200-750f-11eb-8334-0012c77edf71.PNG)


 Sample Output 2
:-------------------------:

![output2](https://user-images.githubusercontent.com/19711677/108757383-64246c80-750f-11eb-9e52-0ec99e8d2cdf.PNG)

 Sample Output 3
:-------------------------:

![output3](https://user-images.githubusercontent.com/19711677/108757396-6686c680-750f-11eb-92f4-2604366ad84b.PNG)

 Sample Output 4
:-------------------------:

![output4](https://user-images.githubusercontent.com/19711677/108757386-65559980-750f-11eb-8c4a-15f1994e9259.PNG)


## Features

* Detect colors by clicking on the color in an image with your mouse
* Get color name
* Get RGB values of colors 


## Technologies
* [Python 3.8](https://www.python.org/)
* [Opencv-Python](https://opencv.org/)
* [Pandas](https://pandas.pydata.org/)
* [NumPy](https://numpy.org/)



## Setup

To run this app, you will need to follow these 4 steps:

#### 1. Requirements
  - a Laptop

  - Text Editor or IDE (eg. vscode, PyCharm)

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your Laptop.
  
  - Command line (CMD) 


#### 2. Install Python and Pipenv
  - [Python3](https://www.python.org/downloads/)
  

  - [Pipenv](https://pipenv-es.readthedocs.io/es/stable/)

#### 3. Local Setup and Running on Windows, Linux and Mac OS

  ```
  
  # Clone this repository into the directory of your choice
  $ git clone https://github.com/Williano/Color-Detection-Application.git

  # Move into project folder
  $ cd Color-Detection-Application

  # Install from Pipfile
  $ pipenv install

  # Activate the Pipenv shell
  $ pipenv shell

  # Create database tables
  (Color-Detection-Application-XXXX) $ python color_detector.py -i <add your image path here>
  
  Example: python src/color_detector.py -i images/pietro-de-grandi.jpg
  

  ```
  
  #### 4. Testing application
  
  - Click on any part of the image to get the color name and RGB value


## Status
Project is: _done_

## Inspiration
This project was for my multimedia class for my MSc. Computer Science degree.

## Contact
Created by [Williano](https://williano.github.io/) - feel free to contact me!

## License
>You can check out the full license [here](https://github.com/Williano/Color-Detection-Application/blob/main/LICENSE)

This project is licensed under the terms of the **MIT** license.

## Contributing

1. Fork it (<https://github.com/Williano/Color-Detection-Application.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
