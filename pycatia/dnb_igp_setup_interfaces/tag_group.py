#! usr/bin/python3.9
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-09-25 14:34:21.593357

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.dnb_igp_setup_interfaces.tag import Tag
from pycatia.system_interfaces.collection import Collection


class TagGroup(Collection):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     TagGroup
                | 
                | Interface representing a TagGroup.
                | 
                | Role: This interface is used to work with TagGroup which consists of a list of
                | Tags.
                | The following code snippet can be used to obtain a TagGroup from a selected
                | Product
                | 
                |   Set ParentObject = CATIA.ActiveDocument.Selection.FindObject("CATIAProduct")	
                |   Set objTagGroup = ParentObject.GetTechnologicalObject("TagGroup")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Tag)
        self.tag_group = com_object

    def create_tag(self, io_tag: Tag) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub CreateTag(Tag ioTag)
                | 
                |     Creates a Tag
                | 
                |     Parameters:
                | 
                |         oTag
                |             Newly created Tag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |
                |     Example:
                |
                |           Dim objTagGroup As TagGroup
                |           ...
                |           Dim objTag As Tag
                |           objTagGroup.CreateTag objTag

        :param Tag io_tag:
        :return: None
        :rtype: None
        """
        return self.tag_group.CreateTag(io_tag.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'create_tag'
        # # vba_code = """
        # # Public Function create_tag(tag_group)
        # #     Dim ioTag (2)
        # #     tag_group.CreateTag ioTag
        # #     create_tag = ioTag
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def delete_tag(self, i_tag: Tag) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub DeleteTag(Tag iTag)
                | 
                |     Deletes a Tag
                | 
                |     Parameters:
                | 
                |         ioTag
                |             Tag to be deleted 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |
                |     Example:
                |
                |           Dim objTagGroup As TagGroup
                |           ...
                |           Dim objTag As Tag
                |           objTagGroup.DeleteTag objTag

        :param Tag i_tag:
        :return: None
        :rtype: None
        """
        return self.tag_group.DeleteTag(i_tag.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'delete_tag'
        # # vba_code = """
        # # Public Function delete_tag(tag_group)
        # #     Dim iTag (2)
        # #     tag_group.DeleteTag iTag
        # #     delete_tag = iTag
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_owner(self, io_parent_product: str) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetOwner(CATBSTR ioParentProduct)
                | 
                |     Retrieves the name of the owner of this TagGroup.
                | 
                |     Parameters:
                | 
                |         ioParentProduct
                |             Name of the owner of this TagGroup. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |
                |     Example:
                |
                |           Dim objTagGroup As TagGroup
                |           ...
                |           Dim ownerName As String
                |           objTagGroup.GetOwner ownerName

        :param str io_parent_product:
        :return: None
        :rtype: None
        """
        return self.tag_group.GetOwner(io_parent_product)

    def get_tag(self, index: int) -> Tag:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Func GetTag(short index) As Tag
                | 
                |     Returns a Tag by Index.
                | 
                |     Parameters:
                | 
                |         index
                |             Index of the required Tag. 
                |         oTag
                |             Returned Tag. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |
                |     Example:
                |
                |           Dim objTagGroup As TagGroup
                |           ...
                |           For i = 1 To objTagGroup.Count
                |             Set objTag = objTagGroup.GetTag(i)
                |             ...
                |           Next

        :param int index:
        :return: Tag
        :rtype: Tag
        """
        return Tag(self.tag_group.GetTag(index))

    def get_tag_list(self, io_tag_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-09-25 14:34:21.593357))
                | o Sub GetTagList(CATSafeArrayVariant ioTagList)
                | 
                |     Gets the List of names of Tags
                | 
                |     Parameters:
                | 
                |         ioTagList
                |             Underlying List of Tag names. 
                | 
                |     Returns:
                |         an HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_FAIL otherwise
                |
                |     Example:
                |
                |           Dim objTagGroup As TagGroup
                |           ...
                |           Dim List(100)
                |           objTagGroup.GetTagList List

        :param tuple io_tag_list:
        :return: None
        :rtype: None
        """
        return self.tag_group.GetTagList(io_tag_list)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_tag_list'
        # # vba_code = """
        # # Public Function get_tag_list(tag_group)
        # #     Dim ioTagList (2)
        # #     tag_group.GetTagList ioTagList
        # #     get_tag_list = ioTagList
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'TagGroup(name="{self.name}")'
