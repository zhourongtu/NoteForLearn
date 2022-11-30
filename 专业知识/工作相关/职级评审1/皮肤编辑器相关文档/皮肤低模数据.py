# -*- coding:utf-8 -*-
from taggeddict import taggeddict as TD

data = TD({
	'fashion_suit_id': 10100035,
	'id': 10400210,
	'model_data': TD({
		'model_path': 'char/t1/t1_arhbd/t1_arhbd.gim',
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
	'sfx_data': TD({
		'jump1': (
			TD({
				'path': (
					'effect/char/char_skin/t1/eff_arhbd_jump_v01.sfx',
				),
				'socket': (
					'eff_arhbd_idle_v03',
				),
				'type': 2,
			}),
		),
		'jump2': (
			TD({
				'path': (
					'effect/char/char_skin/t1/arhbd/eff_arhbd_jump_v03.sfx',
				),
				'type': 1,
			}),
		),
		'rebirth_01': (
			TD({
				'path': (
					'effect/char/char_skin/t1/eff_arhbd_rebirth_v01.sfx',
				),
				'type': 1,
			}),
		),
		'rebirth_02': (
			TD({
				'path': (
					'effect/char/char_skin/t1/eff_arhbd_rebirth_v02.sfx',
				),
				'socket': (
					'origin',
				),
				'type': 1,
			}),
		),
		'roll': (
			TD({
				'path': (
					'effect/char/char_skin/t1/eff_arhbd_trail_v01.sfx',
				),
				'socket': (
					'mid',
				),
				'type': 1,
			}),
		),
		'rush1': (
			TD({
				'path': (
					'effect/char/char_skin/t1/eff_arhbd_run_v01.sfx',
				),
				'socket': (
					'eff_rush',
				),
				'type': 1,
			}),
		),
		'rush2': (
			TD({
				'path': (
					'effect/char/char_skin/t1/eff_arhbd_run_v02.sfx',
				),
				'type': 1,
			}),
		),
	}),
})