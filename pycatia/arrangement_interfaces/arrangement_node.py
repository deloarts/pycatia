#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.move import Move
from pycatia.system_interfaces.any_object import AnyObject


class ArrangementNode(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArrangementNode
                | 
                | This interface provides access to a CATIAArrangementNode
                | object.
                | Use this object to fetch the properties of an ArrangementNode object. Role: Use
                | this object to retrieve the bend angle, bend radius and location of an
                | ArrangementNode object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.arrangement_node = com_object

    @property
    def bend_angle(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BendAngle() As double (Read Only)
                | 
                |     Returns the BendAngle of the current ArrangementNode.
                | 
                |     Example:
                |         This example retrieves the BendAngle of the objNode1
                |         object.
                | 
                |          Dim dblBendAngle   As Double
                |          dblBendBendAngle  = objNode1.BendAngle

        :return: float
        :rtype: float
        """

        return self.arrangement_node.BendAngle

    @property
    def bend_radius(self) -> float:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BendRadius() As double
                | 
                |     Returns or sets the BendRadius of the current
                |     ArrangementNode.
                | 
                |     Example:
                |         This example retrieves the BendRadius of the objNode1
                |         object.
                | 
                |          Dim dblBendRadius   As Double
                |          dblBendRadius  = objNode1.BendRadius

        :return: float
        :rtype: float
        """

        return self.arrangement_node.BendRadius

    @bend_radius.setter
    def bend_radius(self, value: float):
        """
        :param float value:
        """

        self.arrangement_node.BendRadius = value

    def get_point(self, i_rel_axis: Move, io_node_location: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPoint(Move iRelAxis,
                | CATSafeArrayVariant ioNodeLocation)
                | 
                |     Returns the location of the current ArrangementNode.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             The relative axis to be considered when calculating the coordinate.
                |             
                |         ioNodeLocation
                |             The location of the ArrangementNode.
                | 
                |             Example:
                |                 This example retrieves the location of the ArrangementNode
                |                 object objNode1.
                | 
                |                  Dim dblCoords(3)   As Double
                |                  Dim iRelAxis       As Move
                |                  'Fetch iRelAxis from the object containing the
                |                  node
                |                  ...
                |                  objNode1.GetPoint(iRelAxis, dblCoords)

        :param Move i_rel_axis:
        :param tuple io_node_location:
        :return: None
        :rtype: None
        """
        return self.arrangement_node.GetPoint(i_rel_axis.com_object, io_node_location)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_point'
        # # vba_code = """
        # # Public Function get_point(arrangement_node)
        # #     Dim iRelAxis (2)
        # #     arrangement_node.GetPoint iRelAxis
        # #     get_point = iRelAxis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_point(self, i_rel_axis: Move, i_node_location: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPoint(Move iRelAxis,
                | CATSafeArrayVariant iNodeLocation)
                | 
                |     Sets the location of the current ArrangementNode.
                | 
                |     Parameters:
                | 
                |         iRelAxis
                |             The relative axis to be considered when calculating the coordinate.
                |             
                |         ioNodeLocation
                |             The location of the ArrangementNode.
                | 
                |             Example:
                |                 This example sets the location of the ArrangementNode object
                |                 objNode1.
                | 
                |                  Dim dblCoords(3)   As Double
                |                  Dim iRelAxis       As Move
                |                  'Fetch iRelAxis from the object containing the
                |                  node
                |                  ...
                |                  dblCoords(0)       = 300.0 '//X
                |                  dblCoords(1)       = 500.0 '//Y
                |                  dblCoords(2)       = 300.0 '//Z
                |                  objNode1.SetPoint(iRelAxis, dblCoords)

        :param Move i_rel_axis:
        :param tuple i_node_location:
        :return: None
        :rtype: None
        """
        return self.arrangement_node.SetPoint(i_rel_axis.com_object, i_node_location)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_point'
        # # vba_code = """
        # # Public Function set_point(arrangement_node)
        # #     Dim iRelAxis (2)
        # #     arrangement_node.SetPoint iRelAxis
        # #     set_point = iRelAxis
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ArrangementNode(name="{self.name}")'
