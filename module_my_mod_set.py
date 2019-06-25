from header_operations import *
from ID_items import *
from ID_troops import *
from ID_strings import *
from module_constants import *
from module_items import *
from header_item_modifiers import *


def keys_array():
    keys_list = []
    for key_no in xrange(len(keys)):
        keys_list.append((troop_set_slot, "trp_temp_array_a", key_no, keys[key_no]))
    return keys_list[:]


keys = [key_0, key_1, key_2, key_3, key_4, key_5, key_6, key_7, key_8, key_9, key_a, key_b, key_c, key_d, key_e, key_f, key_g, key_h, key_i, key_j, key_k, key_l, key_m, key_n, key_o, key_p, key_q, key_r, key_s, key_t, key_u, key_v, key_w, key_x, key_y, key_z, key_numpad_0, key_numpad_1,
        key_numpad_2, key_numpad_3, key_numpad_4, key_numpad_5, key_numpad_6, key_numpad_7, key_numpad_8, key_numpad_9, key_num_lock, key_numpad_slash, key_numpad_multiply, key_numpad_minus, key_numpad_plus, key_numpad_enter, key_numpad_period, key_insert, key_delete, key_home, key_end, key_page_up,
        key_page_down, key_up, key_down, key_left, key_right, key_f1, key_f2, key_f3, key_f4, key_f5, key_f6, key_f7, key_f8, key_f9, key_f10, key_f11, key_f12, key_space, key_escape, key_enter, key_tab, key_back_space, key_open_braces, key_close_braces, key_comma, key_period, key_slash,
        key_back_slash, key_equals, key_minus, key_semicolon, key_apostrophe, key_tilde, key_caps_lock, key_left_shift, key_right_shift, key_left_control, key_right_control, key_left_alt, key_right_alt]