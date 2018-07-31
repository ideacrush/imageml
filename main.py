import sys,os,glob
from PlotGUI import *
import random
import cv2
from PyQt4.QtGui import *
from PyQt4.Qt import QString
from cv2 import INTER_AREA
import numpy
from numpy import arange,pi,sin
from matplotlib import pyplot as plt
from sklearn.naive_bayes import GaussianNB


class GUIForm(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton , QtCore.SIGNAL('clicked()'), self.PlotFunc)
        QtCore.QObject.connect(self.ui.pushButton_2 , QtCore.SIGNAL('clicked()'), self.LoadImage)
        QtCore.QObject.connect(self.ui.pushButton_3 , QtCore.SIGNAL('clicked()'), self.VectorGen())
    
    def LoadImage(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Select File', "/home/Desktop/Project 7/data" , "Supported Image Files (*.jpg *.jpeg *.tif *.bmp *.png)")
        scene = QGraphicsScene()			#also provides functionality that lets you efficiently determine both the location of 								#items, and for determining what items are visible within an arbitrary area on the scene
        
	    #scene.addPixmap(QPixmap(self.fname))	#QPixmap pixmap(const QSize & size, Mode mode = Normal, State state = Off) const	
        self.ui.graphicsView.setScene(scene)		#displaying image in graphic scene
        img = cv2.imread(str(self.fname))		#Loads an image from a file.
        imgrs = numpy.empty_like(img)			#Return a new uninitialized array.
        
        imgrs = cv2.resize(img,(150,150),interpolation = INTER_AREA)	#Preferable interpolation methods are cv2.INTER_AREA for shrinking and
        
        self.ui.label.setText  ("FileName : " + str(os.path.basename(str(self.fname))))
        self.ui.label_2.setText("Original Image : " + str(img.shape[0]) + " x " + str(img.shape[1]) +
                              "\nAfter Resize   : " + str(imgrs.shape[0]) + " x " + str(imgrs.shape[1]))
        self.ui.label_3.setText("Pixels         : " + str(img.size) + 
                              "\nResized Pixels : " + str(imgrs.size))
           
        red = []
        blue = []
        green = []
        
        self.imgvector = numpy.empty([150,0],dtype = float) #Return a new uninitialized array.
            
        for x in range(0,150):
            for y in range(0,150):
                red.append(imgrs[x][y][0])
                green.append(imgrs[x][y][1])
                blue.append(imgrs[x][y][2])        
        n, bins, patches = plt.hist(red, 50,[0,256])  			#n: is the number of counts in each bin of the histogram
									#bins: is the left hand edge of each bin
									#patches is the individual patches used to create the histogram, e.g a 										#collection of rectangle
									#the histogram of the data




  
        self.imgvector = numpy.append(self.imgvector,n)

        n, bins, patches = plt.hist(green, 50,[0,256])
        self.imgvector = numpy.append(self.imgvector,n)

        n, bins, patches = plt.hist(blue, 50,[0,256])
        self.imgvector = numpy.append(self.imgvector,n)
        
        print (self.imgvector)
        
                
    def PlotFunc(self):
        randomNumbers = random.sample(range(0, 10), 10)
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.ax.plot(randomNumbers)
        self.ui.widget.canvas.draw()

    def VectorGen(self):
        self.ui.pushButton_3.setText("Working ...")
        self.listfile = QFileDialog.getOpenFileName(self, 'Select File', "/home/kc" , "Supported List Files (*.csv *.tsv *.txt);;All Files(*.*)")
        fp = open(self.listfile , "r+")
        fp1 = open("FileVector.txt","w")
        fp2 = open("FileClass.txt","w")        
        while True:
            fileL = fp.readline()
            print (fileL)
            if not fileL: break    
            fileL = fileL.strip()
            fileN,Link = fileL.split("\t")
            fileName = fileN
            classify = fileName[0]    
            img = cv2.imread("../data/"+fileName) #
                
                                
            x= 0
            y= 0
    
            r=[]
            g=[]
            b=[]
            
            for x in range(0,150):
                for y in range(0,150):
                    r.append(img[x][y][0])
                    g.append(img[x][y][1])
                    b.append(img[x][y][2])
            
            imgvector = numpy.empty([150,0],dtype = float)

            n, bins, patches = plt.hist(r, 50,[0,256])    
            imgvector = numpy.append(imgvector,n)
            
            n, bins, patches = plt.hist(g, 50,[0,256])
            imgvector = numpy.append(imgvector,n)
            
            n, bins, patches = plt.hist(b, 50,[0,256])
            imgvector = numpy.append(imgvector,n)

            numpy.savetxt(fp1,imgvector,newline=" ",delimiter = " ")
            fp2.write(classify+"\n")        
            pos = fp1.tell()	#current file position
            fp1.seek(pos-1)     #writing at offset position  
            fp1.write("\n")   
            
    def ClassifierGNB(self):
        
        
        fp.close()
        fp1.close()
        fp2.close()
        self.ui.pushButton_3.setText("Image Vectors Generated..")
         

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    sys.exit(app.exec_())
