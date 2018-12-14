from qgis.core import (
    QgsApplication,
    QgsConditionalStyle,
    QgsProject,
    QgsVectorLayer,
    QgsVectorLayerCache,
)
from qgis.gui import (
    QgsAttributeTableModel,
    QgsAttributeTableFilterModel,
    QgsAttributeTableView,
    QgsMapCanvas,
)
from qgis.PyQt.QtCore import QFileInfo
from qgis.PyQt.QtGui import QColor
from qgis.PyQt.QtWidgets import QPushButton, QVBoxLayout, QWidget

QGIS_PREFIX_PATH = '/home/trimaille/dev/app/local'
PROJECT_PATH = 'data/project.qgz'

QgsApplication.setPrefixPath(QGIS_PREFIX_PATH, True)

qgs = QgsApplication([], True)
qgs.initQgis()

project = QgsProject.instance()
mFile = QFileInfo(PROJECT_PATH)
project.read(mFile)

button = QPushButton('Ajout')
# button.clicked.connect(ajout)

layout = QVBoxLayout()
layout.addWidget(button)

window = QWidget()
window.setLayout(layout)
window.show()

canvas = QgsMapCanvas()

layer = QgsVectorLayer('data/data.geojson', 'layer', 'ogr')

style = QgsConditionalStyle()
style.setName('date peremption')
style.setRule("hiking='yes'")
style.setBackgroundColor(QColor(255, 0, 0, 127))
layer.conditionalStyles().setRowStyles([style])

lyr_cache = QgsVectorLayerCache(layer, 120, qgs)
tbl_model = QgsAttributeTableModel(lyr_cache, qgs)
# tbl_model.loadAttributes()
tbl_model.loadLayer()

# table_view = QTableView()
# table_view.setModel(tbl_model)
# table_view.show()

tbl_filter_model = QgsAttributeTableFilterModel(canvas, tbl_model, qgs)

editor = QgsAttributeTableView()
editor.setModel(tbl_filter_model)

layout.addWidget(editor)

# editor.show()

qgs.exec_()
qgs.exitQgis()
