import os
import subprocess
import sys
import time
import webbrowser

# Ссылка на видео
YOUTUBE_URL = "https://youtu.be/9JgpziW1xFs?si=DZOCyAIvjk7X8uPf"

# Имя файла антивируса в текущей папке
ANTIVIRUS_SCRIPT = "padikissanti.py"

# ASCII-арт fsociety
LOGO = r"""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                        'yMMM   XX
XX   Mh'                                                            'hM   XX
XX   -                                                                -   XX
XX                                                                          XX
XX   ::                                                              ::   XX
XX   MMhh.        ..hhhhhh..                    ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''              'mmMMMMMMMM  MMMMMMMMmm'              '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..    ''''      ''''    ..yyyyy..     'y.    ''mm   XX
XX            MN    .sMMMMMMMMMss.    .    .    .ssMMMMMMMMMs.    NM            XX
XX            N`    MMMMMMMMMMMMMN    M    M    NMMMMMMMMMMMMM    `N            XX
XX             +  .sMNNNNNMMMMMN+    `N    N`    +NMMMMMNNNNNMs.  +             XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                  oo          oo                  Mo         XX
XX          oMMo                M              M                oMMo        XX
XX        +MMMM                 s              s                 MMMM+      XX
XX       +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+     XX
XX      +MMMMMMM+        ++NNMMMMMMMMN+    +NMMMMMMMMNN++        +MMMMMMM+    XX
XX      MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM    XX
XX      yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy    XX
XX    m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m  XX
XX    MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM  XX
XX    MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM  XX
XX    MMMMd   ''''hhhhh        odddo          obbbo        hhhh''''   dMMMM  XX
XX    MMMMMd              'hMMMMMMMMMMddddddMMMMMMMMMMh'              dMMMMM  XX
XX    MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'                dMMMMMM  XX
XX    MMMMMMM-                ''ddMMMMMMMMMMMMMMdd''                -MMMMMMM  XX
XX    MMMMMMMM                    '::dddddddd::'                    MMMMMMMM  XX
XX    MMMMMMMM-                                                     -MMMMMMMM  XX
XX    MMMMMMMMM                                                     MMMMMMMMMM  XX
XX    MMMMMMMMMy                                                    yMMMMMMMMM  XX
XX    MMMMMMMMMMy.                                                .yMMMMMMMMMM  XX
XX    MMMMMMMMMMMMy.                                            .yMMMMMMMMMMMM  XX
XX    MMMMMMMMMMMMMMMy.                                        .yMMMMMMMMMMMMMM  XX
XX    MMMMMMMMMMMMMMMMMs.                                    .sMMMMMMMMMMMMMMMM  XX
XX    MMMMMMMMMMMMMMMMMMss.            ....            .ssMMMMMMMMMMMMMMMMMM  XX
XX    MMMMMMMMMMMMMMMMMMMMNo          oNNNNo          oNMMMMMMMMMMMMMMMMMMMM  XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    .o88o.                               o8o                 .
    888 `"                               `"'               .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.   .o888oo oooo   ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88. .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"     d8'
                                                                .o...P'
                                                                `XER0'
"""

RED = "\033[91m"
RESET = "\033[0m"


def print_logo():
    """Выводит логотип в консоль."""
    sys.stdout.write("\033[H\033[J")
    sys.stdout.write(RED + LOGO + RESET + "\n")
    sys.stdout.flush()


def spawn_process_in_new_window(target_script, args=None):
    """Запускает указанный Python-скрипт в новом окне консоли."""
    if args is None:
        args = []

    cmd = [sys.executable, target_script] + args

    if sys.platform == "win32":
        subprocess.Popen(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)
    elif sys.platform == "darwin":
        cmd_str = f"\"{sys.executable}\" \"{target_script}\" " + " ".join(
            f'"{a}"' for a in args
        )
        subprocess.Popen(
            [
                "osascript",
                "-e",
                f'tell application "Terminal" to do script "{cmd_str}"',
            ]
        )
    else:
        for term in ["x-terminal-emulator", "gnome-terminal", "konsole", "xterm"]:
            try:
                subprocess.Popen([term, "-e"] + cmd)
                break
            except FileNotFoundError:
                continue


def main():
    # Режим выполнения для дочернего окна fsociety
    if "--child" in sys.argv:
        print_logo()
        input("fsociety")
        

    # Главный процесс
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    antivirus_path = os.path.join(base_dir, ANTIVIRUS_SCRIPT)

    # Проверка наличия файла антивируса перед запуском
    if not os.path.exists(antivirus_path):
        print(f"[!] Ошибка: Файл '{ANTIVIRUS_SCRIPT}' не найден в {base_dir}")
        print("Убедитесь, что скрипт антивируса находится в той же папке.")
        input("Нажмите Enter для выхода...")
        return

    print("Запуск видео...")
    webbrowser.open(YOUTUBE_URL)

    seconds_to_wait = 60
    print(f"Ожидание окончания видео ({seconds_to_wait} сек)...")

    for remaining in range(seconds_to_wait, 0, -1):
        sys.stdout.write(f"\rОсталось: {remaining} сек. ")
        sys.stdout.flush()
        time.sleep(1)

    print("\nЗапуск парных окон (fsociety + padikissanti)...")

    # Отображаем логотип в текущей консоли
    print_logo()

    current_script_path = os.path.abspath(sys.argv[0])

    # Запускаем антивирус для текущей консоли
    spawn_process_in_new_window(antivirus_path)

    # Запускаем 4 пары дополнительных окон
    PAIR_COUNT = 999
    for i in range(PAIR_COUNT):
        print(f"Запуск пары {i + 1} из {PAIR_COUNT}...")

        # 1. Окно fsociety
        spawn_process_in_new_window(current_script_path, args=["--child"])

        # 2. Окно антивируса
        spawn_process_in_new_window(antivirus_path)

        time.sleep(0.01)

    print("\nВсе запланированные окна открыты.")
    input("\nНажмите Enter, чтобы завершить главный процесс...")


if __name__ == "__main__":
    main()