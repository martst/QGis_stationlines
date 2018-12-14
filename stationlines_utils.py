# -*- coding:utf-8 -*-

from qgis.core import (
    QgsMapLayer,
    QgsWkbTypes
)
#from qgis.gui import *

def listVectorLayer(canvas):
    """ return all Vector Layers from a LayerType into a list
        input :
            canvas - The MapCanvas
        result :
            A list with a tuple : (An id, Name of the layer)"""
    m = canvas
    return [(id, x.name()) for id, x in enumerate(m.layers()) if x.type() == QgsMapLayer.VectorLayer and x.geometryType() == QgsWkbTypes.LineGeometry]

def listFieldsFromLayer(layer, fieldtype):
    """ return all Fields from a Layer
        input :
            layer - The Vector Layer
            fieldtype - List of type
        result :
            A list with a tuple : (An id, Name of the field)"""
    l = layer.dataProvider()
    return [(id, field.name()) for id, field in enumerate(l.fields()) if field.type() in fieldtype]


