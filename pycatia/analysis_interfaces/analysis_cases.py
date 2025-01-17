#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.analysis_interfaces.analysis_case import AnalysisCase
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class AnalysisCases(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AnalysisCases
                | 
                | The collection of analysis case making an Analysis.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AnalysisCase)
        self.analysis_cases = com_object

    def add(self) -> AnalysisCase:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Add() As AnalysisCase
                | 
                |     Creates a new case and adds it to the case collection. This case will be
                |     plugged under the analysis model.
                | 
                |     Returns:
                |         The created case 
                |     Example:
                |         The following example creates a case NewCase in the case collection of
                |         the ModelAnalysis Analysis model
                | 
                |         .
                | 
                |          Dim ModelAnalysis As AnalysisModel
                |          Dim NewCase As AnalysisCase
                |          Set NewCase = ModelAnalysis.AnalysisCases.Add()

        :return: AnalysisCase
        :rtype: AnalysisCase
        """
        return AnalysisCase(self.analysis_cases.Add())

    def add_existing_case(self, i_case: AnalysisCase) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddExistingCase(AnalysisCase iCase)
                | 
                |     Adds an existing analysis case to the analysis cases
                |     collection.
                | 
                |     Parameters:
                | 
                |         iCase
                |             The Existing Analysis Case. 
                |         Example:
                |             This example adds ThisAnalysisCase in the analysisCases analysis
                |             cases collection.
                | 
                |              Dim ThisAnalysisCase As AnalysisCase
                |              Dim analysisCases As AnalysisCases
                |              ...
                |              analysisCases.AddExistingCase(ThisAnalysisCase)

        :param AnalysisCase i_case:
        :return: None
        :rtype: None
        """
        return self.analysis_cases.AddExistingCase(i_case.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_existing_case'
        # # vba_code = """
        # # Public Function add_existing_case(analysis_cases)
        # #     Dim iCase (2)
        # #     analysis_cases.AddExistingCase iCase
        # #     add_existing_case = iCase
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def item(self, i_index: cat_variant) -> AnalysisCase:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Item(CATVariant iIndex) As AnalysisCase
                | 
                |     Returns a case using its index or its name from the case
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the case to retrieve from the collection
                |             of cases. As a numeric, this index is the rank of the case in the collection.
                |             The index of the first case in the collection is 1, and the index of the last
                |             case is Count. As a string, it is the name you assigned to the case using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved case. 
                |     Example:
                |         This example retrieves in ThisCase the fifth case in the collection and
                |         in ThatCase the case named "MyCase in the case collection of the AnalysisModel
                |         Analysis model.
                | 
                |          Set CaseColl = AnalysisModel.AnalysisCases
                |          Set ThisCase = CaseColl.Item(5)
                |          Set ThatCase = CaseColl.Item("MyCase")

        :param cat_variant i_index:
        :return: AnalysisCase
        :rtype: AnalysisCase
        """
        return AnalysisCase(self.analysis_cases.Item(i_index))

    def new_case(self, i_type: str) -> AnalysisCase:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func NewCase(CATBSTR iType) As AnalysisCase
                | 
                |     Creates a new case and adds it to the case collection. This case will be
                |     plugged under the analysis model.
                | 
                |     Returns:
                |         The created case 
                |     Example:
                |         The following example creates a case NewCase in the case collection of
                |         the ModelAnalysis Analysis model
                | 
                |         .
                | 
                |          Dim ModelAnalysis As AnalysisModel
                |          Dim NewCase As AnalysisCase
                |          Set NewCase = ModelAnalysis.AnalysisCases.NewCase("AnalysisPreproCase")()

        :param str i_type:
        :return: AnalysisCase
        :rtype: AnalysisCase
        """
        return AnalysisCase(self.analysis_cases.NewCase(i_type))

    def remove(self, i_index: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Remove(CATVariant iIndex)
                | 
                |     Removes a case using its index or its name from the case
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the case to retrieve from the collection
                |             of cases. As a numeric, this index is the rank of the case in the collection.
                |             The index of the first case in the collection is 1, and the index of the last
                |             case is Count. As a string, it is the name you assigned to the case using the
                |             
                | 
                |         AnyObject.Name property. 
                |     Example:
                |         This example removes the fifth case in the collection.
                | 
                |          AnalysisModel.AnalysisCases.Remove (5)

        :param cat_variant i_index:
        :return: None
        :rtype: None
        """
        return self.analysis_cases.Remove(i_index)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove'
        # # vba_code = """
        # # Public Function remove(analysis_cases)
        # #     Dim iIndex (2)
        # #     analysis_cases.Remove iIndex
        # #     remove = iIndex
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisCases(name="{self.name}")'
