#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import fnmatch
import time
import subprocess


def get_sn():
    cmd = "adb devices"
    info_lines = os.popen(cmd).readlines()
    sn = info_lines[1].split()
    return sn[0]


size_keyboard = {
    "mx3_note": (0, 1668, 1080, 891),
    "mx3_input_type": (0, 1800, 1080, 1020),
    "note2": (0, 1280, 720, 750),
    "6p_input_type": (0, 2392, 1440, 1363),
    "itel": (0, 854, 480, 486)
}


class MyKeyboard():
    def __init__(self, name_keyboard, size_keyboard):
        print("Create a keyboard Class!")
        self.name = name_keyboard
        self.llx, self.lly, self.urx, self.ury = size_keyboard
        self.hight = self.lly - self.ury
        self.width = self.urx - self.llx
        self.key_pos = self.makekeyboard()

    """
    Basic 场景	Line1	    Line2 	    Line3	    Line4	    Line5
    按键	        Menu face	10 键	    9键	        9键	        6或7键
    apl	                    Qwertyuiop	Asdfghjkl	Caps zxcvbnm back
    """
    def makekeyboard(self):
        key_pos = {}
        line_high = self.hight / 5.0
        alp_wid = self.width / 10.0
        alp_1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        alp_2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        alp_3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        alp_1_1 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        alp_2_1 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        alp_3_1 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']

        line0_pos_y = self.ury + line_high * 0.2
        menu_pos_x = self.llx + alp_wid * 0.5
        key_pos["menu"] = (menu_pos_x, line0_pos_y)

        line1_pos_y = self.ury + line_high * 1.5
        for i in range(10):
            pos_x = self.llx + alp_wid * (0.5 + i)
            key_pos[alp_1[i]] = (pos_x, line1_pos_y)
            key_pos[alp_1_1[i]] = (pos_x, line1_pos_y)
        line2_pos_y = self.ury + line_high * 2.5
        for i in range(9):
            pos_x = self.llx + alp_wid * (1 + i)
            key_pos[alp_2[i]] = (pos_x, line2_pos_y)
            key_pos[alp_2_1[i]] = (pos_x, line2_pos_y)
        line3_pos_y = self.ury + line_high * 3.5
        for i in range(7):
            pos_x = self.llx + alp_wid * (2 + i)
            key_pos[alp_3[i]] = (pos_x, line3_pos_y)
            key_pos[alp_3_1[i]] = (pos_x, line3_pos_y)

        caps_pos_x = self.llx + alp_wid
        back_pos_x = self.llx + alp_wid * 9
        key_pos["Caps"] = (caps_pos_x, line3_pos_y)
        key_pos["back"] = (back_pos_x, line3_pos_y)
        key_pos["#"] = (back_pos_x, line3_pos_y)

        line4_pos_y = self.ury + line_high * 4.5
        blank_pos_x = self.llx + alp_wid * 6
        key_pos[" "] = (blank_pos_x, line4_pos_y)
        key_pos[","] = (self.llx + alp_wid * 3, line4_pos_y)
        key_pos["."] = (self.llx + alp_wid * 8, line4_pos_y)

        num_pos_x = self.llx + alp_wid
        emoji_pos_x = self.llx = alp_wid * 2
        key_pos["num"] = (num_pos_x, line4_pos_y)
        key_pos["emoji"] = (emoji_pos_x, line4_pos_y)

        return key_pos

    def tap_key(self, key):
        if key in self.key_pos.keys():
            x, y = self.key_pos[key]
            # print("tap ", x, y, key)
            cmd = "adb shell input tap " + str(x) + " " + str(y)
            # pid = subprocess.Popen([cmd], shell=True)
            # subprocess.Popen.wait(pid)
            # pid.kill()
            os.popen(cmd)
            time.sleep(0.3)
            return 0
        else:
            # print(key, " not in key_pos! ******** Error ********")
            x, y = self.key_pos[" "]
            # print("tap ", x, y, key)
            cmd = "adb shell input tap " + str(x) + " " + str(y)
            # pid = subprocess.Popen([cmd], shell=True)
            # subprocess.Popen.wait(pid)
            # pid.kill()
            os.popen(cmd)
            time.sleep(0.4)


if __name__ == "__main__":
    # print("hello")
    # kb = MyKeyboard("kika", size_keyboard["6p_input_type"])
    # str1 = "I just configured my db(oracle) and started cloudera manager." \
    #        "It says started but could not see any thing in the logs and " \
    #        "I could not find port 7180 being used. I had succesfully installed cm on this " \
    #        "very machine pointing to postgres a few days ago and it worked fine. " \
    #        "Then I un installed and trying to install to an oracle db.All steps " \
    #        "until this went fine.Any ideas? I tried checking cloudera-scm-server." \
    #        "log but it has log info of old installation(with postgres)." \
    #        "I do not see any information about the new installation." \
    #        "It is obvious that cm did not start because the port was never being used."
    #
    # str2 = "Just lik Chro Timel tool, systrace # captures th operationd of your applica, " \
    #        " using adb and atrace #, whic uses ftrace # and displays them in a conven timeli format. " \
    #        "You ca invok th tool eithe thro Andr Studi or via th command line. " \
    #        "I prefe and this post wil cov th latter bec it lends a bit more " \
    #        "transparenc to any errors you encoun in th proc. This guid wil use Systrace # with Andr and highe, " \
    #        "though th offici guid covers using th tool with all versions of Andr."
    #
    # pid = 2759
    # print(kb.hight,kb.width)
    # for i in range(1):
    #     os.popen("adb reconnect")
    #     time.sleep(2)
    #     for alp in str2:
    #         kb.tap_key(alp)
    sn = get_sn()
    print(sn)


