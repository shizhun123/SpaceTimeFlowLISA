# encoding: latin2
"""
Distance functions from an area to a region
"""
__author__ = "Juan C. Duque"
__credits__ = "Copyright (c) 2009-11 Juan C. Duque"
__license__ = "New BSD License"
__version__ = "1.0.0"
__maintainer__ = "RiSE Group"
__email__ = "contacto@rise-group.org"

import numpy as np
#计算一个区域到一组区域集合质心的距离
def getDistance2RegionCentroid(areaManager, area, areaList, indexData=[]):
    """
    The distance from area "i" to the attribute centroid of region "k"
    @areaManager: AreaManager实例，包含所有区域数据
    @area: AreaCl实例，要计算距离的单个区域
    @areaList: 区域ID列表，定义区域集合
    @indexData: 可选的属性索引列表，指定使用哪些属性计算
    
    """
    sumAttributes = np.zeros(len(area.data))
    if len(areaManager.areas[areaList[0]].data) - len(area.data) == 1:
        for aID in areaList:
            sumAttributes += np.array(areaManager.areas[aID].data[0: -1])
    else:
        for aID in areaList:
            sumAttributes += np.array(areaManager.areas[aID].data)
    centroidRegion = sumAttributes/len(areaList)
    regionDistance = sum((np.array(area.data) - centroidRegion) ** 2)
    return regionDistance

distanceStatDispatcher = {}
distanceStatDispatcher["Centroid"] = getDistance2RegionCentroid
