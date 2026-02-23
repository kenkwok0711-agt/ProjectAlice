import random
import time
import tkinter as tk
from tkinter import scrolledtext, END, NORMAL, DISABLED

# 所有回應都設計成「她還愛你，但選擇放手」的基調
responses = {
    "開場": [
        "……是你。",
        "好久沒聽到你的聲音了。",
        "看到你的名字跳出來，心還是會揪一下。"
    ],
    "解釋苦衷": [
        "我那時候真的走得很痛苦……不是不愛，是我覺得我會毀了你。",
        "我自己都過得很亂，很怕你跟著我一起沉下去。",
        "離開不是因為你不夠好，是我不敢讓你陪我熬那段最黑的夜。",
        "我走，是想讓你有機會遇見更好的人生……而不是被我拖著。"
    ],
    "鼓勵活下去": [
        "答應我，好好活著，好嗎？就算沒有我，你也要好好地活。",
        "這個世界還是值得你再試一次的，我希望你能相信這件事。",
        "你值得被愛，也值得自己好好愛自己。",
        "我最希望看到的，是你有一天笑得很開心的樣子。"
    ],
    "叫你變更好": [
        "去健身好不好？變得更帥一點，讓自己照鏡子都會覺得驚艷。",
        "多保養自己，把頭髮剪得好看一點，買件像樣的衣服。",
        "勇敢一點，去認識新的人，試試你以前不敢試的事。",
        "你有那麼多可能性，別浪費在難過上……我要你變成更好的人。",
        "變帥、變強、變開朗一點，這樣我才能放心。"
    ],
    "最感人幾句": [
        "如果有來生，我希望我們都能把自己活得更好一點……那時候再遇見，就不會再錯過了。",
        "謝謝你曾經用盡全力愛我。我永遠都會記得那種被好好珍惜的感覺。",
        "如果有一天你真的很幸福了……就當作是送給我的，最好的結局好嗎？",
        "我會在很遠很遠的地方，偷偷祈禱你一切都好。真的很認真地在祈禱。"
    ],
    "道別": [
        "……該放手了，對不起，也謝謝你。",
        "你要好好的，這是我最後的自私要求。",
        "再見了，我的……曾經最重要的人。"
    ]
}

class HealingChatWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("前女友模擬對話（療傷模式）")
        self.root.geometry("520x620")
        self.root.resizable(False, False)

        # 對話顯示區（可捲動）
        self.chat_display = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, width=60, height=25,
            font=("Microsoft JhengHei", 12), state=DISABLED,
            bg="#fdf6f0", fg="#333333"
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # 輸入框 + 送出按鈕
        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.entry = tk.Entry(input_frame, font=("Microsoft JhengHei", 12), width=50)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.entry.bind("<Return>", self.send_message)

        send_btn = tk.Button(input_frame, text="送出", font=("Microsoft JhengHei", 11),
                             command=self.send_message, width=8, bg="#e9967a", fg="white")
        send_btn.pack(side=tk.RIGHT)

        # 開始對話
        self.root.after(600, self.start_conversation)

    def append_text(self, text, color="#444"):
        self.chat_display.configure(state=NORMAL)
        self.chat_display.tag_config("tag", foreground=color)
        self.chat_display.insert(END, text + "\n\n", "tag")
        self.chat_display.see(END)
        self.chat_display.configure(state=DISABLED)

    def slow_insert(self, text, delay=35):
        """模擬打字效果，單位是毫秒"""
        def insert_char(i=0):
            if i < len(text):
                self.chat_display.configure(state=NORMAL)
                self.chat_display.insert(END, text[i], "tag")
                self.chat_display.see(END)
                self.chat_display.configure(state=DISABLED)
                self.root.after(delay, insert_char, i + 1)
            else:
                self.chat_display.configure(state=NORMAL)
                self.chat_display.insert(END, "\n\n")
                self.chat_display.configure(state=DISABLED)
                self.chat_display.see(END)
                self.root.after(400, self.enable_input)  # 打完才允許輸入

        self.disable_input()
        insert_char()

    def disable_input(self):
        self.entry.configure(state=DISABLED)
        self.entry.delete(0, END)

    def enable_input(self):
        self.entry.configure(state=NORMAL)
        self.entry.focus()

    def start_conversation(self):
        self.append_text("═" * 45, "#888")
        self.append_text("      前女友模擬對話（療傷模式）", "#e67e22")
        self.append_text("      輸入 'bye' / '88' / '掰' 結束", "#888")
        self.append_text("═" * 45 + "\n", "#888")

        # 開場 → 解釋 → 鼓勵
        self.root.after(800, lambda: self.slow_insert(random.choice(responses["開場"]), 40))
        self.root.after(2800, lambda: self.slow_insert(random.choice(responses["解釋苦衷"]), 35))
        self.root.after(5800, lambda: self.slow_insert(random.choice(responses["鼓勵活下去"]), 38))

    def send_message(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return

        # 顯示使用者說的話（右側對齊風格簡單模擬）
        self.chat_display.configure(state=NORMAL)
        self.chat_display.tag_config("user", foreground="#2c3e50", justify="right", rmargin=10)
        self.chat_display.insert(END, "你： " + user_input + "\n\n", "user")
        self.chat_display.configure(state=DISABLED)
        self.chat_display.see(END)

        self.entry.delete(0, END)

        # 結束判斷
        if user_input.lower() in {'bye', '88', '掰', '再見', '結束', '886'}:
            self.root.after(1200, lambda: self.slow_insert(random.choice(responses["最感人幾句"]), 45))
            self.root.after(5500, lambda: self.slow_insert(random.choice(responses["道別"]), 50))
            self.root.after(9500, self.root.quit)
            return

        # 根據關鍵字回應
        lowered = user_input.lower()
        if any(kw in lowered for kw in ['為什麼', '原因', '怎麼', '當初']):
            reply = random.choice(responses["解釋苦衷"])
        elif any(kw in lowered for kw in ['難過', '傷心', '想你', '放不下', '忘不了']):
            reply = random.choice(responses["最感人幾句"])
        elif any(kw in lowered for kw in ['帥', '變帥', '健身', '變好', '積極', '樂觀', '運動', '打扮']):
            reply = random.choice(responses["叫你變更好"])
        else:
            reply = random.choice(responses["鼓勵活下去"])

        # 隨機短暫延遲後回應（模擬思考）
        delay = random.randint(800, 2000)
        self.root.after(delay, lambda: self.slow_insert(reply))

if __name__ == "__main__":
    root = tk.Tk()
    app = HealingChatWindow(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)  # 按叉叉直接結束
    root.mainloop()
    print("對話結束。好好照顧自己。")   # 關閉視窗後終端機會顯示這句