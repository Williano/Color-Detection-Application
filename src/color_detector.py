"""
    Script: Color Detector or Color blind helper
    Description: An application through which you can automatically get the name
                 and R,G,B values of a color in an image by
                 clicking on the color with your mouse.
    Programmers: William K. Kwabla, Furkan Dinc
"""

# Import libraries
import cv2
import numpy as np
import pandas as pd
import argparse

# Check for user mouse click event
clicked = False

# store red, green, green, x and y coordinates
red_color = green_color = blue_color = x_position = y_position = 0

# store uploaded image by user
global uploaded_image


def get_image_path_from_the_user() -> str:

    # Creates argument parser to take image path from command line and return the image path
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-i', '--image', required=True, help="Image Path")
    arguments = vars(argument_parser.parse_args())
    image_path = arguments['image']

    return image_path


def read_image_with_opencv(image_path) -> str:

    global uploaded_image

    # Reads uploaded image from the path giving to it by the user and returns it
    uploaded_image = cv2.imread(image_path)

    return uploaded_image


def get_color_dataset():

    # Column names for color dataset
    index =["color", "color_name", "hex", "RED", "GREEN", "BLUE"]

    # Reads the csv file containing the colors and gives names to each column
    color_dataset = pd.read_csv('color-dataset/colors.csv', names=index, header=None)

    # Return color dataset
    return color_dataset


# calculates minimum distance from all colors, get the most matching color and return it
def get_color_name(RED, GREEN, BLUE, color_dataset) -> str:

    # Minimum distance from a color
    minimum_distance = 10000

    # Iterates through the color dataset and gets the distance from all colors in the dataset
    for i in range( len(color_dataset) ):
        distance_from_all_colors = abs(RED - int(color_dataset.loc[i, "RED"])) + abs(GREEN - int(color_dataset.loc[i, "GREEN"])) + abs(BLUE - int(color_dataset.loc[i, "BLUE"]))

        # calculates minimum distance from all colors and get the most matching color
        if( distance_from_all_colors <= minimum_distance):
            minimum_distance = distance_from_all_colors
            color_name = color_dataset.loc[i, "color_name"]

    # Returns the color name
    return color_name


# Gets x,y coordinates of mouse left or right button click
def draw_function(event, x , y, flags, param) -> None:

    # Check if the user has clicked his mouse and get the x and y coordinates of the image
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:

        global blue_color, green_color, red_color, x_position, y_position, clicked

        # If there is a click event, extract the x and y coordinates
        clicked = True

        x_position = x

        y_position = y

        # Use the x,y coordinates of the mouse to extract the color the user clicked and store
        # it red, green and blue values
        blue_color, green_color, red_color = uploaded_image[y, x]

        # Convert the coordinates to integers and store them in the r,g,b variables to use for extracting of the color name
        blue_color = int(blue_color)

        green_color = int(green_color)

        red_color = int(red_color)



def display_color_name_when_user_clicks_color_in_image(uploaded_image, color_dataset) -> None:

    global clicked

    # While the user has not closed the program, keep displaying the color names of
    # the colors he/she double clicks on
    while(1):

        # First show the image the user sent to the program to get the color names from
        cv2.imshow("Color Detection Application", uploaded_image)

        # If the user double clicked on the image, get the image properties and call the necessary
        # functions to get the color name.
        if (clicked):

            # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
            cv2.rectangle(uploaded_image,(20,20), (750,60), (blue_color, green_color, red_color), -1)

            # Creates text string to display( Color name and RGB values )
            text = get_color_name(red_color, green_color, blue_color, color_dataset) + ' R=' + str(red_color) + ' G='+ str(green_color) + ' B='+ str(blue_color)

            # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
            cv2.putText(uploaded_image, text, (50,50), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)

            # For very light colours we will display text in black color
            if(red_color + green_color + blue_color >= 600):
                cv2.putText(uploaded_image, text, (50,50), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)

            clicked = False

        # Breaks the loop when user hits 'esc' key
        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()



def main() -> None:

    # Get the image path from the user and store it in a variable for later use
    image_path = get_image_path_from_the_user()

    # Pass the image path to read the image and store it in a variable for later use
    uploaded_image = read_image_with_opencv(image_path)

    # Load all the color dataset and store it in a variable
    color_dataset = get_color_dataset()

    # Display the window and call the draw function
    cv2.namedWindow("Color Detection Application")

    # Gets x,y coordinates of mouse left or right button click and pass it to the draw function
    cv2.setMouseCallback("Color Detection Application", draw_function)

    # Display the color name when the user clicks color in the image loaded
    display_color_name_when_user_clicks_color_in_image(uploaded_image, color_dataset)

# Call the main function if the file is not being imported as a module
if __name__ == "__main__":
    main()


