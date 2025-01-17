#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-07-06 14:02:20.222384

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.in_interfaces.reference import Reference
from pycatia.knowledge_interfaces.length import Length
from pycatia.mec_mod_interfaces.hybrid_shape import HybridShape


class HybridShapeOffset(HybridShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.HybridShape
                |                         HybridShapeOffset
                | 
                | Represents the hybrid shape offset feature object.
                | Role: To access the data of the hybrid shape offset feature object. This data
                | includes:
                | 
                |     The element to offset
                |     The offset direction
                |     The offset value
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeOffset
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.hybrid_shape_offset = com_object

    @property
    def offset_direction(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OffsetDirection() As boolean
                | 
                |     Returns or sets whether the offset direction is to be
                |     inverted.
                |     True to invert the offset direction.

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_offset.OffsetDirection

    @offset_direction.setter
    def offset_direction(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_offset.OffsetDirection = value

    @property
    def offset_value(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OffsetValue() As Length
                | 
                |     Returns or sets the offset value.

        :return: Length
        :rtype: Length
        """

        return Length(self.hybrid_shape_offset.OffsetValue)

    @offset_value.setter
    def offset_value(self, length: Length):
        """
        :param Length length:
        """

        self.hybrid_shape_offset.OffsetValue = length.com_object

    @property
    def offseted_object(self) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property OffsetedObject() As Reference
                | 
                |     Returns or sets the face to offset.
                |     Sub-element(s) supported (see Boundary object): Face.

        :return: Reference
        :rtype: Reference
        """

        return Reference(self.hybrid_shape_offset.OffsetedObject)

    @offseted_object.setter
    def offseted_object(self, reference_object: Reference):
        """
        :param Reference reference_object:
        """

        self.hybrid_shape_offset.OffsetedObject = reference_object.com_object

    @property
    def suppress_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property SuppressMode() As boolean
                | 
                |     Returns or sets suppress mode.
                |     True to activate suppress mode

        :return: bool
        :rtype: bool
        """

        return self.hybrid_shape_offset.SuppressMode

    @suppress_mode.setter
    def suppress_mode(self, value: bool):
        """
        :param bool value:
        """

        self.hybrid_shape_offset.SuppressMode = value

    def add_tricky_face(self, i_tricky_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddTrickyFace(Reference iTrickyFace)
                | 
                |     Adds a tricky face object on the object.

        :param Reference i_tricky_face:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_offset.AddTrickyFace(i_tricky_face.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_tricky_face'
        # # vba_code = """
        # # Public Function add_tricky_face(hybrid_shape_offset)
        # #     Dim iTrickyFace (2)
        # #     hybrid_shape_offset.AddTrickyFace iTrickyFace
        # #     add_tricky_face = iTrickyFace
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_tricky_face(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Func GetTrickyFace(long iRank) As Reference
                | 
                |     Returns the invalid face object on the object.
                |     param : iRank =position of faces ionvalid for offset

        :param int i_rank:
        :return: Reference
        :rtype: Reference
        """
        return Reference(self.hybrid_shape_offset.GetTrickyFace(i_rank))

    def remove_tricky_face(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveTrickyFace(long iRank)
                | 
                |     Remove the tricky face object on the object.
                |     param : iRank =position of the face in the list of TrickyFaces

        :param int i_rank:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_offset.RemoveTrickyFace(i_rank)

    def set_offset_value(self, i_offset: float) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetOffsetValue(double iOffset)
                | 
                |     Set Offset value with input as double.
                |     To be replace in further release by integration in the pragma put_xxx

        :param float i_offset:
        :return: None
        :rtype: None
        """
        return self.hybrid_shape_offset.SetOffsetValue(i_offset)

    def __repr__(self):
        return f'HybridShapeOffset(name="{self.name}")'
