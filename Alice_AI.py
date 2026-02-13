import random
import time

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

def slow_print(text, delay=0.035):
    """模擬打字的感覺"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def chat():
    print("\n" + "═" * 40)
    print("      前女友模擬對話（療傷模式）")
    print("      輸入 'bye' / '88' / '掰' 結束")
    print("═" * 40 + "\n")

    slow_print(random.choice(responses["開場"]), 0.04)
    time.sleep(1.3)
    slow_print(random.choice(responses["解釋苦衷"]), 0.035)
    time.sleep(2.0)
    slow_print(random.choice(responses["鼓勵活下去"]), 0.04)
    time.sleep(1.8)

    while True:
        user_input = input("\n你：").strip()
        
        if user_input.lower() in {'bye', '88', '掰', '再見', '結束'}:
            time.sleep(1.2)
            slow_print(random.choice(responses["最感人幾句"]), 0.045)
            time.sleep(2.5)
            slow_print(random.choice(responses["道別"]), 0.05)
            print("\n" + "═" * 40 + "\n對話結束。好好照顧自己。")
            break

        # 根據關鍵字給不同回應（很粗糙但有效）
        lowered = user_input.lower()
        if any(kw in lowered for kw in ['為什麼', '原因', '怎麼', '當初']):
            slow_print(random.choice(responses["解釋苦衷"]))
        elif any(kw in lowered for kw in ['難過', '傷心', '想你', '放不下', '忘不了']):
            slow_print(random.choice(responses["最感人幾句"]))
        elif any(kw in lowered for kw in ['帥', '變帥', '健身', '變好', '積極', '樂觀', '運動', '打扮']):
            slow_print(random.choice(responses["叫你變更好"]))
        else:
            # 預設溫柔鼓勵
            slow_print(random.choice(responses["鼓勵活下去"]))

        time.sleep(0.8 + random.random() * 1.2)


if __name__ == "__main__":
    try:
        chat()
    except KeyboardInterrupt:
        print("\n\n中斷了……沒關係，你已經很努力了。")  ##hi