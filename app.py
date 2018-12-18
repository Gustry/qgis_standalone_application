#!/usr/bin/env python3

from qgis.core import QgsApplication
from dialog import ApplicationDialog

QgsApplication.setPrefixPath('/home/etienne/dev/app/local/', True)
application = QgsApplication([], True)
application.initQgis()

dialog = ApplicationDialog(application)

application.exitQgis()
