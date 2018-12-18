
import os
from os.path import join, dirname
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog

from qgis.core import (
    QgsDataSourceUri,
    QgsFeature,
    QgsVectorLayer,
    QgsVectorLayerCache,
)
from qgis.gui import (
    QgsAttributeEditorContext,
    QgsAttributeForm,
    QgsAttributeTableModel,
    QgsAttributeTableFilterModel,
    QgsMapCanvas,
)

FORM_CLASS, _ = uic.loadUiType(join(dirname(__file__), 'application.ui'))


class ApplicationDialog(QDialog, FORM_CLASS):

    def __init__(self, parent):
        QDialog.__init__(self)
        self.setupUi(self)

        uri = QgsDataSourceUri()
        uri.setConnection('localhost', '5432', 'etienne', 'postgres', os.environ['APP_PASSWORD'])
        uri.setDataSource('public', 'equipements', None)
        self.layer = QgsVectorLayer(uri.uri(False), 'equipements', 'postgres')

        self.layer_cache = QgsVectorLayerCache(self.layer, 120)
        self.model = QgsAttributeTableModel(self.layer_cache)
        self.model.loadLayer()

        tbl_filter_model = QgsAttributeTableFilterModel(QgsMapCanvas(), self.model)

        self.attribute_table.setModel(tbl_filter_model)
        self.attribute_table.resizeRowsToContents()
        self.attribute_table.resizeColumnsToContents()

        self.add_item.clicked.connect(self.add_new_item)

        self.exec_()

    def add_new_item(self):
        feature = QgsFeature()

        attribute_form = QgsAttributeForm(self.layer, parent=self)
        attribute_form.setMode(QgsAttributeEditorContext.AddFeatureMode)

        attribute_form.show()

        # add_feature_dialog = QgsAttributeDialog(self.layer, feature, True, self)
        # add_feature_dialog.show()
