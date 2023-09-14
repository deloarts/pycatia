#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.funct_system_interfaces.funct_script import FunctScript
from pycatia.system_interfaces.collection import Collection
from pycatia.types.general import cat_variant


class FunctScripts(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     FunctScripts
                | 
                | The interface to access a set of Functional Scripts.
                | 
                | It is managed on a Functional Element, thru the GenerativeKnowledge Facet
                | Manager (GKW).
    
    """

    def __init__(self, com_object, child_object=FunctScript):
        super().__init__(com_object, child_object=FunctScript)
        self.funct_scripts = com_object
        self.child_object = child_object

    def create(self, i_name: str) -> FunctScript:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Create(CATBSTR iName) As FunctScript
                | 
                |     Create a FunctScript.

        :param str i_name:
        :return: FunctScript
        :rtype: FunctScript
        """
        return FunctScript(self.funct_scripts.Create(i_name))

    def delete(self, i_script: FunctScript) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub Delete(FunctScript iScript)
                | 
                |     Delete a FunctScript.

        :param FunctScript i_script:
        :return: None
        :rtype: None
        """
        return self.funct_scripts.Delete(i_script.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'delete'
        # # vba_code = """
        # # Public Function delete(funct_scripts)
        # #     Dim iScript (2)
        # #     funct_scripts.Delete iScript
        # #     delete = iScript
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def elem(self, i_index: cat_variant) -> FunctScript:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func Elem(CATVariant iIndex) As FunctScript
                | 
                |     Returns an association using its index or its name from the Scripts
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Script to retrieve from the collection
                |             of Scripts. As a numerics, this index is the rank of the Script in the
                |             collection. The index of the first Script in the collection is 1, and the index
                |             of the last Script is Count. As a string, it is the name you assigned to the
                |             Script using the 
                | 
                |         AnyObject.Name property. 
                |     Returns:
                |         The retrieved Script 
                |     Example:
                |         This example retrieves in Act1 the fifth Script in the collection and
                |         in Act2 the Script named Moves.
                | 
                |          Dim FunctElem As FunctionalObject
                |          Set FunctElem = FunctDoc.CurrentDescription.Objects.Elem("Valve")
                |          Dim FacetGKW As FunctionalGenScriptMgr
                |          Set FacetGKW = FunctElem.GetFacetByName("GKW")
                |          Dim Assoc1 As FunctScript
                |          Set Assoc1 = FacetGKW.Scripts.Elem(5)
                |          Dim Assoc2 As FunctScript
                |          Set Assoc2 = FacetGKW.Scripts.Elem("Producing the Skeleton 2D")

        :param cat_variant i_index:
        :return: FunctScript
        :rtype: FunctScript
        """
        return FunctScript(self.funct_scripts.Elem(i_index))

    def __repr__(self):
        return f'FunctScripts(name="{self.name}")'
