import streamlit as st
import streamlit.components.v1 as components
import random
import html

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==================== GIAO DIỆN VÀNG ====================

st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden;}

.stApp {
    background:linear-gradient(145deg,#050817,#101a38,#030611);
    color:#FFD700;
}

.block-container {
    max-width:1500px;
    padding:10px 12px 20px;
}

.game-title {
    text-align:center;
    color:#FFD700 !important;
    font-size:clamp(28px,4vw,44px);
    font-weight:1000;
    text-shadow:0 0 12px #B8860B;
}

.game-subtitle {
    text-align:center;
    color:#FFE566 !important;
    font-size:14px;
    font-weight:800;
    margin-bottom:12px;
}

h1,h2,h3,h4,h5,h6 {
    color:#FFD700 !important;
    font-weight:900 !important;
    text-shadow:0 1px 3px #000;
}

p,label,
[data-testid="stWidgetLabel"],
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
    color:#FFE566 !important;
    font-weight:800 !important;
}

[data-testid="stRadio"] label,
[data-testid="stRadio"] label p {
    color:#FFD700 !important;
    font-size:16px !important;
    font-weight:900 !important;
}

.stTextInput input,
.stTextArea textarea {
    color:#FFD700 !important;
    background:#101a32 !important;
    font-weight:800 !important;
    border:1px solid #FFD700 !important;
}

.stSelectbox div {
    font-weight:800 !important;
}

.stButton button {
    width:100%;
    min-height:40px;
    color:#FFD700 !important;
    background:#17213d !important;
    border:1px solid #FFD700 !important;
    border-radius:9px;
    font-size:14px !important;
    font-weight:900 !important;
}

.stButton button:hover {
    background:#493b0b !important;
    border:1px solid #FFF1A8 !important;
}

.stat-box {
    background:#101a32;
    border:1px solid #B8860B;
    border-radius:10px;
    padding:8px 3px;
    text-align:center;
    color:#FFD700;
    font-size:13px;
    font-weight:900;
}

.stat-number {
    color:#FFD700;
    font-size:23px;
    font-weight:1000;
}

[data-testid="stAlert"] p {
    color:#FFD700 !important;
    font-weight:900 !important;
}

hr {
    border-color:#8B7500;
}

@media(max-width:600px) {
    .block-container {padding:4px;}
    .stat-box {font-size:10px;}
    .stat-number {font-size:19px;}
}
</style>
""", unsafe_allow_html=True)

# ==================== DỮ LIỆU GAME ====================

if "players" not in st.session_state:
    st.session_state.players = [
        {"id": i, "name": f"Người {i+1}", "alive": True}
        for i in range(20)
    ]

defaults = {
    "score": 0,
    "round": 1,
    "answered": [],
    "victim_id": None,
    "notice": "🛸 UFO đang bay quanh Trái Đất!",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

players = st.session_state.players

for i, player in enumerate(players):
    player.setdefault("id", i)
    player.setdefault("name", f"Người {i+1}")
    player.setdefault("alive", True)

# ==================== CÂU ĐỐ ====================

riddles = [
    {
        "q": "Cái gì càng lấy đi thì càng lớn?",
        "options": ["Cái hố", "Cái cây", "Dòng sông"],
        "answer": "Cái hố",
    },
    {
        "q": "Tháng nào có 28 ngày?",
        "options": ["Tháng 2", "Tất cả các tháng", "Tháng 6"],
        "answer": "Tất cả các tháng",
    },
    {
        "q": "Cái gì có cổ nhưng không có đầu?",
        "options": ["Cái chai", "Cái bàn", "Cái ghế"],
        "answer": "Cái chai",
    },
    {
        "q": "Vượt qua người đứng thứ hai thì bạn đứng thứ mấy?",
        "options": ["Thứ nhất", "Thứ hai", "Thứ ba"],
        "answer": "Thứ hai",
    },
    {
        "q": "Cái gì có răng nhưng không cắn?",
        "options": ["Cái lược", "Con chó", "Cá mập"],
        "answer": "Cái lược",
    },
    {
        "q": "Bạn lấy 2 quả trong 5 quả táo. Bạn có mấy quả?",
        "options": ["2", "3", "5"],
        "answer": "2",
    },
    {
        "q": "Cái gì càng lau càng ướt?",
        "options": ["Cái khăn", "Cái bàn", "Cái ghế"],
        "answer": "Cái khăn",
    },
    {
        "q": "Cái gì luôn đến nhưng không bao giờ là hôm nay?",
        "options": ["Ngày mai", "Hôm qua", "Buổi sáng"],
        "answer": "Ngày mai",
    },
    {
        "q": "Có 3 con mèo bắt 3 con chuột trong 3 phút. 100 con mèo bắt 100 con chuột trong bao lâu?",
        "options": ["3 phút", "100 phút", "30 phút"],
        "answer": "3 phút",
    },
    {
        "q": "Cái gì có nhiều phím nhưng không mở được cửa?",
        "options": ["Đàn piano", "Chùm chìa khóa", "Cánh cửa"],
        "answer": "Đàn piano",
    },
]

# ==================== KHUNG GAME ====================

st.markdown(
    '<div class="game-title">🛸 UFO HACK NÃO 👽</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="game-subtitle">'
    'THỬ THÁCH TRÍ TUỆ · UFO BẮT CÓC · SINH TỒN NGOÀI HÀNH TINH'
    '</div>',
    unsafe_allow_html=True,
)

alive = [p for p in players if p["alive"]]
captured_count = len(players) - len(alive)

stat_cols = st.columns(4)

for col, (number, label) in zip(
    stat_cols,
    [
        (len(players), "👥 NGƯỜI CHƠI"),
        (len(alive), "🟢 CÒN LẠI"),
        (captured_count, "🛸 ĐÃ BẮT"),
        (st.session_state.score, "🏆 ĐIỂM"),
    ],
):
    with col:
        st.markdown(
            f'<div class="stat-box">'
            f'<div class="stat-number">{number}</div>{label}</div>',
            unsafe_allow_html=True,
        )

left, right = st.columns([1.7, 1], gap="medium")

# ==================== SÂN CHƠI UFO ====================

with left:
    st.markdown("### 🌌 SÂN CHƠI UFO")

    crowd = []

    for i, player in enumerate(players):
        if not player["alive"]:
            continue

        row = i // 10
        col = i % 10

        x = 5 + col * 10 + random.uniform(-1, 1)
        y = 4 + row * 7.5
        name = html.escape(player["name"], quote=True)

        crowd.append(f"""
        <div class="person"
             style="left:{x:.1f}%;bottom:{y:.1f}%"
             title="{name}">
            <div class="head"><span class="eyes">••</span></div>
            <div class="arms"><i></i><i></i></div>
            <div class="body"></div>
            <div class="legs"><i></i><i></i></div>
            <div class="person-name">{name}</div>
        </div>
        """)

    victim = next(
        (
            p for p in players
            if p["id"] == st.session_state.victim_id
        ),
        None,
    )

    victim_html = ""

    if victim:
        victim_name = html.escape(victim["name"], quote=True)
        victim_html = f"""
        <div class="beam"></div>
        <div class="abducted">
            <div class="head big-head"><span class="eyes">••</span></div>
            <div class="body big-body"></div>
            <div class="person-name">{victim_name}</div>
        </div>
        """

    scene = r"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <style>
    * {box-sizing:border-box}
    body {margin:0;background:#050817;font-family:Arial;color:white}
    .scene {
        position:relative;height:440px;overflow:hidden;
        border:2px solid #b8860b;border-radius:14px;
        background:
        radial-gradient(circle at 15% 15%,#fff 1px,transparent 2px),
        radial-gradient(circle at 80% 25%,#fff 1px,transparent 2px),
        linear-gradient(#101b3b,#07101f 78%,#164451);
        background-size:70px 70px,100px 100px,auto;
    }
    .ufo {
        position:absolute;z-index:100;top:15px;left:50%;
        width:140px;height:75px;transform:translateX(-50%);
        animation:hover 3s ease-in-out infinite;
    }
    .dome {
        position:absolute;left:45px;top:0;width:50px;height:36px;
        border:3px solid #fde68a;border-radius:50% 50% 20% 20%;
        background:linear-gradient(130deg,#fef3c7,#a78bfa);
        box-shadow:0 0 18px #facc15;
    }
    .disk {
        position:absolute;top:26px;width:140px;height:38px;
        border:3px solid #facc15;border-radius:50%;
        background:linear-gradient(#fef3c7,#a16207,#272653);
        box-shadow:0 0 20px #facc15;
    }
    .lights {
        position:absolute;top:41px;left:15px;width:110px;
        display:flex;justify-content:space-around;
    }
    .lights i {
        width:7px;height:7px;border-radius:50%;
        background:#fff1a8;box-shadow:0 0 8px #facc15;
        animation:blink 1s infinite alternate;
    }
    .person {
        position:absolute;width:10%;height:80px;min-width:28px;
        transform:translateX(-50%);text-align:center;z-index:10;
    }
    .head {
        position:relative;width:27px;height:26px;margin:auto;
        border:2px solid #bbf7d0;border-radius:48%;
        background:linear-gradient(#86efac,#22c55e);
        box-shadow:0 0 7px #4ade80;z-index:2;
    }
    .eyes {
        position:absolute;top:5px;left:5px;width:14px;
        color:#06111c;font-size:12px;font-weight:900;letter-spacing:2px;
    }
    .arms {
        position:absolute;top:29px;left:50%;width:38px;
        transform:translateX(-50%);
        display:flex;justify-content:space-between;
    }
    .arms i {
        display:block;width:7px;height:20px;border-radius:5px;
        background:#a78bfa;border:1px solid #ddd6fe;
    }
    .body {
        position:relative;z-index:2;width:21px;height:26px;
        margin:-1px auto 0;border:2px solid #facc15;
        border-radius:7px;background:linear-gradient(90deg,#7c3aed,#a78bfa,#5b21b6);
    }
    .legs {
        width:17px;height:12px;display:flex;justify-content:space-between;
        margin:-1px auto 0;
    }
    .legs i {
        display:block;width:7px;height:12px;border-radius:3px;
        background:#cbd5e1;
    }
    .person-name {
        position:relative;z-index:5;margin:2px auto 0;
        max-width:80px;overflow:hidden;text-overflow:ellipsis;
        white-space:nowrap;color:#ffe566;background:#07101fee;
        border:1px solid #b8860b;border-radius:4px;
        padding:2px;font-size:10px;font-weight:900;
    }
    .beam {
        position:absolute;z-index:50;left:35%;top:55px;width:30%;
        height:350px;pointer-events:none;
        clip-path:polygon(42% 0,58% 0,100% 100%,0 100%);
        background:linear-gradient(to bottom,#fef08a99,#facc1533,transparent);
        animation:blink .7s infinite alternate;
    }
    .abducted {
        position:absolute;z-index:80;top:55px;left:50%;
        width:100px;text-align:center;transform:translateX(-50%);
        animation:abduct 3s ease-in-out forwards;
    }
    .big-head {width:34px;height:33px}
    .big-body {width:28px;height:34px}
    .ground {
        position:absolute;bottom:0;width:100%;height:10px;
        background:#164e63;border-top:2px solid #facc15;
    }
    @keyframes hover {50%{margin-top:-7px}}
    @keyframes blink {from{opacity:.4}to{opacity:1}}
    @keyframes abduct {
        0% {top:330px;opacity:0;transform:translateX(-50%) scale(.8)}
        15% {opacity:1}
        75% {top:100px;opacity:1;transform:translateX(-50%) scale(1)}
        100% {top:35px;opacity:0;transform:translateX(-50%) scale(.5)}
    }
    @media(max-width:600px) {
        .scene {height:380px}
        .person {height:65px}
        .head {width:22px;height:22px}
        .eyes {top:4px;left:3px;font-size:10px}
        .body {width:18px;height:22px}
        .arms {top:25px;width:32px}
        .arms i {height:16px}
        .legs i {height:10px}
        .person-name {font-size:8px;max-width:52px}
    }
    </style>
    </head>
    <body>
    <div class="scene">
        <div class="ufo">
            <div class="dome"></div>
            <div class="disk"></div>
            <div class="lights"><i></i><i></i><i></i><i></i><i></i></div>
        </div>
        __CROWD__
        __VICTIM__
        <div class="ground"></div>
    </div>
    </body>
    </html>
    """

    scene = scene.replace("__CROWD__", "".join(crowd))
    scene = scene.replace("__VICTIM__", victim_html)

    components.html(scene, height=450, scrolling=False)

    if st.button("🚨 UFO BẮT NGƯỜI NGẪU NHIÊN", type="primary"):
        candidates = [p for p in players if p["alive"]]

        if candidates:
            target = random.choice(candidates)
            target["alive"] = False
            st.session_state.victim_id = target["id"]
            st.session_state.notice = f"🛸 UFO đã bắt {target['name']}!"
        else:
            st.session_state.notice = "Tất cả người chơi đã bị bắt!"

        st.rerun()

    st.info(st.session_state.notice)

# ==================== CÂU ĐỐ VÀ QUẢN LÝ ====================

with right:
    st.markdown("### 🧠 CÂU ĐỐ HACK NÃO")

    riddle = riddles[(st.session_state.round - 1) % len(riddles)]

    st.caption(f"CÂU SỐ {st.session_state.round}")
    st.markdown(f"**{riddle['q']}**")

    answer_key = f"answer_{st.session_state.round}"

    selected_answer = st.radio(
        "CHỌN ĐÁP ÁN:",
        riddle["options"],
        key=answer_key,
    )

    if st.button("✅ KIỂM TRA ĐÁP ÁN"):
        if st.session_state.round in st.session_state.answered:
            st.warning("Bạn đã trả lời câu này rồi.")
        else:
            st.session_state.answered.append(st.session_state.round)

            if selected_answer == riddle["answer"]:
                st.session_state.score += 1
                st.success("🎉 CHÍNH XÁC!")
            else:
                st.error(f"ĐÁP ÁN ĐÚNG: {riddle['answer']}")

    if st.button("➡️ CÂU TIẾP THEO"):
        st.session_state.round += 1
        st.rerun()

    st.markdown("---")
    st.markdown("### 👥 QUẢN LÝ NGƯỜI CHƠI")

    if st.button("➕ THÊM 10 NGƯỜI"):
        amount = min(10, 100 - len(players))
        next_id = max((p["id"] for p in players), default=-1) + 1

        for i in range(amount):
            players.append({
                "id": next_id + i,
                "name": f"Người {next_id+i+1}",
                "alive": True,
            })

        if amount == 0:
            st.warning("Đã đạt giới hạn 100 người chơi.")
        else:
            st.rerun()

    selected_id = st.selectbox(
        "CHỌN NHÂN VẬT ĐỂ ĐỔI TÊN",
        [p["id"] for p in players],
        format_func=lambda pid: next(
            f"{p['name']} (ID {pid})"
            for p in players if p["id"] == pid
        ),
    )

    new_name = st.text_input("TÊN NHÂN VẬT MỚI", max_chars=24)

    if st.button("✏️ LƯU TÊN"):
        if new_name.strip():
            target = next(p for p in players if p["id"] == selected_id)
            target["name"] = new_name.strip()
            st.rerun()
        else:
            st.warning("Hãy nhập tên trước nhé.")

    st.markdown("---")
    st.markdown("### 🔊 NHẠC UFO")

    volume = st.slider(
        "ÂM LƯỢNG",
        min_value=0.0,
        max_value=0.6,
        value=0.2,
        step=0.05,
    )

    # Khung nhạc riêng để trình duyệt cho phép bấm phát âm thanh.
    music_html = r"""
    <html><body style="margin:0;background:#101a32;color:#FFD700;text-align:center;font-family:Arial;padding:8px">
    <button id="play" style="padding:10px;background:#493b0b;color:#FFD700;border:1px solid #FFD700;border-radius:8px;font-weight:bold">▶ PHÁT NHẠC</button>
    <button id="stop" style="padding:10px;background:#17213d;color:#FFD700;border:1px solid #FFD700;border-radius:8px;font-weight:bold">■ DỪNG NHẠC</button>
    <script>
    let ctx=null, timer=null;
    function stopMusic(){
      if(timer!==null){clearInterval(timer);timer=null;}
      if(ctx){ctx.close().catch(()=>{});ctx=null;}
    }
    async function playMusic(){
      stopMusic();
      const AC=window.AudioContext||window.webkitAudioContext;
      if(!AC){alert("Trình duyệt không hỗ trợ âm thanh");return;}
      ctx=new AC();
      if(ctx.state==="suspended")await ctx.resume();
      const master=ctx.createGain();
      master.gain.value=__VOLUME__;
      master.connect(ctx.destination);
      const drone=ctx.createOscillator();
      const dg=ctx.createGain();
      drone.type="sawtooth";
      drone.frequency.value=48;
      dg.gain.value=.025;
      drone.connect(dg);dg.connect(master);drone.start();
      let n=0;
      timer=setInterval(()=>{
        if(!ctx)return;
        const osc=ctx.createOscillator();
        const gain=ctx.createGain();
        osc.type="triangle";
        osc.frequency.value=n%2?65:82;
        gain.gain.setValueAtTime(.001,ctx.currentTime);
        gain.gain.linearRampToValueAtTime(.035,ctx.currentTime+.05);
        gain.gain.linearRampToValueAtTime(.001,ctx.currentTime+.3);
        osc.connect(gain);gain.connect(master);
        osc.start();osc.stop(ctx.currentTime+.35);n++;
      },600);
    }
    document.getElementById("play").onclick=playMusic;
    document.getElementById("stop").onclick=stopMusic;
    </script>
    </body></html>
    """

    music_html = music_html.replace("__VOLUME__", str(float(volume)))
    components.html(music_html, height=65, scrolling=False)

    st.caption("Nếu chưa nghe thấy nhạc, hãy bấm PHÁT NHẠC. Nên giữ âm lượng vừa phải.")

    if st.button("🔄 CHƠI LẠI TỪ ĐẦU"):
        for player in players:
            player["alive"] = True

        st.session_state.victim_id = None
        st.session_state.round = 1
        st.session_state.score = 0
        st.session_state.answered = []
        st.session_state.notice = "🛸 UFO đã quay lại!"
        st.rerun()

    with st.expander("📋 DANH SÁCH NGƯỜI CHƠI"):
        for player in players:
            status = "🛸 ĐÃ BỊ BẮT" if not player["alive"] else "🟢 CÒN LẠI"
            st.markdown(
                f"**{player['name']}** — {status}"
            )

st.markdown(
    '<div style="text-align:center;color:#FFD700;font-weight:900;'
    'padding:10px">🛸 UFO HACK NÃO · CHÚC BẠN CHƠI VUI! 👽</div>',
    unsafe_allow_html=True,
)
