"""
/***************************************************************************
Name			 	 : SP
Description          : Tool for matching speed limits
Date                 : 23/Dec/17 
copyright            : (C) 2017 by MK
email                : mateuszkob@wp.pl 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore, QtGui 
from Ui_speedLimit_connector import Ui_speedLimit_connector
# create the dialog for speedLimit_connector
class speedLimit_connectorDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_speedLimit_connector ()
    self.ui.setupUi(self)