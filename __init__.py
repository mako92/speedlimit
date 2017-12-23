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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "SP" 
def description():
  return "Tool for matching speed limits"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load speedLimit_connector class from file speedLimit_connector
  from speedLimit_connector import speedLimit_connector 
  return speedLimit_connector(iface)
