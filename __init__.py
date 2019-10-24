# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Text_transform
                                 A QGIS plugin
 Parce text files
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-10-24
        copyright            : (C) 2019 by wahha
        email                : wahha@mail.ru
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Text_transform class from file Text_transform.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .GGS_text_parsing import Text_transform
    return Text_transform(iface)
