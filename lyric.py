import time
from threading import Thread, Lock

Lock = Lock()

def animate_text(text, delay=0.1):
    with Lock:
     for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        print()

        def sing_lyric(lyric, delay, speed):
         time.sleep(delay)
        animate_text(lyric, delay)
        def sing_song():
            lyric =[
                ("nỗi nhớ em trong đêm thật dài", 0,1),
                ("thêm lí do cho anh tồn tại", 0,1),
                ("Để lại chạm vào bờ môi ấy dịu dàng", 0,1),
                ("Lời thì thầm ngọt ngào bên tai", 0,1),
                ("ta mất nhau thật rồi em ơi", 0,2),
                ("Tan vỡ hai cực đành chia đôi", 0,8),
                ("Anh sẽ luôn ghi nhớ em trong từng tế bảo", 0,1),
                ("Vậy mà dừng lại như thế sao?", 0,1),
                ("Ye... chẳng cần vật chất, chẳng cần spotlight",0.1),
                ("Chỉ cần vài nốt nhạc hoà cùng cây mic", 0.1),
            ]
            