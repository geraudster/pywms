# -*- coding: utf-8 *-*
import pyxb
import wms
import pyxb.binding.datatypes as xs

from xml.dom.minidom import parseString

def get_GetMap():
    GetMap = wms.GetMap(Format = ['png'])
    GetMap.DCPType = [wms.DCPType()]
    GetMap.DCPType[0].HTTP = wms.HTTP()
    GetMap.DCPType[0].HTTP.Get = wms.Get()
    GetMap.DCPType[0].HTTP.Get.OnlineResource = wms.OnlineResource(href='http://example.com/wms')
    return GetMap


def get_GetCapabilities():
    GetCapabilities = wms.GetCapabilities(Format = ['png'])
    GetCapabilities.DCPType = [wms.DCPType()]
    GetCapabilities.DCPType[0].HTTP = wms.HTTP()
    GetCapabilities.DCPType[0].HTTP.Get = wms.Get()
    GetCapabilities.DCPType[0].HTTP.Get.OnlineResource = wms.OnlineResource(href='http://example.com/wms')
    return GetCapabilities

def get_Exception():
    _Exception = wms.Exception(Format = ['png'])
    return _Exception

def get_Request():
    request = wms.Request()
    request.GetCapabilities = get_GetCapabilities()
    request.GetMap = get_GetMap()
    return request

def get_Capability():
    doc = wms.Capability()
    doc.Request = get_Request()
    doc.Exception = get_Exception()
    doc.Layer = get_Layer('Server Layer', [ get_Layer('temperature'),
                                            get_Layer('hydro') ])
    return doc

def get_Layer(name = None, layers = []):
    doc = wms.Layer(queryable=True, cascaded=0, opaque=False, noSubsets=False, fixedWidth=0, fixedHeight=0)
    doc.Title = "title"
    doc.Name = name
    if layers : doc.Layer = layers
    return doc

def get_Service():
    doc = wms.Service(Name = 'WMS', Title = 'Test getCapabilities',
                      Abstract = 'Test de web service WMS en Python',
                      )
    doc.OnlineResource = wms.OnlineResource(href = 'http://example.com')
    return doc
    
def get_WMS_Capabilities():
    doc = wms.WMS_Capabilities(version = '1.3.0', updateSequence = '0')
    doc.Capability = get_Capability()
    doc.Service = get_Service()
    return doc
    
txt = get_WMS_Capabilities().toxml("utf-8")
print parseString(txt).toprettyxml()
