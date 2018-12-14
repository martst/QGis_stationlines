# -*- coding: utf-8 -*-
"""
/***************************************************************************
 StationLines
                                 A QGIS plugin
 Create lines along a polyline with specifications (length, side, angle)
                              -------------------
        begin                : 2014-04-11
        copyright            : (C) 2014 by Loïc BARTOLETTI
        email                : l.bartoletti@free.fr
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
from __future__ import absolute_import
# Import the PyQt and QGIS libraries
from builtins import zip
from builtins import str
from builtins import object
from qgis.PyQt.QtCore import (
    QCoreApplication,
    QSettings,
    QTranslator,
    QVariant
)
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from qgis.core import (
    Qgis,
    QgsApplication,
    QgsMapLayer,
    QgsWkbTypes
)
from qgis.gui import QgsMessageBar
# Initialize Qt resources from file resources.py
from . import resources_rc
# Import the code for the dialog
from .stationlinesdialog import StationLinesDialog
import os.path

# Import outils
from .stationlines_utils import *
from .stationlines_algo import *
from .stationlines_side import *

class StationLines(object):

    #####################################################
    #                                                   #
    #                   INITIALISATION                  #
    #                                                   #
    #####################################################
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'stationlines_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)
            QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = StationLinesDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/stationlines/icon.png"),
            u"Station Lines", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Station Lines", self.action)
        self.iface.addPluginToVectorMenu(u"&Station Lines", self.action)

        # help
        self.dlg.buttonBox.helpRequested.connect(self.show_help)

        # Init slots
        self.dlg.chk_distance.clicked.connect(self._slotChkDistanceClicked) # checkbox distance

        self.dlg.but_distance_field.clicked.connect(self._slotFieldDistanceClicked) # radio button Field Distance
        self.dlg.but_distance_value.clicked.connect(self._slotValueDistanceClicked) # radio button Value Distance

        self.dlg.but_side_field.clicked.connect(self._slotFieldSideClicked) # radio button Field Side
        self.dlg.but_side_value.clicked.connect(self._slotValueSideClicked) # radio button Value Side

        self.dlg.but_length_field.clicked.connect(self._slotFieldLengthClicked) # radio button Field Length
        self.dlg.but_length_value.clicked.connect(self._slotValueLengthClicked) # radio button Value Length

        self.dlg.but_angle_field.clicked.connect(self._slotFieldAngleClicked) # radio button Field Angle
        self.dlg.but_angle_value.clicked.connect(self._slotValueAngleClicked) # radio button Value Angle

        self.dlg.combo_layer.currentIndexChanged.connect(self._slotComboLayerChanged)


    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Station Lines", self.action)
        self.iface.removePluginVectorMenu(u"&Station Lines", self.action)
        self.iface.removeToolBarIcon(self.action)

    # Définitions et actions des slots

    # Méthode appelée quand on clique sur la checkbox distance
    def _slotChkDistanceClicked(self):
        if self.dlg.chk_distance.isChecked() == True:
            self.dlg.distance_groupbox.setEnabled(True)
            if self.dlg.but_distance_value.isChecked() == True:
                self.dlg.spin_distance_value.setEnabled(True)
                self.dlg.combo_distance_field.setEnabled(False)
            else:
                self.dlg.spin_distance_value.setEnabled(False)
                self.dlg.combo_distance_field.setEnabled(True)
        else:
            self.dlg.distance_groupbox.setEnabled(False)

    # Si le combo du Layer à changé
    def _slotComboLayerChanged(self):
        self.dlg.combo_distance_field.clear()
        self.dlg.combo_length_field.clear()
        self.dlg.combo_angle_field.clear()
        self.dlg.combo_side_field.clear()
        self._getIdNameOfLayer()
        self._getStringFieldsFromLayer()
        self._getNumericFieldsFromLayer()

    # Radiobuttons Distance
    def _slotFieldDistanceClicked(self):
        self.dlg.spin_distance_value.setEnabled(False)
        self.dlg.combo_distance_field.setEnabled(True)
    def _slotValueDistanceClicked(self):
        self.dlg.spin_distance_value.setEnabled(True)
        self.dlg.combo_distance_field.setEnabled(False)

    # Radiobuttons Side
    def _slotFieldSideClicked(self):
        self.dlg.combo_side_value.setEnabled(False)
        self.dlg.combo_side_field.setEnabled(True)
    def _slotValueSideClicked(self):
        self.dlg.combo_side_value.setEnabled(True)
        self.dlg.combo_side_field.setEnabled(False)

    # Radiobuttons Length
    def _slotFieldLengthClicked(self):
        self.dlg.spin_length_value.setEnabled(False)
        self.dlg.combo_length_field.setEnabled(True)
    def _slotValueLengthClicked(self):
        self.dlg.spin_length_value.setEnabled(True)
        self.dlg.combo_length_field.setEnabled(False)

    # Radiobuttons Angle
    def _slotFieldAngleClicked(self):
        self.dlg.spin_angle_value.setEnabled(False)
        self.dlg.combo_angle_field.setEnabled(True)
    def _slotValueAngleClicked(self):
        self.dlg.spin_angle_value.setEnabled(True)
        self.dlg.combo_angle_field.setEnabled(False)

    #####################################################
    #                                                   #
    #                   PARAMETRES                      #
    #                                                   #
    #####################################################

    def _getFeatures(self):
        if self.dlg.chk_selectedFeatures.isChecked() and self.nb_features:
            feat = self.layer.selectedFeatures()
        else:
            feat = self.layer.getFeatures()

        return feat


    # Récupère les paramètres - fonction appellée quand on clique sur OK
    def _getParam(self):
        self.nodes = self.dlg.chk_vertices.isChecked()
        self.distance_choice = self.dlg.chk_distance.isChecked()
        self.params = []
        self.selectedFeatures = self.dlg.chk_selectedFeatures.isChecked()
        if self.selectedFeatures:
            self.nb_features = self.layer.selectedFeatureCount()
            if not self.nb_features:
                self.nb_features = self.layer.featureCount()
        else:
            self.nb_features = self.layer.featureCount()

        # Side
        if self.dlg.but_side_field.isChecked():
            list_side = []
            feature = self._getFeatures()
            for f in feature:
                att = f.attribute(self.dlg.combo_side_field.currentText())
                try:
                    if att.capitalize() in ["Right", "Left", "Both", "0", "1", "2"]:
                        if att.capitalize() == "Right" or att == "0":
                            list_side.append(Side.Right)
                        elif att.capitalize() == "Left" or att == "1":
                            list_side.append(Side.Left)
                        elif att.capitalize() == "Both" or att == "2":
                            list_side.append(Side.Both)
                        else:
                            title = QCoreApplication.translate("StationLines", "Side error", None, QApplication.UnicodeUTF8)
                            message = QCoreApplication.translate("StationLines", "Error at line : "+ str(f.id()), None, QApplication.UnicodeUTF8)
                            iface.messageBar().pushMessage(title, message, level=Qgis.Critical)
                            # Bug !
                            return False
                except:
                    title = QCoreApplication.translate("StationLines", "Side error", None, QApplication.UnicodeUTF8)
                    message = QCoreApplication.translate("StationLines", "Error at line : "+ str(f.id()), None, QApplication.UnicodeUTF8)
                    iface.messageBar().pushMessage(title, message, level=Qgis.Critical)
                    return False
            self.params.append(list_side)
        else:
            self.params.append([self.dlg.combo_side_value.currentIndex()] * self.nb_features)

        # Length
        if self.dlg.but_length_field.isChecked():
            feature = self._getFeatures()
            list_long = []
            for f in feature:
                try:
                    longueur = float(f.attribute(self.dlg.combo_length_field.currentText()))
                    list_long.append(longueur)
                except:
                    title = QCoreApplication.translate("StationLines", "Length error", None, QApplication.UnicodeUTF8)
                    message = QCoreApplication.translate("StationLines", "Error at line : "+ str(f.id()), None, QApplication.UnicodeUTF8)
                    iface.messageBar().pushMessage(title, message, level=Qgis.Critical)
                    return False
            self.params.append(list_long)
        else:
            self.params.append([self.dlg.spin_length_value.value()] * self.nb_features)

        # Angle
        if self.dlg.but_angle_field.isChecked():
            feature = self._getFeatures()
            list_angle = []
            for f in feature:
                try:
                    angle = float(f.attribute(self.dlg.combo_angle_field.currentText()))
                    list_angle.append(angle)
                except:
                    title = QCoreApplication.translate("StationLines", "Angle error", None, QApplication.UnicodeUTF8)
                    message = QCoreApplication.translate("StationLines", "Error at line : "+ str(f.id()), None, QApplication.UnicodeUTF8)
                    iface.messageBar().pushMessage(title, message, level=Qgis.Critical)
                    return False

            self.params.append(list_angle)
        else:
            self.params.append([self.dlg.spin_angle_value.value()] * self.nb_features)

        # Distance
        if self.distance_choice == True:
            list_distance = []
            if self.dlg.but_distance_field.isChecked():
                feature = self._getFeatures()
                # Get each values
                for f in feature:
                    try:
                        dist = float(f.attribute(self.dlg.combo_distance_field.currentText()))
                        list_distance.append(dist)
                    except:
                        title = QCoreApplication.translate("StationLines", "Distance error", None, QApplication.UnicodeUTF8)
                        message = QCoreApplication.translate("StationLines", "Error at line : "+ str(f.id()), None, QApplication.UnicodeUTF8)
                        iface.messageBar().pushMessage(title, message, level=Qgis.Critical)
                        return False
                self.params.append(list_distance)
            else:
                self.params.append([self.dlg.spin_distance_value.value()] * self.nb_features) # Fill list with value
        else:
            self.params.append([] * self.nb_features)

        return True

    # Récupère l'ID et le Nom du layer
    def _getIdNameOfLayer(self):
        self.layer_name = self.dlg.combo_layer.currentText()
        if self.layer_name != '':
            self.id_of_layer = list(zip(*self.list_layer))[0][list(zip(*self.list_layer))[1].index(self.layer_name)]
            self.layer = self.canvas.layer(self.id_of_layer)

    # Récupère les champs numériques de la couche sélectionnée
    def _getNumericFieldsFromLayer(self):
        numericFields = [fields for id,fields in listFieldsFromLayer(self.layer, [QVariant.Int, QVariant.Double])]
        self.dlg.combo_distance_field.clear()
        self.dlg.combo_distance_field.addItems(numericFields)
        self.dlg.combo_length_field.clear()
        self.dlg.combo_length_field.addItems(numericFields)
        self.dlg.combo_angle_field.clear()
        self.dlg.combo_angle_field.addItems(numericFields)

    def _getStringFieldsFromLayer(self):
        self.dlg.combo_side_field.clear()
        self.dlg.combo_side_field.addItems([fields for id,fields in listFieldsFromLayer(self.layer, [QVariant.String])])


    def show_help(self):
        help_file = "file:///"+ self.plugin_dir + "/help/index.html"
        QDesktopServices.openUrl(QUrl(help_file))

    # run method that performs all the real work
    def run(self):
        # charge les couches vectorielles
        self.canvas = self.iface.mapCanvas()
        self.list_layer = listVectorLayer(self.canvas)
        # affiche dans la combobox
        self.dlg.combo_layer.clear()
        self.dlg.combo_layer.addItems([layers for id,layers in self.list_layer])

        # Initialise la variable du layer
        self._getIdNameOfLayer()
        # charge les champs
        if self.layer_name != '':
            self._getNumericFieldsFromLayer()
            self._getStringFieldsFromLayer()

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            self._runStationLines()



    def _runStationLines(self):
        if self._getParam() == False:
            return False
        if self.nodes == False and self.distance_choice == False:
            title = QCoreApplication.translate("StationLines", "Choices error", None, QApplication.UnicodeUTF8)
            message = QCoreApplication.translate("StationLines", "You need to check at least one options between Vertices and Distance : ", None, QApplication.UnicodeUTF8)
            iface.messageBar().pushMessage(title, message, level=Qgis.Critical)
            return False

        # Test si seulement géométries sélectionnées
        # layer
        vl = "LineString?crs="+self.layer.crs().authid()
        mem_layer = QgsVectorLayer(vl, "Station Lines", "memory")

        algo(mem_layer, self.layer, [self.nodes, self.distance_choice, self.selectedFeatures], self.params)

        QgsProject.instance().addMapLayer(mem_layer)

        # set extent to the extent of our layer
        self.canvas.setExtent(mem_layer.extent())

        # set the map canvas layer set
        self.canvas.setLayers([mem_layer])

