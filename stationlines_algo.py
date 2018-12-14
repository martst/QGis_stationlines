#-*- coding:utf-8 -*-

from __future__ import absolute_import
from builtins import range
from qgis.core import *
from qgis.gui import *
from math import *
from .stationlines_side import *
from qgis.PyQt.QtCore import QVariant


def normalizeAngle(angle):
    """
    Normalize angle to be between 0 and 360

    :param angle: Angle ot normalize
    :type angle: float
    :return: angle normalized
    :rtype: float
    """
    signe = 1
    if angle < 0:
        signe = -1

    n = angle // 360

    angle -= n*360

    return signe*angle

def calcOrientationLigne(p1, p2):
    """
    Check if the x of first point is superior to the x of second point

    :param p1: The first point
    :param p2: The second point
    :type p1: list
    :type p2: list
    :return: -1 if p1.x > p2.x else 1
    :rtype: int
    """

    if p1[0] > p2[0]:
        return -1
    else:
        return 1

def calcPente(p1, p2):
    """
    Return the slope of the line represents by two points : p1 and p2

    :param p1: The first point
    :param p2: The second point
    :type p1: list
    :type p2: list
    :return: Return the slope (degre)
    :rtype: float
    """

    num = p1[0] - p2[0]
    denum = p1[1] - p2[1]

    # Avoid division by zero
    if num == 0:
        # Return a negative value if denum > 0
        if denum > 0:
            return -90
        else:
        # else return a positive value
            return 90
    # Same as above with denum
    elif denum == 0:
        if num > 0:
            return -90
        else:
            return 90
    else:
        return denum/num

def calcAngleExistant(p1, p2):
    """
    Return the angle of the line represents by two points : p1 and p2

    :param p1: The first point
    :param p2: The second point
    :type p1: list
    :type p2: list
    :return: Return the angle (degre)
    :rtype: float
    """

    a = calcPente(p1, p2) # The slope of the segment p1-p2
    length_p1p2 = calcDistance(p1, p2) # Hypotenuse
    length_adjacent = fabs(p2[1] - p1[1]) # Adjacent
    if length_p1p2 == 0: # Normally you can't have a length of 0 but avoid division by zero
        angle_CAB = 0
    else:
        angle_CAB = acos(length_adjacent/length_p1p2)

    # Correction of angle_CAB
    if a < 0:
        angle_CAB = angle_CAB - pi/2
    elif a > 0:
        angle_CAB = pi/2 - angle_CAB

    return angle_CAB

def calcDistance(p1, p2):
    """
    Return the length of the line represents by two points : p1 and p2

    :param p1: The first point
    :param p2: The second point
    :type p1: list
    :type p2: list
    :return: Return the length
    :rtype: int
    """

    return sqrt(pow(p1[0] - p2[0], 2.0) + pow(p1[1] - p2[1], 2.0))

def calcStationLines(point, length, orientation, angle, angle_exist):
    """
    Return the Station Line of the point with length, orientation and angle

    :param point: The first point
    :param length: Length of the station line
    :param orientation: Orientation of the station line
    :param angle: Angle of the station line
    :param angle_exist: Angle of the segment where is point
    :type point: list
    :type length: float
    :type orientation: Side
    :type angle: float
    :type angle_exist: float
    :return: Return the station line
    :rtype: list
    """


    # Declare points for line (p_g, p_d)
    p_g = QgsPoint() # left point of the line
    p_d = QgsPoint() # right point of the line

    if orientation == Side.Left or orientation == Side.Both:
        p_g.setX(point[0] + length * cos(radians(angle) + angle_exist))
        p_g.setY(point[1] + length * sin(radians(angle) + angle_exist))
        if orientation != Side.Both:
            p_d = QgsPoint(point[0], point[1])

    if orientation == Side.Right or orientation == Side.Both:
        p_d.setX(point[0] + -length * cos(radians(angle) + angle_exist))
        p_d.setY(point[1] + -length * sin(radians(angle) + angle_exist))
        if orientation != Side.Both:
            p_g = QgsPoint(point[0], point[1])

    line = [p_g, p_d]
    return line

def pointFromDistance(line, distance):
    """
    Return coordinate of a point at distance from first point of line

    :param line: The line
    :param distance: Distance from first point of line
    :type line: list
    :type distance: float
    :return: Coordinate x,y of a point from distance
    :rtype: list
    """
    # Create vector
    vector = (line[1].x() - line[0].x(), line[1].y() - line[0].y())
    # Length of the segment
    length_segment = calcDistance(line[0], line[1])

    # Get (x,y) by the distance with the first point of the segment
    #Thales
    x = (vector[0] * distance / length_segment) + line[0].x()
    y = (vector[1] * distance / length_segment) + line[0].y()

    return [x,y]

def calc_distance_along_line(line, distance):
    """
    Return a list contains segmentation of the line by a distance
    For example a polyline with 3 lines:
        Length of line1 is 5
        Length of line2 is 17
        Length of line3 is 20
        Distance of segmentation is 10
        line1 can't be segmented (except first node) - the remainder is 5
        line2 have 2 segments: +5, +15 - the remainder is 2
        line3 have 2 segments: +8, +18
        the return is [[], [5,15], [8,18]]

    :param line: Polyline
    :param distance: Segmentation distance of the polyline
    :type line: list of points
    :type distance: float
    :return: List of list of segmentation - Each line of polyline have a list of value for the segmentation
    :rtype: list
    """

    nb_segments = len(line)-1 # Number of segment into the polyline
    list_pts_segments = [] # Declare the list of list of points on segment

    rest = 0 # Remainder of the calculation on a line with distance

    for i in range(nb_segments):
        pts = []
        d = calcDistance(line[i+1], line[i])

        # Calculation of the points
        nb_pts = int((d + rest) // distance)
        if nb_pts > 0:
            if rest ==0:
                nb_pts += 1
            for i in range(0, nb_pts):
                if rest == 0:
                    pts.append(rest + i*distance)
                else:
                    pts.append(distance -rest + i*distance)

            # Calculation of the remainder
            if rest == 0:
                rest = (d+rest) - (nb_pts -1 )*distance
            else:
                rest = (d+rest) - nb_pts*distance
        else:
            rest +=d

        # add list of points
        list_pts_segments.append(pts)


    return list_pts_segments

def returnStrOrientation(orientation):
    """
    Return the "Word" of the side

    :param orientation: Value of Orientation/Side
    :type orientation: int
    :return: The "word" of orientation/side
    :rtype: string
    """

    if orientation == Side.Both:
        return "Both"
    elif orientation == Side.Right:
        return "Right"
    elif orientation == Side.Left:
        return "Left"
    else: # Prevent eventually bug ?
        return ""

def algo(mem_layer, layer, options, parametres):
    """
    Main function of the calculation of polyline

    :param mem_layer: Return's memory layer
    :param layer: Vector layer
    :param options: Options for create stations. 0: Vertices. 1: Distance. 2: Use only selected features
    :param parametres: All parameters for create stations. 0: Side/Orientation of SL. 1: Length of SL. 2: Angle of SL. 3: Distance of segmentation.
    """

    position = 0
    pts = None
    if options[2]:
        features = layer.selectedFeatures()
    else:
        features = layer.getFeatures()

    for feat in features:
        # For Multi LineString
        if feat.geometry().isMultipart():
            multi = feat.geometry().asMultiPolyline()
            for line in multi:
                if options[1] == True:
                    pts = calc_distance_along_line(line, parametres[3][position]) # Calculation of distance for the LineString

                algo_line(mem_layer, line, parametres[0][position], parametres[1][position], parametres[2][position], options, position, pts)
        else :
            line = feat.geometry().asPolyline()
            if options[1] == True:
                pts = calc_distance_along_line(line, parametres[3][position]) # Calculation of distance for the LineString

            algo_line(mem_layer, line, parametres[0][position], parametres[1][position], parametres[2][position], options, position, pts)

        position += 1

def algo_line(mem_layer, line, orientation, length, angle, options, fid, pts=None):
    """
    Create station lines

    :param mem_layer: Return's memory layer
    :param line: segment of the linestring used to create SL
    :param orientation: parameters for Side/Orientation define into Class Side
    :param length: parameters for length of the SL
    :param angle: parameters for the angle of the SL with the angle of the line
    :param options: Options for create stations. 0: Vertices. 1: Distance
    :param fid: fid of line
    :param pts: If segmentization by distance, the list of points
    """

    angle = normalizeAngle(angle)

    pr = mem_layer.dataProvider()
    # Create attributes
    # FID: ID of the original linestring
    # SL_ID: ID of the station lines. Each SL have a unique ID
    # SL_SEGMENT: ID of the segment of the linestring
    # SL_ANGLE: Angle of the SL
    # SL_LENGTH: Length of the SL
    # SL_ORIENT: Orientation/Side of the SL
    pr.addAttributes( [ QgsField("FID", QVariant.Int),
                    QgsField("SL_ID",  QVariant.Int),
                    QgsField("SL_SEGMENT",  QVariant.Int),
                    QgsField("SL_ANGLE", QVariant.Double),
                    QgsField("SL_LENGTH", QVariant.Double),
                    QgsField("SL_ORIENT", QVariant.String)]  )

    mem_layer.updateFields()

    sl_id = 1
    sl_dist = 0;

    for i in range(len(line)-1):
        sl_segment = i+1

        angle_exist = calcAngleExistant(line[i], line[i+1])
        signe = calcOrientationLigne(line[i], line[i+1])

        # If Node (start)
        if options[0] == True:
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPolyline(calcStationLines(line[i], signe*length, orientation, angle, angle_exist)))
            fet.setAttributes([fid, sl_id, sl_segment, angle, length, returnStrOrientation(orientation)])
            pr.addFeatures([fet])
            sl_id +=1

        # If Distance
        if options[1] == True:
            if pts and len(pts[i]) > 0:
                for p in pts[i]:
                    if p > 0 or options[0] == False: # Avoid double line on nodes
                        fet = QgsFeature()
                        fet.setGeometry(QgsGeometry.fromPolyline(calcStationLines(pointFromDistance([line[i], line[i+1]], p), signe*length, orientation, angle, angle_exist)))
                        fet.setAttributes([fid, sl_id, sl_segment, angle, length, returnStrOrientation(orientation)])
                        pr.addFeatures([fet])
                        sl_id += 1

        # If Node (end)
        if options[0] == True:
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPolyline(calcStationLines(line[i+1], signe*length, orientation, angle, angle_exist)))
            fet.setAttributes([fid, sl_id, sl_segment, angle, length, returnStrOrientation(orientation)])
            pr.addFeatures([fet])
            sl_id += 1

    mem_layer.commitChanges()
    mem_layer.updateExtents()

