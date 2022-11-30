# -*- coding:utf-8 -*-

class TemplateDescType(object):
	INT = 1
	FLOAT = 2
	STR = 3
	LIST = 4
	TUPLE = 5
	DICT = 6
	EXTEND_DICT = 7

	# 时装描述类(共2个)
	FASHION_DESC = 101
	FASHION_SHOW_DESC = 102

	# 染色描述类(共11个)
	DYE_DESC = 103
	DYE_SHOW_DESC = 104
	DYE_MODEL_DATA_DESC = 105
	SUB_MODEL_INFO_DESC = 107
	DYE_TEXTURE_DATA_DESC = 108
	DYE_SFX_DATA_DESC = 109
	SUB_MODEL_SOCKET_DESC = 111 # 子模型挂接点
	SUB_MODEL_EXTEND_ACTION_FILE_PATH_DESC = 112 # 子模型的扩展动作文件路径
	SUB_MODEL_ANIMATION_GRAPH_PATH_DESC = 113 # 子模型的动画图文件路径
	SUB_MODEL_ANIMATION_GRAPH_MAP_DICT_DESC = 114 # 子模型动作同步




# =========================================== 基础描述信息 ===============================================
class TemplateDesc(object):
	def __init__(self, title):
		self.title = title

# =========================================== 基础描述类 begin ===============================================
class TemplateInt(TemplateDesc):
	def __init__(self, title):
		super(TemplateInt, self).__init__(title)


class TemplateFloat(TemplateDesc):
	def __init__(self, title):
		super(TemplateFloat, self).__init__(title)


class TemplateStr(TemplateDesc):
	def __init__(self, title):
		super(TemplateStr, self).__init__(title)


class TemplateDict(TemplateDesc):
	def __init__(self, title, key_type, key_title, value_type, value_title):
		super(TemplateDict, self).__init__(title)
		self.key_type = key_type
		self.value_type = value_type
		self.key_title = key_title
		self.value_title = value_title


class TemplateExtendDict(TemplateDesc):
	def __init__(self, title, key_type=TemplateDescType.STR, key_title="字段"):
		super(TemplateDesc, self).__init__(title)
		self.key_type = key_type
		self.key_title = key_title


class TemplateList(TemplateDesc):
	def __init__(self, title, value_type, value_title):
		super(TemplateList, self).__init__(title)
		self.value_type = value_type
		self.value_title = value_title


class TemplateTuple(TemplateDesc):
	def __init__(self, title, value_type_list=[]):
		super(TemplateDesc, self).__init__(title)
		self.value_type_list = value_type_list


# =========================================== 基础描述类 begin ===============================================


# =========================================== 时装描述 begin =================================================
class FashionDesc(TemplateExtendDict):
	def __init__(self):
		super(FashionDesc, self).__init__("时装数据")
		self.id = TemplateInt("时装ID")
		self.default_dye_id = TemplateInt("染色ID")
		self.dye_ids = TemplateList("全部染色", value_type=TemplateDescType.INT, value_title="染色ID")
		self.accessory_2_socket_name = TemplateDict("特殊配饰挂接", key_type=TemplateDescType.INT, key_title="配饰ID", value_type=TemplateDescType.STR, value_title="挂接点")
		self.exclude_bind_pos_type_list = TemplateList("不允许佩戴的配饰位置", value_type=TemplateDescType.INT, value_title="挂接位置")
		self.anim_resmap_path = TemplateStr("皮肤扩展动作文件路径")
		self.race_id = TemplateInt("种族")


class FashionShowDesc(TemplateExtendDict):
	def __init__(self):
		super(FashionShowDesc, self).__init__("时装高模(展示)数据")
		self.id = TemplateInt("时装ID")
		self.default_dye_id = TemplateInt("染色ID")
		self.dye_ids = TemplateList("全部染色", value_type=TemplateDescType.INT, value_title="染色ID")
		self.accessory_2_socket_name = TemplateDict("特殊配饰挂接", key_type=TemplateDescType.INT, key_title="配饰ID", value_type=TemplateDescType.STR, value_title="挂接点")
		self.exclude_bind_pos_type_list = TemplateList("不允许佩戴的配饰位置", value_type=TemplateDescType.INT, value_title="挂接位置")
		self.anim_resmap_path = TemplateStr("皮肤扩展动作文件路径")
		self.race_id = TemplateInt("种族")
# =========================================== 时装描述 end =================================================


# =========================================== 染色描述 begin ==============================================
class SubModelSocketDesc(TemplateStr):
	def __init__(self):
		super(SubModelSocket, self).__init__(title="子模型挂接点")
class SubModelExtendActionFilePathDesc(TemplateStr):
	def __init__(self):
		super(SubModelExtendActionFilePath, self).__init__(title="子模型的扩展动作文件路径")
class SubModelAnimationGraphPathDesc(TemplateStr):
	def __init__(self):
		super(SubModelAnimationGraphPath, self).__init__(title="子模型的动画图文件路径")
class SubModelAnimationMapDictDesc(TemplateDict):
	def __init__(self):
		super(SubModelAnimationMapDict, self).__init__(title="子模型动作同步", key_type=TemplateStr, key_title="主模型动作", value_type=TemplateStr, value_title="子模型动作")
class SubModelDesc(TemplateTuple):
	def __init__(self, title):
		value_type_list = []
		value_type_list.append(TemplateDescType.SUB_MODEL_SOCKET_DESC)
		value_type_list.append(TemplateDescType.SUB_MODEL_EXTEND_ACTION_FILE_PATH_DESC)
		value_type_list.append(TemplateDescType.SUB_MODEL_ANIMATION_GRAPH_PATH_DESC)
		value_type_list.append(TemplateDescType.SUB_MODEL_ANIMATION_GRAPH_MAP_DICT_DESC)
		super(SubModelDesc, self).__init__(title, value_type_list=value_type_list)


class DyeModelDataDesc(TemplateDesc):
	def __init__(self, title):
		super(DyeModelDataDesc, self).__init__(title)
		self.model_path = TemplateStr("模型路径")
		self.submesh_num = TemplateInt("submesh数量"),
		self.sub_model = TemplateList("子模型列表", value_type=TemplateDescType.SUB_MODEL_INFO_DESC, value_title="子模型信息")
		self.special_sfx_path = TemplateList("默认特效列表", value_type=TemplateDescType.STR, value_title="默认特效路径")
		self.special_socket_name = TemplateList("默认特效挂接点列表", value_type=TemplateDescType.STR, value_title="默认特效挂接点")
		self.remove_special_sfx_in_status = TemplateList("移除默认特效动作列表", value_type=TemplateDescType.STR, value_title="动作名")


class DyeTextureDataDesc(TemplateDesc):
	def __init__(self, title):
		super(DyeModelDataDesc, self).__init__(title)
		self.mix_texture_path = TemplateStr("mix贴图路径")
		self.mtg_path = TemplateStr("mtg路径")
		self.normal_texture_path = TemplateStr("法线贴图路径")
		self.texture_path = TemplateStr("贴图路径")


class DyeSfxDataDesc(TemplateDesc):
	def __init__(self, title):
		super(DyeSfxDataDesc, self).__init__(title)
		self.random_rate = TemplateFloat("播放概率")
		self.path = TemplateList("特效路径列表", value_type=TemplateDescType.STR, value_title="特效路径")
		self.socket = TemplateList("特效挂点列表", value_type=TemplateDescType.STR, value_title="特效挂点")
		self.type = TemplateInt("特效类型") # 1.原有替换、2.原有增加


class DyeDesc(TemplateExtendDict):
	def __init__(self, title="染色数据"):
		super(DyeDesc, self).__init__(title=title)
		self.id = TemplateInt("染色ID")
		self.fashion_suit_id = TemplateInt("时装ID")
		self.model_data = DyeModelDataDesc("染色模型数据")
		self.texture_data = DyeTextureDataDesc("染色贴图数据")
		self.sfx_data = TemplateDict("皮肤特效数据", key_type=TemplateDescType.STR, key_title="动作名", value_type=TemplateDescType.DYE_SFX_DATA_DESC, value_title="特效数据")


class DyeShowDesc(DyeDesc):
	def __init__(self):
		super(DyeShowDesc, self).__init__(title="染色高模(展示)数据")
# =========================================== 染色描述 end ==============================================