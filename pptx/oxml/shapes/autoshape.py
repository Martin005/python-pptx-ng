# encoding: utf-8

"""
lxml custom element classes for shape-related XML elements.
"""

from __future__ import absolute_import

from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE, PP_PLACEHOLDER
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls
from pptx.oxml.shapes.shared import BaseShapeElement
from pptx.oxml.simpletypes import (
    ST_Coordinate,
    ST_PositiveCoordinate,
    ST_ShapeType,
    XsdBoolean,
    XsdString,
    ST_AdjCoordinate,
    ST_PathFillMode,
    ST_AdjAngle,
)
from pptx.oxml.text import CT_TextBody
from pptx.oxml.xmlchemy import (
    BaseOxmlElement,
    OneAndOnlyOne,
    OptionalAttribute,
    RequiredAttribute,
    ZeroOrOne,
    ZeroOrMore,
    OneOrMore,
)


class CT_AdjPoint2D(BaseOxmlElement):
    """`a:pt` custom element class."""

    x = RequiredAttribute("x", ST_AdjCoordinate)
    y = RequiredAttribute("y", ST_AdjCoordinate)


class CT_CustomGeometry2D(BaseOxmlElement):
    """`a:custGeom` custom element class."""

    _tag_seq = ("a:avLst", "a:gdLst", "a:ahLst", "a:cxnLst", "a:rect", "a:pathLst")
    avLst = ZeroOrOne("a:avLst", successors=_tag_seq[1:])
    gdLst = ZeroOrOne("a:gdLst", successors=_tag_seq[2:])
    ahLst = ZeroOrOne("a:ahLst", successors=_tag_seq[3:])
    cxnLst = ZeroOrOne("a:cxnLst", successors=_tag_seq[4:])
    rect = ZeroOrOne("a:rect", successors=_tag_seq[5:])
    pathLst = ZeroOrOne("a:pathLst", successors=_tag_seq[6:])
    del _tag_seq


class CT_GeomGuide(BaseOxmlElement):
    """
    ``<a:gd>`` custom element class, defining a "guide", corresponding to
    a yellow diamond-shaped handle on an autoshape.
    """

    name = RequiredAttribute("name", XsdString)
    fmla = RequiredAttribute("fmla", XsdString)


class CT_GeomGuideList(BaseOxmlElement):
    """
    ``<a:avLst>`` and ``<a:gdLst>`` custom element class
    """

    gd = ZeroOrMore("a:gd")


class CT_ConnectionSiteList(BaseOxmlElement):
    """
    ``<a:cxnLst>`` custom element class
    """
    cxn = ZeroOrMore("a:cxn")

class CT_ConnectionSite(BaseOxmlElement):
    """
    ``<a:cxn>`` custom element class
    """
    pos = ZeroOrOne("a:pos")

    ang = RequiredAttribute("ang", ST_AdjAngle)


class CT_GeomRect(BaseOxmlElement):
    """
    ``<a:rect>`` custom element class
    """
    l = RequiredAttribute("l", ST_AdjCoordinate)
    t = RequiredAttribute("t", ST_AdjCoordinate)
    r = RequiredAttribute("r", ST_AdjCoordinate)
    b = RequiredAttribute("b", ST_AdjCoordinate)


class CT_NonVisualDrawingShapeProps(BaseShapeElement):
    """
    ``<p:cNvSpPr>`` custom element class
    """

    spLocks = ZeroOrOne("a:spLocks")
    txBox = OptionalAttribute("txBox", XsdBoolean)


class CT_Path2D(BaseOxmlElement):
    """`a:path` custom element class."""

    close = ZeroOrMore("a:close", successors=())
    moveTo = ZeroOrMore("a:moveTo", successors=())
    lnTo = ZeroOrMore("a:lnTo", successors=())
    arcTo = ZeroOrMore("a:arcTo", successors=())
    quadBezTo = ZeroOrMore("a:quadBezTo", successors=())
    cubicBezTo = ZeroOrMore("a:cubicBezTo", successors=())

    w = OptionalAttribute("w", ST_PositiveCoordinate)
    h = OptionalAttribute("h", ST_PositiveCoordinate)
    fill = OptionalAttribute("fill", ST_PathFillMode, default="norm")
    stroke = OptionalAttribute("stroke", XsdBoolean, default=True)
    extrusionOk = OptionalAttribute("extrusionOk", XsdBoolean, default=True)

    def add_close(self):
        """Return a newly created `a:close` element.

        The new `a:close` element is appended to this `a:path` element.
        """
        return self._add_close()

    def add_lnTo(self, x, y):
        """Return a newly created `a:lnTo` subtree with end point *(x, y)*.

        The new `a:lnTo` element is appended to this `a:path` element.
        """
        lnTo = self._add_lnTo()
        pt = lnTo._add_pt()
        pt.x, pt.y = x, y
        return lnTo

    def add_moveTo(self, x, y):
        """Return a newly created `a:moveTo` subtree with point *(x, y)*.

        The new `a:moveTo` element is appended to this `a:path` element.
        """
        moveTo = self._add_moveTo()
        pt = moveTo._add_pt()
        pt.x, pt.y = x, y
        return moveTo

    def add_arcTo(self, wR, hR, stAng, swAng):
        """Return a newly created `a:moveTo` subtree with point *(x, y)*.

        The new `a:moveTo` element is appended to this `a:path` element.
        """
        arcTo = self._add_arcTo()
        arcTo.wR = wR
        arcTo.hR = hR
        arcTo.stAng = stAng
        arcTo.swAng = swAng
        return arcTo

    def add_quadBezTo(self, point1, point2):
        """Return a newly created `a:quadBezTo` subtree with two  points *(x, y)*.

        The new `a:quadBezTo` element is appended to this `a:path` element.
        """
        quadBezTo = self._add_quadBezTo()
        pt1 = quadBezTo._add_pt()
        pt1.x, pt1.y = point1[0], point1[1]
        pt2 = quadBezTo._add_pt()
        pt2.x, pt2.y = point2[0], point2[1]
        return quadBezTo


    def add_cubicBezTo(self, point1, point2, point3):
        """Return a newly created `a:cubicBezTo` subtree with two  points *(x, y)*.

        The new `a:cubicBezTo` element is appended to this `a:path` element.
        """
        cubicBezTo = self._add_cubicBezTo()
        pt1 = cubicBezTo._add_pt()
        pt1.x, pt1.y = point1[0], point1[1]
        pt2 = cubicBezTo._add_pt()
        pt2.x, pt2.y = point2[0], point2[1]
        pt3 = cubicBezTo._add_pt()
        pt3.x, pt3.y = point3[0], point3[1]
        return cubicBezTo


class CT_Path2DClose(BaseOxmlElement):
    """`a:close` custom element class."""


class CT_Path2DLineTo(BaseOxmlElement):
    """`a:lnTo` custom element class."""

    pt = ZeroOrOne("a:pt", successors=())


class CT_Path2DArcTo(BaseOxmlElement):
    """`a:arcTo` custom element class."""

    wR = RequiredAttribute("wR", ST_AdjCoordinate)
    hR = RequiredAttribute("hR", ST_AdjCoordinate)
    stAng = RequiredAttribute("stAng", ST_AdjAngle)
    swAng = RequiredAttribute("swAng", ST_AdjAngle)

class CT_Path2DList(BaseOxmlElement):
    """`a:pathLst` custom element class."""

    path = ZeroOrMore("a:path", successors=())

    def add_path(self, w, h):
        """Return a newly created `a:path` child element."""
        path = self._add_path()
        path.w, path.h = w, h
        return path


class CT_Path2DQuadBezierTo(BaseOxmlElement):
    """`a:quadBezTo` custom element class."""
    # Technically this should be a TwoAndOnlyTwo()
    pt = OneOrMore("a:pt")

class CT_Path2DCubicBezierTo(BaseOxmlElement):
    """`a:cubicBezTo` custom element class."""
    # Technically this should be a ThreeAndOnlyThree()
    pt = OneOrMore("a:pt")

class CT_Path2DMoveTo(BaseOxmlElement):
    """`a:moveTo` custom element class."""
    # Should be OneAndOnlyOne()
    pt = ZeroOrOne("a:pt", successors=())


class CT_PresetGeometry2D(BaseOxmlElement):
    """
    <a:prstGeom> custom element class
    """

    avLst = ZeroOrOne("a:avLst")
    preset = RequiredAttribute("prst", ST_ShapeType)

    @property
    def prst(self):
        """ 
        Handles list of shapes for both AutoShapes and Connectors
        If it is an autoshape, it returns a member of MSO_AUTO_SHAPE_TYPE while
        connectors just receive the text string from the XML.
        """
        connector_list = [
            "line",
            "straightConnector1",
            "bentConnector2",
            "bentConnector3",
            "bentConnector4",
            "bentConnector5",
            "curvedConnector2",
            "curvedConnector3",
            "curvedConnector4",
            "curvedConnector5",
        ]
        if self.preset in connector_list:
            return self.preset
        return MSO_AUTO_SHAPE_TYPE.from_xml(self.preset)
    
    @property
    def gd_lst(self):
        """
        Sequence containing the ``gd`` element children of ``<a:avLst>``
        child element, empty if none are present.
        """
        avLst = self.avLst
        if avLst is None:
            return []
        return avLst.gd_lst

    def rewrite_guides(self, guides):
        """
        Remove any ``<a:gd>`` element children of ``<a:avLst>`` and replace
        them with ones having (name, val) in *guides*.
        """
        self._remove_avLst()
        avLst = self._add_avLst()
        for name, val in guides:
            gd = avLst._add_gd()
            gd.name = name
            gd.fmla = "val %d" % val

class CT_Shape(BaseShapeElement):
    """
    ``<p:sp>`` custom element class
    """

    nvSpPr = OneAndOnlyOne("p:nvSpPr")
    spPr = OneAndOnlyOne("p:spPr")
    txBody = ZeroOrOne("p:txBody", successors=("p:extLst",))

    def add_path(self, w, h):
        """Reference to `a:custGeom` descendant or |None| if not present."""
        custGeom = self.spPr.custGeom
        if custGeom is None:
            raise ValueError("shape must be freeform")
        pathLst = custGeom.get_or_add_pathLst()
        return pathLst.add_path(w=w, h=h)

    def get_or_add_ln(self):
        """
        Return the <a:ln> grandchild element, newly added if not present.
        """
        return self.spPr.get_or_add_ln()

    @property
    def has_custom_geometry(self):
        """True if this shape has custom geometry, i.e. is a freeform shape.

        A shape has custom geometry if it has a `p:spPr/a:custGeom`
        descendant (instead of `p:spPr/a:prstGeom`).
        """
        return self.spPr.custGeom is not None

    @property
    def is_autoshape(self):
        """
        True if this shape is an auto shape. A shape is an auto shape if it
        has a ``<a:prstGeom>`` element and does not have a txBox="1" attribute
        on cNvSpPr.
        """
        prstGeom = self.prstGeom
        if prstGeom is None:
            return False
        if self.nvSpPr.cNvSpPr.txBox is True:
            return False
        return True

    @property
    def is_textbox(self):
        """
        True if this shape is a text box. A shape is a text box if it has a
        ``txBox`` attribute on cNvSpPr that resolves to |True|. The default
        when the txBox attribute is missing is |False|.
        """
        if self.nvSpPr.cNvSpPr.txBox is True:
            return True
        return False

    @property
    def ln(self):
        """
        ``<a:ln>`` grand-child element or |None| if not present
        """
        return self.spPr.ln

    @staticmethod
    def new_autoshape_sp(id_, name, prst, left, top, width, height):
        """
        Return a new ``<p:sp>`` element tree configured as a base auto shape.
        """
        tmpl = CT_Shape._autoshape_sp_tmpl()
        xml = tmpl % (id_, name, left, top, width, height, prst)
        sp = parse_xml(xml)
        return sp

    @staticmethod
    def new_freeform_sp(shape_id, name, x, y, cx, cy):
        """Return new `p:sp` element tree configured as freeform shape.

        The returned shape has a `a:custGeom` subtree but no paths in its
        path list.
        """
        tmpl = CT_Shape._freeform_sp_tmpl()
        xml = tmpl % (shape_id, name, x, y, cx, cy)
        sp = parse_xml(xml)
        return sp

    @staticmethod
    def new_placeholder_sp(id_, name, ph_type, orient, sz, idx):
        """
        Return a new ``<p:sp>`` element tree configured as a placeholder
        shape.
        """
        tmpl = CT_Shape._ph_sp_tmpl()
        xml = tmpl % (id_, name)
        sp = parse_xml(xml)

        ph = sp.nvSpPr.nvPr.get_or_add_ph()
        ph.type = ph_type
        ph.idx = idx
        ph.orient = orient
        ph.sz = sz

        placeholder_types_that_have_a_text_frame = (
            PP_PLACEHOLDER.TITLE,
            PP_PLACEHOLDER.CENTER_TITLE,
            PP_PLACEHOLDER.SUBTITLE,
            PP_PLACEHOLDER.BODY,
            PP_PLACEHOLDER.OBJECT,
        )

        if ph_type in placeholder_types_that_have_a_text_frame:
            sp.append(CT_TextBody.new())

        return sp

    @staticmethod
    def new_textbox_sp(id_, name, left, top, width, height):
        """
        Return a new ``<p:sp>`` element tree configured as a base textbox
        shape.
        """
        tmpl = CT_Shape._textbox_sp_tmpl()
        xml = tmpl % (id_, name, left, top, width, height)
        sp = parse_xml(xml)
        return sp

    @property
    def prst(self):
        """
        Value of ``prst`` attribute of ``<a:prstGeom>`` element or |None| if
        not present.
        """
        prstGeom = self.prstGeom
        if prstGeom is None:
            return None
        return prstGeom.prst

    @property
    def prstGeom(self):
        """
        Reference to ``<a:prstGeom>`` child element or |None| if this shape
        doesn't have one, for example, if it's a placeholder shape.
        """
        return self.spPr.prstGeom

    @property
    def custGeom(self):
        """
        Reference to ``<a:custGeom>`` child element or |None| if this shape 
        doesn't have one.
        """
        return self.spPr.custGeom


    @staticmethod
    def _autoshape_sp_tmpl():
        return (
            "<p:sp %s>\n"
            "  <p:nvSpPr>\n"
            '    <p:cNvPr id="%s" name="%s"/>\n'
            "    <p:cNvSpPr/>\n"
            "    <p:nvPr/>\n"
            "  </p:nvSpPr>\n"
            "  <p:spPr>\n"
            "    <a:xfrm>\n"
            '      <a:off x="%s" y="%s"/>\n'
            '      <a:ext cx="%s" cy="%s"/>\n'
            "    </a:xfrm>\n"
            '    <a:prstGeom prst="%s">\n'
            "      <a:avLst/>\n"
            "    </a:prstGeom>\n"
            "  </p:spPr>\n"
            "  <p:style>\n"
            '    <a:lnRef idx="1">\n'
            '      <a:schemeClr val="accent1"/>\n'
            "    </a:lnRef>\n"
            '    <a:fillRef idx="3">\n'
            '      <a:schemeClr val="accent1"/>\n'
            "    </a:fillRef>\n"
            '    <a:effectRef idx="2">\n'
            '      <a:schemeClr val="accent1"/>\n'
            "    </a:effectRef>\n"
            '    <a:fontRef idx="minor">\n'
            '      <a:schemeClr val="lt1"/>\n'
            "    </a:fontRef>\n"
            "  </p:style>\n"
            "  <p:txBody>\n"
            '    <a:bodyPr rtlCol="0" anchor="ctr"/>\n'
            "    <a:lstStyle/>\n"
            "    <a:p>\n"
            '      <a:pPr algn="ctr"/>\n'
            "    </a:p>\n"
            "  </p:txBody>\n"
            "</p:sp>" % (nsdecls("a", "p"), "%d", "%s", "%d", "%d", "%d", "%d", "%s")
        )

    @staticmethod
    def _freeform_sp_tmpl():
        return (
            "<p:sp %s>\n"
            "  <p:nvSpPr>\n"
            '    <p:cNvPr id="%s" name="%s"/>\n'
            "    <p:cNvSpPr/>\n"
            "    <p:nvPr/>\n"
            "  </p:nvSpPr>\n"
            "  <p:spPr>\n"
            "    <a:xfrm>\n"
            '      <a:off x="%s" y="%s"/>\n'
            '      <a:ext cx="%s" cy="%s"/>\n'
            "    </a:xfrm>\n"
            "    <a:custGeom>\n"
            "      <a:avLst/>\n"
            "      <a:gdLst/>\n"
            "      <a:ahLst/>\n"
            "      <a:cxnLst/>\n"
            '      <a:rect l="l" t="t" r="r" b="b"/>\n'
            "      <a:pathLst/>\n"
            "    </a:custGeom>\n"
            "  </p:spPr>\n"
            "  <p:style>\n"
            '    <a:lnRef idx="1">\n'
            '      <a:schemeClr val="accent1"/>\n'
            "    </a:lnRef>\n"
            '    <a:fillRef idx="3">\n'
            '      <a:schemeClr val="accent1"/>\n'
            "    </a:fillRef>\n"
            '    <a:effectRef idx="2">\n'
            '      <a:schemeClr val="accent1"/>\n'
            "    </a:effectRef>\n"
            '    <a:fontRef idx="minor">\n'
            '      <a:schemeClr val="lt1"/>\n'
            "    </a:fontRef>\n"
            "  </p:style>\n"
            "  <p:txBody>\n"
            '    <a:bodyPr rtlCol="0" anchor="ctr"/>\n'
            "    <a:lstStyle/>\n"
            "    <a:p>\n"
            '      <a:pPr algn="ctr"/>\n'
            "    </a:p>\n"
            "  </p:txBody>\n"
            "</p:sp>" % (nsdecls("a", "p"), "%d", "%s", "%d", "%d", "%d", "%d")
        )

    def _new_txBody(self):
        return CT_TextBody.new_p_txBody()

    @staticmethod
    def _ph_sp_tmpl():
        return (
            "<p:sp %s>\n"
            "  <p:nvSpPr>\n"
            '    <p:cNvPr id="%s" name="%s"/>\n'
            "    <p:cNvSpPr>\n"
            '      <a:spLocks noGrp="1"/>\n'
            "    </p:cNvSpPr>\n"
            "    <p:nvPr/>\n"
            "  </p:nvSpPr>\n"
            "  <p:spPr/>\n"
            "</p:sp>" % (nsdecls("a", "p"), "%d", "%s")
        )

    @staticmethod
    def _textbox_sp_tmpl():
        return (
            "<p:sp %s>\n"
            "  <p:nvSpPr>\n"
            '    <p:cNvPr id="%s" name="%s"/>\n'
            '    <p:cNvSpPr txBox="1"/>\n'
            "    <p:nvPr/>\n"
            "  </p:nvSpPr>\n"
            "  <p:spPr>\n"
            "    <a:xfrm>\n"
            '      <a:off x="%s" y="%s"/>\n'
            '      <a:ext cx="%s" cy="%s"/>\n'
            "    </a:xfrm>\n"
            '    <a:prstGeom prst="rect">\n'
            "      <a:avLst/>\n"
            "    </a:prstGeom>\n"
            "    <a:noFill/>\n"
            "  </p:spPr>\n"
            "  <p:txBody>\n"
            '    <a:bodyPr wrap="none">\n'
            "      <a:spAutoFit/>\n"
            "    </a:bodyPr>\n"
            "    <a:lstStyle/>\n"
            "    <a:p/>\n"
            "  </p:txBody>\n"
            "</p:sp>" % (nsdecls("a", "p"), "%d", "%s", "%d", "%d", "%d", "%d")
        )


class CT_ShapeNonVisual(BaseShapeElement):
    """
    ``<p:nvSpPr>`` custom element class
    """

    cNvPr = OneAndOnlyOne("p:cNvPr")
    cNvSpPr = OneAndOnlyOne("p:cNvSpPr")
    nvPr = OneAndOnlyOne("p:nvPr")
