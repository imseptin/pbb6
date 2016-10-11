# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PBB
                                 A QGIS plugin
 Gis for PBB Kota Palu
                             -------------------
        begin                : 2016-10-07
        copyright            : (C) 2016 by Septin M Rezki
        email                : septinmulatsihrezki@gmail.com
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
    """Load PBB class from file PBB.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gis_pbb import PBB
    return PBB(iface)
