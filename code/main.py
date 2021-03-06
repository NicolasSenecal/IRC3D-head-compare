from FaceDetector import FaceDetector
from MeshManager import MeshManager
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from VideoManager import VideoManager
import argparse
import json
import math
import os
import sys
import time
import timeit
from ui import main
import utils
from utils import debounce

# python3 main.py --video ../videos/CCTV_1.mp4 --mesh ../faces/PAUL/FinalExport.obj

def parse_args():
  """Parse input arguments."""
  parser = argparse.ArgumentParser(description='Head pose estimation using the Hopenet network.')
  parser.add_argument('--video', dest='video_path', help='Path of video', default='')
  parser.add_argument('--mesh', dest='mesh_path', help='Path of mesh', default='../config.json')
  parser.add_argument('--config', dest='config_path', help='Path of the configuraiton JSON file', default='../config.json')
  args = parser.parse_args()
  return args

class MainWindow(main.Ui_MainWindow, QtWidgets.QMainWindow):
  def __init__(self, parent=None):
    # INIT QT WINDOWS
    super(MainWindow, self).__init__(parent=parent)
    self.setupUi(self)
    
    # DEFAULT VARIABLES
    self.videoManager = VideoManager()
    self.meshManager = MeshManager()
    self.isDragging = False
    self.faceDetector = None
    self.progressDialog = QtWidgets.QProgressDialog("Loading...", "Stop", 0, 100, self)
    self.lastUpdate = 0
    self.maxWidth = self.VideoWidget.geometry().width()
    self.maxHeight = self.VideoWidget.geometry().height()
    self.centerX = self.maxWidth / 2. # center of the video
    self.centerY = self.maxHeight / 2.
    self.zoom = 1.
    self.mousePos = QtCore.QPointF(0, 0)
    self.videoFormats = []
    self.meshFormats = []
    
    # DISABLED ALL BUTTONS
    self.setEnabledButtons(False)

    
    # PUSH BUTTONS EVENTS
    self.read_PB.clicked.connect(lambda: self.videoManager.play())
    self.pause_PB.clicked.connect(lambda: self.videoManager.pause())
    self.nextFrame_PB.clicked.connect(lambda: self.videoManager.moveFrame(1, self.draw))
    self.lastFrame_PB.clicked.connect(lambda: self.videoManager.moveFrame(-1, self.draw))
    self.next10Frame_PB.clicked.connect(lambda: self.videoManager.moveFrame(10, self.draw))
    self.last10Frame_PB.clicked.connect(lambda: self.videoManager.moveFrame(-10, self.draw))
    self.headPosition_PB.clicked.connect(lambda: self.getHeadPosition())
    self.processAllVideo_PB.clicked.connect(lambda: self.processAllVideo())
    self.coordinates_PB.clicked.connect(lambda: self.drawAxisEvent())
    self.square_BT.clicked.connect(lambda: self.drawSquareEvent())
    self.screenshot_PB.clicked.connect(lambda: self.screenshotEvent())
    self.resetOrientation_PB.clicked.connect(lambda: self.resetOrientationEvent())
    self.resetTSH_PB.clicked.connect(lambda: self.resetTHSEvent())
    self.resetBC_PB.clicked.connect(lambda: self.resetBCEvent())
    
    # MENU BAR EVENTS
    self.actionOpen_video.triggered.connect(self.selectVideo)
    self.actionOpen_model.triggered.connect(self.selectModel)
    
    # SLIDERS EVENTS
    self.videoSlider.actionTriggered.connect(lambda: self.sliderChanged())
    self.confidenceSlider.actionTriggered.connect(lambda: self.confidenceChanged())
    self.fovySlider.actionTriggered.connect(lambda: self.fovyChanged())
    self.yawSlider.actionTriggered.connect(lambda: self.yawChanged())
    self.pitchSlider.actionTriggered.connect(lambda: self.pitchChanged())
    self.rollSlider.actionTriggered.connect(lambda: self.rollChanged())
    self.temperatureSlider.actionTriggered.connect(lambda: self.temperatureChanged())
    self.saturationSlider.actionTriggered.connect(lambda: self.saturationChanged())
    self.hueSlider.actionTriggered.connect(lambda: self.hueChanged())
    self.brightnessSlider.actionTriggered.connect(lambda: self.brightnessChanged())
    self.contrastSlider.actionTriggered.connect(lambda: self.contrastChanged())
    
    # MOUSE EVENTS
    self.VideoWidget.wheelEvent = self.wheelEvent
    self.VideoWidget.mousePressEvent = self.mousePressEvent
    self.VideoWidget.mouseReleaseEvent = self.mouseReleaseEvent
    self.VideoWidget.mouseMoveEvent = self.mouseMoveEvent
    self.GLWidget.wheelEvent = self.wheelEvent
    self.GLWidget.mousePressEvent = self.mousePressEvent
    self.GLWidget.mouseReleaseEvent = self.mouseReleaseEvent
    self.GLWidget.mouseMoveEvent = self.mouseMoveEvent
    
    # RESIZE EVENT
    self.VideoWidget.resizeEvent = self.resizeEvent
    self.videoProcessTable.resizeEvent = self.resizeProcessTable


  
  #################################
  ### ==== EVENTS ON FRAME ==== ###
  #################################
 
  def mousePressEvent(self, event):
    """ Event call at each click on the VideoWidget. Get the mouse pos and active dragging """
    self.mousePos = event.pos()
    self.isDragging = True
  
  
  def mouseReleaseEvent(self, event):
    """ Event call at each realse click on the VideoWidget. Disable dragging """
    self.isDragging = False


  def mouseMoveEvent(self, event):
    """ Event call at each mouse movement on VideoWidget. Change the center with the dragging """
    if (self.isDragging):
      self.centerX -= (event.pos().x() - self.mousePos.x()) 
      self.centerY -= (event.pos().y() - self.mousePos.y())
      self.draw() #we redraw the frame
    self.mousePos = event.pos()
    
    
  def wheelEvent(self, event):
    """ Event call at each mouse wheel action on videoSlider. Zoom, change the center and redraw the frame """
    x = event.pos().x()
    y = event.pos().y()
    
    if x > self.maxWidth: # if we are on the second screen
      x -= self.maxWidth
      
    self.zoom = utils.clamp(1., self.zoom + event.angleDelta().y() * 0.002, 20.)
    if(self.zoom == 1):
      self.centerX = self.maxWidth / 2. # center of the video
      self.centerY = self.maxHeight / 2.
    else:
      self.centerX = x * self.zoom
      self.centerY = y * self.zoom
    self.draw() #we redraw the frame



  #################################
  ### ==== EVENTS ON MENU  ==== ###
  #################################

 
  def drawAxisEvent(self):
    """ Event call with the push of coordinates_PB. Active or disable the draw of axis and redraw the frame """
    if(self.videoManager.ifDrawAxis):
      self.videoManager.ifDrawAxis = False
    else:
      self.videoManager.ifDrawAxis = True
    self.drawVideo() #we redraw the frame
    
    
  def drawSquareEvent(self):
    """ Event call with the push of square_BT. Active or disable the draw of square and redraw the frame """
    if(self.videoManager.ifDrawSquare):
      self.videoManager.ifDrawSquare = False
    else:
      self.videoManager.ifDrawSquare = True
    self.drawVideo() #we redraw the frame


  def resetOrientationEvent(self):
    self.meshManager.rx = self.meshManager.ry = self.meshManager.rz = 0
    self.yawInfo.setText("0")
    self.pitchInfo.setText("0")
    self.rollInfo.setText("0")
    self.yawSlider.setValue(0)
    self.pitchSlider.setValue(0)
    self.rollSlider.setValue(0)
    self.draw() #we redraw the frame


  def resetTHSEvent(self):
    self.meshManager.temperature = self.meshManager.hue = 0
    self.meshManager.saturation = 1
    self.temperatureInfo.setText("0")
    self.hueInfo.setText("0")
    self.saturationInfo.setText("1")
    self.temperatureSlider.setValue(0)
    self.hueSlider.setValue(0)
    self.saturationSlider.setValue(1)
    self.draw() #we redraw the frame


  def resetBCEvent(self):
    self.meshManager.brightness = self.meshManager.contrast = 0
    self.brightnessInfo.setText("0")
    self.contrastInfo.setText("0")
    self.brightnessSlider.setValue(0)
    self.contrastSlider.setValue(0)
    self.draw() #we redraw the frame

  
  def sliderChanged(self):
    """ Event call at each videoSlider changements. Set the new frame """
    self.isPlaying = False
    if(self.videoSlider.value() + 1 == self.videoManager.currentFrameNumber): # if the value is the same, we not reset the frame
      return
    self.videoManager.setFrame(self.videoSlider.value() + 1, self.draw)
    
    
  def confidenceChanged(self):
    """ Event call at each confidenceSlider changements. Change the confThreshold and redraw the frame """
    self.faceDetector.confThreshold = self.confidenceSlider.value() / 100.
    self.confidenceInfo.setText("{0:.2f}".format(self.faceDetector.confThreshold))
    self.draw() #we redraw the frame


  def fovyChanged(self):
    """ Event call at each fovySlider changements. Change the fovy and redraw the frame """
    self.meshManager.fovy = self.fovySlider.value()
    self.fovyInfo.setText(str(self.meshManager.fovy))
    self.draw() #we redraw the frame


  def yawChanged(self):
    """ Event call at each yawSlider changements. Change the fovy and redraw the frame """
    self.meshManager.rz = self.yawSlider.value()
    self.yawInfo.setText(str(self.meshManager.rz))
    self.draw() #we redraw the frame


  def pitchChanged(self):
    """ Event call at each pitchSlider changements. Change the fovy and redraw the frame """
    self.meshManager.rx = self.pitchSlider.value()
    self.pitchInfo.setText(str(self.meshManager.rx))
    self.draw() #we redraw the frame


  def rollChanged(self):
    """ Event call at each rollSlider changements. Change the fovy and redraw the frame """
    self.meshManager.ry = self.rollSlider.value()
    self.rollInfo.setText(str(self.meshManager.ry))
    self.draw() #we redraw the frame
    
    
  def temperatureChanged(self):
    """ Event call at each temperatureSlider changements. Change the fovy and redraw the frame """
    self.meshManager.temperature = self.temperatureSlider.value()
    self.temperatureInfo.setText(str(self.meshManager.temperature))
    self.draw() #we redraw the frame
    
    
  def saturationChanged(self):
    """ Event call at each saturationSlider changements. Change the fovy and redraw the frame """
    self.meshManager.saturation = self.saturationSlider.value()
    self.saturationInfo.setText(str(self.meshManager.saturation))
    self.draw() #we redraw the frame


  def hueChanged(self):
    """ Event call at each hueSlider changements. Change the fovy and redraw the frame """
    self.meshManager.hue = self.hueSlider.value()
    self.hueInfo.setText(str(self.meshManager.hue))
    self.draw() #we redraw the frame


  def brightnessChanged(self):
    """ Event call at each brightnessSlider changements. Change the fovy and redraw the frame """
    self.meshManager.brightness = self.brightnessSlider.value()
    self.brightnessInfo.setText(str(self.meshManager.brightness))
    self.draw() #we redraw the frame


  def contrastChanged(self):
    """ Event call at each contrastSlider changements. Change the fovy and redraw the frame """
    self.meshManager.contrast = self.contrastSlider.value()
    self.contrastInfo.setText(str(self.meshManager.contrast))
    self.draw() #we redraw the frame
      
      
  def screenshotEvent(self):
    """ Event call at each click on screenshot_PB. Opens a save selection window and save the screenshot. """
    if self.videoManager.isLoaded() == False:
      return
    
    # Default path = VIDEO_PATH/VIDEO_NAME(without extension)-frame(currentFrameNumber)
    defaultPath = os.path.splitext(self.videoManager.videoPath)[0] + "-frame" + str(self.videoManager.currentFrameNumber)
    
    # Open save file window 
    fileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Save the screenshot', defaultPath, "PNG (*.png);;JPEG (*.jpg)")[0]
    
    # Screenshot
    self.screenshot(fileName)
    print("Screenshot save at", fileName)
    
    
  def selectVideo(self):
    """ Event call at each click on actionOpen_video. Opens a video selection window and load the selected video """
    fileFilter = "*." + " *.".join(self.videoFormats)
    fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Video', '../', "Video Files (%s)" % (fileFilter))[0]
    if fileName != '':
      self.loadVideo(str(fileName))
  
  
  def selectModel(self):
    """ Event call at each click on actionOpen_model. Opens a mesh selection window and load the selected mesh """
    fileFilter = "*." + " *.".join(self.meshFormats)
    fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Select 3D Model', '../', "3D Model (%s)" % (fileFilter))[0]
    if fileName != '':
      self.loadModel(str(fileName))

    
  def stopFaceDetector(self):
    """ Stop the frame calculation of the face detector """
    self.faceDetector.stop()
    

  def processAllVideo(self):
    """ Launch the getHeadPosition function for all frame from the current frame """
    # Set progress bar
    self.setProgressDialog("Get head position (%d/%d)" % (self.videoManager.currentFrameNumber, self.videoManager.frameCount), self.stopFaceDetector)
    
    # Get faces for all frames
    self.videoManager.getAllHeadPosition(self.updateProgressDialog, self.draw)
    
    # End progress bar
    self.updateProgressDialog(1.0, "End of the faces calculation")
    

  def getHeadPosition(self):
    """ Launch the calculation to get the faces of the current frame and saves it in the cache file """
    # test if the faces have already been calculated on this frame
    if self.videoManager.isFacesLoaded():
      return
    
    # Set progress bar
    self.setProgressDialog("Get head position (%d/%d)" % (self.videoManager.currentFrameNumber, self.videoManager.frameCount), self.stopFaceDetector)
    
    # Get faces
    data = self.videoManager.getHeadPosition(self.updateProgressDialog)
    
    # Redraw the frame
    self.draw()
    
    # End progress bar
    self.updateProgressDialog(1.0, "End of the faces calculation")
    
    # return 
    return data


  #################################
  ### === EVENTS ON RESIZE  === ###
  #################################

  @debounce(0.1)
  def resizeProcessTable(self, event=None):
    if self.videoManager.isLoaded() == False:
      return
    width = self.videoProcessTable.frameGeometry().width()
    halfCellWidth = width / (self.videoManager.frameCount * 2.)
    cellWidth = width / (self.videoManager.frameCount - 1)
    rest = 0.
    for i in range(1, self.videoManager.frameCount - 1):
      realCellWidth = cellWidth + rest
      rest = realCellWidth % 1
      self.videoProcessTable.setColumnWidth(i, realCellWidth)
    # we reduce by half the first and last cell to match with the slider below
    self.videoProcessTable.setColumnWidth(self.videoManager.frameCount - 1, math.floor(halfCellWidth))
    self.videoProcessTable.setColumnWidth(0, math.ceil(halfCellWidth))

  
  def resizeEvent(self, event):
    """ Event call at each resize. Resize the window and update the VideoWidget """
    self.maxWidth = self.VideoWidget.geometry().width()
    self.maxHeight = self.VideoWidget.geometry().height()
    self.draw() #we redraw the frame



  #################################
  ### ====   PROGRESS BAR  ==== ###
  #################################
  
  def setProgressDialog(self, title="Traitement", stopCallback=None):
    """ Create the QProgressDialog and show it """
    self.progressDialog.setWindowTitle(title)
    self.progressDialog.setMinimumWidth(400)
    button = self.progressDialog.findChildren(QtWidgets.QPushButton)[0] #get cancel button
    if stopCallback != None:
      button.show()
      self.progressDialog.canceled.connect(stopCallback)
    else:
      button.hide()
    self.progressDialog.show()


  def updateProgressDialog(self, percentage, msg='', title=''):
    """ Update the QProgressDialog """
    self.progressDialog.setValue(percentage * 100)
    if msg != '':
      self.progressDialog.setLabelText(msg)
    if title != '':
      self.progressDialog.setWindowTitle(title)
    if percentage >= 1.:
      self.progressDialog.reset()
    QtCore.QCoreApplication.processEvents()
 
  
  
  #################################
  ### ====     LOADING     ==== ###
  #################################
  
  def load(self, jsonFile):
    """ Loads data with JSON configuration file """
    if not os.path.exists(jsonFile):
      sys.exit('ERROR : Configuration file does not exist')
    with open(jsonFile) as json_file:
      data = json.load(json_file)
      self.snapshot = data['snapshot']
      self.face_model = data['face_model']
      self.gpu_id = data['gpu_id']   
      self.cache_string = data['cache_string']
      self.videoFormats = data['video_formats']
      self.meshFormats = data['mesh_formats']
      
    self.loadFaceDetector()
    self.confidenceChanged()


  def loadFaceDetector(self):
    """ Init and load FaceDetector class """
    self.setProgressDialog("Load Face Detector")
    self.faceDetector = FaceDetector(self.face_model, self.snapshot, self.gpu_id)
    self.confidenceSlider.setValue(self.faceDetector.confThreshold * 100)
    self.faceDetector.load(self.updateProgressDialog)
    self.videoManager.faceDetector = self.faceDetector


  def loadModel(self, fileName):
    """ Load a 3D model """
    self.meshManager.load(fileName)
    
    # we draw the first frame
    self.draw() 
    
    
  def loadVideo(self, fileName):
    """ Load a video """
    self.setProgressDialog("Loading video")
    
    self.videoManager.load(fileName, self.cache_string, self.updateProgressDialog)
    
    self.updateProgressDialog(0.9, "Initializing OpenGL context")

    # InitGL context with video size
    width = int(self.videoManager.video.get(3))
    height = int(self.videoManager.video.get(4))
    self.meshManager.viewWidth = width
    self.meshManager.viewHeight = height
    self.meshManager.initGL()
    
    self.updateProgressDialog(0.95, "Update layers")
    
    # we set the slider and enabled all buttons
    self.videoSlider.setMaximum(self.videoManager.frameCount - 1) 
    self.setEnabledButtons(True)
    
    # and we load the process table view
    self.initProcessTable()
    
    # we draw the first frame
    self.draw() 
    
    self.updateProgressDialog(1.0, "The video is loaded")


  def initProcessTable(self):
    """ Create the process table according to the video (the colored table that shows the loaded frames below the video) """
    if self.videoManager.frameCount > 30000: # if the number of frames is too many, we mask the process table
      self.videoProcessTable.hide()
      return 
    self.videoProcessTable.show()
    self.videoProcessTable.setColumnCount(self.videoManager.frameCount)
    for i in range(self.videoManager.frameCount):
      item = QtWidgets.QTableWidgetItem()
      self.videoProcessTable.setItem(0, i, item)
      self.updateProcessTable(i)
    self.resizeProcessTable()
  
  
    
  #################################
  ### ====     ACTIONS     ==== ###
  #################################
  
  def screenshot(self, path):
    """ Take a screenshot of both windows (with zooms) and save it in 'path' """
    if self.videoManager.isLoaded() == False or self.meshManager.isLoaded() == False:
      return

    # get currents frames QPixmap
    videoScreen = self.VideoWidget.grab()
    meshScreen = self.GLWidget.grab()
    
    # coordinates
    width = videoScreen.width() + meshScreen.width()
    height = max(videoScreen.height(), meshScreen.height())
    leftRect = QtCore.QRectF(0, 0, videoScreen.width(), height)
    rightRect = QtCore.QRectF(videoScreen.width(), 0, meshScreen.width(), height)
    
    # screenshot initialisation
    screenshot = QtGui.QPixmap(width, height)
    
    # we paint the two frames
    painter = QtGui.QPainter(screenshot)
    painter.begin(self)
    painter.drawPixmap(leftRect, videoScreen, QtCore.QRectF(videoScreen.rect()))
    painter.drawPixmap(rightRect, meshScreen, QtCore.QRectF(meshScreen.rect()))
    painter.end()
    
    # we save the screenshot
    screenshot.save(path, 'png')
    
  
  def setEnabledButtons(self, isEnable=True):
    """ Enable all buttons (or disable is 'isEnable' is False). """
    self.last10Frame_PB.setEnabled(isEnable)
    self.lastFrame_PB.setEnabled(isEnable)
    self.read_PB.setEnabled(isEnable)
    self.pause_PB.setEnabled(isEnable)
    self.nextFrame_PB.setEnabled(isEnable)
    self.next10Frame_PB.setEnabled(isEnable)
    self.headPosition_PB.setEnabled(isEnable)
    self.processAllVideo_PB.setEnabled(isEnable)
    self.screenshot_PB.setEnabled(isEnable)
    self.coordinates_PB.setEnabled(isEnable)
    self.square_BT.setEnabled(isEnable)
    
    
    
  #################################
  ### ====     DRAWING     ==== ###
  #################################

  def drawVideo(self):
    """ Draw the current video frame on the screens """
    # get the current video frame
    pixmap, index = self.videoManager.frame()
    
    # draw it
    self.drawOn(pixmap, self.VideoWidget)
    
    # update the slider
    self.videoSlider.setValue(index - 1)
    
    # update the processTable
    self.updateProcessTable(index - 1)


  def drawGL(self):
    # get faces
    faces = self.videoManager.faces()
    # get the mesh frame
    pixmap = self.meshManager.frame(faces)
    # draw it
    self.drawOn(pixmap, self.GLWidget)
    
    
  def draw(self):
    """ Draw the video and the mesh"""
    if self.videoManager.isLoaded() == False:
      return
    self.drawVideo()
    self.drawGL()
    self.updateInfo()
    
    
  def drawOn(self, cv_image, widget):
    """ Draw the 'pixmap' on the QGraphicsView 'widget' by applying the zoom and the displacements """
    

    # Convert cv_image to QT format
    convertToQtFormat = QtGui.QImage(cv_image.data, cv_image.shape[1], cv_image.shape[0], QtGui.QImage.Format_RGB888)
    convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
    pixmap = QtGui.QPixmap(convertToQtFormat)

    # Resize with zoom
    pixmap = pixmap.scaled(self.maxWidth * self.zoom, self.maxHeight * self.zoom, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
    
    # Add image
    scene = QtWidgets.QGraphicsScene() 
    scene.addItem(QtWidgets.QGraphicsPixmapItem(pixmap))
    widget.setScene(scene) 
    
    #Center on the appropriate position
    widget.centerOn(self.centerX, self.centerY)
  
  
  
  #################################
  ### ====     UPDATE      ==== ###
  #################################


  def updateInfo(self):
    """ Update the frame informations displayed on the screen and disabled headPosition_PB if faces are already loaded """
    
    # Frame information
    frameInfo = "Frame: " + str(int(self.videoManager.currentFrameNumber)) + "/" + str(int(self.videoManager.frameCount))
    self.frameInfo.setText(frameInfo)
    
    # Data information
    currentData = self.videoManager.getCurrentCacheData()
    if(currentData['isLoaded']):
      
      # disabled headPosition_PB
      self.headPosition_PB.setEnabled(False)
      
      # show face(s) information
      faceNumber = currentData['faces'].__len__()
      if(faceNumber > 0):
        facesInfo = str(faceNumber) + " face(s) detected"
        self.facesInfo.setStyleSheet("color: rgb(0, 153, 0);")
      else:
        facesInfo = "No face was detected"
        self.facesInfo.setStyleSheet("color: rgb(255, 102, 0);")
    else:
      # enabled headPosition_PB
      self.headPosition_PB.setEnabled(True)
      
      # show face information
      facesInfo = "Frame not process"
      self.facesInfo.setStyleSheet("color: rgb(255, 0, 0);")
    self.facesInfo.setText(facesInfo)
   

  def updateProcessTable(self, index):
    """ Update the frame informations displayed on the screen """
    if not self.videoProcessTable.isVisible(): # if videoProcessTable is not set (to much frames)
      return 
    bg = QtGui.QColor(153, 153, 153) #default background (gray)
    data = self.videoManager.getCacheData(index)
    # if a frame is loas
    if(data['isLoaded']):
      # Frame with faces
      if(data['faces'].__len__() > 0):
        bg = QtGui.QColor(0, 153, 0)
      # Frame without faces
      else:
        bg = QtGui.QColor(255, 102, 0)
    self.videoProcessTable.item(0, index).setBackground(bg)
    

  def update(self):
    """ Update function to call in loop """
    # PLAY THE VIDEO
    if(self.videoManager.isPlaying):
      self.videoManager.read()
      self.draw()
      
      # FPS CONTROLLER
      elapsedTime = timeit.default_timer() - self.lastUpdate
      if (elapsedTime < 1. / self.videoManager.fps): 
        time.sleep(1. / self.videoManager.fps - elapsedTime)

    self.lastUpdate = timeit.default_timer()

  


if __name__ == '__main__':
  sys._excepthook = sys.excepthook 
  def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback) 
    sys.exit(1) 
  sys.excepthook = exception_hook 
  
  args = parse_args()
 
  
  app = QtWidgets.QApplication(sys.argv)
  window = MainWindow()
  window.show()

  window.load(args.config_path)

  if(args.mesh_path != ""): 
    window.loadModel(args.mesh_path);
  
  if(args.video_path != ""): 
    window.loadVideo(args.video_path);
  
  timer = QtCore.QTimer()
  timer.timeout.connect(window.update)
  timer.start(10)

  sys.exit(app.exec_())