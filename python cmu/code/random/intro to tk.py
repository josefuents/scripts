from Tkinter import *
root = Tk()
canvas = Canvas(root, width=300, height=200)
canvas.pack()
def drawBelgianFlag(canvas, x0, y0, x1, y1):
    # draw a Belgian flag in the area bounded by (x0,y0) in
    # the top-left and (x1,y1) in the bottom-right
    width = (x1 - x0)
    canvas.create_rectangle(x0, y0, x0+width/3, y1, fill="black", width=0)
    canvas.create_rectangle(x0+width/3, y0, x0+width*2/3, y1, fill="yellow", width=0)
    canvas.create_rectangle(x0+width*2/3, y0, x1, y1, fill="red", width=0)

# Draw a large Belgian flag
drawBelgianFlag(canvas, 25, 25, 175, 150)

# And draw a smaller one below it
drawBelgianFlag(canvas, 75, 160, 125, 200)

# Now let's have some fun and draw a whole grid of Belgian flags!
width = 30
height = 25
margin = 5
for row in range(3):
    for col in range(3):
        left = 200 + col * width + margin
        top = 50 + row * height + margin
        right = left + width - margin
        bottom = top + height - margin
        drawBelgianFlag(canvas, left, top, right, bottom)

# Finally, don't forge to display the window!
root.mainloop()
