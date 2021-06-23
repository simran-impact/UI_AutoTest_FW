import pandas as pd

#
# col_list = ["dept", "sub_dept"]
# csv_path = "C:\\Users\\terrance.alfred\\PycharmProjects\\UI_AutoTest_FW\\resources\\filesToUpload\\toUploadAndProcessBatch\\exploreBatchData.csv"
# df = pd.read_csv(csv_path, usecols=col_list)
#
#
# # get L1_Category List
# def get_L1_Category():
#     l1 = 'dept'
#     # l2 = 'sub_dept'
#     l1_category = df[l1].unique().tolist()
#     # l2_category = df[l2].unique().tolist()
#     return l1_category
#
#
# # get mapping of L1 category with L2 category list
# def get_L2_Category():
#     list = df.values.tolist()
#     #print(list)
#     my_map = {}  # create a map
#     for i in list:
#         if i[1] in my_map.keys():
#             print(i[1])
#             print(i[0])
#             my_map[i[1]].add(i[0])  # add all other l2_categories in loop
#         else:
#             my_map.update({i[1]: {i[0]}})  # add first l2_category to key (l1_category)
#     return my_map
#
#
# # get list of all brands of L1 category
# def get_Sub_brands(l1_category):
#     list_map = get_L2_Category()
#     #print(list_map)
#     return list_map.get(l1_category)
#
# print(get_L1_Category())
# print(get_Sub_brands("MENS ATHLETIC APPAREL"))
col_list = ["style_id", "sub_dept", "dept"]
csv_path = "C:\\Users\\terrance.alfred\\PycharmProjects\\UI_AutoTest_FW\\resources\\filesToUpload\\toViewProductAndAttributes\\exploreBatchData.csv"
df = pd.read_csv(csv_path, usecols=col_list)
list = df.values.tolist()
print(list)


# ### get dept with brand and style id mapping
# def get_styleId_Brand_Mapping():
#     l1_category_map = {}
#     for i in list:
#         if i[2] in l1_category_map.keys():
#             styleid_map = l1_category_map.get(i[2])
#             if i[1] in styleid_map.keys():
#                 styleid_map[i[1]].add(i[0])
#             else:
#                 styleid_map.update({i[1]: {i[0]}})
#         else:
#             l1_category_map.update({i[2]: {i[1]: {i[0]}}})
#             #print(l1_category_map)
#     print(l1_category_map)
#     return l1_category_map
#
#
# def getStyleIdCount():
#     style_brand_map = get_styleId_Brand_Mapping()
#     brand_Id_Map = style_brand_map.get('WOMENS ATHLETIC APPAREL')
#     styleId_set = brand_Id_Map.get('NIKE')
#     #print(styleId_set)
#     print(styleId_set.__len__())
#     print(brand_Id_Map.keys())
#     print(brand_Id_Map)
#     return styleId_set.__len__()
#
#
# #get_styleId_Brand_Mapping()
# getStyleIdCount()
