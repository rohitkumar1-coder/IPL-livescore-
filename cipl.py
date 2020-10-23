#"DISPLAYING IPL LIVE SCORE"
#For this project, we need 4 major python libraries/modules
#tkinter used for GUI(Graphical User Interface)
#Python Image Library(PIL) for opening, manipulating and saving many different image file formats.
#BeautifulSoup for Web Scraping
#urllib for fetching the url to our program
#We need to install these libraries in our system by using pip command in CMD or Anaconda Prompt.
#Installation commands are:
            #pip install bs4(bs4 is a library for BeautifulSoup4
            #pip install PIL
            #pip install tkinter
            #pip install urllib
#First of all we need to import those 4 modules in to our program
from tkinter import *
from PIL import ImageTk, Image
from os import *
from bs4 import BeautifulSoup as BS
import urllib.request
#Save the program before further writing of code

#Fetch the link and open it using urllib
score_page = 'http://static.cricinfo.com/rss/livescores.xml'

#This xml file contains live scores for currently ongoing matches so we can fetch this file into our program

page = urllib.request.urlopen(score_page)

#livescores.xml is successfully fetched to our program

soup = BS(page, 'html.parser')
res = soup.find_all('description')

#We now used BeautifulSoup for scraping the xml file and fetch all the data inside the description tags using find_all method

liveScore = []

#This list is used to store all the score related information

for score_part in res:
	liveScore.append(score_part.get_text())

#By this for loop we are appending all the fetched information inside description tags and putting them inside live Scores list

#We use to method score() and clear() for displaying the score and also the clear the old score..
	
def score():
	T.insert(END, liveScore)
def clear():
	T.delete(1.0, END)

#Now we create a window using the tkinter module	
	
root = Tk()

#Window has been created

root.title("IPL LIVE SCORES 2020") #title of the window
root.geometry('800x600')#height and width of the window
root.configure(background="black")#background color inside the window

#now we import the background image for our window
img = ImageTk.PhotoImage(Image.open ("Downloads/ipl.jpg"))

panel = Label(root, image=img)
panel.place(x=0, y=0)

#Now our image will be placed inside the window starting from top left corner i.e x=0, y=0

T = Text(root)
T.place(x=200, y=250, height=100, width=400)

#By using the above code we are placing a text box inside our window at x=200, y=250 position
#We will be displaying the livescore in this text box

l = Label(root, text="LIVE SCORE", fg="white", bg="red")
l.place(x=200, y=350, height=30, width=400)

#Now we created a label which shows LIVE SCORE as the text
#fg means ForeGround color
#bg means BackGround color

#Now we will be creating 2 buttons score and clear for displaying the score and clearing off the old score

b1 = Button(root, text="DISPLAY SCORE", bg="black", fg="white", command=score)
b1.place(x=120, y=450, height=80, width=250)

b2 = Button(root, text="CLEAR SCORE", bg="black", fg="white", command=clear)
b2.place(x=420, y=450, height=80, width=250)

#After creating the buttons, label and also text box we can now execute the program

root.mainloop()
