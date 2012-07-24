# .\wms.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1733b08f38ec3fb9d78827021073a0bfa72a91f1
# Generated 2012-07-24 14:24:13.878000 by PyXB version 1.1.4
# Namespace http://www.opengis.net/wms

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:7a67511e-d58a-11e1-b5d8-0016419cfff8')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _xlink

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.opengis.net/wms', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, _fallback_namespace=default_namespace)


# Atomic SimpleTypeDefinition
class longitudeType (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'longitudeType')
    _Documentation = None
longitudeType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=longitudeType, value=pyxb.binding.datatypes.double(180.0))
longitudeType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=longitudeType, value=pyxb.binding.datatypes.double(-180.0))
longitudeType._InitializeFacetMap(longitudeType._CF_maxInclusive,
   longitudeType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'longitudeType', longitudeType)

# Atomic SimpleTypeDefinition
class latitudeType (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'latitudeType')
    _Documentation = None
latitudeType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=latitudeType, value=pyxb.binding.datatypes.double(90.0))
latitudeType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=latitudeType, value=pyxb.binding.datatypes.double(-90.0))
latitudeType._InitializeFacetMap(latitudeType._CF_maxInclusive,
   latitudeType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'latitudeType', latitudeType)

# Atomic SimpleTypeDefinition
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.WMS = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'WMS', tag=u'WMS')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Complex type CTD_ANON with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}Get uses Python identifier Get
    __Get = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Get'), 'Get', '__httpwww_opengis_netwms_CTD_ANON_httpwww_opengis_netwmsGet', False)

    
    Get = property(__Get.value, __Get.set, None, u'\n        The URL prefix for the HTTP "Get" request method.\n      ')

    
    # Element {http://www.opengis.net/wms}Post uses Python identifier Post
    __Post = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Post'), 'Post', '__httpwww_opengis_netwms_CTD_ANON_httpwww_opengis_netwmsPost', False)

    
    Post = property(__Post.value, __Post.set, None, u'\n        The URL prefix for the HTTP "Post" request method.\n      ')


    _ElementMap = {
        __Get.name() : __Get,
        __Post.name() : __Post
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_ with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'href'), 'href', '__httpwww_opengis_netwms_CTD_ANON__httpwww_w3_org1999xlinkhref', _xlink.hrefType)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'arcrole'), 'arcrole', '__httpwww_opengis_netwms_CTD_ANON__httpwww_w3_org1999xlinkarcrole', _xlink.arcroleType)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'title'), 'title', '__httpwww_opengis_netwms_CTD_ANON__httpwww_w3_org1999xlinktitle', _xlink.titleAttrType)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'show'), 'show', '__httpwww_opengis_netwms_CTD_ANON__httpwww_w3_org1999xlinkshow', _xlink.showType)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'role'), 'role', '__httpwww_opengis_netwms_CTD_ANON__httpwww_w3_org1999xlinkrole', _xlink.roleType)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'actuate'), 'actuate', '__httpwww_opengis_netwms_CTD_ANON__httpwww_w3_org1999xlinkactuate', _xlink.actuateType)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink'), u'type'), 'type', '__httpwww_opengis_netwms_CTD_ANON__httpwww_w3_org1999xlinktype', _xlink.typeType, fixed=True, unicode_default=u'simple')
    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __href.name() : __href,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __role.name() : __role,
        __actuate.name() : __actuate,
        __type.name() : __type
    }



# Complex type CTD_ANON_2 with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_2_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Element {http://www.opengis.net/wms}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netwms_CTD_ANON_2_httpwww_opengis_netwmsFormat', False)

    
    Format = property(__Format.value, __Format.set, None, u"\n        A container for listing an available format's MIME type.\n      ")

    
    # Attribute height uses Python identifier height
    __height = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'height'), 'height', '__httpwww_opengis_netwms_CTD_ANON_2_height', pyxb.binding.datatypes.positiveInteger)
    
    height = property(__height.value, __height.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'width'), 'width', '__httpwww_opengis_netwms_CTD_ANON_2_width', pyxb.binding.datatypes.positiveInteger)
    
    width = property(__width.value, __width.set, None, None)


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource,
        __Format.name() : __Format
    }
    _AttributeMap = {
        __height.name() : __height,
        __width.name() : __width
    }



# Complex type CTD_ANON_3 with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_3_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Element {http://www.opengis.net/wms}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Title'), 'Title', '__httpwww_opengis_netwms_CTD_ANON_3_httpwww_opengis_netwmsTitle', False)

    
    Title = property(__Title.value, __Title.set, None, u'\n        The Title is for informative display to a human.\n      ')

    
    # Element {http://www.opengis.net/wms}LogoURL uses Python identifier LogoURL
    __LogoURL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LogoURL'), 'LogoURL', '__httpwww_opengis_netwms_CTD_ANON_3_httpwww_opengis_netwmsLogoURL', False)

    
    LogoURL = property(__LogoURL.value, __LogoURL.set, None, None)


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource,
        __Title.name() : __Title,
        __LogoURL.name() : __LogoURL
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_4 with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}ContactOrganization uses Python identifier ContactOrganization
    __ContactOrganization = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactOrganization'), 'ContactOrganization', '__httpwww_opengis_netwms_CTD_ANON_4_httpwww_opengis_netwmsContactOrganization', False)

    
    ContactOrganization = property(__ContactOrganization.value, __ContactOrganization.set, None, None)

    
    # Element {http://www.opengis.net/wms}ContactPerson uses Python identifier ContactPerson
    __ContactPerson = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactPerson'), 'ContactPerson', '__httpwww_opengis_netwms_CTD_ANON_4_httpwww_opengis_netwmsContactPerson', False)

    
    ContactPerson = property(__ContactPerson.value, __ContactPerson.set, None, None)


    _ElementMap = {
        __ContactOrganization.name() : __ContactOrganization,
        __ContactPerson.name() : __ContactPerson
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_5 with content type ELEMENT_ONLY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}City uses Python identifier City
    __City = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'City'), 'City', '__httpwww_opengis_netwms_CTD_ANON_5_httpwww_opengis_netwmsCity', False)

    
    City = property(__City.value, __City.set, None, None)

    
    # Element {http://www.opengis.net/wms}StateOrProvince uses Python identifier StateOrProvince
    __StateOrProvince = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StateOrProvince'), 'StateOrProvince', '__httpwww_opengis_netwms_CTD_ANON_5_httpwww_opengis_netwmsStateOrProvince', False)

    
    StateOrProvince = property(__StateOrProvince.value, __StateOrProvince.set, None, None)

    
    # Element {http://www.opengis.net/wms}PostCode uses Python identifier PostCode
    __PostCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'PostCode'), 'PostCode', '__httpwww_opengis_netwms_CTD_ANON_5_httpwww_opengis_netwmsPostCode', False)

    
    PostCode = property(__PostCode.value, __PostCode.set, None, None)

    
    # Element {http://www.opengis.net/wms}Country uses Python identifier Country
    __Country = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Country'), 'Country', '__httpwww_opengis_netwms_CTD_ANON_5_httpwww_opengis_netwmsCountry', False)

    
    Country = property(__Country.value, __Country.set, None, None)

    
    # Element {http://www.opengis.net/wms}AddressType uses Python identifier AddressType
    __AddressType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AddressType'), 'AddressType', '__httpwww_opengis_netwms_CTD_ANON_5_httpwww_opengis_netwmsAddressType', False)

    
    AddressType = property(__AddressType.value, __AddressType.set, None, None)

    
    # Element {http://www.opengis.net/wms}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Address'), 'Address', '__httpwww_opengis_netwms_CTD_ANON_5_httpwww_opengis_netwmsAddress', False)

    
    Address = property(__Address.value, __Address.set, None, None)


    _ElementMap = {
        __City.name() : __City,
        __StateOrProvince.name() : __StateOrProvince,
        __PostCode.name() : __PostCode,
        __Country.name() : __Country,
        __AddressType.name() : __AddressType,
        __Address.name() : __Address
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_6 with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_6_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Element {http://www.opengis.net/wms}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netwms_CTD_ANON_6_httpwww_opengis_netwmsFormat', False)

    
    Format = property(__Format.value, __Format.set, None, u"\n        A container for listing an available format's MIME type.\n      ")

    
    # Attribute height uses Python identifier height
    __height = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'height'), 'height', '__httpwww_opengis_netwms_CTD_ANON_6_height', pyxb.binding.datatypes.positiveInteger)
    
    height = property(__height.value, __height.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'width'), 'width', '__httpwww_opengis_netwms_CTD_ANON_6_width', pyxb.binding.datatypes.positiveInteger)
    
    width = property(__width.value, __width.set, None, None)


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource,
        __Format.name() : __Format
    }
    _AttributeMap = {
        __height.name() : __height,
        __width.name() : __width
    }



# Complex type CTD_ANON_7 with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}ContactPosition uses Python identifier ContactPosition
    __ContactPosition = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactPosition'), 'ContactPosition', '__httpwww_opengis_netwms_CTD_ANON_7_httpwww_opengis_netwmsContactPosition', False)

    
    ContactPosition = property(__ContactPosition.value, __ContactPosition.set, None, None)

    
    # Element {http://www.opengis.net/wms}ContactAddress uses Python identifier ContactAddress
    __ContactAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactAddress'), 'ContactAddress', '__httpwww_opengis_netwms_CTD_ANON_7_httpwww_opengis_netwmsContactAddress', False)

    
    ContactAddress = property(__ContactAddress.value, __ContactAddress.set, None, None)

    
    # Element {http://www.opengis.net/wms}ContactVoiceTelephone uses Python identifier ContactVoiceTelephone
    __ContactVoiceTelephone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactVoiceTelephone'), 'ContactVoiceTelephone', '__httpwww_opengis_netwms_CTD_ANON_7_httpwww_opengis_netwmsContactVoiceTelephone', False)

    
    ContactVoiceTelephone = property(__ContactVoiceTelephone.value, __ContactVoiceTelephone.set, None, None)

    
    # Element {http://www.opengis.net/wms}ContactFacsimileTelephone uses Python identifier ContactFacsimileTelephone
    __ContactFacsimileTelephone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactFacsimileTelephone'), 'ContactFacsimileTelephone', '__httpwww_opengis_netwms_CTD_ANON_7_httpwww_opengis_netwmsContactFacsimileTelephone', False)

    
    ContactFacsimileTelephone = property(__ContactFacsimileTelephone.value, __ContactFacsimileTelephone.set, None, None)

    
    # Element {http://www.opengis.net/wms}ContactElectronicMailAddress uses Python identifier ContactElectronicMailAddress
    __ContactElectronicMailAddress = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactElectronicMailAddress'), 'ContactElectronicMailAddress', '__httpwww_opengis_netwms_CTD_ANON_7_httpwww_opengis_netwmsContactElectronicMailAddress', False)

    
    ContactElectronicMailAddress = property(__ContactElectronicMailAddress.value, __ContactElectronicMailAddress.set, None, None)

    
    # Element {http://www.opengis.net/wms}ContactPersonPrimary uses Python identifier ContactPersonPrimary
    __ContactPersonPrimary = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactPersonPrimary'), 'ContactPersonPrimary', '__httpwww_opengis_netwms_CTD_ANON_7_httpwww_opengis_netwmsContactPersonPrimary', False)

    
    ContactPersonPrimary = property(__ContactPersonPrimary.value, __ContactPersonPrimary.set, None, None)


    _ElementMap = {
        __ContactPosition.name() : __ContactPosition,
        __ContactAddress.name() : __ContactAddress,
        __ContactVoiceTelephone.name() : __ContactVoiceTelephone,
        __ContactFacsimileTelephone.name() : __ContactFacsimileTelephone,
        __ContactElectronicMailAddress.name() : __ContactElectronicMailAddress,
        __ContactPersonPrimary.name() : __ContactPersonPrimary
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_8 with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_8_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Element {http://www.opengis.net/wms}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netwms_CTD_ANON_8_httpwww_opengis_netwmsFormat', False)

    
    Format = property(__Format.value, __Format.set, None, u"\n        A container for listing an available format's MIME type.\n      ")

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__httpwww_opengis_netwms_CTD_ANON_8_type', pyxb.binding.datatypes.NMTOKEN, required=True)
    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource,
        __Format.name() : __Format
    }
    _AttributeMap = {
        __type.name() : __type
    }



# Complex type CTD_ANON_9 with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netwms_CTD_ANON_9_httpwww_opengis_netwmsFormat', True)

    
    Format = property(__Format.value, __Format.set, None, u"\n        A container for listing an available format's MIME type.\n      ")


    _ElementMap = {
        __Format.name() : __Format
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_10 with content type SIMPLE
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute authority uses Python identifier authority
    __authority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'authority'), 'authority', '__httpwww_opengis_netwms_CTD_ANON_10_authority', pyxb.binding.datatypes.string, required=True)
    
    authority = property(__authority.value, __authority.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __authority.name() : __authority
    }



# Complex type CTD_ANON_11 with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_11_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Element {http://www.opengis.net/wms}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netwms_CTD_ANON_11_httpwww_opengis_netwmsFormat', False)

    
    Format = property(__Format.value, __Format.set, None, u"\n        A container for listing an available format's MIME type.\n      ")


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource,
        __Format.name() : __Format
    }
    _AttributeMap = {
        
    }



# Complex type OperationType with content type ELEMENT_ONLY
class OperationType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'OperationType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}DCPType uses Python identifier DCPType
    __DCPType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DCPType'), 'DCPType', '__httpwww_opengis_netwms_OperationType_httpwww_opengis_netwmsDCPType', True)

    
    DCPType = property(__DCPType.value, __DCPType.set, None, u'\n        Available Distributed Computing Platforms (DCPs) are listed here.\n        At present, only HTTP is defined.\n      ')

    
    # Element {http://www.opengis.net/wms}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netwms_OperationType_httpwww_opengis_netwmsFormat', True)

    
    Format = property(__Format.value, __Format.set, None, u"\n        A container for listing an available format's MIME type.\n      ")


    _ElementMap = {
        __DCPType.name() : __DCPType,
        __Format.name() : __Format
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'OperationType', OperationType)


# Complex type CTD_ANON_12 with content type ELEMENT_ONLY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_12_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Element {http://www.opengis.net/wms}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netwms_CTD_ANON_12_httpwww_opengis_netwmsFormat', False)

    
    Format = property(__Format.value, __Format.set, None, u"\n        A container for listing an available format's MIME type.\n      ")


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource,
        __Format.name() : __Format
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_13 with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_13_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Element {http://www.opengis.net/wms}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netwms_CTD_ANON_13_httpwww_opengis_netwmsFormat', False)

    
    Format = property(__Format.value, __Format.set, None, u"\n        A container for listing an available format's MIME type.\n      ")


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource,
        __Format.name() : __Format
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_14 with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), 'Abstract', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsAbstract', False)

    
    Abstract = property(__Abstract.value, __Abstract.set, None, u'\n        The abstract is a longer narrative description of an object.\n      ')

    
    # Element {http://www.opengis.net/wms}KeywordList uses Python identifier KeywordList
    __KeywordList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'KeywordList'), 'KeywordList', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsKeywordList', False)

    
    KeywordList = property(__KeywordList.value, __KeywordList.set, None, u'\n        List of keywords or keyword phrases to help catalog searching.\n      ')

    
    # Element {http://www.opengis.net/wms}LayerLimit uses Python identifier LayerLimit
    __LayerLimit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LayerLimit'), 'LayerLimit', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsLayerLimit', False)

    
    LayerLimit = property(__LayerLimit.value, __LayerLimit.set, None, None)

    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Element {http://www.opengis.net/wms}MaxWidth uses Python identifier MaxWidth
    __MaxWidth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxWidth'), 'MaxWidth', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsMaxWidth', False)

    
    MaxWidth = property(__MaxWidth.value, __MaxWidth.set, None, None)

    
    # Element {http://www.opengis.net/wms}MaxHeight uses Python identifier MaxHeight
    __MaxHeight = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxHeight'), 'MaxHeight', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsMaxHeight', False)

    
    MaxHeight = property(__MaxHeight.value, __MaxHeight.set, None, None)

    
    # Element {http://www.opengis.net/wms}ContactInformation uses Python identifier ContactInformation
    __ContactInformation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ContactInformation'), 'ContactInformation', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsContactInformation', False)

    
    ContactInformation = property(__ContactInformation.value, __ContactInformation.set, None, u'\n        Information about a contact person for the service.\n      ')

    
    # Element {http://www.opengis.net/wms}Fees uses Python identifier Fees
    __Fees = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Fees'), 'Fees', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsFees', False)

    
    Fees = property(__Fees.value, __Fees.set, None, None)

    
    # Element {http://www.opengis.net/wms}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Title'), 'Title', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsTitle', False)

    
    Title = property(__Title.value, __Title.set, None, u'\n        The Title is for informative display to a human.\n      ')

    
    # Element {http://www.opengis.net/wms}AccessConstraints uses Python identifier AccessConstraints
    __AccessConstraints = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints'), 'AccessConstraints', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsAccessConstraints', False)

    
    AccessConstraints = property(__AccessConstraints.value, __AccessConstraints.set, None, None)

    
    # Element {http://www.opengis.net/wms}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpwww_opengis_netwms_CTD_ANON_14_httpwww_opengis_netwmsName', False)

    
    Name = property(__Name.value, __Name.set, None, None)


    _ElementMap = {
        __Abstract.name() : __Abstract,
        __KeywordList.name() : __KeywordList,
        __LayerLimit.name() : __LayerLimit,
        __OnlineResource.name() : __OnlineResource,
        __MaxWidth.name() : __MaxWidth,
        __MaxHeight.name() : __MaxHeight,
        __ContactInformation.name() : __ContactInformation,
        __Fees.name() : __Fees,
        __Title.name() : __Title,
        __AccessConstraints.name() : __AccessConstraints,
        __Name.name() : __Name
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_15 with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}HTTP uses Python identifier HTTP
    __HTTP = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'HTTP'), 'HTTP', '__httpwww_opengis_netwms_CTD_ANON_15_httpwww_opengis_netwmsHTTP', False)

    
    HTTP = property(__HTTP.value, __HTTP.set, None, u'\n        Available HTTP request methods.  At least "Get" shall be supported.\n      ')


    _ElementMap = {
        __HTTP.name() : __HTTP
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_16 with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_16_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_17 with content type ELEMENT_ONLY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}Keyword uses Python identifier Keyword
    __Keyword = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Keyword'), 'Keyword', '__httpwww_opengis_netwms_CTD_ANON_17_httpwww_opengis_netwmsKeyword', True)

    
    Keyword = property(__Keyword.value, __Keyword.set, None, u'\n        A single keyword or phrase.\n      ')


    _ElementMap = {
        __Keyword.name() : __Keyword
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_18 with content type ELEMENT_ONLY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}eastBoundLongitude uses Python identifier eastBoundLongitude
    __eastBoundLongitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'eastBoundLongitude'), 'eastBoundLongitude', '__httpwww_opengis_netwms_CTD_ANON_18_httpwww_opengis_netwmseastBoundLongitude', False)

    
    eastBoundLongitude = property(__eastBoundLongitude.value, __eastBoundLongitude.set, None, None)

    
    # Element {http://www.opengis.net/wms}southBoundLatitude uses Python identifier southBoundLatitude
    __southBoundLatitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'southBoundLatitude'), 'southBoundLatitude', '__httpwww_opengis_netwms_CTD_ANON_18_httpwww_opengis_netwmssouthBoundLatitude', False)

    
    southBoundLatitude = property(__southBoundLatitude.value, __southBoundLatitude.set, None, None)

    
    # Element {http://www.opengis.net/wms}northBoundLatitude uses Python identifier northBoundLatitude
    __northBoundLatitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'northBoundLatitude'), 'northBoundLatitude', '__httpwww_opengis_netwms_CTD_ANON_18_httpwww_opengis_netwmsnorthBoundLatitude', False)

    
    northBoundLatitude = property(__northBoundLatitude.value, __northBoundLatitude.set, None, None)

    
    # Element {http://www.opengis.net/wms}westBoundLongitude uses Python identifier westBoundLongitude
    __westBoundLongitude = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'westBoundLongitude'), 'westBoundLongitude', '__httpwww_opengis_netwms_CTD_ANON_18_httpwww_opengis_netwmswestBoundLongitude', False)

    
    westBoundLongitude = property(__westBoundLongitude.value, __westBoundLongitude.set, None, None)


    _ElementMap = {
        __eastBoundLongitude.name() : __eastBoundLongitude,
        __southBoundLatitude.name() : __southBoundLatitude,
        __northBoundLatitude.name() : __northBoundLatitude,
        __westBoundLongitude.name() : __westBoundLongitude
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_19 with content type EMPTY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute miny uses Python identifier miny
    __miny = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'miny'), 'miny', '__httpwww_opengis_netwms_CTD_ANON_19_miny', pyxb.binding.datatypes.double, required=True)
    
    miny = property(__miny.value, __miny.set, None, None)

    
    # Attribute maxx uses Python identifier maxx
    __maxx = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxx'), 'maxx', '__httpwww_opengis_netwms_CTD_ANON_19_maxx', pyxb.binding.datatypes.double, required=True)
    
    maxx = property(__maxx.value, __maxx.set, None, None)

    
    # Attribute maxy uses Python identifier maxy
    __maxy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'maxy'), 'maxy', '__httpwww_opengis_netwms_CTD_ANON_19_maxy', pyxb.binding.datatypes.double, required=True)
    
    maxy = property(__maxy.value, __maxy.set, None, None)

    
    # Attribute resx uses Python identifier resx
    __resx = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'resx'), 'resx', '__httpwww_opengis_netwms_CTD_ANON_19_resx', pyxb.binding.datatypes.double)
    
    resx = property(__resx.value, __resx.set, None, None)

    
    # Attribute resy uses Python identifier resy
    __resy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'resy'), 'resy', '__httpwww_opengis_netwms_CTD_ANON_19_resy', pyxb.binding.datatypes.double)
    
    resy = property(__resy.value, __resy.set, None, None)

    
    # Attribute CRS uses Python identifier CRS
    __CRS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'CRS'), 'CRS', '__httpwww_opengis_netwms_CTD_ANON_19_CRS', pyxb.binding.datatypes.string, required=True)
    
    CRS = property(__CRS.value, __CRS.set, None, None)

    
    # Attribute minx uses Python identifier minx
    __minx = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'minx'), 'minx', '__httpwww_opengis_netwms_CTD_ANON_19_minx', pyxb.binding.datatypes.double, required=True)
    
    minx = property(__minx.value, __minx.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __miny.name() : __miny,
        __maxx.name() : __maxx,
        __maxy.name() : __maxy,
        __resx.name() : __resx,
        __resy.name() : __resy,
        __CRS.name() : __CRS,
        __minx.name() : __minx
    }



# Complex type CTD_ANON_20 with content type SIMPLE
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'units'), 'units', '__httpwww_opengis_netwms_CTD_ANON_20_units', pyxb.binding.datatypes.string, required=True)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute unitSymbol uses Python identifier unitSymbol
    __unitSymbol = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'unitSymbol'), 'unitSymbol', '__httpwww_opengis_netwms_CTD_ANON_20_unitSymbol', pyxb.binding.datatypes.string)
    
    unitSymbol = property(__unitSymbol.value, __unitSymbol.set, None, None)

    
    # Attribute default uses Python identifier default
    __default = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'default'), 'default', '__httpwww_opengis_netwms_CTD_ANON_20_default', pyxb.binding.datatypes.string)
    
    default = property(__default.value, __default.set, None, None)

    
    # Attribute multipleValues uses Python identifier multipleValues
    __multipleValues = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'multipleValues'), 'multipleValues', '__httpwww_opengis_netwms_CTD_ANON_20_multipleValues', pyxb.binding.datatypes.boolean)
    
    multipleValues = property(__multipleValues.value, __multipleValues.set, None, None)

    
    # Attribute nearestValue uses Python identifier nearestValue
    __nearestValue = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'nearestValue'), 'nearestValue', '__httpwww_opengis_netwms_CTD_ANON_20_nearestValue', pyxb.binding.datatypes.boolean)
    
    nearestValue = property(__nearestValue.value, __nearestValue.set, None, None)

    
    # Attribute current uses Python identifier current
    __current = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'current'), 'current', '__httpwww_opengis_netwms_CTD_ANON_20_current', pyxb.binding.datatypes.boolean)
    
    current = property(__current.value, __current.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_opengis_netwms_CTD_ANON_20_name', pyxb.binding.datatypes.string, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __units.name() : __units,
        __unitSymbol.name() : __unitSymbol,
        __default.name() : __default,
        __multipleValues.name() : __multipleValues,
        __nearestValue.name() : __nearestValue,
        __current.name() : __current,
        __name.name() : __name
    }



# Complex type CTD_ANON_21 with content type SIMPLE
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute vocabulary uses Python identifier vocabulary
    __vocabulary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'vocabulary'), 'vocabulary', '__httpwww_opengis_netwms_CTD_ANON_21_vocabulary', pyxb.binding.datatypes.string)
    
    vocabulary = property(__vocabulary.value, __vocabulary.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __vocabulary.name() : __vocabulary
    }



# Complex type CTD_ANON_22 with content type ELEMENT_ONLY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_22_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__httpwww_opengis_netwms_CTD_ANON_22_name', pyxb.binding.datatypes.NMTOKEN, required=True)
    
    name = property(__name.value, __name.set, None, None)


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource
    }
    _AttributeMap = {
        __name.name() : __name
    }



# Complex type CTD_ANON_23 with content type ELEMENT_ONLY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}Exception uses Python identifier Exception
    __Exception = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Exception'), 'Exception', '__httpwww_opengis_netwms_CTD_ANON_23_httpwww_opengis_netwmsException', False)

    
    Exception = property(__Exception.value, __Exception.set, None, u'\n        An Exception element indicates which error-reporting formats are\n        supported.\n      ')

    
    # Element {http://www.opengis.net/wms}_ExtendedCapabilities uses Python identifier ExtendedCapabilities
    __ExtendedCapabilities = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'_ExtendedCapabilities'), 'ExtendedCapabilities', '__httpwww_opengis_netwms_CTD_ANON_23_httpwww_opengis_netwms_ExtendedCapabilities', True)

    
    ExtendedCapabilities = property(__ExtendedCapabilities.value, __ExtendedCapabilities.set, None, u'\n        Individual service providers may use this element to report extended\n        capabilities.\n      ')

    
    # Element {http://www.opengis.net/wms}Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Layer'), 'Layer', '__httpwww_opengis_netwms_CTD_ANON_23_httpwww_opengis_netwmsLayer', False)

    
    Layer = property(__Layer.value, __Layer.set, None, u'\n        Nested list of zero or more map Layers offered by this server.\n      ')

    
    # Element {http://www.opengis.net/wms}Request uses Python identifier Request
    __Request = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Request'), 'Request', '__httpwww_opengis_netwms_CTD_ANON_23_httpwww_opengis_netwmsRequest', False)

    
    Request = property(__Request.value, __Request.set, None, u'\n        Available WMS Operations are listed in a Request element.\n      ')


    _ElementMap = {
        __Exception.name() : __Exception,
        __ExtendedCapabilities.name() : __ExtendedCapabilities,
        __Layer.name() : __Layer,
        __Request.name() : __Request
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_24 with content type ELEMENT_ONLY
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}Capability uses Python identifier Capability
    __Capability = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Capability'), 'Capability', '__httpwww_opengis_netwms_CTD_ANON_24_httpwww_opengis_netwmsCapability', False)

    
    Capability = property(__Capability.value, __Capability.set, None, u'\n        A Capability lists available request types, how exceptions may be\n        reported, and whether any extended capabilities are defined.\n        It also includes an optional list of map layers available from this\n        server.\n      ')

    
    # Element {http://www.opengis.net/wms}Service uses Python identifier Service
    __Service = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Service'), 'Service', '__httpwww_opengis_netwms_CTD_ANON_24_httpwww_opengis_netwmsService', False)

    
    Service = property(__Service.value, __Service.set, None, u'\n        General service metadata.\n      ')

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_opengis_netwms_CTD_ANON_24_version', pyxb.binding.datatypes.string, fixed=True, unicode_default=u'1.3.0')
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute updateSequence uses Python identifier updateSequence
    __updateSequence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'updateSequence'), 'updateSequence', '__httpwww_opengis_netwms_CTD_ANON_24_updateSequence', pyxb.binding.datatypes.string)
    
    updateSequence = property(__updateSequence.value, __updateSequence.set, None, None)


    _ElementMap = {
        __Capability.name() : __Capability,
        __Service.name() : __Service
    }
    _AttributeMap = {
        __version.name() : __version,
        __updateSequence.name() : __updateSequence
    }



# Complex type CTD_ANON_25 with content type ELEMENT_ONLY
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}GetFeatureInfo uses Python identifier GetFeatureInfo
    __GetFeatureInfo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GetFeatureInfo'), 'GetFeatureInfo', '__httpwww_opengis_netwms_CTD_ANON_25_httpwww_opengis_netwmsGetFeatureInfo', False)

    
    GetFeatureInfo = property(__GetFeatureInfo.value, __GetFeatureInfo.set, None, None)

    
    # Element {http://www.opengis.net/wms}GetMap uses Python identifier GetMap
    __GetMap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GetMap'), 'GetMap', '__httpwww_opengis_netwms_CTD_ANON_25_httpwww_opengis_netwmsGetMap', False)

    
    GetMap = property(__GetMap.value, __GetMap.set, None, None)

    
    # Element {http://www.opengis.net/wms}GetCapabilities uses Python identifier GetCapabilities
    __GetCapabilities = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'GetCapabilities'), 'GetCapabilities', '__httpwww_opengis_netwms_CTD_ANON_25_httpwww_opengis_netwmsGetCapabilities', False)

    
    GetCapabilities = property(__GetCapabilities.value, __GetCapabilities.set, None, None)

    
    # Element {http://www.opengis.net/wms}_ExtendedOperation uses Python identifier ExtendedOperation
    __ExtendedOperation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'_ExtendedOperation'), 'ExtendedOperation', '__httpwww_opengis_netwms_CTD_ANON_25_httpwww_opengis_netwms_ExtendedOperation', True)

    
    ExtendedOperation = property(__ExtendedOperation.value, __ExtendedOperation.set, None, None)


    _ElementMap = {
        __GetFeatureInfo.name() : __GetFeatureInfo,
        __GetMap.name() : __GetMap,
        __GetCapabilities.name() : __GetCapabilities,
        __ExtendedOperation.name() : __ExtendedOperation
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_26 with content type ELEMENT_ONLY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_26_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_27 with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}OnlineResource uses Python identifier OnlineResource
    __OnlineResource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), 'OnlineResource', '__httpwww_opengis_netwms_CTD_ANON_27_httpwww_opengis_netwmsOnlineResource', False)

    
    OnlineResource = property(__OnlineResource.value, __OnlineResource.set, None, u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')

    
    # Element {http://www.opengis.net/wms}Format uses Python identifier Format
    __Format = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Format'), 'Format', '__httpwww_opengis_netwms_CTD_ANON_27_httpwww_opengis_netwmsFormat', False)

    
    Format = property(__Format.value, __Format.set, None, u"\n        A container for listing an available format's MIME type.\n      ")


    _ElementMap = {
        __OnlineResource.name() : __OnlineResource,
        __Format.name() : __Format
    }
    _AttributeMap = {
        
    }



# Complex type CTD_ANON_28 with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}DataURL uses Python identifier DataURL
    __DataURL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'DataURL'), 'DataURL', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsDataURL', True)

    
    DataURL = property(__DataURL.value, __DataURL.set, None, u'\n        A Map Server may use DataURL offer a link to the underlying data represented\n        by a particular layer.\n      ')

    
    # Element {http://www.opengis.net/wms}Dimension uses Python identifier Dimension
    __Dimension = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Dimension'), 'Dimension', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsDimension', True)

    
    Dimension = property(__Dimension.value, __Dimension.set, None, u'\n        The Dimension element declares the existence of a dimension and indicates what\n        values along a dimension are valid.\n      ')

    
    # Element {http://www.opengis.net/wms}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), 'Abstract', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsAbstract', False)

    
    Abstract = property(__Abstract.value, __Abstract.set, None, u'\n        The abstract is a longer narrative description of an object.\n      ')

    
    # Element {http://www.opengis.net/wms}FeatureListURL uses Python identifier FeatureListURL
    __FeatureListURL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'FeatureListURL'), 'FeatureListURL', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsFeatureListURL', True)

    
    FeatureListURL = property(__FeatureListURL.value, __FeatureListURL.set, None, u'\n        A Map Server may use FeatureListURL to point to a list of the\n        features represented in a Layer.\n      ')

    
    # Element {http://www.opengis.net/wms}Attribution uses Python identifier Attribution
    __Attribution = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Attribution'), 'Attribution', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsAttribution', False)

    
    Attribution = property(__Attribution.value, __Attribution.set, None, u"\n        Attribution indicates the provider of a Layer or collection of Layers.\n        The provider's URL, descriptive title string, and/or logo image URL\n        may be supplied.  Client applications may choose to display one or\n        more of these items.  A format element indicates the MIME type of\n        the logo image located at LogoURL.  The logo image's width and height\n        assist client applications in laying out space to display the logo.\n      ")

    
    # Element {http://www.opengis.net/wms}KeywordList uses Python identifier KeywordList
    __KeywordList = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'KeywordList'), 'KeywordList', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsKeywordList', False)

    
    KeywordList = property(__KeywordList.value, __KeywordList.set, None, u'\n        List of keywords or keyword phrases to help catalog searching.\n      ')

    
    # Element {http://www.opengis.net/wms}Style uses Python identifier Style
    __Style = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Style'), 'Style', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsStyle', True)

    
    Style = property(__Style.value, __Style.set, None, u'\n        A Style element lists the name by which a style is requested and a\n        human-readable title for pick lists, optionally (and ideally)\n        provides a human-readable description, and optionally gives a style\n        URL.\n      ')

    
    # Element {http://www.opengis.net/wms}AuthorityURL uses Python identifier AuthorityURL
    __AuthorityURL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'AuthorityURL'), 'AuthorityURL', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsAuthorityURL', True)

    
    AuthorityURL = property(__AuthorityURL.value, __AuthorityURL.set, None, u'\n        A Map Server may use zero or more Identifier elements to list ID\n        numbers or labels defined by a particular Authority.  For example,\n        the Global Change Master Directory (gcmd.gsfc.nasa.gov) defines a\n        DIF_ID label for every dataset.  The authority name and explanatory\n        URL are defined in a separate AuthorityURL element, which may be\n        defined once and inherited by subsidiary layers.  Identifiers\n        themselves are not inherited.\n      ')

    
    # Element {http://www.opengis.net/wms}CRS uses Python identifier CRS
    __CRS = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'CRS'), 'CRS', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsCRS', True)

    
    CRS = property(__CRS.value, __CRS.set, None, u'\n        Identifier for a single Coordinate Reference System (CRS).\n      ')

    
    # Element {http://www.opengis.net/wms}MinScaleDenominator uses Python identifier MinScaleDenominator
    __MinScaleDenominator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MinScaleDenominator'), 'MinScaleDenominator', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsMinScaleDenominator', False)

    
    MinScaleDenominator = property(__MinScaleDenominator.value, __MinScaleDenominator.set, None, u'\n        Minimum scale denominator for which it is appropriate to\n        display this layer.\n      ')

    
    # Element {http://www.opengis.net/wms}Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), 'Identifier', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsIdentifier', True)

    
    Identifier = property(__Identifier.value, __Identifier.set, None, None)

    
    # Element {http://www.opengis.net/wms}EX_GeographicBoundingBox uses Python identifier EX_GeographicBoundingBox
    __EX_GeographicBoundingBox = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'EX_GeographicBoundingBox'), 'EX_GeographicBoundingBox', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsEX_GeographicBoundingBox', False)

    
    EX_GeographicBoundingBox = property(__EX_GeographicBoundingBox.value, __EX_GeographicBoundingBox.set, None, u'\n        The EX_GeographicBoundingBox attributes indicate the limits of the enclosing\n        rectangle in longitude and latitude decimal degrees.\n      ')

    
    # Element {http://www.opengis.net/wms}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsName', False)

    
    Name = property(__Name.value, __Name.set, None, u'\n        The Name is typically for machine-to-machine communication.\n      ')

    
    # Element {http://www.opengis.net/wms}MaxScaleDenominator uses Python identifier MaxScaleDenominator
    __MaxScaleDenominator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MaxScaleDenominator'), 'MaxScaleDenominator', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsMaxScaleDenominator', False)

    
    MaxScaleDenominator = property(__MaxScaleDenominator.value, __MaxScaleDenominator.set, None, u'\n        Maximum scale denominator for which it is appropriate to\n        display this layer.\n      ')

    
    # Element {http://www.opengis.net/wms}MetadataURL uses Python identifier MetadataURL
    __MetadataURL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'MetadataURL'), 'MetadataURL', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsMetadataURL', True)

    
    MetadataURL = property(__MetadataURL.value, __MetadataURL.set, None, u'\n        A Map Server may use zero or more MetadataURL elements to offer\n        detailed, standardized metadata about the data underneath a\n        particular layer. The type attribute indicates the standard to which\n        the metadata complies.  The format element indicates how the metadata is structured.\n      ')

    
    # Element {http://www.opengis.net/wms}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Title'), 'Title', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsTitle', False)

    
    Title = property(__Title.value, __Title.set, None, u'\n        The Title is for informative display to a human.\n      ')

    
    # Element {http://www.opengis.net/wms}BoundingBox uses Python identifier BoundingBox
    __BoundingBox = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), 'BoundingBox', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsBoundingBox', True)

    
    BoundingBox = property(__BoundingBox.value, __BoundingBox.set, None, u'\n        The BoundingBox attributes indicate the limits of the bounding box\n        in units of the specified coordinate reference system.\n      ')

    
    # Element {http://www.opengis.net/wms}Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Layer'), 'Layer', '__httpwww_opengis_netwms_CTD_ANON_28_httpwww_opengis_netwmsLayer', True)

    
    Layer = property(__Layer.value, __Layer.set, None, u'\n        Nested list of zero or more map Layers offered by this server.\n      ')

    
    # Attribute noSubsets uses Python identifier noSubsets
    __noSubsets = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'noSubsets'), 'noSubsets', '__httpwww_opengis_netwms_CTD_ANON_28_noSubsets', pyxb.binding.datatypes.boolean, unicode_default=u'0')
    
    noSubsets = property(__noSubsets.value, __noSubsets.set, None, None)

    
    # Attribute fixedWidth uses Python identifier fixedWidth
    __fixedWidth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixedWidth'), 'fixedWidth', '__httpwww_opengis_netwms_CTD_ANON_28_fixedWidth', pyxb.binding.datatypes.nonNegativeInteger)
    
    fixedWidth = property(__fixedWidth.value, __fixedWidth.set, None, None)

    
    # Attribute fixedHeight uses Python identifier fixedHeight
    __fixedHeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fixedHeight'), 'fixedHeight', '__httpwww_opengis_netwms_CTD_ANON_28_fixedHeight', pyxb.binding.datatypes.nonNegativeInteger)
    
    fixedHeight = property(__fixedHeight.value, __fixedHeight.set, None, None)

    
    # Attribute queryable uses Python identifier queryable
    __queryable = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'queryable'), 'queryable', '__httpwww_opengis_netwms_CTD_ANON_28_queryable', pyxb.binding.datatypes.boolean, unicode_default=u'0')
    
    queryable = property(__queryable.value, __queryable.set, None, None)

    
    # Attribute cascaded uses Python identifier cascaded
    __cascaded = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cascaded'), 'cascaded', '__httpwww_opengis_netwms_CTD_ANON_28_cascaded', pyxb.binding.datatypes.nonNegativeInteger)
    
    cascaded = property(__cascaded.value, __cascaded.set, None, None)

    
    # Attribute opaque uses Python identifier opaque
    __opaque = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'opaque'), 'opaque', '__httpwww_opengis_netwms_CTD_ANON_28_opaque', pyxb.binding.datatypes.boolean, unicode_default=u'0')
    
    opaque = property(__opaque.value, __opaque.set, None, None)


    _ElementMap = {
        __DataURL.name() : __DataURL,
        __Dimension.name() : __Dimension,
        __Abstract.name() : __Abstract,
        __FeatureListURL.name() : __FeatureListURL,
        __Attribution.name() : __Attribution,
        __KeywordList.name() : __KeywordList,
        __Style.name() : __Style,
        __AuthorityURL.name() : __AuthorityURL,
        __CRS.name() : __CRS,
        __MinScaleDenominator.name() : __MinScaleDenominator,
        __Identifier.name() : __Identifier,
        __EX_GeographicBoundingBox.name() : __EX_GeographicBoundingBox,
        __Name.name() : __Name,
        __MaxScaleDenominator.name() : __MaxScaleDenominator,
        __MetadataURL.name() : __MetadataURL,
        __Title.name() : __Title,
        __BoundingBox.name() : __BoundingBox,
        __Layer.name() : __Layer
    }
    _AttributeMap = {
        __noSubsets.name() : __noSubsets,
        __fixedWidth.name() : __fixedWidth,
        __fixedHeight.name() : __fixedHeight,
        __queryable.name() : __queryable,
        __cascaded.name() : __cascaded,
        __opaque.name() : __opaque
    }



# Complex type CTD_ANON_29 with content type ELEMENT_ONLY
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/wms}LegendURL uses Python identifier LegendURL
    __LegendURL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'LegendURL'), 'LegendURL', '__httpwww_opengis_netwms_CTD_ANON_29_httpwww_opengis_netwmsLegendURL', True)

    
    LegendURL = property(__LegendURL.value, __LegendURL.set, None, u'\n        A Map Server may use zero or more LegendURL elements to provide an\n        image(s) of a legend relevant to each Style of a Layer.  The Format\n        element indicates the MIME type of the legend. Width and height\n        attributes may be provided to assist client applications in laying out\n        space to display the legend.\n      ')

    
    # Element {http://www.opengis.net/wms}StyleSheetURL uses Python identifier StyleSheetURL
    __StyleSheetURL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StyleSheetURL'), 'StyleSheetURL', '__httpwww_opengis_netwms_CTD_ANON_29_httpwww_opengis_netwmsStyleSheetURL', False)

    
    StyleSheetURL = property(__StyleSheetURL.value, __StyleSheetURL.set, None, u'\n        StyleSheeetURL provides symbology information for each Style of a Layer.\n      ')

    
    # Element {http://www.opengis.net/wms}StyleURL uses Python identifier StyleURL
    __StyleURL = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'StyleURL'), 'StyleURL', '__httpwww_opengis_netwms_CTD_ANON_29_httpwww_opengis_netwmsStyleURL', False)

    
    StyleURL = property(__StyleURL.value, __StyleURL.set, None, u'\n        A Map Server may use StyleURL to offer more information about the\n        data or symbology underlying a particular Style. While the semantics\n        are not well-defined, as long as the results of an HTTP GET request\n        against the StyleURL are properly MIME-typed, Viewer Clients and\n        Cascading Map Servers can make use of this. A possible use could be\n        to allow a Map Server to provide legend information.\n      ')

    
    # Element {http://www.opengis.net/wms}Name uses Python identifier Name
    __Name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Name'), 'Name', '__httpwww_opengis_netwms_CTD_ANON_29_httpwww_opengis_netwmsName', False)

    
    Name = property(__Name.value, __Name.set, None, u'\n        The Name is typically for machine-to-machine communication.\n      ')

    
    # Element {http://www.opengis.net/wms}Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Title'), 'Title', '__httpwww_opengis_netwms_CTD_ANON_29_httpwww_opengis_netwmsTitle', False)

    
    Title = property(__Title.value, __Title.set, None, u'\n        The Title is for informative display to a human.\n      ')

    
    # Element {http://www.opengis.net/wms}Abstract uses Python identifier Abstract
    __Abstract = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), 'Abstract', '__httpwww_opengis_netwms_CTD_ANON_29_httpwww_opengis_netwmsAbstract', False)

    
    Abstract = property(__Abstract.value, __Abstract.set, None, u'\n        The abstract is a longer narrative description of an object.\n      ')


    _ElementMap = {
        __LegendURL.name() : __LegendURL,
        __StyleSheetURL.name() : __StyleSheetURL,
        __StyleURL.name() : __StyleURL,
        __Name.name() : __Name,
        __Title.name() : __Title,
        __Abstract.name() : __Abstract
    }
    _AttributeMap = {
        
    }



HTTP = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HTTP'), CTD_ANON, documentation=u'\n        Available HTTP request methods.  At least "Get" shall be supported.\n      ')
Namespace.addCategoryObject('elementBinding', HTTP.name().localName(), HTTP)

Attribution = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Attribution'), CTD_ANON_3, documentation=u"\n        Attribution indicates the provider of a Layer or collection of Layers.\n        The provider's URL, descriptive title string, and/or logo image URL\n        may be supplied.  Client applications may choose to display one or\n        more of these items.  A format element indicates the MIME type of\n        the logo image located at LogoURL.  The logo image's width and height\n        assist client applications in laying out space to display the logo.\n      ")
Namespace.addCategoryObject('elementBinding', Attribution.name().localName(), Attribution)

LogoURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogoURL'), CTD_ANON_2)
Namespace.addCategoryObject('elementBinding', LogoURL.name().localName(), LogoURL)

LegendURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LegendURL'), CTD_ANON_6, documentation=u'\n        A Map Server may use zero or more LegendURL elements to provide an\n        image(s) of a legend relevant to each Style of a Layer.  The Format\n        element indicates the MIME type of the legend. Width and height\n        attributes may be provided to assist client applications in laying out\n        space to display the legend.\n      ')
Namespace.addCategoryObject('elementBinding', LegendURL.name().localName(), LegendURL)

ContactInformation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactInformation'), CTD_ANON_7, documentation=u'\n        Information about a contact person for the service.\n      ')
Namespace.addCategoryObject('elementBinding', ContactInformation.name().localName(), ContactInformation)

MetadataURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MetadataURL'), CTD_ANON_8, documentation=u'\n        A Map Server may use zero or more MetadataURL elements to offer\n        detailed, standardized metadata about the data underneath a\n        particular layer. The type attribute indicates the standard to which\n        the metadata complies.  The format element indicates how the metadata is structured.\n      ')
Namespace.addCategoryObject('elementBinding', MetadataURL.name().localName(), MetadataURL)

Name = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, documentation=u'\n        The Name is typically for machine-to-machine communication.\n      ')
Namespace.addCategoryObject('elementBinding', Name.name().localName(), Name)

Abstract = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), pyxb.binding.datatypes.string, documentation=u'\n        The abstract is a longer narrative description of an object.\n      ')
Namespace.addCategoryObject('elementBinding', Abstract.name().localName(), Abstract)

Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), CTD_ANON_10)
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

DataURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataURL'), CTD_ANON_11, documentation=u'\n        A Map Server may use DataURL offer a link to the underlying data represented\n        by a particular layer.\n      ')
Namespace.addCategoryObject('elementBinding', DataURL.name().localName(), DataURL)

OnlineResource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      ')
Namespace.addCategoryObject('elementBinding', OnlineResource.name().localName(), OnlineResource)

Service = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Service'), CTD_ANON_14, documentation=u'\n        General service metadata.\n      ')
Namespace.addCategoryObject('elementBinding', Service.name().localName(), Service)

Format = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, documentation=u"\n        A container for listing an available format's MIME type.\n      ")
Namespace.addCategoryObject('elementBinding', Format.name().localName(), Format)

ContactPersonPrimary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactPersonPrimary'), CTD_ANON_4)
Namespace.addCategoryObject('elementBinding', ContactPersonPrimary.name().localName(), ContactPersonPrimary)

StyleURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StyleURL'), CTD_ANON_13, documentation=u'\n        A Map Server may use StyleURL to offer more information about the\n        data or symbology underlying a particular Style. While the semantics\n        are not well-defined, as long as the results of an HTTP GET request\n        against the StyleURL are properly MIME-typed, Viewer Clients and\n        Cascading Map Servers can make use of this. A possible use could be\n        to allow a Map Server to provide legend information.\n      ')
Namespace.addCategoryObject('elementBinding', StyleURL.name().localName(), StyleURL)

ContactOrganization = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactOrganization'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', ContactOrganization.name().localName(), ContactOrganization)

ContactPosition = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactPosition'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', ContactPosition.name().localName(), ContactPosition)

MinScaleDenominator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinScaleDenominator'), pyxb.binding.datatypes.double, documentation=u'\n        Minimum scale denominator for which it is appropriate to\n        display this layer.\n      ')
Namespace.addCategoryObject('elementBinding', MinScaleDenominator.name().localName(), MinScaleDenominator)

MaxScaleDenominator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxScaleDenominator'), pyxb.binding.datatypes.double, documentation=u'\n        Maximum scale denominator for which it is appropriate to\n        display this layer.\n      ')
Namespace.addCategoryObject('elementBinding', MaxScaleDenominator.name().localName(), MaxScaleDenominator)

AddressType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AddressType'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', AddressType.name().localName(), AddressType)

Address = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', Address.name().localName(), Address)

Keyword = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Keyword'), CTD_ANON_21, documentation=u'\n        A single keyword or phrase.\n      ')
Namespace.addCategoryObject('elementBinding', Keyword.name().localName(), Keyword)

PostCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PostCode'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', PostCode.name().localName(), PostCode)

StyleSheetURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StyleSheetURL'), CTD_ANON_12, documentation=u'\n        StyleSheeetURL provides symbology information for each Style of a Layer.\n      ')
Namespace.addCategoryObject('elementBinding', StyleSheetURL.name().localName(), StyleSheetURL)

ContactVoiceTelephone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactVoiceTelephone'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', ContactVoiceTelephone.name().localName(), ContactVoiceTelephone)

ContactFacsimileTelephone = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactFacsimileTelephone'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', ContactFacsimileTelephone.name().localName(), ContactFacsimileTelephone)

ContactElectronicMailAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactElectronicMailAddress'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', ContactElectronicMailAddress.name().localName(), ContactElectronicMailAddress)

City = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'City'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', City.name().localName(), City)

Fees = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fees'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', Fees.name().localName(), Fees)

AccessConstraints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', AccessConstraints.name().localName(), AccessConstraints)

WMS_Capabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WMS_Capabilities'), CTD_ANON_24, documentation=u'\n        A WMS_Capabilities document is returned in response to a\n        GetCapabilities request made on a WMS.\n      ')
Namespace.addCategoryObject('elementBinding', WMS_Capabilities.name().localName(), WMS_Capabilities)

MaxWidth = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxWidth'), pyxb.binding.datatypes.positiveInteger)
Namespace.addCategoryObject('elementBinding', MaxWidth.name().localName(), MaxWidth)

MaxHeight = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxHeight'), pyxb.binding.datatypes.positiveInteger)
Namespace.addCategoryObject('elementBinding', MaxHeight.name().localName(), MaxHeight)

Capability = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Capability'), CTD_ANON_23, documentation=u'\n        A Capability lists available request types, how exceptions may be\n        reported, and whether any extended capabilities are defined.\n        It also includes an optional list of map layers available from this\n        server.\n      ')
Namespace.addCategoryObject('elementBinding', Capability.name().localName(), Capability)

Request = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Request'), CTD_ANON_25, documentation=u'\n        Available WMS Operations are listed in a Request element.\n      ')
Namespace.addCategoryObject('elementBinding', Request.name().localName(), Request)

GetCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GetCapabilities'), OperationType)
Namespace.addCategoryObject('elementBinding', GetCapabilities.name().localName(), GetCapabilities)

GetMap = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GetMap'), OperationType)
Namespace.addCategoryObject('elementBinding', GetMap.name().localName(), GetMap)

GetFeatureInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GetFeatureInfo'), OperationType)
Namespace.addCategoryObject('elementBinding', GetFeatureInfo.name().localName(), GetFeatureInfo)

ExtendedOperation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'_ExtendedOperation'), OperationType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', ExtendedOperation.name().localName(), ExtendedOperation)

ContactAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactAddress'), CTD_ANON_5)
Namespace.addCategoryObject('elementBinding', ContactAddress.name().localName(), ContactAddress)

DCPType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DCPType'), CTD_ANON_15, documentation=u'\n        Available Distributed Computing Platforms (DCPs) are listed here.\n        At present, only HTTP is defined.\n      ')
Namespace.addCategoryObject('elementBinding', DCPType.name().localName(), DCPType)

Get = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Get'), CTD_ANON_16, documentation=u'\n        The URL prefix for the HTTP "Get" request method.\n      ')
Namespace.addCategoryObject('elementBinding', Get.name().localName(), Get)

Post = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Post'), CTD_ANON_26, documentation=u'\n        The URL prefix for the HTTP "Post" request method.\n      ')
Namespace.addCategoryObject('elementBinding', Post.name().localName(), Post)

FeatureListURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FeatureListURL'), CTD_ANON_27, documentation=u'\n        A Map Server may use FeatureListURL to point to a list of the\n        features represented in a Layer.\n      ')
Namespace.addCategoryObject('elementBinding', FeatureListURL.name().localName(), FeatureListURL)

Exception = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Exception'), CTD_ANON_9, documentation=u'\n        An Exception element indicates which error-reporting formats are\n        supported.\n      ')
Namespace.addCategoryObject('elementBinding', Exception.name().localName(), Exception)

KeywordList = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KeywordList'), CTD_ANON_17, documentation=u'\n        List of keywords or keyword phrases to help catalog searching.\n      ')
Namespace.addCategoryObject('elementBinding', KeywordList.name().localName(), KeywordList)

ExtendedCapabilities = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'_ExtendedCapabilities'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), documentation=u'\n        Individual service providers may use this element to report extended\n        capabilities.\n      ')
Namespace.addCategoryObject('elementBinding', ExtendedCapabilities.name().localName(), ExtendedCapabilities)

Layer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Layer'), CTD_ANON_28, documentation=u'\n        Nested list of zero or more map Layers offered by this server.\n      ')
Namespace.addCategoryObject('elementBinding', Layer.name().localName(), Layer)

ContactPerson = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactPerson'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', ContactPerson.name().localName(), ContactPerson)

AuthorityURL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AuthorityURL'), CTD_ANON_22, documentation=u'\n        A Map Server may use zero or more Identifier elements to list ID\n        numbers or labels defined by a particular Authority.  For example,\n        the Global Change Master Directory (gcmd.gsfc.nasa.gov) defines a\n        DIF_ID label for every dataset.  The authority name and explanatory\n        URL are defined in a separate AuthorityURL element, which may be\n        defined once and inherited by subsidiary layers.  Identifiers\n        themselves are not inherited.\n      ')
Namespace.addCategoryObject('elementBinding', AuthorityURL.name().localName(), AuthorityURL)

Title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Title'), pyxb.binding.datatypes.string, documentation=u'\n        The Title is for informative display to a human.\n      ')
Namespace.addCategoryObject('elementBinding', Title.name().localName(), Title)

Style = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Style'), CTD_ANON_29, documentation=u'\n        A Style element lists the name by which a style is requested and a\n        human-readable title for pick lists, optionally (and ideally)\n        provides a human-readable description, and optionally gives a style\n        URL.\n      ')
Namespace.addCategoryObject('elementBinding', Style.name().localName(), Style)

CRS = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRS'), pyxb.binding.datatypes.string, documentation=u'\n        Identifier for a single Coordinate Reference System (CRS).\n      ')
Namespace.addCategoryObject('elementBinding', CRS.name().localName(), CRS)

EX_GeographicBoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EX_GeographicBoundingBox'), CTD_ANON_18, documentation=u'\n        The EX_GeographicBoundingBox attributes indicate the limits of the enclosing\n        rectangle in longitude and latitude decimal degrees.\n      ')
Namespace.addCategoryObject('elementBinding', EX_GeographicBoundingBox.name().localName(), EX_GeographicBoundingBox)

StateOrProvince = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StateOrProvince'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', StateOrProvince.name().localName(), StateOrProvince)

Country = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Country'), pyxb.binding.datatypes.string)
Namespace.addCategoryObject('elementBinding', Country.name().localName(), Country)

BoundingBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), CTD_ANON_19, documentation=u'\n        The BoundingBox attributes indicate the limits of the bounding box\n        in units of the specified coordinate reference system.\n      ')
Namespace.addCategoryObject('elementBinding', BoundingBox.name().localName(), BoundingBox)

LayerLimit = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LayerLimit'), pyxb.binding.datatypes.positiveInteger)
Namespace.addCategoryObject('elementBinding', LayerLimit.name().localName(), LayerLimit)

Dimension = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Dimension'), CTD_ANON_20, documentation=u'\n        The Dimension element declares the existence of a dimension and indicates what\n        values along a dimension are valid.\n      ')
Namespace.addCategoryObject('elementBinding', Dimension.name().localName(), Dimension)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Get'), CTD_ANON_16, scope=CTD_ANON, documentation=u'\n        The URL prefix for the HTTP "Get" request method.\n      '))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Post'), CTD_ANON_26, scope=CTD_ANON, documentation=u'\n        The URL prefix for the HTTP "Post" request method.\n      '))
CTD_ANON._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Get')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Post')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_2, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, documentation=u"\n        A container for listing an available format's MIME type.\n      "))
CTD_ANON_2._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_2._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_2._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_3, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Title'), pyxb.binding.datatypes.string, scope=CTD_ANON_3, documentation=u'\n        The Title is for informative display to a human.\n      '))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogoURL'), CTD_ANON_2, scope=CTD_ANON_3))
CTD_ANON_3._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogoURL')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_3._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_3._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactOrganization'), pyxb.binding.datatypes.string, scope=CTD_ANON_4))

CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactPerson'), pyxb.binding.datatypes.string, scope=CTD_ANON_4))
CTD_ANON_4._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactPerson')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactOrganization')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_4._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_4._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'City'), pyxb.binding.datatypes.string, scope=CTD_ANON_5))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StateOrProvince'), pyxb.binding.datatypes.string, scope=CTD_ANON_5))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PostCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_5))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Country'), pyxb.binding.datatypes.string, scope=CTD_ANON_5))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AddressType'), pyxb.binding.datatypes.string, scope=CTD_ANON_5))

CTD_ANON_5._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), pyxb.binding.datatypes.string, scope=CTD_ANON_5))
CTD_ANON_5._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AddressType')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Address')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'City')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StateOrProvince')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PostCode')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_5._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Country')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_5._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_5._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_6, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))

CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, scope=CTD_ANON_6, documentation=u"\n        A container for listing an available format's MIME type.\n      "))
CTD_ANON_6._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_6._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_6._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactPosition'), pyxb.binding.datatypes.string, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactAddress'), CTD_ANON_5, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactVoiceTelephone'), pyxb.binding.datatypes.string, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactFacsimileTelephone'), pyxb.binding.datatypes.string, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactElectronicMailAddress'), pyxb.binding.datatypes.string, scope=CTD_ANON_7))

CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactPersonPrimary'), CTD_ANON_4, scope=CTD_ANON_7))
CTD_ANON_7._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactPersonPrimary')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactPosition')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactAddress')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactVoiceTelephone')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactFacsimileTelephone')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactElectronicMailAddress')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_7._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_7._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_8, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))

CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, scope=CTD_ANON_8, documentation=u"\n        A container for listing an available format's MIME type.\n      "))
CTD_ANON_8._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_8._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_8._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, scope=CTD_ANON_9, documentation=u"\n        A container for listing an available format's MIME type.\n      "))
CTD_ANON_9._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format')), min_occurs=1, max_occurs=None)
    )
CTD_ANON_9._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_9._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_11, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))

CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, scope=CTD_ANON_11, documentation=u"\n        A container for listing an available format's MIME type.\n      "))
CTD_ANON_11._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_11._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_11._GroupModel, min_occurs=1, max_occurs=1)



OperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DCPType'), CTD_ANON_15, scope=OperationType, documentation=u'\n        Available Distributed Computing Platforms (DCPs) are listed here.\n        At present, only HTTP is defined.\n      '))

OperationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, scope=OperationType, documentation=u"\n        A container for listing an available format's MIME type.\n      "))
OperationType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(OperationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format')), min_occurs=1, max_occurs=None),
    pyxb.binding.content.ParticleModel(OperationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DCPType')), min_occurs=1, max_occurs=None)
    )
OperationType._ContentModel = pyxb.binding.content.ParticleModel(OperationType._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_12, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))

CTD_ANON_12._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, scope=CTD_ANON_12, documentation=u"\n        A container for listing an available format's MIME type.\n      "))
CTD_ANON_12._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_12._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_12._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_12._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_13, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, scope=CTD_ANON_13, documentation=u"\n        A container for listing an available format's MIME type.\n      "))
CTD_ANON_13._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_13._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_13._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, documentation=u'\n        The abstract is a longer narrative description of an object.\n      '))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KeywordList'), CTD_ANON_17, scope=CTD_ANON_14, documentation=u'\n        List of keywords or keyword phrases to help catalog searching.\n      '))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LayerLimit'), pyxb.binding.datatypes.positiveInteger, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_14, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxWidth'), pyxb.binding.datatypes.positiveInteger, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxHeight'), pyxb.binding.datatypes.positiveInteger, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContactInformation'), CTD_ANON_7, scope=CTD_ANON_14, documentation=u'\n        Information about a contact person for the service.\n      '))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Fees'), pyxb.binding.datatypes.string, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Title'), pyxb.binding.datatypes.string, scope=CTD_ANON_14, documentation=u'\n        The Title is for informative display to a human.\n      '))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints'), pyxb.binding.datatypes.string, scope=CTD_ANON_14))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), STD_ANON, scope=CTD_ANON_14))
CTD_ANON_14._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'KeywordList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContactInformation')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Fees')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AccessConstraints')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LayerLimit')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxWidth')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxHeight')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_14._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_14._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HTTP'), CTD_ANON, scope=CTD_ANON_15, documentation=u'\n        Available HTTP request methods.  At least "Get" shall be supported.\n      '))
CTD_ANON_15._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'HTTP')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_15._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_15._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_16, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))
CTD_ANON_16._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_16._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_16._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_17._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Keyword'), CTD_ANON_21, scope=CTD_ANON_17, documentation=u'\n        A single keyword or phrase.\n      '))
CTD_ANON_17._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_17._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Keyword')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_17._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_17._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eastBoundLongitude'), longitudeType, scope=CTD_ANON_18))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'southBoundLatitude'), latitudeType, scope=CTD_ANON_18))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'northBoundLatitude'), latitudeType, scope=CTD_ANON_18))

CTD_ANON_18._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'westBoundLongitude'), longitudeType, scope=CTD_ANON_18))
CTD_ANON_18._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'westBoundLongitude')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'eastBoundLongitude')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'southBoundLatitude')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_18._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'northBoundLatitude')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_18._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_18._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_22._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_22, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))
CTD_ANON_22._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_22._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_22._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_22._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Exception'), CTD_ANON_9, scope=CTD_ANON_23, documentation=u'\n        An Exception element indicates which error-reporting formats are\n        supported.\n      '))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'_ExtendedCapabilities'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_23, documentation=u'\n        Individual service providers may use this element to report extended\n        capabilities.\n      '))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Layer'), CTD_ANON_28, scope=CTD_ANON_23, documentation=u'\n        Nested list of zero or more map Layers offered by this server.\n      '))

CTD_ANON_23._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Request'), CTD_ANON_25, scope=CTD_ANON_23, documentation=u'\n        Available WMS Operations are listed in a Request element.\n      '))
CTD_ANON_23._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Request')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Exception')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'_ExtendedCapabilities')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_23._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Layer')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_23._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_23._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Capability'), CTD_ANON_23, scope=CTD_ANON_24, documentation=u'\n        A Capability lists available request types, how exceptions may be\n        reported, and whether any extended capabilities are defined.\n        It also includes an optional list of map layers available from this\n        server.\n      '))

CTD_ANON_24._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Service'), CTD_ANON_14, scope=CTD_ANON_24, documentation=u'\n        General service metadata.\n      '))
CTD_ANON_24._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Service')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_24._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Capability')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_24._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_24._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GetFeatureInfo'), OperationType, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GetMap'), OperationType, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'GetCapabilities'), OperationType, scope=CTD_ANON_25))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'_ExtendedOperation'), OperationType, abstract=pyxb.binding.datatypes.boolean(1), scope=CTD_ANON_25))
CTD_ANON_25._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GetCapabilities')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GetMap')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'GetFeatureInfo')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'_ExtendedOperation')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_25._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_25._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_26._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_26, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))
CTD_ANON_26._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_26._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_26._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_26._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource'), CTD_ANON_, scope=CTD_ANON_27, documentation=u'\n        An OnlineResource is typically an HTTP URL.  The URL is placed in\n        the xlink:href attribute, and the value "simple" is placed in the\n        xlink:type attribute.\n      '))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Format'), pyxb.binding.datatypes.string, scope=CTD_ANON_27, documentation=u"\n        A container for listing an available format's MIME type.\n      "))
CTD_ANON_27._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Format')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OnlineResource')), min_occurs=1, max_occurs=1)
    )
CTD_ANON_27._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_27._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DataURL'), CTD_ANON_11, scope=CTD_ANON_28, documentation=u'\n        A Map Server may use DataURL offer a link to the underlying data represented\n        by a particular layer.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Dimension'), CTD_ANON_20, scope=CTD_ANON_28, documentation=u'\n        The Dimension element declares the existence of a dimension and indicates what\n        values along a dimension are valid.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, documentation=u'\n        The abstract is a longer narrative description of an object.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FeatureListURL'), CTD_ANON_27, scope=CTD_ANON_28, documentation=u'\n        A Map Server may use FeatureListURL to point to a list of the\n        features represented in a Layer.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Attribution'), CTD_ANON_3, scope=CTD_ANON_28, documentation=u"\n        Attribution indicates the provider of a Layer or collection of Layers.\n        The provider's URL, descriptive title string, and/or logo image URL\n        may be supplied.  Client applications may choose to display one or\n        more of these items.  A format element indicates the MIME type of\n        the logo image located at LogoURL.  The logo image's width and height\n        assist client applications in laying out space to display the logo.\n      "))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KeywordList'), CTD_ANON_17, scope=CTD_ANON_28, documentation=u'\n        List of keywords or keyword phrases to help catalog searching.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Style'), CTD_ANON_29, scope=CTD_ANON_28, documentation=u'\n        A Style element lists the name by which a style is requested and a\n        human-readable title for pick lists, optionally (and ideally)\n        provides a human-readable description, and optionally gives a style\n        URL.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AuthorityURL'), CTD_ANON_22, scope=CTD_ANON_28, documentation=u'\n        A Map Server may use zero or more Identifier elements to list ID\n        numbers or labels defined by a particular Authority.  For example,\n        the Global Change Master Directory (gcmd.gsfc.nasa.gov) defines a\n        DIF_ID label for every dataset.  The authority name and explanatory\n        URL are defined in a separate AuthorityURL element, which may be\n        defined once and inherited by subsidiary layers.  Identifiers\n        themselves are not inherited.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'CRS'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, documentation=u'\n        Identifier for a single Coordinate Reference System (CRS).\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MinScaleDenominator'), pyxb.binding.datatypes.double, scope=CTD_ANON_28, documentation=u'\n        Minimum scale denominator for which it is appropriate to\n        display this layer.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Identifier'), CTD_ANON_10, scope=CTD_ANON_28))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EX_GeographicBoundingBox'), CTD_ANON_18, scope=CTD_ANON_28, documentation=u'\n        The EX_GeographicBoundingBox attributes indicate the limits of the enclosing\n        rectangle in longitude and latitude decimal degrees.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, documentation=u'\n        The Name is typically for machine-to-machine communication.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MaxScaleDenominator'), pyxb.binding.datatypes.double, scope=CTD_ANON_28, documentation=u'\n        Maximum scale denominator for which it is appropriate to\n        display this layer.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MetadataURL'), CTD_ANON_8, scope=CTD_ANON_28, documentation=u'\n        A Map Server may use zero or more MetadataURL elements to offer\n        detailed, standardized metadata about the data underneath a\n        particular layer. The type attribute indicates the standard to which\n        the metadata complies.  The format element indicates how the metadata is structured.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Title'), pyxb.binding.datatypes.string, scope=CTD_ANON_28, documentation=u'\n        The Title is for informative display to a human.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox'), CTD_ANON_19, scope=CTD_ANON_28, documentation=u'\n        The BoundingBox attributes indicate the limits of the bounding box\n        in units of the specified coordinate reference system.\n      '))

CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Layer'), CTD_ANON_28, scope=CTD_ANON_28, documentation=u'\n        Nested list of zero or more map Layers offered by this server.\n      '))
CTD_ANON_28._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'KeywordList')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'CRS')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EX_GeographicBoundingBox')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'BoundingBox')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Dimension')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Attribution')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AuthorityURL')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Identifier')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MetadataURL')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DataURL')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'FeatureListURL')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Style')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MinScaleDenominator')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'MaxScaleDenominator')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Layer')), min_occurs=0L, max_occurs=None)
    )
CTD_ANON_28._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_28._GroupModel, min_occurs=1, max_occurs=1)



CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LegendURL'), CTD_ANON_6, scope=CTD_ANON_29, documentation=u'\n        A Map Server may use zero or more LegendURL elements to provide an\n        image(s) of a legend relevant to each Style of a Layer.  The Format\n        element indicates the MIME type of the legend. Width and height\n        attributes may be provided to assist client applications in laying out\n        space to display the legend.\n      '))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StyleSheetURL'), CTD_ANON_12, scope=CTD_ANON_29, documentation=u'\n        StyleSheeetURL provides symbology information for each Style of a Layer.\n      '))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StyleURL'), CTD_ANON_13, scope=CTD_ANON_29, documentation=u'\n        A Map Server may use StyleURL to offer more information about the\n        data or symbology underlying a particular Style. While the semantics\n        are not well-defined, as long as the results of an HTTP GET request\n        against the StyleURL are properly MIME-typed, Viewer Clients and\n        Cascading Map Servers can make use of this. A possible use could be\n        to allow a Map Server to provide legend information.\n      '))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Name'), pyxb.binding.datatypes.string, scope=CTD_ANON_29, documentation=u'\n        The Name is typically for machine-to-machine communication.\n      '))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Title'), pyxb.binding.datatypes.string, scope=CTD_ANON_29, documentation=u'\n        The Title is for informative display to a human.\n      '))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Abstract'), pyxb.binding.datatypes.string, scope=CTD_ANON_29, documentation=u'\n        The abstract is a longer narrative description of an object.\n      '))
CTD_ANON_29._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Name')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Abstract')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LegendURL')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StyleSheetURL')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StyleURL')), min_occurs=0L, max_occurs=1)
    )
CTD_ANON_29._ContentModel = pyxb.binding.content.ParticleModel(CTD_ANON_29._GroupModel, min_occurs=1, max_occurs=1)
