# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stationlines.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StationLines(object):
    def setupUi(self, StationLines):
        StationLines.setObjectName("StationLines")
        StationLines.resize(338, 648)
        self.verticalLayout = QtWidgets.QVBoxLayout(StationLines)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label = QtWidgets.QLabel(StationLines)
        self.label.setObjectName("label")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.combo_layer = QtWidgets.QComboBox(StationLines)
        self.combo_layer.setObjectName("combo_layer")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_layer)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.chk_selectedFeatures = QtWidgets.QCheckBox(StationLines)
        self.chk_selectedFeatures.setObjectName("chk_selectedFeatures")
        self.verticalLayout.addWidget(self.chk_selectedFeatures)
        self.choices_groupbox = QtWidgets.QGroupBox(StationLines)
        self.choices_groupbox.setObjectName("choices_groupbox")
        self.gridLayout = QtWidgets.QGridLayout(self.choices_groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.chk_distance = QtWidgets.QCheckBox(self.choices_groupbox)
        self.chk_distance.setObjectName("chk_distance")
        self.gridLayout.addWidget(self.chk_distance, 1, 0, 1, 1)
        self.chk_vertices = QtWidgets.QCheckBox(self.choices_groupbox)
        self.chk_vertices.setChecked(True)
        self.chk_vertices.setObjectName("chk_vertices")
        self.gridLayout.addWidget(self.chk_vertices, 0, 0, 1, 1)
        self.distance_groupbox = QtWidgets.QGroupBox(self.choices_groupbox)
        self.distance_groupbox.setEnabled(False)
        self.distance_groupbox.setObjectName("distance_groupbox")
        self.formLayout_5 = QtWidgets.QFormLayout(self.distance_groupbox)
        self.formLayout_5.setObjectName("formLayout_5")
        self.but_distance_field = QtWidgets.QRadioButton(self.distance_groupbox)
        self.but_distance_field.setChecked(False)
        self.but_distance_field.setAutoExclusive(True)
        self.but_distance_field.setObjectName("but_distance_field")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.but_distance_field)
        self.combo_distance_field = QtWidgets.QComboBox(self.distance_groupbox)
        self.combo_distance_field.setEnabled(False)
        self.combo_distance_field.setObjectName("combo_distance_field")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_distance_field)
        self.but_distance_value = QtWidgets.QRadioButton(self.distance_groupbox)
        self.but_distance_value.setChecked(True)
        self.but_distance_value.setObjectName("but_distance_value")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.but_distance_value)
        self.spin_distance_value = QtWidgets.QDoubleSpinBox(self.distance_groupbox)
        self.spin_distance_value.setEnabled(False)
        self.spin_distance_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin_distance_value.setDecimals(3)
        self.spin_distance_value.setMaximum(9999.99)
        self.spin_distance_value.setProperty("value", 10.0)
        self.spin_distance_value.setObjectName("spin_distance_value")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_distance_value)
        self.gridLayout.addWidget(self.distance_groupbox, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.choices_groupbox)
        self.side_groupbox = QtWidgets.QGroupBox(StationLines)
        self.side_groupbox.setObjectName("side_groupbox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.side_groupbox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.but_side_field = QtWidgets.QRadioButton(self.side_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_side_field.sizePolicy().hasHeightForWidth())
        self.but_side_field.setSizePolicy(sizePolicy)
        self.but_side_field.setObjectName("but_side_field")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.but_side_field)
        self.but_side_value = QtWidgets.QRadioButton(self.side_groupbox)
        self.but_side_value.setChecked(True)
        self.but_side_value.setObjectName("but_side_value")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.but_side_value)
        self.combo_side_value = QtWidgets.QComboBox(self.side_groupbox)
        self.combo_side_value.setObjectName("combo_side_value")
        self.combo_side_value.addItem("")
        self.combo_side_value.addItem("")
        self.combo_side_value.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.combo_side_value)
        self.combo_side_field = QtWidgets.QComboBox(self.side_groupbox)
        self.combo_side_field.setEnabled(False)
        self.combo_side_field.setEditable(False)
        self.combo_side_field.setObjectName("combo_side_field")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_side_field)
        self.verticalLayout.addWidget(self.side_groupbox)
        self.length_groupbox = QtWidgets.QGroupBox(StationLines)
        self.length_groupbox.setObjectName("length_groupbox")
        self.formLayout = QtWidgets.QFormLayout(self.length_groupbox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.but_length_field = QtWidgets.QRadioButton(self.length_groupbox)
        self.but_length_field.setChecked(False)
        self.but_length_field.setAutoExclusive(True)
        self.but_length_field.setObjectName("but_length_field")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.but_length_field)
        self.combo_length_field = QtWidgets.QComboBox(self.length_groupbox)
        self.combo_length_field.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_length_field.sizePolicy().hasHeightForWidth())
        self.combo_length_field.setSizePolicy(sizePolicy)
        self.combo_length_field.setObjectName("combo_length_field")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_length_field)
        self.but_length_value = QtWidgets.QRadioButton(self.length_groupbox)
        self.but_length_value.setChecked(True)
        self.but_length_value.setObjectName("but_length_value")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.but_length_value)
        self.spin_length_value = QtWidgets.QDoubleSpinBox(self.length_groupbox)
        self.spin_length_value.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_length_value.sizePolicy().hasHeightForWidth())
        self.spin_length_value.setSizePolicy(sizePolicy)
        self.spin_length_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spin_length_value.setDecimals(3)
        self.spin_length_value.setMaximum(99999.0)
        self.spin_length_value.setProperty("value", 10.0)
        self.spin_length_value.setObjectName("spin_length_value")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_length_value)
        self.verticalLayout.addWidget(self.length_groupbox)
        self.angle_groupbox = QtWidgets.QGroupBox(StationLines)
        self.angle_groupbox.setObjectName("angle_groupbox")
        self.formLayout_3 = QtWidgets.QFormLayout(self.angle_groupbox)
        self.formLayout_3.setObjectName("formLayout_3")
        self.but_angle_field = QtWidgets.QRadioButton(self.angle_groupbox)
        self.but_angle_field.setChecked(False)
        self.but_angle_field.setAutoExclusive(True)
        self.but_angle_field.setObjectName("but_angle_field")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.but_angle_field)
        self.combo_angle_field = QtWidgets.QComboBox(self.angle_groupbox)
        self.combo_angle_field.setEnabled(False)
        self.combo_angle_field.setObjectName("combo_angle_field")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_angle_field)
        self.but_angle_value = QtWidgets.QRadioButton(self.angle_groupbox)
        self.but_angle_value.setChecked(True)
        self.but_angle_value.setObjectName("but_angle_value")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.but_angle_value)
        self.spin_angle_value = QtWidgets.QDoubleSpinBox(self.angle_groupbox)
        self.spin_angle_value.setEnabled(True)
        self.spin_angle_value.setDecimals(3)
        self.spin_angle_value.setMaximum(360.0)
        self.spin_angle_value.setProperty("value", 90.0)
        self.spin_angle_value.setObjectName("spin_angle_value")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_angle_value)
        self.verticalLayout.addWidget(self.angle_groupbox)
        self.buttonBox = QtWidgets.QDialogButtonBox(StationLines)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(StationLines)
        self.combo_side_value.setCurrentIndex(2)
        self.buttonBox.accepted.connect(StationLines.accept)
        self.buttonBox.rejected.connect(StationLines.reject)
        QtCore.QMetaObject.connectSlotsByName(StationLines)

    def retranslateUi(self, StationLines):
        _translate = QtCore.QCoreApplication.translate
        StationLines.setWindowTitle(_translate("StationLines", "Station Lines"))
        self.label.setText(_translate("StationLines", "Layer"))
        self.chk_selectedFeatures.setText(_translate("StationLines", "Use only selected features"))
        self.choices_groupbox.setTitle(_translate("StationLines", "Stations choices"))
        self.chk_distance.setText(_translate("StationLines", "Distance"))
        self.chk_vertices.setText(_translate("StationLines", "Vertices"))
        self.distance_groupbox.setTitle(_translate("StationLines", "Distance"))
        self.but_distance_field.setText(_translate("StationLines", "Field"))
        self.but_distance_value.setText(_translate("StationLines", "Va&lue"))
        self.side_groupbox.setTitle(_translate("StationLines", "Side"))
        self.but_side_field.setText(_translate("StationLines", "Field"))
        self.but_side_value.setText(_translate("StationLines", "Val&ue"))
        self.combo_side_value.setItemText(0, _translate("StationLines", "Right"))
        self.combo_side_value.setItemText(1, _translate("StationLines", "Left"))
        self.combo_side_value.setItemText(2, _translate("StationLines", "Both"))
        self.length_groupbox.setTitle(_translate("StationLines", "Length"))
        self.but_length_field.setText(_translate("StationLines", "Field"))
        self.but_length_value.setText(_translate("StationLines", "Value"))
        self.angle_groupbox.setTitle(_translate("StationLines", "Angle"))
        self.but_angle_field.setText(_translate("StationLines", "Field"))
        self.but_angle_value.setText(_translate("StationLines", "Value"))
