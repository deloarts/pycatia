#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia.analysis_interfaces.analysis_images import AnalysisImages
from pycatia.analysis_interfaces.analysis_supports import AnalysisSupports
from pycatia.in_interfaces.reference import Reference
from pycatia.mec_mod_interfaces.constraint import Constraint
from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.publication import Publication
from pycatia.system_interfaces.any_object import AnyObject
from pycatia.types.general import cat_variant

if TYPE_CHECKING:
    from pycatia.analysis_interfaces.basic_components import BasicComponents


class AnalysisLocalEntity(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AnalysisLocalEntity
                | 
                | Represent the analysis local entity object.
                | This class provides services to describe a analysis entity. It represents some
                | local preprocessing activities.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.analysis_local_entity = com_object

    @property
    def analysis_images(self) -> AnalysisImages:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisImages() As AnalysisImages (Read Only)
                | 
                |     Returns the analysis images collection associated with an analysis
                |     entity.
                | 
                |     Returns:
                |         a collection of CATIAAnalysisImages. 
                |     Example:
                | 
                |           This example retrieves analysis images collection 
                | 
                |          
                | 
                |          Dim MyEntity As AnalysisEntity
                |          Dim myAnalysisImages As AnalysisImages
                |          Set myAnalysisImages = MyEntity.AnalysisImages

        :return: AnalysisImages
        :rtype: AnalysisImages
        """

        return AnalysisImages(self.analysis_local_entity.AnalysisImages)

    @property
    def analysis_supports(self) -> AnalysisSupports:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property AnalysisSupports() As AnalysisSupports (Read Only)
                | 
                |     Returns the list of Analysis Supports (Selection of geometrical or mesh
                |     entities) which define the area on which the analysis is applied on.

        :return: AnalysisSupports
        :rtype: AnalysisSupports
        """

        return AnalysisSupports(self.analysis_local_entity.AnalysisSupports)

    @property
    def basic_components(self) -> 'BasicComponents':
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property BasicComponents() As BasicComponents (Read Only)
                | 
                |     Returns the basic components collection associated with an analysis
                |     entity.
                | 
                |     Returns:
                |         a collection of CATIABasicComponents. 
                |     Example:
                | 
                |           This example retrieves Basic components collection 
                | 
                |          
                | 
                |          Dim MyEntity As AnalysisEntity
                |          Dim myBasicComponents As BasicComponents
                |          Set myBasicComponents = MyEntity.BasicComponents

        :return: BasicComponents
        :rtype: BasicComponents
        """
        from pycatia.analysis_interfaces.basic_components import BasicComponents
        return BasicComponents(self.analysis_local_entity.BasicComponents)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Type() As CATBSTR (Read Only)
                | 
                |     Returns the type of the analysis Entity.
                | 
                |     Returns:
                |         The string that represent the analysis entity type.

        :return: str
        :rtype: str
        """

        return self.analysis_local_entity.Type

    def add_support_from_constraint(self, i_constraint_product: Product, i_constraint: Constraint) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromConstraint(Product iConstraintProduct,
                | Constraint iConstraint)
                | 
                |     Creates a new support and add it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iConstraintProduct
                |             the CATIA Product of the Constraint.
                |         iConstraint
                |             the CATIA Constraint that represent the object to
                |             linked.
                | 
                |     See also:
                |         Reference, Part

        :param Product i_constraint_product:
        :param Constraint i_constraint:
        :return: None
        :rtype: None
        """
        return self.analysis_local_entity.AddSupportFromConstraint(
            i_constraint_product.com_object,
            i_constraint.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_constraint'
        # # vba_code = """
        # # Public Function add_support_from_constraint(analysis_local_entity)
        # #     Dim iConstraintProduct (2)
        # #     analysis_local_entity.AddSupportFromConstraint iConstraintProduct
        # #     add_support_from_constraint = iConstraintProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_from_product(self, i_product: Product, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromProduct(Product iProduct,
                | Reference iSupport)
                | 
                |     Creates a new support and add it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             the CATIA Product that represent the object to
                |             linked.
                |         iSupport
                |             the CATIA Reference that represent the object to
                |             linked.
                | 
                |     See also:
                |         Reference, Product

        :param Product i_product:
        :param Reference i_support:
        :return: None
        :rtype: None
        """
        return self.analysis_local_entity.AddSupportFromProduct(i_product.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_product'
        # # vba_code = """
        # # Public Function add_support_from_product(analysis_local_entity)
        # #     Dim iProduct (2)
        # #     analysis_local_entity.AddSupportFromProduct iProduct
        # #     add_support_from_product = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_from_publication(self, i_product: Product, i_publication: Publication) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromPublication(Product iProduct,
                | Publication iPublication)
                | 
                |     Creates a new support and add it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iProduct
                |             the CATIA Product that represent the object to
                |             linked.
                |         iPublication
                |             the CATIA Publication that represent the object to
                |             linked.
                | 
                |     See also:
                |         Publication, Product

        :param Product i_product:
        :param Publication i_publication:
        :return: None
        :rtype: None
        """
        return self.analysis_local_entity.AddSupportFromPublication(i_product.com_object, i_publication.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_publication'
        # # vba_code = """
        # # Public Function add_support_from_publication(analysis_local_entity)
        # #     Dim iProduct (2)
        # #     analysis_local_entity.AddSupportFromPublication iProduct
        # #     add_support_from_publication = iProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_support_from_reference(self, i_reference: Reference, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddSupportFromReference(Reference iReference,
                | Reference iSupport)
                | 
                |     Creates a new support and add it to the description of the Analysis
                |     Entity.
                | 
                |     Parameters:
                | 
                |         iReference
                |             the CATIA Reference that represent the object to linked. This
                |             identification, may locate the instance of the
                |             object
                |         iSupport
                |             the CATIA Reference that represent the object to
                |             linked.
                | 
                |     See also:
                |         Reference

        :param Reference i_reference:
        :param Reference i_support:
        :return: None
        :rtype: None
        """
        return self.analysis_local_entity.AddSupportFromReference(i_reference.com_object, i_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_support_from_reference'
        # # vba_code = """
        # # Public Function add_support_from_reference(analysis_local_entity)
        # #     Dim iReference (2)
        # #     analysis_local_entity.AddSupportFromReference iReference
        # #     add_support_from_reference = iReference
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_reference(
            self,
            i_component: str,
            i_label: str,
            i_line_index: int,
            i_column_index: int,
            i_layer_index: int) -> Reference:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetReference(CATBSTR iComponent,
                | CATBSTR iLabel,
                | long iLineIndex,
                | long iColumnIndex,
                | long iLayerIndex) As Reference
                | 
                |     Returns the reference corresponding to the given
                |     component.
                | 
                |     Parameters:
                | 
                |         iComponent
                |             The identifier if the basic component.
                |         iLabel
                |             The label of the block containing the value.
                |         iLineIndex
                |             The line index of the value.
                |         iColumnIndex
                |             The column index of the value.
                |         iLayerIndex
                |             The layer index of the value.

        :param str i_component:
        :param str i_label:
        :param int i_line_index:
        :param int i_column_index:
        :param int i_layer_index:
        :return: Reference
        :rtype: Reference
        """
        return Reference(
            self.analysis_local_entity.GetReference(
                i_component,
                i_label,
                i_line_index,
                i_column_index,
                i_layer_index
            )
        )

    def get_value(
            self,
            i_component: str,
            i_label: str,
            i_line_index: int,
            i_column_index: int,
            i_layer_index: int) -> cat_variant:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetValue(CATBSTR iComponent,
                | CATBSTR iLabel,
                | long iLineIndex,
                | long iColumnIndex,
                | long iLayerIndex) As CATVariant
                | 
                |     Returns the value corresponding to the given component.
                | 
                |     Parameters:
                | 
                |         iComponent
                |             The identifier if the basic component.
                |         iLabel
                |             The label of the block containing the value.
                |         iLineIndex
                |             The line index of the value.
                |         iColumnIndex
                |             The column index of the value.
                |         iLayerIndex
                |             The layer index of the value.

        :param str i_component:
        :param str i_label:
        :param int i_line_index:
        :param int i_column_index:
        :param int i_layer_index:
        :return: cat_variant
        :rtype: cat_variant
        """
        return self.analysis_local_entity.GetValue(i_component, i_label, i_line_index, i_column_index, i_layer_index)

    def set_reference(
            self,
            i_component: str,
            i_label: str,
            i_line_index: int,
            i_column_index: int,
            i_layer_index: int,
            i_value: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetReference(CATBSTR iComponent,
                | CATBSTR iLabel,
                | long iLineIndex,
                | long iColumnIndex,
                | long iLayerIndex,
                | Reference iValue)
                | 
                |     Sets the reference corresponding to the given component.
                | 
                |     Parameters:
                | 
                |         iComponent
                |             The identifier if the basic component.
                |         iLabel
                |             The label of the block containing the value.
                |         iLineIndex
                |             The line index of the value.
                |         iColumnIndex
                |             The column index of the value.
                |         iLayerIndex
                |             The layer index of the value.
                |             If the the component has a single value, assign 0 to the 3
                |             parameters.

        :param str i_component:
        :param str i_label:
        :param int i_line_index:
        :param int i_column_index:
        :param int i_layer_index:
        :param Reference i_value:
        :return: None
        :rtype: None
        """
        return self.analysis_local_entity.SetReference(
            i_component,
            i_label,
            i_line_index,
            i_column_index,
            i_layer_index,
            i_value.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_reference'
        # # vba_code = """
        # # Public Function set_reference(analysis_local_entity)
        # #     Dim iComponent (2)
        # #     analysis_local_entity.SetReference iComponent
        # #     set_reference = iComponent
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_value(
            self,
            i_component: str,
            i_label: str,
            i_line_index: int,
            i_column_index: int,
            i_layer_index: int,
            i_value: cat_variant) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetValue(CATBSTR iComponent,
                | CATBSTR iLabel,
                | long iLineIndex,
                | long iColumnIndex,
                | long iLayerIndex,
                | CATVariant iValue)
                | 
                |     Sets the value corresponding to the given component.
                | 
                |     Parameters:
                | 
                |         iComponent
                |             The identifier if the basic component.
                |         iLabel
                |             The label of the block containing the value.
                |         iLineIndex
                |             The line index of the value.
                |         iColumnIndex
                |             The column index of the value.
                |         iLayerIndex
                |             The layer index of the value.
                |             If the the component has a single value, assign 0 to the 3
                |             parameters. 
                | 
                |     Example:
                | 
                |           This example create ThisAnalysisEntity in the analysisEntities
                |           collection 
                | 
                |          The entity to create is supposed to be a pressure defined in a load
                |          set. We
                | 
                |          will valuate the basic component that contain the pressure data
                |          "SAMPressureMag".
                |          
                | 
                |          Dim analysisEntities As CATIAAnalysisEntities
                |          Dim ThisAnalysisEntity As AnalysisEntity
                |          Set ThisAnalysisEntity = analysisEntities.Add("SAMPressure")
                |          ThisAnalysisEntity.SetValue("SAMPressureMag","
                |          ",0,0,0,100)

        :param str i_component:
        :param str i_label:
        :param int i_line_index:
        :param int i_column_index:
        :param int i_layer_index:
        :param cat_variant i_value:
        :return: None
        :rtype: None
        """
        return self.analysis_local_entity.SetValue(
            i_component,
            i_label,
            i_line_index,
            i_column_index,
            i_layer_index,
            i_value)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_value'
        # # vba_code = """
        # # Public Function set_value(analysis_local_entity)
        # #     Dim iComponent (2)
        # #     analysis_local_entity.SetValue iComponent
        # #     set_value = iComponent
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'AnalysisLocalEntity(name="{self.name}")'
