#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dmaps_interfaces.activity import Activity
from pycatia.dnb_dpm_interfaces.mfg_assembly import MfgAssembly
from pycatia.dnb_human_sim_interfaces.worker_activity import WorkerActivity
from pycatia.product_structure_interfaces.product import Product


class PlaceActivity(WorkerActivity):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DMAPSInterfaces.Activity
                |                         DNBHumanSimInterfaces.WorkerActivity
                |                             PlaceActivity
                | 
                | The object that represents an PlaceActivity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.place_activity = com_object

    def add_placed_mfg_assembly(self, p_picked_item: MfgAssembly, vb_sav: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPlacedMfgAssembly(MfgAssembly pPickedItem,
                | CATSafeArrayVariant vbSAV)
                | 
                |     Adds a Manufacturing Assembly to the List of placed Items

        :param MfgAssembly p_picked_item:
        :param tuple vb_sav:
        :return: None
        :rtype: None
        """
        return self.place_activity.AddPlacedMfgAssembly(p_picked_item.com_object, vb_sav)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_placed_mfg_assembly'
        # # vba_code = """
        # # Public Function add_placed_mfg_assembly(place_activity)
        # #     Dim pPickedItem (2)
        # #     place_activity.AddPlacedMfgAssembly pPickedItem
        # #     add_placed_mfg_assembly = pPickedItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_placed_product(self, p_picked_item: Product, vb_sav: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub AddPlacedProduct(Product pPickedItem,
                | CATSafeArrayVariant vbSAV)
                | 
                |     Adds a product to the List of placed Items

        :param Product p_picked_item:
        :param tuple vb_sav:
        :return: None
        :rtype: None
        """
        return self.place_activity.AddPlacedProduct(p_picked_item.com_object, vb_sav)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_placed_product'
        # # vba_code = """
        # # Public Function add_placed_product(place_activity)
        # #     Dim pPickedItem (2)
        # #     place_activity.AddPlacedProduct pPickedItem
        # #     add_placed_product = pPickedItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_offset(self, o_offset_trans_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOffset(CATSafeArrayVariant oOffsetTransList)
                | 
                |     This method gets the relative offset List for placing the
                |     product
                | 
                |     Parameters:
                | 
                |         oOffsetTrans
                |             list of Offsets between EndEff and Product at time of placing first
                |             12 values represent 1st offset, next 12, 2nd offset and so on.. The offset
                |             matrix is interpreted as follows: The first 9 entries correspond to the
                |             rotation matrix and the next 3 entries correspond to the position vector The
                |             first 9 entries are interpreted row wise for the matrix shown
                |             below
                |             R1x R1y R1z
                |             R2x R2y R2z
                |             R3x R3y R3z
                |             Px Py Pz
                |             R1x:x-component of x axis
                |             R2x:y-component of x axis
                |             R3x:z-component of x axis
                |             R1y:x-component of y axis
                |             R2y:y-component of y axis
                |             R3y:z-component of y axis
                |             R1z:x-component of z axis
                |             R2z:y-component of z axis
                |             R3z:z-component of z axis

        :param tuple o_offset_trans_list:
        :return: None
        :rtype: None
        """
        return self.place_activity.GetOffset(o_offset_trans_list)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_offset'
        # # vba_code = """
        # # Public Function get_offset(place_activity)
        # #     Dim oOffsetTransList (2)
        # #     place_activity.GetOffset oOffsetTransList
        # #     get_offset = oOffsetTransList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_placed_products(self, p_placed_prods: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetPlacedProducts(CATSafeArrayVariant pPlacedProds)
                | 
                |     Returns or Sets Placed Products

        :param tuple p_placed_prods:
        :return: None
        :rtype: None
        """
        return self.place_activity.GetPlacedProducts(p_placed_prods)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_placed_products'
        # # vba_code = """
        # # Public Function get_placed_products(place_activity)
        # #     Dim pPlacedProds (2)
        # #     place_activity.GetPlacedProducts pPlacedProds
        # #     get_placed_products = pPlacedProds
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_placed_mfg_assembly(self, p_picked_item: MfgAssembly) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemovePlacedMfgAssembly(MfgAssembly pPickedItem)
                | 
                |     Removes a Manufacturing Assembly from the list of placed items

        :param MfgAssembly p_picked_item:
        :return: None
        :rtype: None
        """
        return self.place_activity.RemovePlacedMfgAssembly(p_picked_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_placed_mfg_assembly'
        # # vba_code = """
        # # Public Function remove_placed_mfg_assembly(place_activity)
        # #     Dim pPickedItem (2)
        # #     place_activity.RemovePlacedMfgAssembly pPickedItem
        # #     remove_placed_mfg_assembly = pPickedItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_placed_product(self, p_picked_item: Product) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub RemovePlacedProduct(Product pPickedItem)
                | 
                |     Removes a product from the list of placed items

        :param Product p_picked_item:
        :return: None
        :rtype: None
        """
        return self.place_activity.RemovePlacedProduct(p_picked_item.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_placed_product'
        # # vba_code = """
        # # Public Function remove_placed_product(place_activity)
        # #     Dim pPickedItem (2)
        # #     place_activity.RemovePlacedProduct pPickedItem
        # #     remove_placed_product = pPickedItem
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_offset(self, o_offset_trans_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetOffset(CATSafeArrayVariant oOffsetTransList)
                | 
                |     This method sets the relative offsets for placing the
                |     product
                | 
                |     Parameters:
                | 
                |         oOffsetTransList
                |             list of Offsets between EndEffs and Products at time of placing
                |             first 12 values represent 1st offset, next 12, 2nd offset and so on.. The offset
                |             matrix is interpreted as follows: The first 9 entries correspond to the
                |             rotation matrix and the next 3 entries correspond to the position
                |             vector
                |             R1x R1y R1z
                |             R2x R2y R2z
                |             R3x R3y R3z
                |             Px Py Pz
                |             R1x:x-component of x axis
                |             R2x:y-component of x axis
                |             R3x:z-component of x axis
                |             R1y:x-component of y axis
                |             R2y:y-component of y axis
                |             R3y:z-component of y axis
                |             R1z:x-component of z axis
                |             R2z:y-component of z axis
                |             R3z:z-component of z axis
                | 
                |     Example:
                | 
                |           This example shows how the offset list needs to be
                |           populated
                |
                |          ' Example of 45 degree rotation around the x-axis of placing
                |          hand
                |         Dim oOffsetTransList(11) ' 0 to 11; relative transformation between
                |         hand and object
                |         ' X axis rotation component
                |         oOffsetTransList( 0 )  = 1
                |         oOffsetTransList( 3 )  = 0
                |         oOffsetTransList( 6 )  = 0
                |         ' Y axis rotation component
                |         oOffsetTransList( 1 )  = 0
                |         oOffsetTransList( 4 )  = 0.7071
                |         oOffsetTransList( 7 )  = 0.7071
                |         ' Z axis rotation component
                |         oOffsetTransList( 2 )  = 0
                |         oOffsetTransList( 5 )  = -0.7071
                |         oOffsetTransList( 8 )  = 0.7071
                |         ' position vector (relative vector between the hand and
                |         object)
                |         oOffsetTransList( 9 )  = 0
                |         oOffsetTransList( 10 )  = 0
                |         oOffsetTransList( 11 )  = 0

        :param tuple o_offset_trans_list:
        :return: None
        :rtype: None
        """
        return self.place_activity.SetOffset(o_offset_trans_list)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_offset'
        # # vba_code = """
        # # Public Function set_offset(place_activity)
        # #     Dim oOffsetTransList (2)
        # #     place_activity.SetOffset oOffsetTransList
        # #     set_offset = oOffsetTransList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_pick_act(self, pick_act: Activity) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPickAct(Activity pickAct)
                | 
                |     Sets or append a link to a Pick activity

        :param Activity pick_act:
        :return: None
        :rtype: None
        """
        return self.place_activity.SetPickAct(pick_act.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_pick_act'
        # # vba_code = """
        # # Public Function set_pick_act(place_activity)
        # #     Dim pickAct (2)
        # #     place_activity.SetPickAct pickAct
        # #     set_pick_act = pickAct
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_placed_products(self, p_placed_prods: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub SetPlacedProducts(CATSafeArrayVariant pPlacedProds)

        :param tuple p_placed_prods:
        :return: None
        :rtype: None
        """
        return self.place_activity.SetPlacedProducts(p_placed_prods)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_placed_products'
        # # vba_code = """
        # # Public Function set_placed_products(place_activity)
        # #     Dim pPlacedProds (2)
        # #     place_activity.SetPlacedProducts pPlacedProds
        # #     set_placed_products = pPlacedProds
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PlaceActivity(name="{self.name}")'
