import collections 
import collections.abc
from pptx import Presentation
from pptx.util import Inches
from PIL import Image

pr1 = Presentation()
#number of slides

var = input("How many slides? ")
i = int(var)
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
    i -= 1
    slide_number_register = pr1.slide_layouts[0]
    slide_number = pr1.slides.add_slide(slide_number_register)

    title_number = slide_number.shapes.title
    title_number.text = str(var2)

    subtitle1 = slide_number.placeholders[1]
    subtitle1.text = str(var3)
    x = x+1

  while x==1:
    i -= 1
    slide_number_register = pr1.slide_layouts[1]
    slide_number = pr1.slides.add_slide(slide_number_register)

    title_number = slide_number.shapes.title
    title_number.text = ("What is "+ str(var2.lower()) + "?")

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

    while i == 0:
      slide_number_register = pr1.slide_layouts[0]
      slide_number = pr1.slides.add_slide(slide_number_register)

      title_number = slide_number.shapes.title
      title_number.text = "Are there any questions?"

      subtitle1 = slide_number.placeholders[1]
      subtitle1.text = "Have a wonderful day!"
      x = x+1
      i -= 1
  
else:
  pr1.save("Testing.pptx")
  print("Presentation done!")
