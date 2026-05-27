###Ryleigh’s encode
from PIL import Image
 
# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):
 
        # list of binary codes
        # of given data
        newd = []
 
        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd
 
# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
 
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
 
    for i in range(lendata):
 
        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]
 
        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
 
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1
 
        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
 
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
 
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]
 
def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
 
    for pixel in modPix(newimg.getdata(), data):
 
        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


####ryleigh’s updated verison:

import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from time import *
from encode import *

# ONE root window only
canvas = Tk()
canvas.title("🎀 Secret Stego 🎀")
canvas.geometry('700x730+400+100')
canvas.configure(bg='LightPink')
title_label = Label(canvas, text="🎀 Secret Stego 🎀",
                    font=("Helvetica", 22, "bold"),
                    bg="#FFB6C1", fg="#880044")
title_label.pack(pady=(10, 0))
# Window setup ----------------------------------------------

#Canvas setup
img_canvas= Canvas(canvas, width= 400, height= 300, bg='#FFF0F5', highlightbackground = '#FF69B4', highlightthickness=3)
canvas.lift()
canvas.attributes('-topmost', True)
canvas.after_idle(canvas.attributes, '-topmost', False)

# Quit Button
quit_button = Button(canvas, text="✖ Quit",bd=0, bg="#FF69B4",font="Helvetica 9 bold",fg="white",
                     activebackground= '#FF1493',activeforeground='white', padx=14, pady=6,
                     cursor='heart',relief="flat",command=canvas.destroy)
quit_button.pack(side=TOP, pady=(15, 0))

#flags
image = None
image_added = False
decrypted_flag = False

#open image
def open_image():
    global image, image_added
    img_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if img_path:
        image = Image.open(img_path).convert('RGB')
        max_width = 450
        max_height = 450
        image.thumbnail((max_width, max_height))
        photo = ImageTk.PhotoImage(image, master=canvas)  # master= is the key
        img_canvas.create_image(0, 0, anchor=NW, image=photo)
        img_canvas.image = photo
        image_added = True
        add_image_text.config(text="✅ Image Added", fg='#1E8449')
##def open_image():
##    global image, image_added
##    import easygui
##    img = easygui.fileopenbox(title="Select an image",filetypes=["*.png", "*.jpg", "*.jpeg", "*.bmp"])
##    if img:
##        image = Image.open(img).convert('RGB')
##        max_width = 450
##        max_height = 450
##        image.thumbnail((max_width, max_height))
##        photo = ImageTk.PhotoImage(image)
##        img_canvas.create_image(0, 0, anchor=NW, image=photo)
##        img_canvas.image = photo
##        image_added = True
##        add_image_text.config(text="✅Image Added", fg = '#1E8449')
        
##def open_image():
##    global image, image_added
##    import subprocess
##    result = subprocess.run(
##        ['/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13', '-c',
##        '''
##import tkinter as tk
##from tkinter import filedialog
##root = tk.Tk()
##root.withdraw()
##path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
##print(path)
##'''],
##        capture_output=True, text=True
##    )
##    print("STDOUT:", result.stdout)
##    print("STDERR:", result.stderr)  # this will show the error
##    print("Return code:", result.returncode)
##    img = result.stdout.strip()
##    if img:
##        image = Image.open(img).convert('RGB')
##        max_width = 450
##        max_height = 450
##        image.thumbnail((max_width, max_height))
##        photo = ImageTk.PhotoImage(image)
##        img_canvas.create_image(0, 0, anchor=NW, image=photo)
##        img_canvas.image = photo
##        image_added = True
##        add_image_text.config(text="Image Added")

##def open_image():
##    global image, image_added
##    root.deiconify()
##    img = filedialog.askopenfilename(
##        parent=canvas,
##        title="Select an image",
##        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
##    )
##    root.withdrawn()
##    if img:
##        image = Image.open(img).convert('RGB')
##        image = Image.open(img)
##        max_width = 450
##        max_height = 450
##        image.thumbnail((max_width, max_height))
##        photo = ImageTk.PhotoImage(image)
##        img_canvas.create_image(0, 0, anchor=NW, image=photo)
##        img_canvas.image = photo
##        image_added = True
##        add_image_text.config(text="Image Added")

#add image
def add_image():
    global image_added
    open_button = Button(canvas, text="Add Image",bd=0,
                        bg="tan1",fg='blue', activebackground='#D68910',
                        activeforeground='white', font="Helvetica 10 bold", command=open_image)
    open_button.pack()
    add_image_text.config(text="")
    
    if image_added:
        add_image_text.config(text="Image Added")
    else:
        add_image_text.config(text="No Image Added Yet")

#show image canvas
def show_image_canvas():
    if img_canvas.winfo_ismapped():
        img_canvas.pack_forget()
    else:
        img_canvas.pack()

#start button
def start_button():
    start = Button(canvas, text="🎀 START 🎀",font="Helvetica 20 bold", bd='5', bg="#FF69B4",fg= "white",
                   activebackground="#FF1493",activeforeground="white",
                   command= lambda:[two_buttons(),show_image_canvas(), add_image(),start.destroy()])
    start.pack(padx = 0,pady = 0)

#Decrypt and encrypt buttons
def two_buttons():
    encrypt = Button(canvas, text="ENCRYPT",font="Sans 10 bold", bd='5',
                     bg="#FFB6C1", fg="#880044", activebackground="#FF69B4",command = lambda: [encrypts()])
    encrypt.pack()
    
    decrypt = Button(canvas, text="DECRYPT",font="Sans 10 bold",
                     bg="#FADADD", fg="#880044", activebackground="#FF69B4", command= lambda:[decrypts()])
    decrypt.pack()
    
Input = Text(canvas, height=10, width=25, bg="bisque")
#Decrypt code
def decrypts():
    global image, Input, data
    if image is None:
        labels = Label(canvas, text="⚠️ Please add an image first!", fg="red")
        labels.pack()
        return
    if not hasattr(decrypts, 'decrypted_flag') or not decrypts.decrypted_flag:
        row, col = image.size
        data = ''
        imgdata = iter(image.getdata())
     
        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3]]
     
            # string of binary data
            binstr = ''
            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                labels = Label(canvas, text=f"Decrypted Message: {data}")
                labels.pack()
                decrypts.decrypted_flag = True
                return data
                
        #labels = Label(canvas, text=f"Decrypted Message: {data}")
        labels.pack()
                #image.config(text=f"Decrypted Message: {data}")
    ##    Input.delete(1.0, "end-1c")  # Clear previous text in the Text widget
    ##
    ##    msg = ''
    ##    imgmsg = iter(image.getdata())
    ##
    ##    while True:
    ##        pix = [value for value in next(imgmsg)[:3] +
    ##               next(imgmsg)[:3] +
    ##               next(imgmsg)[:3]]
    ##        binstr = ''
    ##
    ##        for i in pix[:8]:
    ##            if i % 2 == 0:
    ##                binstr += '0'
    ##            else:
    ##                binstr += '1'
    ##
    ##        char = chr(int(binstr, 2))
    ##        
    ##        if char == '\x00':  # Use '\x00' as the delimiter indicating the end of the message
    ##            break
    ##
    ##        msg += char
    ##
    ##    Input.insert(1.0, msg)
        #print("Decrypted message:", data)

#Encrypts message    
def encrypts():
    global image, Input
    if image is None:
        label = Label(canvas, text="⚠️ Please add an image first!", fg="red")
        label.pack()
        return
    
    row, col = image.size

    # Text Box
    Text_input = Text(canvas, height=10, width=25,bg="#FFF0F5",
                  fg="#880044", insertbackground="#FF69B4",
                  font="Helvetica 11", relief="groove")
    Text_input.pack()
    
    label = Label(canvas, text="")
    label.pack()

    # Submits encryption
    def get_input():
        Input = Text_input.get("1.0", END)
        if Input:
            label.config(text=f"Message Entered: {Input}")
            msg = Input
            Text_input.pack_forget()
            currX = 0
            currY = 0

            #newimg = image.copy()
            encode_enc(image, msg)

##            def modPix(pixels, data):
##                for i in range(3):
##                    if currX < len(data):
##                        pixels[i] = int(format(pixels[i], '08b')[:-1] + data[currX], 2)
##                        currX += 1
##                return tuple(pixels)
##
##            for i in range(len(msg) + 1):
##                if i < len(msg):
##                    s = format(ord(msg[i]), '08b')
##                else:
##                    s = '00000000'
##
##                r, g, b = image.getpixel((currX, currY))
##                new_pixel = modPix([r, g, b], s)
##                image.putpixel((currX, currY), new_pixel)
##
##                currX += 1
##                if currX >= row:
##                    currX = 0
##                    currY += 1
##
##            # Save the image
##            new_img_name = input("Enter the name of the new image (with extension): ")
##            image.save(new_img_name, str(new_img_name.split(".")[1].upper()))

            print("encrypting")

    # Encrypt Button for encrypt and closes the text box
    submit = Button(canvas, text="✉️ Submit", bd=5, bg="#DA70D6", fg="white",
                font="Sans 10 bold", activebackground="#BA55D3", command=get_input)
    submit.pack(padx=0, pady=0)

    label = Label(canvas, text="")
    label.pack()

    
    #Save_input = Text(canvas, height=2, width=25, bg="light green")
    #Save_input.pack()

    def save_image():
        global image
       
        if image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", \
                         filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),\
                         ("All files", "*.*")])
            if not save_path:
                  return
        image.save(save_path)
        label.config(text="Saved!")


        
    save_button = Button(canvas, text="💾 Save Encrypted Image", bd=5,
                     bg="#FF69B4", fg="white", font="Sans 10 bold",
                     activebackground="#FF1493", command=save_image)
    save_button.pack()
    

add_image_text = Label(canvas, text=" ", font=("Sans bold", 14),
                       bg="#FFB6C1", fg="#880044")
add_image_text.pack()
start_button()
#quit_button()
canvas.mainloop()
