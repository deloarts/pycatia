#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_sch_platform_interfaces.sch_grr_route import SchGRRRoute
from pycatia.system_interfaces.any_object import AnyObject


class SchArrowDisplay(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SchArrowDisplay
                | 
                | Manage the graphical representation of a schematic route.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sch_arrow_display = com_object

    def is_arrow_shown(self, o_b_yes: bool) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub IsArrowShown(boolean oBYes)
                | 
                |     Query whether flow arrows are shown (arrow attributes
                |     exist).
                | 
                |     Parameters:
                | 
                |         oBYes
                |             If TRUE, then Flow arrows are shown (arrow attributes exist). If
                |             FALSE, then Flow arrows are not shown (arrow attributes do not exist).
                |
                |     Example:
                |
                |          Dim objThisIntf As SchArrowDisplay
                |          Dim bVar1 As boolean
                |           ...
                |          objThisIntf.IsArrowShownbVar1

        :param bool o_b_yes:
        :return: None
        :rtype: None
        """
        return self.sch_arrow_display.IsArrowShown(o_b_yes)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'is_arrow_shown'
        # # vba_code = """
        # # Public Function is_arrow_shown(sch_arrow_display)
        # #     Dim oBYes (2)
        # #     sch_arrow_display.IsArrowShown oBYes
        # #     is_arrow_shown = oBYes
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_arrow(self, i_grr: SchGRRRoute, i_seg_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetArrow(SchGRRRoute iGRR,
                | long iSegNum)
                | 
                |     Add arrow display attributes on the route.
                | 
                |     Parameters:
                | 
                |         iGRR
                |             iGRR means apply only to segments of iGRR.
                |             (if iGRR = NULL, apply to segments of all GRR's of the route, and ignore iSegNum)
                |         iSegNum
                |             iSegNum = 0 means apply to all segments of iGRR.
                |             iSegnum > 0 means apply to only to segment number iSegNum iGRR.
                | 
                |     Example:
                | 
                |          Dim objThisIntf As SchArrowDisplay
                |          Dim objArg1 As SchGRRRoute
                |          Dim intVar2 As Integer
                |           ...
                |          objThisIntf.SetArrowobjArg1,intVar2

        :param SchGRRRoute i_grr:
        :param int i_seg_num:
        :return: None
        :rtype: None
        """
        return self.sch_arrow_display.SetArrow(i_grr.com_object, i_seg_num)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_arrow'
        # # vba_code = """
        # # Public Function set_arrow(sch_arrow_display)
        # #     Dim iGRR (2)
        # #     sch_arrow_display.SetArrow iGRR
        # #     set_arrow = iGRR
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def unset_arrow(self, i_grr: SchGRRRoute, i_seg_num: int) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub UnsetArrow(SchGRRRoute iGRR,
                | long iSegNum)
                | 
                |     Remove arrow display attributes on the route.
                | 
                |     Parameters:
                | 
                |         iGRR
                |             iGRR means apply only to segments of iGRR. (if iGRR = NULL, apply to segments of all GRR's of the route, and ignore iSegNum) 
                |         iSegNum
                |             iSegNum = 0 means apply to all segments of iGRR. iSegnum > 0 means apply to only to segment number iSegNum iGRR. 
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim objThisIntf As SchArrowDisplay
                |          Dim objArg1 As SchGRRRoute
                |          Dim intVar2 As Integer
                |           ...
                |          objThisIntf.UnsetArrowobjArg1,intVar2

        :param SchGRRRoute i_grr:
        :param int i_seg_num:
        :return: None
        :rtype: None
        """
        return self.sch_arrow_display.UnsetArrow(i_grr.com_object, i_seg_num)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'unset_arrow'
        # # vba_code = """
        # # Public Function unset_arrow(sch_arrow_display)
        # #     Dim iGRR (2)
        # #     sch_arrow_display.UnsetArrow iGRR
        # #     unset_arrow = iGRR
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SchArrowDisplay(name="{self.name}")'
