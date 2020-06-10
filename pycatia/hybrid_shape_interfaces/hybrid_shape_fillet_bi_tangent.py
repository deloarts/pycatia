#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-09 09:53:18.676780

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.hybrid_shape_interfaces.hybrid_shape_integrated_law import HybridShapeIntegratedLaw
from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeFilletBiTangent(HybridShape):

    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeFilletBiTangent
                | 
                | Fillet Bi-Tangent feature.
                | Role: Manipulation of Fillet Bi-Tangent feature Allows to access data of the
                | Fillet Bi-Tangent feature created by using two support surfaces, their
                | orientation, a radius, and options (supports trimming and fillet extremities
                | type)
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_fillet_bi_tangent = com_object

    @property
    def conical_section_parameter(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property ConicalSectionParameter() As double
                | 
                |     Returns or Sets parameter for conical section.

        :return: float
        """

        return self.hybrid_shape_fillet_bi_tangent.ConicalSectionParameter

    @conical_section_parameter.setter
    def conical_section_parameter(self, value):
        """
        :param float value:
        """

        self.hybrid_shape_fillet_bi_tangent.ConicalSectionParameter = value

    @property
    def first_elem(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property FirstElem() As Reference
                | 
                |     Returns or Sets the first support surface feature.

        :return: Reference
        """

        return Reference(self.hybrid_shape_fillet_bi_tangent.FirstElem)

    @first_elem.setter
    def first_elem(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_fillet_bi_tangent.FirstElem = value

    @property
    def first_law_relimiter(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property FirstLawRelimiter() As Reference
                | 
                |     Gets or sets Law first relimiter for variable shape fillet with law
                |     management.
                |     Relimiters must be point on spine.
                |     The input law will be mapped between first and second relimiters. This
                |     example retrieves in HybLaw the first law relimiter for the Fillet hybrid shape
                |     feature.
                | 
                |      Dim HybLaw As Reference
                |      HybLaw = Fillet.FirstLawRelimiter

        :return: Reference
        """

        return Reference(self.hybrid_shape_fillet_bi_tangent.FirstLawRelimiter)

    @first_law_relimiter.setter
    def first_law_relimiter(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_fillet_bi_tangent.FirstLawRelimiter = value

    @property
    def first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property FirstOrientation() As long
                | 
                |     Returns or Setsthe first orientation used to specify fillet center
                |     position.
                |     Orientation is same or inverse than the normal to the first surface support

        :return: int
        """

        return self.hybrid_shape_fillet_bi_tangent.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_bi_tangent.FirstOrientation = value

    @property
    def hold_curve(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property HoldCurve() As Reference
                | 
                |     Returns or Sets the Hold Curve feature.

        :return: Reference
        """

        return Reference(self.hybrid_shape_fillet_bi_tangent.HoldCurve)

    @hold_curve.setter
    def hold_curve(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_fillet_bi_tangent.HoldCurve = value

    @property
    def integrated_law(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property IntegratedLaw() As HybridShapeIntegratedLaw
                | 
                |     Gets or sets Integrated Law to manage Variable Shape Fillet with
                |     law.
                | 
                |     Parameters:
                | 
                |         oILaw
                |             Integrated law This example retrieves in HybridIntegratedLaw the
                |             IntegratedLaw for the Fillet hybrid shape feature.
                | 
                |              Dim HybridIntegratedLaw
                |              Set HybridIntegratedLaw = Fillet.IntegratedLaw

        :return: HybridShapeIntegratedLaw
        """

        return HybridShapeIntegratedLaw(self.hybrid_shape_fillet_bi_tangent.IntegratedLaw)

    @integrated_law.setter
    def integrated_law(self, value):
        """
        :param HybridShapeIntegratedLaw value:
        """

        self.hybrid_shape_fillet_bi_tangent.IntegratedLaw = value

    @property
    def radius(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Radius() As Length (Read Only)
                | 
                |     Returns fillet radius in a CATIALength.

        :return: Length
        """

        return Length(self.hybrid_shape_fillet_bi_tangent.Radius)

    @property
    def radius_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RadiusType() As long
                | 
                |     Returns or Sets fillet radius type.
                |     Fillet radius type :
                |     - CATGSMRadiusDefault (0)
                |     - CATGSMRadiusChordLength(1)

        :return: int
        """

        return self.hybrid_shape_fillet_bi_tangent.RadiusType

    @radius_type.setter
    def radius_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_bi_tangent.RadiusType = value

    @property
    def radius_value(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RadiusValue() As double
                | 
                |     Returns or Sets fillet radius value.

        :return: float
        """

        return self.hybrid_shape_fillet_bi_tangent.RadiusValue

    @radius_value.setter
    def radius_value(self, value):
        """
        :param float value:
        """

        self.hybrid_shape_fillet_bi_tangent.RadiusValue = value

    @property
    def ribbon_relimitation_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property RibbonRelimitationMode() As long
                | 
                |     Returns or Sets fillet ribbon relimitation mode (or fillet extremities
                |     mode).
                |     Fillet extremities mode :
                |     - CATGSMSmooth (0)
                |     - CATGSMStraight(1)
                |     - CATGSMMaximum (2)
                |     - CATGSMMinimum (3)

        :return: int
        """

        return self.hybrid_shape_fillet_bi_tangent.RibbonRelimitationMode

    @ribbon_relimitation_mode.setter
    def ribbon_relimitation_mode(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_bi_tangent.RibbonRelimitationMode = value

    @property
    def second_elem(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SecondElem() As Reference
                | 
                |     Returns or sets the Second support surface feature.

        :return: Reference
        """

        return Reference(self.hybrid_shape_fillet_bi_tangent.SecondElem)

    @second_elem.setter
    def second_elem(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_fillet_bi_tangent.SecondElem = value

    @property
    def second_law_relimiter(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SecondLawRelimiter() As Reference
                | 
                |     Gets or sets Law second relimiter for variable shape fillet with law
                |     management.
                |     Relimiters must be point on spine.
                |     The input law will be mapped between first and second relimiters. This
                |     example retrieves in HybLaw the second law relimiter for the Fillet hybrid
                |     shape feature.
                | 
                |      Dim HybLaw As Reference
                |      HybLaw = Fillet.SecondLawRelimiter

        :return: Reference
        """

        return Reference(self.hybrid_shape_fillet_bi_tangent.SecondLawRelimiter)

    @second_law_relimiter.setter
    def second_law_relimiter(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_fillet_bi_tangent.SecondLawRelimiter = value

    @property
    def second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SecondOrientation() As long
                | 
                |     Returns or Sets the Second orientation used to specify fillet center
                |     position.
                |     Orientation is same or inverse than the normal to the Second surface
                |     support

        :return: int
        """

        return self.hybrid_shape_fillet_bi_tangent.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_bi_tangent.SecondOrientation = value

    @property
    def section_type(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SectionType() As long
                | 
                |     Returns or Sets fillet section type.
                |     Fillet radius type :
                |     - CATGSMCircularSection(0)
                |     - CATGSMConicalSection (1)

        :return: int
        """

        return self.hybrid_shape_fillet_bi_tangent.SectionType

    @section_type.setter
    def section_type(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_bi_tangent.SectionType = value

    @property
    def spine(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property Spine() As Reference
                | 
                |     Returns or Sets the spine feature.

        :return: Reference
        """

        return Reference(self.hybrid_shape_fillet_bi_tangent.Spine)

    @spine.setter
    def spine(self, value):
        """
        :param Reference value:
        """

        self.hybrid_shape_fillet_bi_tangent.Spine = value

    @property
    def supports_trim_mode(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780)
                | o Property SupportsTrimMode() As long
                | 
                |     Returns or Sets whether support surfaces are trimmed or not. Possible values of SupportsTrimMode = 0 : No trim of fillet supports. = 1 : Trim of both fillet supports. = 2 : Trim of fillet support 1. = 3 : Trim of fillet support 2.

        :return: int
        """

        return self.hybrid_shape_fillet_bi_tangent.SupportsTrimMode

    @supports_trim_mode.setter
    def supports_trim_mode(self, value):
        """
        :param int value:
        """

        self.hybrid_shape_fillet_bi_tangent.SupportsTrimMode = value

    def append_new_face_to_keep(self, i_face=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub AppendNewFaceToKeep(Reference iFace)
                | 
                |     Append a new face to keep.
                | 
                |     Parameters:
                | 
                |         iFace

        :param Reference i_face:
        :return: None
        """
        return self.hybrid_shape_fillet_bi_tangent.AppendNewFaceToKeep(i_face)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'append_new_face_to_keep'
        # # vba_code = """
        # # Public Function append_new_face_to_keep(hybrid_shape_fillet_bi_tangent)
        # #     Dim iFace (2)
        # #     hybrid_shape_fillet_bi_tangent.AppendNewFaceToKeep iFace
        # #     append_new_face_to_keep = iFace
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_face_to_keep(self, i_pos=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Func GetFaceToKeep(long iPos) As Reference
                | 
                |     Gets the face to keep for fillet operation.
                | 
                |     Parameters:
                | 
                |         oFace
                |             The face to keep for fillet operation. 
                |         iPos
                |             Position of the face to be retrieved.

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.hybrid_shape_fillet_bi_tangent.GetFaceToKeep(i_pos))

    def invert_first_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub InvertFirstOrientation()
                | 
                |     Inverts first orientation used to specify fillet center position.

        :return: None
        """
        return self.hybrid_shape_fillet_bi_tangent.InvertFirstOrientation()

    def invert_second_orientation(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub InvertSecondOrientation()
                | 
                |     Inverts second orientation used to specify fillet center position.

        :return: None
        """
        return self.hybrid_shape_fillet_bi_tangent.InvertSecondOrientation()

    def remove_all_faces_to_keep(self):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveAllFacesToKeep()
                | 
                |     Remove all the faces to keep.

        :return: None
        """
        return self.hybrid_shape_fillet_bi_tangent.RemoveAllFacesToKeep()

    def remove_face_to_keep(self, i_face=None):
        """
        .. note::
            CAA V5 Visual Basic Help (2020-06-09 09:53:18.676780))
                | o Sub RemoveFaceToKeep(Reference iFace)
                | 
                |     Remove a face to keep.
                | 
                |     Parameters:
                | 
                |         iFace

        :param Reference i_face:
        :return: None
        """
        return self.hybrid_shape_fillet_bi_tangent.RemoveFaceToKeep(i_face)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_face_to_keep'
        # # vba_code = """
        # # Public Function remove_face_to_keep(hybrid_shape_fillet_bi_tangent)
        # #     Dim iFace (2)
        # #     hybrid_shape_fillet_bi_tangent.RemoveFaceToKeep iFace
        # #     remove_face_to_keep = iFace
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'HybridShapeFilletBiTangent(name="{ self.name }")'