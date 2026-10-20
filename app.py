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

# ==================== GIAO DIỆN ====================

st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden;}

.stApp {
    background:linear-gradient(145deg,#070b1c,#101c3d,#030611);
    color:#ffffff;
}
.block-container {
    max-width:1500px;
    padding:10px 12px 25px;
}
.game-box {
    background:linear-gradient(145deg,#121d3d,#080d20);
    border:2px solid #475e9b;
    border-radius:18px;
    padding:14px;
    box-shadow:0 0 22px #312e8144;
}
.game-title {
    text-align:center;
    font-size:clamp(28px,4vw,44px);
    font-weight:900;
    color:#a5f3fc;
    text-shadow:0 0 14px #06b6d4;
}
.game-subtitle {
    text-align:center;
    font-size:14px;
    color:#ddd6fe;
    margin-bottom:12px;
}
.stat-box {
    text-align:center;
    background:#111c38;
    border:1px solid #53669a;
    border-radius:10px;
    padding:8px 3px;
    color:white;
    font-size:13px;
}
.stat-number {
    color:#67e8f9;
    font-size:23px;
    font-weight:900;
}
.stButton button {
    width:100%;
    min-height:40px;
    font-weight:800;
    border-radius:9px;
}
div[data-testid="stVerticalBlock"] {
    gap:.5rem;
}
@media(max-width:600px) {
    .block-container {padding:4px;}
    .game-box {padding:7px;}
    .stat-box {font-size:10px;}
    .stat-number {font-size:19px;}
}
</style>
""", unsafe_allow_html=True)

# ==================== TRẠNG THÁI GAME ====================

if "players" not in st.session_state:
    st.session_state.players = [
        {"id": i, "name": f"Người {i+1}", "alive": True}
        for i in range(20)
    ]

if "score" not in st.session_state:
    st.session_state.score = 0

if "round" not in st.session_state:
    st.session_state.round = 1

if "answered" not in st.session_state:
    st.session_state.answered = []

if "victim_id" not in st.session_state:
    st.session_state.victim_id = None

if "notice" not in st.session_state:
    st.session_state.notice = "🛸 UFO đang bay quanh Trái Đất!"

if "music_on" not in st.session_state:
    st.session_state.music_on = False

for i, player in enumerate(st.session_state.players):
    player.setdefault("id", i)
    player.setdefault("name", f"Người {i+1}")
    player.setdefault("alive", True)

players = st.session_state.players

# ==================== MỘT KHUNG GAME ====================

st.markdown('<div class="game-box">', unsafe_allow_html=True)

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

stats = [
    (len(players), "👥 Người chơi"),
    (len(alive), "🟢 Còn lại"),
    (captured_count, "🛸 Đã bắt"),
    (st.session_state.score, "🏆 Điểm"),
]

for col, (number, label) in zip(stat_cols, stats):
    with col:
        st.markdown(
            f'<div class="stat-box">'
            f'<div class="stat-number">{number}</div>{label}</div>',
            unsafe_allow_html=True,
        )

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
        "q": "Bạn vượt qua người đứng thứ hai. Bạn đứng thứ mấy?",
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
]

# ==================== CHIA KHU VỰC ====================

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

        x = 5 + col * 10 + random.uniform(-1.2, 1.2)
        y = 4 + row * 7.5
        name = html.escape(player["name"])

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
        victim_html = f"""
        <div class="beam"></div>
        <div class="abducted">
            <div class="head big-head"><span class="eyes">••</span></div>
            <div class="body big-body"></div>
            <div class="person-name">{html.escape(victim["name"])}</div>
        </div>
        """

    scene_start = r"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    * {box-sizing:border-box}
    body {margin:0;background:#050817;font-family:Arial;color:white}
    .scene {
        position:relative;width:100%;height:440px;overflow:hidden;
        border:2px solid #52669a;border-radius:14px;
        background:
        radial-gradient(circle at 15% 15%,white 1px,transparent 2px),
        radial-gradient(circle at 80% 25%,white 1px,transparent 2px),
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
        border:3px solid #a5f3fc;border-radius:50% 50% 20% 20%;
        background:linear-gradient(130deg,#dbeafe,#6366f1);
        box-shadow:0 0 18px #22d3ee;
    }
    .disk {
        position:absolute;top:26px;width:140px;height:38px;
        border:3px solid #c4b5fd;border-radius:50%;
        background:linear-gradient(#c7d2fe,#6366f1,#272653);
        box-shadow:0 0 20px #818cf8;
    }
    .lights {
        position:absolute;top:41px;left:15px;width:110px;
        display:flex;justify-content:space-around;
    }
    .lights i {
        width:7px;height:7px;border-radius:50%;
        background:#a5f3fc;box-shadow:0 0 8px #22d3ee;
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
        color:#06111c;font-size:12px;font-weight:900;
        letter-spacing:2px;
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
        margin:-1px auto 0;border:2px solid #c4b5fd;
        border-radius:7px;background:linear-gradient(90deg,#7c3aed,#a78bfa,#5b21b6);
    }
    .legs {
        width:17px;height:12px;display:flex;justify-content:space-between;
        margin:-1px auto 0;
    }
    .legs i {
        display:block;width:7px;height:12px;border-radius:3px;
        background:#64748b;
    }
    .person-name {
        position:relative;z-index:5;margin:2px auto 0;
        max-width:80px;overflow:hidden;text-overflow:ellipsis;
        white-space:nowrap;color:#fff;background:#07101fee;
        border:1px solid #5269a4;border-radius:4px;
        padding:2px;font-size:10px;font-weight:bold;
    }
    .beam {
        position:absolute;z-index:50;left:35%;top:55px;width:30%;
        height:350px;pointer-events:none;
        clip-path:polygon(42% 0,58% 0,100% 100%,0 100%);
        background:linear-gradient(to bottom,#a5f3fc99,#67e8f944,transparent);
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
        background:#164e63;border-top:2px solid #22d3ee;
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
    <body><div class="scene">
    <div class="ufo">
        <div class="dome"></div><div class="disk"></div>
        <div class="lights"><i></i><i></i><i></i><i></i><i></i></div>
    </div>
    __CROWD__
    __VICTIM__
    <div class="ground"></div>
    </div></body></html>
    """

    scene = scene_start.replace(
        "__CROWD__", "".join(crowd)
    ).replace(
        "__VICTIM__", victim_html
    )

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

# ==================== CÂU ĐỐ VÀ ĐIỀU KHIỂN ====================

with right:
    st.markdown("### 🧠 CÂU ĐỐ HACK NÃO")

    riddle = riddles[(st.session_state.round - 1) % len(riddles)]

    st.caption(f"Câu số {st.session_state.round}")
    st.markdown(f"**{riddle['q']}**")

    selected_answer = st.radio(
        "Chọn đáp án:",
        riddle["options"],
        key=f"answer_{st.session_state.round}",
    )

    if st.button("✅ KIỂM TRA ĐÁP ÁN"):
        if st.session_state.round in st.session_state.answered:
            st.warning("Bạn đã trả lời câu này rồi.")
        else:
            st.session_state.answered.append(st.session_state.round)

            if selected_answer == riddle["answer"]:
                st.session_state.score += 1
                st.success("🎉 Chính xác!")
            else:
                st.error(f"Đáp án đúng: {riddle['answer']}")

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

        st.rerun()

    ids = [p["id"] for p in players]

    selected_id = st.selectbox(
        "Chọn nhân vật để đổi tên",
        ids,
        format_func=lambda pid: next(
            f"{p['name']} (ID {pid})"
            for p in players if p["id"] == pid
        ),
    )

    new_name = st.text_input("Tên nhân vật mới", max_chars=24)

    if st.button("✏️ LƯU TÊN"):
        if new_name.strip():
            target = next(p for p in players if p["id"] == selected_id)
            target["name"] = new_name.strip()
            st.rerun()
        else:
            st.warning("Hãy nhập tên trước nhé.")

    st.markdown("---")
    st.markdown("### 🔊 NHẠC NỀN")

    music_volume = st.slider(
        "Âm lượng nhạc",
        0.0,
        0.6,
        0.2,
        0.05,
    )

    music_html = r"""
    <html><body style="margin:0;background:#111c38;color:white;text-align:center;font-family:Arial;padding:8px">
    <button id="play" style="padding:10px;background:#7c3aed;color:white;border:0;border-radius:8px;font-weight:bold">▶ PHÁT NHẠC</button>
    <button id="stop" style="padding:10px;background:#475569;color:white;border:0;border-radius:8px;font-weight:bold">■ DỪNG</button>
    <script>
    let ctx=null, timer=null;
    function stopMusic(){
      if(timer)clearInterval(timer);
      timer=null;
      if(ctx){ctx.close().catch(()=>{});ctx=null;}
    }
    function playMusic(){
      stopMusic();
      const AC=window.AudioContext||window.webkitAudioContext;
      if(!AC){alert("Trình duyệt không hỗ trợ âm thanh");return;}
      ctx=new AC();
      const master=ctx.createGain();
      master.gain.value=__VOLUME__;
      master.connect(ctx.destination);
      const drone=ctx.createOscillator();
      const dg=ctx.createGain();
      drone.type="sawtooth";
      drone.frequency.value=48;
      dg.gain.value=.035;
      drone.connect(dg);dg.connect(master);drone.start();
      let n=0;
      timer=setInterval(()=>{
        if(!ctx)return;
        const osc=ctx.createOscillator();
        const gain=ctx.createGain();
        osc.type="triangle";
        osc.frequency.value=n%2?65:82;
        gain.gain.setValueAtTime(.001,ctx.currentTime);
        gain.gain.linearRampToValueAtTime(.05,ctx.currentTime+.05);
        gain.gain.linearRampToValueAtTime(.001,ctx.currentTime+.3);
        osc.connect(gain);gain.connect(master);
        osc.start();osc.stop(ctx.currentTime+.35);n++;
      },600);
    }
    document.getElementById("play").onclick=playMusic;
    document.getElementById("stop").onclick=stopMusic;
    </script></body></html>
    """

    music_html = music_html.replace(
        "__VOLUME__", str(float(music_volume))
    )

    components.html(music_html, height=65, scrolling=False)

    if st.button("🔄 CHƠI LẠI TỪ ĐẦU"):
        for player in players:
            player["alive"] = True

        st.session_state.victim_id = None
        st.session_state.round = 1
        st.session_state.score = 0
        st.session_state.answered = []
        st.session_state.notice = "🛸 UFO đã quay lại!"
        st.rerun()

    with st.expander("📋 XEM DANH SÁCH NGƯỜI CHƠI"):
        for p in players:
            status = "🛸 Đã bị bắt" if not p["alive"] else "🟢 Còn lại"
            st.write(f"**{p['name']}** — {status}")

st.markdown("</div>", unsafe_allow_html=True)
