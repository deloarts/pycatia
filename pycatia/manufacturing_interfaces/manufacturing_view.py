#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.knowledge_interfaces.relations import Relations
from pycatia.manufacturing_interfaces.manufacturing_features import ManufacturingFeatures
from pycatia.product_structure_interfaces.product import Product
from pycatia.system_interfaces.any_object import AnyObject


class ManufacturingView(AnyObject):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingView
                | 
                | The Manufacturing View is the object that holds all the manufacturing features
                | of the model.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.manufacturing_view = com_object

    @property
    def manufacturing_features(self) -> ManufacturingFeatures:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property ManufacturingFeatures() As ManufacturingFeatures (Read
                | Only)
                | 
                |     Returns the Manufacturing Features of a Manufacturing
                |     View.
                | 
                |     Example:
                |         The following example returns in ManufacturingFeatures the
                |         Manufacturing Features of the Manufacturing View
                |         MfgView:
                | 
                |          Set ManufacturingFeatures = MfgView.ManufacturingFeatures

        :return: ManufacturingFeatures
        :rtype: ManufacturingFeatures
        """

        return ManufacturingFeatures(self.manufacturing_view.ManufacturingFeatures)

    @property
    def relations(self) -> Relations:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)
                | o Property Relations() As Relations (Read Only)
                | 
                |     Returns the Relations Set owned by a Manufacturing View.
                | 
                |     Example:
                |         The following example returns in Relations the Relations Set of the
                |         Manufacturing View MfgView:
                | 
                |          Set Relations = MfgView.Relations

        :return: Relations
        :rtype: Relations
        """

        return Relations(self.manufacturing_view.Relations)

    def create_all_machinable_area_features_from_tech_results_of_udf(self, i_finish_part_product: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateAllMachinableAreaFeaturesFromTechResultsOfUDF(Product
                | iFinishPartProduct)
                | 
                |     Creates Machinable feature using TR of UDF.
                | 
                |     Example:
                |         The following example takes iFinishPartProduct and Create MAF in
                |         MfgView:
                | 
                |         MfgView.CreateAllMachinableAreaFeaturesFromTechResultsOfUDF(iFinishPartProduct)

        :param Product i_finish_part_product:
        :return: None
        :rtype: None
        """
        return self.manufacturing_view.CreateAllMachinableAreaFeaturesFromTechResultsOfUDF(
            i_finish_part_product.com_object
        )
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_all_machinable_area_features_from_tech_results_of_udf'
        # # vba_code = """
        # # Public Function create_all_machinable_area_features_from_tech_results_of_udf(manufacturing_view)
        # #     Dim iFinishPartProduct (2)
        # #     manufacturing_view.CreateAllMachinableAreaFeaturesFromTechResultsOfUDF iFinishPartProduct
        # #     create_all_machinable_area_features_from_tech_results_of_udf = iFinishPartProduct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'ManufacturingView(name="{self.name}")'
