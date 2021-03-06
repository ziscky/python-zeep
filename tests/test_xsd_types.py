import pytest
import six
from lxml import etree

from zeep.xsd import types


def test_base_type():
    # Basically just for coverage... ;-)
    base = types.Type()
    with pytest.raises(NotImplementedError):
        base.accept('x')

    with pytest.raises(NotImplementedError):
        base.parse_xmlelement(None)

    with pytest.raises(NotImplementedError):
        base.parsexml(None)

    with pytest.raises(NotImplementedError):
        base.render(None, None)

    with pytest.raises(NotImplementedError):
        base.resolve()

    base.signature() == ''


def test_simpletype_eq():
    type_1 = types.SimpleType()
    type_2 = types.SimpleType()

    assert type_1 == type_2


def test_simpletype_parse():
    node = etree.Element('foobar')
    item = types.SimpleType()

    assert item.parse_xmlelement(node) is None


def test_simpletype_xmlvalue():
    item = types.SimpleType()

    with pytest.raises(NotImplementedError):
        item.xmlvalue(None)


def test_simpletype_pythonvalue():
    item = types.SimpleType()

    with pytest.raises(NotImplementedError):
        item.pythonvalue(None)


def test_simpletype_call_wrong_arg_count():
    item = types.SimpleType()

    with pytest.raises(TypeError):
        item('foo', 'bar')


def test_simpletype_call_wrong_kwarg():
    item = types.SimpleType()

    with pytest.raises(TypeError):
        item(uhhh='x')


def test_simpletype_str():
    item = types.SimpleType()
    item.name = u'foobar'
    assert six.text_type(item) == u'foobar'


def test_complextype_parse_xmlelement_no_childs():
    xmlelement = etree.Element('foobar')
    item = types.ComplexType()
    assert item.parse_xmlelement(xmlelement, None) is None
