# -*- coding: utf-8 -*-

import os
import sys

from PyQt4.QtGui import QWidget, QBoxLayout, QLabel, QPushButton

from roam.api.plugins import Page

pydev_path = '/home/lmotta/eclipse/plugins/org.python.pydev_3.9.2.201502050007/pysrc/'

class RemoteDebug(QWidget, Page):
  title = "Remote Debug Eclipse"
  icon = os.path.join( os.path.dirname(__file__), "icon.png" )

  def __init__(self, api, parent=None):

    def setupUi():
      layout = QBoxLayout( QBoxLayout.LeftToRight, self )
      layout.setContentsMargins( 0, 0, 0, 0 )
      self.label = QLabel('Not active debugger', self)
      layout.addWidget( self.label )
      self.btnRun = QPushButton( "Run debugger", self )
      layout.addWidget( self.btnRun )
      self.setLayout( layout )
      self.btnRun.clicked.connect( self.run )

    super(RemoteDebug, self).__init__(parent)
    setupUi()
    sys.path.append(pydev_path)

  def run(self):
    self.btnRun.setEnabled( False )
    self.btnRun.hide()
    started = False
    try:
      import pydevd
      pydevd.settrace(port=5678, suspend=False)
      started = True
      self.label.setText( u"PyDev debugging active" )
    except:
      pass
    if not started:
      self.label.setText( u"Debugging connection failed" )


def pages():
  return [ RemoteDebug ]

