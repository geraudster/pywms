# .\_xlink.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b43cd366527ddb6a0e58594876e07421e0148f30
# Generated 2012-07-24 14:24:13.878000 by PyXB version 1.1.4
# Namespace http://www.w3.org/1999/xlink [xmlns:xlink]

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
import pyxb.binding.xml_

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink', create_if_missing=True)
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
class typeType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'typeType')
    _Documentation = None
typeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=typeType, enum_prefix=None)
typeType.simple = typeType._CF_enumeration.addEnumeration(unicode_value=u'simple', tag=u'simple')
typeType.extended = typeType._CF_enumeration.addEnumeration(unicode_value=u'extended', tag=u'extended')
typeType.title = typeType._CF_enumeration.addEnumeration(unicode_value=u'title', tag=u'title')
typeType.resource = typeType._CF_enumeration.addEnumeration(unicode_value=u'resource', tag=u'resource')
typeType.locator = typeType._CF_enumeration.addEnumeration(unicode_value=u'locator', tag=u'locator')
typeType.arc = typeType._CF_enumeration.addEnumeration(unicode_value=u'arc', tag=u'arc')
typeType._InitializeFacetMap(typeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'typeType', typeType)

# Atomic SimpleTypeDefinition
class titleAttrType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'titleAttrType')
    _Documentation = None
titleAttrType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'titleAttrType', titleAttrType)

# Atomic SimpleTypeDefinition
class roleType (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'roleType')
    _Documentation = None
roleType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
roleType._InitializeFacetMap(roleType._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'roleType', roleType)

# Atomic SimpleTypeDefinition
class labelType (pyxb.binding.datatypes.NCName):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'labelType')
    _Documentation = None
labelType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'labelType', labelType)

# Atomic SimpleTypeDefinition
class hrefType (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'hrefType')
    _Documentation = None
hrefType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'hrefType', hrefType)

# Atomic SimpleTypeDefinition
class showType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'showType')
    _Documentation = None
showType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=showType, enum_prefix=None)
showType.new = showType._CF_enumeration.addEnumeration(unicode_value=u'new', tag=u'new')
showType.replace = showType._CF_enumeration.addEnumeration(unicode_value=u'replace', tag=u'replace')
showType.embed = showType._CF_enumeration.addEnumeration(unicode_value=u'embed', tag=u'embed')
showType.other = showType._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
showType.none = showType._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
showType._InitializeFacetMap(showType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'showType', showType)

# Atomic SimpleTypeDefinition
class actuateType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'actuateType')
    _Documentation = None
actuateType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=actuateType, enum_prefix=None)
actuateType.onLoad = actuateType._CF_enumeration.addEnumeration(unicode_value=u'onLoad', tag=u'onLoad')
actuateType.onRequest = actuateType._CF_enumeration.addEnumeration(unicode_value=u'onRequest', tag=u'onRequest')
actuateType.other = actuateType._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
actuateType.none = actuateType._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
actuateType._InitializeFacetMap(actuateType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'actuateType', actuateType)

# Atomic SimpleTypeDefinition
class fromType (pyxb.binding.datatypes.NCName):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fromType')
    _Documentation = None
fromType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'fromType', fromType)

# Atomic SimpleTypeDefinition
class toType (pyxb.binding.datatypes.NCName):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'toType')
    _Documentation = None
toType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'toType', toType)

# Atomic SimpleTypeDefinition
class arcroleType (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'arcroleType')
    _Documentation = None
arcroleType._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
arcroleType._InitializeFacetMap(arcroleType._CF_minLength)
Namespace.addCategoryObject('typeBinding', u'arcroleType', arcroleType)

# Complex type locatorType with content type ELEMENT_ONLY
class locatorType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'locatorType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org1999xlink_locatorType_httpwww_w3_org1999xlinktitle', True)

    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'href'), 'href', '__httpwww_w3_org1999xlink_locatorType_httpwww_w3_org1999xlinkhref', hrefType, required=True)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_w3_org1999xlink_locatorType_httpwww_w3_org1999xlinktype', typeType, fixed=True, unicode_default=u'locator', required=True)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'role'), 'role', '__httpwww_w3_org1999xlink_locatorType_httpwww_w3_org1999xlinkrole', roleType)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title_
    __title_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title_', '__httpwww_w3_org1999xlink_locatorType_httpwww_w3_org1999xlinktitle_', titleAttrType)
    
    title_ = property(__title_.value, __title_.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'label'), 'label', '__httpwww_w3_org1999xlink_locatorType_httpwww_w3_org1999xlinklabel', labelType)
    
    label = property(__label.value, __label.set, None, None)


    _ElementMap = {
        __title.name() : __title
    }
    _AttributeMap = {
        __href.name() : __href,
        __type.name() : __type,
        __role.name() : __role,
        __title_.name() : __title_,
        __label.name() : __label
    }
Namespace.addCategoryObject('typeBinding', u'locatorType', locatorType)


# Complex type resourceType with content type MIXED
class resourceType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'resourceType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_w3_org1999xlink_resourceType_httpwww_w3_org1999xlinktype', typeType, fixed=True, unicode_default=u'resource', required=True)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'label'), 'label', '__httpwww_w3_org1999xlink_resourceType_httpwww_w3_org1999xlinklabel', labelType)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org1999xlink_resourceType_httpwww_w3_org1999xlinktitle', titleAttrType)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'role'), 'role', '__httpwww_w3_org1999xlink_resourceType_httpwww_w3_org1999xlinkrole', roleType)
    
    role = property(__role.value, __role.set, None, None)

    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __type.name() : __type,
        __label.name() : __label,
        __title.name() : __title,
        __role.name() : __role
    }
Namespace.addCategoryObject('typeBinding', u'resourceType', resourceType)


# Complex type arcType with content type ELEMENT_ONLY
class arcType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'arcType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org1999xlink_arcType_httpwww_w3_org1999xlinktitle', True)

    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title_
    __title_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title_', '__httpwww_w3_org1999xlink_arcType_httpwww_w3_org1999xlinktitle_', titleAttrType)
    
    title_ = property(__title_.value, __title_.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'arcrole'), 'arcrole', '__httpwww_w3_org1999xlink_arcType_httpwww_w3_org1999xlinkarcrole', arcroleType)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'show'), 'show', '__httpwww_w3_org1999xlink_arcType_httpwww_w3_org1999xlinkshow', showType)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'actuate'), 'actuate', '__httpwww_w3_org1999xlink_arcType_httpwww_w3_org1999xlinkactuate', actuateType)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_w3_org1999xlink_arcType_httpwww_w3_org1999xlinktype', typeType, fixed=True, unicode_default=u'arc', required=True)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'from'), 'from_', '__httpwww_w3_org1999xlink_arcType_httpwww_w3_org1999xlinkfrom', fromType)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'to'), 'to', '__httpwww_w3_org1999xlink_arcType_httpwww_w3_org1999xlinkto', toType)
    
    to = property(__to.value, __to.set, None, None)


    _ElementMap = {
        __title.name() : __title
    }
    _AttributeMap = {
        __title_.name() : __title_,
        __arcrole.name() : __arcrole,
        __show.name() : __show,
        __actuate.name() : __actuate,
        __type.name() : __type,
        __from.name() : __from,
        __to.name() : __to
    }
Namespace.addCategoryObject('typeBinding', u'arcType', arcType)


# Complex type titleEltType with content type MIXED
class titleEltType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'titleEltType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_w3_org1999xlink_titleEltType_httpwww_w3_org1999xlinktype', typeType, fixed=True, unicode_default=u'title', required=True)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org1999xlink_titleEltType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    
    lang = property(__lang.value, __lang.set, None, None)

    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __type.name() : __type,
        __lang.name() : __lang
    }
Namespace.addCategoryObject('typeBinding', u'titleEltType', titleEltType)


# Complex type simple with content type MIXED
class simple (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'simple')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org1999xlink_simple_httpwww_w3_org1999xlinktitle', titleAttrType)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'role'), 'role', '__httpwww_w3_org1999xlink_simple_httpwww_w3_org1999xlinkrole', roleType)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'show'), 'show', '__httpwww_w3_org1999xlink_simple_httpwww_w3_org1999xlinkshow', showType)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'actuate'), 'actuate', '__httpwww_w3_org1999xlink_simple_httpwww_w3_org1999xlinkactuate', actuateType)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_w3_org1999xlink_simple_httpwww_w3_org1999xlinktype', typeType, fixed=True, unicode_default=u'simple')
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'href'), 'href', '__httpwww_w3_org1999xlink_simple_httpwww_w3_org1999xlinkhref', hrefType)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'arcrole'), 'arcrole', '__httpwww_w3_org1999xlink_simple_httpwww_w3_org1999xlinkarcrole', arcroleType)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __title.name() : __title,
        __role.name() : __role,
        __show.name() : __show,
        __actuate.name() : __actuate,
        __type.name() : __type,
        __href.name() : __href,
        __arcrole.name() : __arcrole
    }
Namespace.addCategoryObject('typeBinding', u'simple', simple)


# Complex type extended with content type ELEMENT_ONLY
class extended (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'extended')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/1999/xlink}arc uses Python identifier arc
    __arc = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'arc'), 'arc', '__httpwww_w3_org1999xlink_extended_httpwww_w3_org1999xlinkarc', True)

    
    arc = property(__arc.value, __arc.set, None, None)

    
    # Element {http://www.w3.org/1999/xlink}locator uses Python identifier locator
    __locator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'locator'), 'locator', '__httpwww_w3_org1999xlink_extended_httpwww_w3_org1999xlinklocator', True)

    
    locator = property(__locator.value, __locator.set, None, None)

    
    # Element {http://www.w3.org/1999/xlink}resource uses Python identifier resource
    __resource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'resource'), 'resource', '__httpwww_w3_org1999xlink_extended_httpwww_w3_org1999xlinkresource', True)

    
    resource = property(__resource.value, __resource.set, None, None)

    
    # Element {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org1999xlink_extended_httpwww_w3_org1999xlinktitle', True)

    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title_
    __title_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title_', '__httpwww_w3_org1999xlink_extended_httpwww_w3_org1999xlinktitle_', titleAttrType)
    
    title_ = property(__title_.value, __title_.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'role'), 'role', '__httpwww_w3_org1999xlink_extended_httpwww_w3_org1999xlinkrole', roleType)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_w3_org1999xlink_extended_httpwww_w3_org1999xlinktype', typeType, fixed=True, unicode_default=u'extended', required=True)
    
    type = property(__type.value, __type.set, None, None)


    _ElementMap = {
        __arc.name() : __arc,
        __locator.name() : __locator,
        __resource.name() : __resource,
        __title.name() : __title
    }
    _AttributeMap = {
        __title_.name() : __title_,
        __role.name() : __role,
        __type.name() : __type
    }
Namespace.addCategoryObject('typeBinding', u'extended', extended)


resource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), resourceType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', resource.name().localName(), resource)

locator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'locator'), locatorType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', locator.name().localName(), locator)

arc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'arc'), arcType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', arc.name().localName(), arc)

title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), titleEltType, abstract=pyxb.binding.datatypes.boolean(1))
Namespace.addCategoryObject('elementBinding', title.name().localName(), title)



locatorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), titleEltType, abstract=pyxb.binding.datatypes.boolean(1), scope=locatorType))
locatorType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(locatorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=0L, max_occurs=None)
    )
locatorType._ContentModel = pyxb.binding.content.ParticleModel(locatorType._GroupModel, min_occurs=1, max_occurs=1)


resourceType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), min_occurs=0L, max_occurs=None)
    )
resourceType._ContentModel = pyxb.binding.content.ParticleModel(resourceType._GroupModel, min_occurs=1, max_occurs=1)



arcType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), titleEltType, abstract=pyxb.binding.datatypes.boolean(1), scope=arcType))
arcType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(arcType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=0L, max_occurs=None)
    )
arcType._ContentModel = pyxb.binding.content.ParticleModel(arcType._GroupModel, min_occurs=1, max_occurs=1)


titleEltType._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), min_occurs=0L, max_occurs=None)
    )
titleEltType._ContentModel = pyxb.binding.content.ParticleModel(titleEltType._GroupModel, min_occurs=1, max_occurs=1)


simple._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), min_occurs=0L, max_occurs=None)
    )
simple._ContentModel = pyxb.binding.content.ParticleModel(simple._GroupModel, min_occurs=1, max_occurs=1)



extended._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'arc'), arcType, abstract=pyxb.binding.datatypes.boolean(1), scope=extended))

extended._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'locator'), locatorType, abstract=pyxb.binding.datatypes.boolean(1), scope=extended))

extended._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), resourceType, abstract=pyxb.binding.datatypes.boolean(1), scope=extended))

extended._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), titleEltType, abstract=pyxb.binding.datatypes.boolean(1), scope=extended))
extended._GroupModel = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(extended._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(extended._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'resource')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(extended._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'locator')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(extended._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'arc')), min_occurs=1, max_occurs=1)
    )
extended._ContentModel = pyxb.binding.content.ParticleModel(extended._GroupModel, min_occurs=0L, max_occurs=None)
