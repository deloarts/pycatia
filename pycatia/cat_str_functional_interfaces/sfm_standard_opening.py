#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.cat_str_functional_interfaces.sfm_standard_contour_parameters import SFMStandardContourParameters
from pycatia.cat_str_functional_interfaces.sfm_standard_pos_strategy_parameters import SFMStandardPosStrategyParameters
from pycatia.system_interfaces.any_object import AnyObject


class SFMStandardOpening(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfmStandardOpening
                | 
                | Defines Edition Techniques for Standard Openings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.sfm_standard_opening = com_object

    def get_contour(self, o_contour_name: str, o_list_contour_params: SFMStandardContourParameters) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetContour(CATBSTR oContourName,
                | SfmStandardContourParameters oListContourParams)
                | 
                |     Gets Contour Information for Standard Opening.
                | 
                |     Parameters:
                | 
                |         oContourName
                |             [out] The name of the Standard Opening contour for this opening.
                |             
                |         oListContourParams
                |             [out] A list of volatile objects (accessed through CATIAParameter)
                |             specifying Cke parameters controlling the size of this contour. The Cke
                |             parameters are retrieved using the CATIAParameter interface. These Cke
                |             parameters are normally persistent parameter objects in the model (if they have
                |             been stored), but in some cases, these may be volatile parameters. The
                |             parameters are locked if they cannot be modified. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example retrieves the contour information for standard
                |             opening.
                | 
                |              Dim StrContourName As String
                |              Dim StrContourParams As
                |              SfmStandardContourParameters
                |              StdOpening.GetContour StrContourName,
                |              StrContourParams

        :param str o_contour_name:
        :param SFMStandardContourParameters o_list_contour_params:
        :return: None
        :rtype: None
        """
        return self.sfm_standard_opening.GetContour(o_contour_name, o_list_contour_params.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_contour'
        # # vba_code = """
        # # Public Function get_contour(sfm_standard_opening)
        # #     Dim oContourName (2)
        # #     sfm_standard_opening.GetContour oContourName
        # #     get_contour = oContourName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_positioning_strategy(
            self,
            o_pos_strategy_name: str,
            o_list_pos_params: SFMStandardPosStrategyParameters
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPositioningStrategy(CATBSTR oPosStrategyName,
                | SfmStandardPosStrategyParameters oListPosParams)
                | 
                |     Gets the list of Position Strategy Parameters.
                | 
                |     Parameters:
                | 
                |         oPosStrategyName
                |             [out] The name of the Standard Opening Position Strategy for this
                |             opening. 
                |         oListPosParams
                |             [out] A list of the parameter group objects defining the
                |             Positioning Specification. The number and types of objects in this list depend
                |             on the Positioning Strategy name. 
                | 
                |     See also:
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example retrieves the Position Strategy information for
                |             existing standard opening.
                | 
                |              Dim StrPosStrategyName As String
                |              Dim StrPosStrategyParams As
                |              SfmStandardPosStrategyParameters
                |              StdOpening1.GetPositioningStrategy StrPosStrategyName,
                |              StrPosStrategyParams

        :param str o_pos_strategy_name:
        :param SFMStandardPosStrategyParameters o_list_pos_params:
        :return: None
        :rtype: None
        """
        return self.sfm_standard_opening.GetPositioningStrategy(o_pos_strategy_name, o_list_pos_params.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_positioning_strategy'
        # # vba_code = """
        # # Public Function get_positioning_strategy(sfm_standard_opening)
        # #     Dim oPosStrategyName (2)
        # #     sfm_standard_opening.GetPositioningStrategy oPosStrategyName
        # #     get_positioning_strategy = oPosStrategyName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_contour(self, i_contour_name: str, i_list_contour_params: SFMStandardContourParameters) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetContour(CATBSTR iContourName,
                | SfmStandardContourParameters iListContourParams)
                | 
                |     Sets Contour Information for Standard Opening.
                | 
                |     Parameters:
                | 
                |         iContourName
                |             [in] The name of the Standard Opening contour for this opening.
                |             
                |         iListContourParams
                |             [in] A list of volatile objects (accessed through CATIAParameter)
                |             specifying Cke parameters controlling the size of this contour. The Cke
                |             parameters are retrieved using the CATIAParameter interface. These Cke
                |             parameters are normally persistent parameter objects in the model (if they have
                |             been stored), but in some cases, these may be volatile parameters. The
                |             parameters are locked if they cannot be modified. 
                | 
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example changes the parameter values for existing opening
                |             created using "Sfm_rect" contour.
                | 
                |              ' First Get the Conotur.
                |              Dim StrContourName As String
                |              Dim StrContourParams As
                |              SfmStandardContourParameters
                |              StdOpening.GetContour StrContourName StrContourParams
                |              
                |              ' Get The count
                |              Dim NbofParams As Long
                |              NbofParams = StrContourParams .Count
                |              ' Modify the values inside the for loop
                |              Dim ParamName As String
                |              Dim ParamValue As Parameter
                |              For i = 1 To NbofParams 
                |               Set ParamValue = StrContourParams .Item(i)
                |               ParamName = ParamValue.Name
                |               If ParamName = "Sfm_Width" Then
                |                 ParamValue .ValuateFromString ("1000mm")
                |                 End If
                |               If ParamName = "Sfm_Height" Then
                |                 ParamValue .ValuateFromString ("1000mm")
                |                  End If
                |               If ParamName = "Sfm_CornerRadius" Then
                |                 ParamValue .ValuateFromString ("25mm")
                |                  End If
                |              Next
                |              ' Set the contour with new values
                |              StdOpening.SetContour StrContourName , StrContourParams

        :param str i_contour_name:
        :param SFMStandardContourParameters i_list_contour_params:
        :return: None
        :rtype: None
        """
        return self.sfm_standard_opening.SetContour(i_contour_name, i_list_contour_params.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_contour'
        # # vba_code = """
        # # Public Function set_contour(sfm_standard_opening)
        # #     Dim iContourName (2)
        # #     sfm_standard_opening.SetContour iContourName
        # #     set_contour = iContourName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_positioning_strategy(
            self,
            i_pos_strategy_name: str,
            i_list_pos_params: SFMStandardPosStrategyParameters
    ) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPositioningStrategy(CATBSTR iPosStrategyName,
                | SfmStandardPosStrategyParameters iListPosParams)
                | 
                |     Sets the Position Strategy and Positin Strategy
                |     Parameters.
                | 
                |     Parameters:
                | 
                |         iPosStrategyName
                |             [in] The name of the Standard Opening Position Strategy for this
                |             opening. 
                |         iListPosParams
                |             [in] A list of the parameter group objects defining the Positioning
                |             Specification. The number and types of objects in this list depend on the
                |             Positioning Strategy name. 
                | 
                |     See also:
                |     Returns:
                |         S_OK if everything ran ok
                | 
                |         Example:
                |             This Example modifies the Position Strategy Parameters for existing
                |             standard opening created using
                |             CATSfmPosOffsetOffset.
                | 
                |              'Prepare a New List for U References. The list will now contain
                |              one element.
                |              Dim UrefListNew As SfmReferences
                |              Dim UrefNew As Reference
                |              Set UrefNew = Part1.FindObjectByName("CROSS.95")
                |              UrefListNew.Add UrefNew
                |              'Prepare a New List for VReferences. The list will now contain one
                |              element.
                |              Dim VrefListNew As SfmReferences
                |              Dim VrefNew As Reference
                |              Set VrefNew = Part1.FindObjectByName("LONG.0")
                |              VrefListNew.Add VrefNew
                |              'Get Position Strategy Name and Parameters
                |              Dim StrPosStrategyName As String
                |              Dim StrPosStrategyParams As
                |              SfmStandardPosStrategyParameters
                |              StdOpening1.GetPositioningStrategy StrPosStrategyName,
                |              StrPosStrategyParams
                |              'SetPosParamData on retrieved StrPosStrategyParams. Enter new
                |              values for offset, rotation angle & reference
                |              list
                |              StrPosStrategyParams.SetPosParamData "CATSfmPosOffsetOffset", 40,
                |              UrefListNew, 25, UrefListNew, 30
                |              StdOpening1.SetPositioningStrategy StrPosStrategyName,
                |              StrPosStrategyParams
                |              Part1.Update

        :param str i_pos_strategy_name:
        :param SFMStandardPosStrategyParameters i_list_pos_params:
        :return: None
        :rtype: None
        """
        return self.sfm_standard_opening.SetPositioningStrategy(i_pos_strategy_name, i_list_pos_params.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_positioning_strategy'
        # # vba_code = """
        # # Public Function set_positioning_strategy(sfm_standard_opening)
        # #     Dim iPosStrategyName (2)
        # #     sfm_standard_opening.SetPositioningStrategy iPosStrategyName
        # #     set_positioning_strategy = iPosStrategyName
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SFMStandardOpening(name="{self.name}")'
