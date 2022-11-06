import collections 
import collections.abc
from pptx import Presentation
from pptx.util import Inches
from PIL import Image

pr1 = Presentation()
#number of slides

var = input("How many slides? ")
i = int(var)
# i = 5
x = 0

var2 = input("The title of the presentation? ")

var3 = input("Who is making the presentation? ")


i = i - 1

while i > 0:
  i -= 1
  slide = "slide"
  title = "title"
  slide_number = (slide + str(x))
  title_number = (title + str(x))
  #print(slide_number)

  while x == 0:
    slide_number_register = pr1.slide_layouts[0]
    slide_number = pr1.slides.add_slide(slide_number_register)

    title_number = slide_number.shapes.title
    title_number.text = str(var2)

    subtitle1 = slide_number.placeholders[1]
    subtitle1.text = str(var3)
    x = x+1

  else:

    slide_number_register = pr1.slide_layouts[1]
    slide_number = pr1.slides.add_slide(slide_number_register)

    title_number = slide_number.shapes.title
    input1_question = "Please enter the title of the "
    input1_ending = "slide"
    var = input('Title of slide number ' + str(x+1) + ':')
    title_number.text = var
  

  x = x+1
else:
  pr1.save("Testing.pptx")

# for i in range(0,n):
#     print(i)

# slide1_register = pr1.slide_layouts[0]
# slide0 = pr1.slides.add_slide(slide1_register)

# title1 = slide0.shapes.title
# var = input("Please enter the topic of the presentation: ")
# title1.text = var

# subtitle1 = slide0.placeholders[1]
# var2 = input("Please enter who made the presentation:")
# subtitle1.text = var2

# slide2_register = pr1.slide_layouts[1]
# slide2 = pr1.slides.add_slide(slide2_register)

# title2 = slide2.shapes.title
# title2.text = "Propoganda"

# pr1.save("Testing.pptx")