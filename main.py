import win32api, win32gui, win32con
from init_app import child_app, app_rect
import random
from time import sleep
from print_format import print_format
from check_stage import check_is_video, check_is_home
from global_variable import increase_bot_time, get_bot_time

heart_button = [3546 - app_rect[0], 625 - app_rect[1]]

comment_button = [3544 - app_rect[0], 748 - app_rect[1]]
comment_box = [3159 - app_rect[0], 1254 - app_rect[1]]
send_comment = [3533 - app_rect[0], 656 - app_rect[1]]
close_comment_box = [3558 - app_rect[0], 263 - app_rect[1]]

share_button = [3538 - app_rect[0], 1006 - app_rect[1]]
copy_link_button = [2959 - app_rect[0], 974 - app_rect[1]]

home = [3047 - app_rect[0], 1068 - app_rect[1]]
blank_rect = [3241 - app_rect[0], 653 - app_rect[1]]
back_button = [2932 - app_rect[0], 128 - app_rect[1]]

fixed_comment = ""
# fixed_comment = "Mọi người cho mình xin 1 follow với ạ, mình cảm ơnnn ạ <3"

comments = [
    "cảm giác tệ thật...",
    "mình sẽ chữa lành trái tim cậu",
    # "Wow, video hay quá!",
    # "Cười bể bụng với video này =))",
    # "Cảnh quay đẹppppp",
    # "Tui gục ngã :))",
    # "Đáng iu quá",
    # "Tuyệt vời!",
    # "Cho tớ xin tuyệt chiêu làm video như thế này đi!",
    # "Cảm xúc tích cực!",
    # "Tôi rất thích video của bạn!",
    # "Cảm ơn bạn!",
    # "Cảm ơn bạn đã chia sẻ!",
    # "Ngưỡng mộ quá",
]


def click_heart():
    heart_click = win32api.MAKELONG(heart_button[0], heart_button[1])

    win32gui.SendMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, heart_click
    )
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, heart_click)


def click_comment():
    comment_click = win32api.MAKELONG(comment_button[0], comment_button[1])

    win32gui.SendMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, comment_click
    )
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, comment_click)


def input_comment():
    comment = comments[random.randint(0, len(comments) - 1)]
    print_format("Randomized comment:" + comment)
    combined_comment = comment + "\n" + fixed_comment

    for c in combined_comment:
        win32api.SendMessage(child_app, win32con.WM_CHAR, ord(c), 0)


def write_comment():
    comment_write_box = win32api.MAKELONG(comment_box[0], comment_box[1])

    win32gui.SendMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, comment_write_box
    )
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, comment_write_box)
    sleep(3)
    input_comment()
    sleep(1)


def send_comment_post():
    send_comment_click = win32api.MAKELONG(send_comment[0], send_comment[1])
    win32gui.SendMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, send_comment_click
    )
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, send_comment_click)


def close_comment():
    close_comment_click = win32api.MAKELONG(close_comment_box[0], close_comment_box[1])

    win32gui.SendMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, close_comment_click
    )
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, close_comment_click)


def click_share():
    share_click = win32api.MAKELONG(share_button[0], share_button[1])

    win32gui.SendMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, share_click
    )
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, share_click)


def copy_link():
    copy_link_click = win32api.MAKELONG(copy_link_button[0], copy_link_button[1])

    win32gui.SendMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, copy_link_click
    )
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, copy_link_click)


def back_to_home():
    home_click = win32api.MAKELONG(home[0], home[1])

    win32gui.SendMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, home_click
    )
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, home_click)


def scroll():
    scroll_event = win32api.MAKELONG(blank_rect[0], blank_rect[1])

    win32gui.PostMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, scroll_event
    )
    win32gui.PostMessage(
        child_app,
        win32con.WM_MOUSEMOVE,
        win32con.MK_LBUTTON,
        win32api.MAKELONG(blank_rect[0], 101),
    )
    win32gui.PostMessage(child_app, win32con.WM_LBUTTONUP, None, scroll_event)


def click_back():
    back_click = win32api.MAKELONG(back_button[0], back_button[1])

    win32gui.SendMessage(
        child_app, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, back_click
    )
    win32gui.SendMessage(child_app, win32con.WM_LBUTTONUP, None, back_click)


def break_task_time():
    sleep(random.randint(2, 4))


def main():
    while get_bot_time() < 10:
        is_home = check_is_home()
        if is_home == True:
            click_back()  # for hashtag search
            # back_to_home() // fyp page
            break_task_time()
            scroll()
            continue

        is_video = check_is_video()
        if is_video == False:
            print_format("Skipped due it's not a video")
            scroll()
            continue

        play_time = random.randint(16, 24)
        print_format("Viewing time:" + str(play_time) + "sec")
        sleep(play_time)
        print_format("Start heart click process")
        click_heart()
        break_task_time()
        print_format("Start comments process")
        click_comment()
        break_task_time()
        write_comment()
        send_comment_post()
        break_task_time()
        close_comment()
        break_task_time()
        close_comment()
        break_task_time()
        print_format("Start share + copy link process")
        click_share()
        break_task_time()
        copy_link()
        break_task_time()
        scroll()
        increase_bot_time()
        break_task_time()


main()
