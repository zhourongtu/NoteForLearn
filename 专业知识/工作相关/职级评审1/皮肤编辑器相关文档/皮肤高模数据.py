# -*- coding:utf-8 -*-
from taggeddict import taggeddict as TD

data = TD({
	'fashion_suit_id': 10100035,
	'id': 10400210,
	'model_data': TD({
		'model_path': 'char/loading/t1/t1_arhbd_loading/t1_arhbd_loading.gim',
		'remove_special_sfx_in_status': (
			'fling2',
			'jump',
		),
		'special_sfx_path': (
			'effect/char/char_skin/t1/eff_arhbd_idel_v01.sfx',
			'effect/char/char_skin/t1/eff_arhbd_idel_v02.sfx',
		),
		'special_socket_name': (
			'eff_arhbd_idle_v01',
			'eff_arhbd_idle02',
		),
		'submesh_num': 1,
	}),
	'name': '艾瑞和巴蒂染色1',
	'show_config_data': TD({
		'appear_ani_t': 10.766,
		'appear_face_anim': 'face_anim/appear_arhbd.json',
		'camera_trk': 'track/appear_arbd.trk',
		'extra_models': (
			TD({
				'appear_ani': 'appear_arhbd',
				'appear_ani_t': 10.76,
				'auto_update_aabb': 1,
				'idle_ani': 'idle1_arhbd',
				'is_idle_circle': 1,
				'name': '艾瑞和巴蒂小人',
				'random_ani': 'idle2_arhbd',
				'random_ani_t': 4.6,
				'sex': 1,
				'socket': 't1_arbd',
			}),
			TD({
				'appear_ani': 'appear_arhbd',
				'appear_ani_t': 10.76,
				'auto_update_aabb': 1,
				'is_idle_circle': 1,
				'model_angle': '0,0,0',
				'model_path': 'char/parts_appear/t1_arhbd/jiqiren.gim',
				'model_pos': '0,0,0',
				'name': '艾瑞巴蒂被撞',
				'sex': 1,
			}),
		),
		'fov': 55.0,
		'has_appear': 1,
		'has_idle': 1,
		'has_random': 1,
		'idle_ani_t': 2.0,
		'model_pos': (
			0.0,
			0.0,
			0.0,
		),
		'random_ani_t': 4.6,
		'random_time': (
			3.0,
			5.0,
		),
		'scene': 'scene_w/t1_loading/airuihebadi_loading/airuihebadi_loading.scn',
	}),
	'ui_data': TD({
		'item_icon': 'gui2/char/t1/t1_arhbd/t1_arhbd_d_p.png',
		'share_icon': 'gui2/char/t1/t1_arhbd/t1_arhbd_d_p.png',
	}),
})