## Third party Lyrics presentation dock plugin for <a href="https://obsproject.com/" target="_blank">OBS Studio</a>

### Summary

The **Third party Lyrics presentation dock plugin for <a href="https://obsproject.com/" target="_blank">OBS Studio</a>** provides hymn lyrics as presentation slides with style that you can manage in real time or at preparation time. 

**Lyrics** are words that make up a song, usually consisting of verses and choruses. Basic song structure consists of an intro, verse, pre-chorus, chorus and bridge. In this plugin, the blank line is the separator dividing lyrics in many presentation slides.

As for the **presentation** slides, it is tricky to find a balance between keeping them creative but not overly distracting, making sure the color of the lyrics is always in contrast with the background. 

The third party plugin is free and provides the following features:

- Quick and easy addition of hymns
- Easy enough use to get it up and running
- Searching hymn by title
- Choosing text animation
- Choosing image background
- Choosing background gradient colors and lyrics text color
- Increase or decrease of the font size and of the line height
- Management of the hymn playlist
- Choosing and storing for every playlist the following: the text animation, font size, background image, background, foreground colors
- Real time changing of text animation, font size, image background, background and foreground colors

### Compatibility
It has been tested in Windows/IIS web server and Python 3.12. It could be compatible with Windows, Linux and macOS.

The html pages are written in javascript/jquery code and are listening/sending messages via the BroadcastChannel javascript object. No database is used, each hymn is a txt type file, therefore it is enough to add/change txt type files with lyrics by bulk copy/paste or via the Python script **lyrics_data.py**. The script **lyrics_data.py** uses the obspython library, so, it is executable via the menu item Tools > Scripts. The scipt provides the abiblity to add/change the hymn files, the background/foreground colors and the background images according to the presentation style needs.

### Installation
- A web server must be installed plus a decent distribution of Python.
- Download the plugin and unzip it to a folder that web server can point.<br> For example ```http://localhost/lyrics/```
- Change the variable **my_path** of script **lyrics_data.py** to point to the main folder.<br> For example ```my_path = "C:\\inetpub\\wwwroot\\lyrics"```
- Open the Scripts dialog window, displayed via the menu item Tools > Scripts and add within the scripts folder the **lyrics_data.py**. Also, the Python Install Path must be set in the tab Python Settings.
- Install the python pillow library, the other libraries are embedded in the Python Interpreter.

Thereafter the downloaded sample must be working.

### Simple data management
You can manage all the information, hymns, colors and images, through the Python script **lyrics_data.py** located in the Tools > Scripts menu.

**It is not necessary to open/change/copy files if there is no technical knowledge.**

![lyrics_data](https://github.com/user-attachments/assets/7d2c20a3-874b-400e-8fda-07bd113ace66)

### Data management via the Python script lyrics_data.py
Because of the **obspython** library used by the script, four buttons are presented via the menu Tools > Scripts > lyrics_data.py.

The button **1. Add/Change Hymns** to add or change hymn files. The script suggests the title of a new hymn the max available 3-digit number of directory titles plus the words of first line lyrics.

The button **2. Prepare Hymns** copies the hymn files from the folder **my_hymns** to the folder **data** and creates the **titles.txt** file which has the names of the files as content.

It is necessary to utilize the button **2. Prepare Hymns** every time you add/change hymn texts via **1. Add/Change Hymns** button.

The third button **Colors Palette** add/change colors according to the presentation style needs. You can define **linear-gradient** themes with the following properties:
- foreground text color
- foreground text shadow
- background gradient color1
- background gradient color2
- background gradient color3
- The gradient stop of color2 in percentage
- The gradient line's angle of direction in degrees

In the link <a href="https://htmlpreview.github.io/?https://github.com/ManolisMariakakis/lyrics-presentation/blob/main/LinearGradient.html" target="_blank">3-Color Linear-Gradient Generator</a> you will find a generator that helps you make your own backgrounds.

Additionally to the  linear gradient background, there is the option to use background image as a previous layer under the linear gradient background.

The fourth button **Image Viewer** view or replace the images that can be selected as background image layer.

The script adds at the end of color themes the W_transparent (white foreground) and B_transparent (black foreground) in case you don't need gradient colors background.

### Files handling without the use of the Python script lyrics_data.py
This is the alternative data management method for users with technical knowledge. It is okay also to alternate the two methods.

In the folder **my_hymns** add the hymns in txt files and in UTF-8 format. For the naming of the files make sure that the title is starting with a **unique 3-digit number** (from 001 to 999). The number **000** is used for the playlist.

**Lyrics are separated by a blank line, the existed text between two blank lines is a presentation slide**.

It is needed to utilize the button **2. Prepare Hymns** every time you add/change hymn texts via bulk copy/paste of txt files.

The **colors.txt** file can be found in the **data** folder, to which you **can add your own** background and foreground color themes.

The **colors.txt** file information is separated by a semi colon delimiter: 
- color title
- foreground text color
- foreground text shadow
- background gradient color1
- background gradient color2
- background gradient color3
- The gradient stop of color2 in percentage
- The gradient line's angle of direction in degrees

The style is composed with the 3 gradient colors according to the syntax<br>
```linear-gradient(${degrees}deg, ${color3} 0%, ${color2} ${stop}%, ${color1} 100%);```

Additionally there is the option to use a background image as a previous layer underneath the gradient colors.

In the **images** folder there are 20 background jpg images (img001.jpg .. img020.jpg), which you can change or leave it or not use. Background images are overlayed with background colors using the style syntax<br>
```background-blend-mode: overlay; background-image: url("images/img${image}.jpg"), linear-gradient(${degrees}deg, ${color3} 0%, ${color2} ${stop}%, ${color1} 100%);```


### LIB folder
The **lib** folder includes the following javascript libraries:

- jquery: https://github.com/jquery/jquery
- WebSlides: https://github.com/webslides/WebSlides
- Animate.css: https://github.com/animate-css/animate.css

Concerning the **webslide** library, everything you need to make html presentations in a beautiful way is provided. Each **section** tag in the webslides element is an individual slide.

**Animate.css** is a library of ready-to-use, cross-browser animations. The following styles are used for lyrics/text animation:
- animate__fadeIn
- animate__fadeInDown
- animate__fadeInLeft
- animate__fadeInRight
- animate__fadeInRight
- animate__fadeInUp
- animate__fadeInTopLeft
- animate__fadeInTopRight
- animate__fadeInBottomLeft
- animate__fadeInBottomRight
- animate__flipInX
- animate__jackInTheBox
- animate__rollIn
- animate__zoomIn
- animate__zoomInDown
- animate__zoomInLeft
- animate__zoomInRight
- animate__zoomInUp
- animate__slideInDown
- animate__slideInLeft
- animate__slideInRight
- animate__slideInUp

### Docks and Browser source
The plugin includes the 5 following docks plus the browser source

1. The list of hymn/song titles<br>
http://localhost/lyrics/titles.html
2. The lyrics to navigate slides, when specific hymn is selected<br>
http://localhost/lyrics/lyrics.html
3. Slide display options, animation, background color, foreground color, background image, font size<br>
http://localhost/lyrics/selections.html
4. The hymn playlist<br>
http://localhost/lyrics/images.html
5. The Images selection from thumbnail gallery<br>
http://localhost/lyrics/playlist.html
6. The browser source<br>
http://localhost/lyrics/webslides.html

The result is as in the image below (with the help of dock layouts plugin <a href="https://obsproject.com/forum/resources/jrdockie-save-and-load-window-and-dock-layouts.1955/" target="_blank">jrdockie</a>).

![docs](https://github.com/user-attachments/assets/b7f12757-7978-4ebf-a4d9-a0ac2e41a77c)


### Training on the online sample

- https://ymnoi.gr/lyrics/titles.html
- https://ymnoi.gr/lyrics/selections.html
- https://ymnoi.gr/lyrics/lyrics.html
- https://ymnoi.gr/lyrics/playlist.html
- https://ymnoi.gr/lyrics/images.html
- https://ymnoi.gr/lyrics/webslides.html

1. Add the first 4 pages (titles, selections, lyrics, playlist) as dock page via the menu Docs > Custome Browser Docs
2. Add the 5th page (webslides) as Browser source (width=800, height=600)
3. Choose on the selections page, [w_dark_blue, fadein, Image001]
4. Click on the titles page the 002 hymn
5. Check lyrics page to see the 002 lyrics/slides, click on a non blank slide
6. Check webslides page, the selected slide must be displayed
7. Increase and decrease the font size from the selections page
8. Repeat steps 4 to 6 with next lyrics/slide
9. Choose on the selections page [w_indian_red, rollIn, without image]
10. Check webslides page, the selected slide must be displayed with the new style
11. Delete all records on the playlist page
12. Choose on the selections page [w_indian_red, rollIn, without image]
13. Click the button on the titles page of the 002 hymn
14. Check the playlist page to see the new record
15. Choose on the selections page [w_dark_blue, fadein, Image001]
16. Click the button on the titles page of the 003 hymn
17. Check the playlist page to see the playlist records
18. Click on the titles page the "000 Playlist"
19. Check lyrics page to see the playlist lyrics/slides, click on a non blank slide
20. Check webslides page, the selected slide must be displayed
21. Repeat steps 19 to 20 with next lyrics/slide, a blank page existed between two hymns of playlist

Enjoy
