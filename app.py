import html
import random
import streamlit as st
import streamlit.components.v1 as components

# ==================================================
# CẤU HÌNH
# ==================================================

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide",
)

# ==================================================
# GIAO DIỆN
# ==================================================

st.markdown("""
<style>
.stApp {
    background: radial-gradient(ellipse at top, #172650, #080d20 60%, #02040b);
    color: white;
}
.block-container {
    max-width: 1400px;
    padding-top: 1.2rem;
}
h1, h2, h3, p, label {
    color: white !important;
}
.hero {
    text-align: center;
    font-size: clamp(32px, 5vw, 58px);
    font-weight: 1000;
    color: #a5f3fc;
    text-shadow: 0 0 14px #06b6d4, 0 0 30px #7c3aed;
}
.subtitle {
    text-align: center;
    color: #c4b5fd;
    margin-bottom: 24px;
}
.card {
    background: rgba(17, 24, 55, .95);
    border: 1px solid #46558a;
    border-radius: 14px;
    padding: 15px;
    margin: 10px 0;
}
.stat {
    text-align: center;
    background: #111a35;
    border: 1px solid #475569;
    border-radius: 12px;
    padding: 12px 5px;
}
.number {
    color: #67e8f9;
    font-size: 27px;
    font-weight: 900;
}
div.stButton > button {
    width: 100%;
    min-height: 43px;
    border-radius: 10px;
    font-weight: bold;
}
@media(max-width:600px) {
    .block-container {
        padding-left: 10px;
        padding-right: 10px;
    }
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# KHỞI TẠO TRẠNG THÁI
# ==================================================

if "players" not in st.session_state:
    st.session_state.players = [
        {"id": i, "name": f"Người {i + 1}", "alive": True}
        for i in range(20)
    ]

if "round" not in st.session_state:
    st.session_state.round = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = []

if "message" not in st.session_state:
    st.session_state.message = "🛸 UFO đang bay quanh Trái Đất!"

if "victim_id" not in st.session_state:
    st.session_state.victim_id = None

if "abduction_event" not in st.session_state:
    st.session_state.abduction_event = 0

# Chuẩn hóa dữ liệu người chơi cũ để tránh lỗi thiếu khóa.
for i, player in enumerate(st.session_state.players):
    player.setdefault("id", i)
    player.setdefault("name", f"Người {i + 1}")
    player.setdefault("alive", True)

# ==================================================
# TIÊU ĐỀ
# ==================================================

st.markdown(
    '<div class="hero">🛸 UFO HACK NÃO 👽</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">THỬ THÁCH TRÍ TUỆ · UFO BẮT CÓC · SINH TỒN NGOÀI HÀNH TINH</div>',
    unsafe_allow_html=True,
)

# ==================================================
# NHẠC UFO
# ==================================================

st.markdown("## 🔊 NHẠC UFO")

volume = st.slider(
    "Âm lượng",
    min_value=0.0,
    max_value=0.6,
    value=0.2,
    step=0.05,
)

music_html = r"""
<!DOCTYPE html>
<html>
<body style="margin:0;background:#111a35;color:white;font-family:Arial">
<div style="padding:12px;text-align:center;border-radius:12px">
    <button id="play" style="padding:12px;background:#7c3aed;color:white;border:0;border-radius:8px;font-weight:bold">
        ▶️ PHÁT NHẠC
    </button>
    <button id="stop" style="padding:12px;background:#475569;color:white;border:0;border-radius:8px;font-weight:bold">
        ⏹ DỪNG NHẠC
    </button>
    <div style="font-size:12px;margin-top:8px;color:#cbd5e1">
        Bấm phát để nghe nhạc điện tử ngoài hành tinh.
    </div>
</div>
<script>
(() => {
    let ctx = null;
    let timer = null;

    function stopMusic() {
        if (timer !== null) {
            clearInterval(timer);
            timer = null;
        }
        if (ctx !== null) {
            ctx.close().catch(() => {});
            ctx = null;
        }
    }

    function playMusic() {
        stopMusic();

        const AC = window.AudioContext || window.webkitAudioContext;
        if (!AC) {
            alert("Trình duyệt không hỗ trợ âm thanh.");
            return;
        }

        ctx = new AC();
        const master = ctx.createGain();
        master.gain.value = __VOLUME__;
        master.connect(ctx.destination);

        const drone = ctx.createOscillator();
        const droneGain = ctx.createGain();
        drone.type = "sawtooth";
        drone.frequency.value = 48;
        droneGain.gain.value = 0.045;
        drone.connect(droneGain);
        droneGain.connect(master);
        drone.start();

        let count = 0;
        timer = setInterval(() => {
            if (!ctx) return;

            const osc = ctx.createOscillator();
            const gain = ctx.createGain();

            osc.type = "triangle";
            osc.frequency.value = count % 2 === 0 ? 82 : 65;

            gain.gain.setValueAtTime(0.001, ctx.currentTime);
            gain.gain.linearRampToValueAtTime(0.06, ctx.currentTime + 0.05);
            gain.gain.linearRampToValueAtTime(0.001, ctx.currentTime + 0.35);

            osc.connect(gain);
            gain.connect(master);
            osc.start();
            osc.stop(ctx.currentTime + 0.4);
            count++;
        }, 600);
    }

    document.getElementById("play").onclick = playMusic;
    document.getElementById("stop").onclick = stopMusic;
})();
</script>
</body>
</html>
"""

music_html = music_html.replace("__VOLUME__", str(float(volume)))

components.html(music_html, height=105, scrolling=False)

st.caption("Nhạc chạy trong khung riêng. Bấm PHÁT NHẠC để bắt đầu; hãy giữ âm lượng ở mức dễ chịu.")

# ==================================================
# QUẢN LÝ NGƯỜI CHƠI
# ==================================================

st.markdown("## 👥 QUẢN LÝ NGƯỜI CHƠI")
st.write(f"Số người chơi: **{len(st.session_state.players)}/100**")

if st.button("➕ THÊM 10 NGƯỜI"):
    players = st.session_state.players
    amount = min(10, 100 - len(players))

    next_id = max((p["id"] for p in players), default=-1) + 1

    for i in range(amount):
        players.append({
            "id": next_id + i,
            "name": f"Người {next_id + i + 1}",
            "alive": True,
        })

    st.session_state.message = (
        f"Đã thêm {amount} người chơi."
        if amount > 0
        else "Đã đủ 100 người chơi!"
    )
    st.rerun()

with st.expander("✏️ ĐỔI TÊN NHÂN VẬT"):
    players = st.session_state.players

    if players:
        player_ids = [p["id"] for p in players]
        player_by_id = {p["id"]: p for p in players}

        selected_id = st.selectbox(
            "Chọn nhân vật",
            player_ids,
            format_func=lambda pid: (
                f"{player_by_id[pid]['name']} (ID {pid})"
            ),
        )

        new_name = st.text_input("Nhập tên mới", max_chars=24)

        if st.button("💾 LƯU TÊN MỚI"):
            cleaned_name = new_name.strip()

            if not cleaned_name:
                st.warning("Bạn hãy nhập tên trước khi lưu.")
            else:
                player_by_id[selected_id]["name"] = cleaned_name
                st.session_state.message = f"Đã đổi tên thành {cleaned_name}."
                st.rerun()

# ==================================================
# CÂU ĐỐ
# ==================================================

riddles = [
    {
        "q": "Cái gì càng lấy đi thì càng lớn?",
        "options": ["Cái hố", "Ngọn núi", "Cái cây", "Dòng sông"],
        "answer": "Cái hố",
        "explain": "Càng đào đất đi thì cái hố càng lớn.",
    },
    {
        "q": "Tháng nào có 28 ngày?",
        "options": ["Tháng 2", "Tháng 4", "Tất cả các tháng", "Tháng 6"],
        "answer": "Tất cả các tháng",
        "explain": "Tất cả các tháng đều có ít nhất 28 ngày.",
    },
    {
        "q": "Cái gì có cổ nhưng không có đầu?",
        "options": ["Cái chai", "Con hươu", "Cái bàn", "Cái quạt"],
        "answer": "Cái chai",
        "explain": "Cái chai có cổ chai.",
    },
    {
        "q": "Bạn vượt qua người đứng thứ hai. Bạn đứng thứ mấy?",
        "options": ["Thứ nhất", "Thứ hai", "Thứ ba", "Thứ tư"],
        "answer": "Thứ hai",
        "explain": "Bạn chiếm vị trí của người đứng thứ hai.",
    },
    {
        "q": "Cái gì có nhiều răng nhưng không cắn được?",
        "options": ["Cá mập", "Cái lược", "Cá sấu", "Con mèo"],
        "answer": "Cái lược",
        "explain": "Cái lược có răng lược.",
    },
    {
        "q": "Có 5 quả táo, bạn lấy 2 quả. Bạn có mấy quả?",
        "options": ["2", "3", "5", "7"],
        "answer": "2",
        "explain": "Bạn lấy 2 quả nên bạn có 2 quả.",
    },
    {
        "q": "Cái gì càng lau càng ướt?",
        "options": ["Cái khăn", "Cái bàn", "Cái ghế", "Quyển sách"],
        "answer": "Cái khăn",
        "explain": "Khăn thấm nước khi lau.",
    },
    {
        "q": "Cái gì luôn đến nhưng không bao giờ là hôm nay?",
        "options": ["Ngày mai", "Hôm qua", "Buổi sáng", "Mặt trời"],
        "answer": "Ngày mai",
        "explain": "Ngày mai đến thì lại trở thành hôm nay.",
    },
    {
        "q": "Một tuần có bao nhiêu ngày?",
        "options": ["5", "6", "7", "8"],
        "answer": "7",
        "explain": "Một tuần có 7 ngày.",
    },
    {
        "q": "Cái gì có mặt nhưng không có mũi, miệng?",
        "options": ["Đồng hồ", "Cái ghế", "Cái bàn", "Cái bút"],
        "answer": "Đồng hồ",
        "explain": "Đồng hồ có mặt đồng hồ.",
    },
]

st.markdown("## 🧠 THỬ THÁCH HACK NÃO")

round_no = st.session_state.round
riddle = riddles[(round_no - 1) % len(riddles)]

st.markdown(
    '<div class="card"><b>CÂU ĐỐ SỐ '
    + str(round_no)
    + "</b><h3>"
    + html.escape(riddle["q"])
    + "</h3></div>",
    unsafe_allow_html=True,
)

answer = st.radio(
    "Chọn đáp án:",
    riddle["options"],
    key=f"answer_{round_no}",
)

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ KIỂM TRA ĐÁP ÁN"):
        if round_no in st.session_state.answered:
            st.info("Bạn đã trả lời câu này rồi.")
        elif answer == riddle["answer"]:
            st.session_state.score += 1
            st.session_state.answered.append(round_no)
            st.success("🎉 Chính xác! " + riddle["explain"])
        else:
            st.session_state.answered.append(round_no)
            st.error("Chưa đúng! Đáp án là: " + riddle["answer"])

with col2:
    if st.button("➡️ CÂU TIẾP THEO"):
        st.session_state.round += 1
        st.rerun()

st.write(f"🏆 Điểm số: **{st.session_state.score}**")

# ==================================================
# UFO BẮT CÓC
# ==================================================

st.markdown("## 🛸 UFO ĐANG SĂN NGƯỜI")

players = st.session_state.players
alive_players = [p for p in players if p["alive"]]
captured_count = len(players) - len(alive_players)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        f'<div class="stat"><div class="number">{len(players)}</div>Tổng người</div>',
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f'<div class="stat"><div class="number">{len(alive_players)}</div>Còn trên mặt đất</div>',
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f'<div class="stat"><div class="number">{captured_count}</div>Đã bị bắt</div>',
        unsafe_allow_html=True,
    )

if st.button("🚨 CHO UFO BẮT NGẪU NHIÊN", type="primary"):
    alive_players = [
        p for p in st.session_state.players if p["alive"]
    ]

    if alive_players:
        victim = random.choice(alive_players)
        victim["alive"] = False
        st.session_state.victim_id = victim["id"]
        st.session_state.abduction_event += 1
        st.session_state.message = f"🚨 UFO đã bắt {victim['name']}!"
    else:
        st.session_state.message = "Tất cả người chơi đã bị bắt. Hãy chơi lại!"

    st.rerun()

if st.button("🔄 CHƠI LẠI TỪ ĐẦU"):
    for player in st.session_state.players:
        player["alive"] = True

    st.session_state.victim_id = None
    st.session_state.round = 1
    st.session_state.score = 0
    st.session_state.answered = []
    st.session_state.abduction_event += 1
    st.session_state.message = "UFO đã quay lại!"

    st.rerun()

st.markdown(
    '<div class="card" style="text-align:center;font-size:20px">'
    + html.escape(st.session_state.message)
    + "</div>",
    unsafe_allow_html=True,
)

# ==================================================
# CẢNH UFO - KHÔNG DÙNG .format() CHO CSS
# ==================================================

st.markdown("## 🌌 CẢNH UFO BẮT CÓC")

crowd_parts = []

for index, player in enumerate(st.session_state.players):
    if not player["alive"]:
        continue

    row = index // 10
    col = index % 10

    left = 5 + col * 10 + random.uniform(-2, 2)
    bottom = 7 + row * 7

    safe_name = html.escape(player["name"])

    person_html = f"""
    <div class="person"
         style="left:{left:.2f}%;bottom:{bottom:.2f}%;z-index:{10 + row}"
         title="{safe_name}">
        <div class="head">👽</div>
        <div class="body"></div>
        <div class="name">{safe_name}</div>
    </div>
    """

    crowd_parts.append(person_html)

crowd_html = "".join(crowd_parts)

captured_html = ""

if st.session_state.victim_id is not None:
    victim = next(
        (
            p for p in st.session_state.players
            if p["id"] == st.session_state.victim_id
        ),
        None,
    )

    if victim is not None:
        safe_victim_name = html.escape(victim["name"])
        captured_html = f"""
        <div class="captured">
            <div class="beam"></div>
            <div class="alien">👽</div>
            <div class="captured-name">{safe_victim_name}</div>
        </div>
        """

scene_start = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    overflow: hidden;
    font-family: Arial, sans-serif;
    background: #02040d;
    color: white;
}
.scene {
    position: relative;
    width: 100%;
    height: 560px;
    overflow: hidden;
    border: 1px solid #52639c;
    border-radius: 16px;
    background:
        radial-gradient(circle at 12% 13%, white 1px, transparent 2px),
        radial-gradient(circle at 78% 19%, white 1px, transparent 2px),
        radial-gradient(ellipse at bottom, #123847, #071326 50%, #02040d);
    background-size: 100px 100px, 140px 120px, auto;
}
.ufo {
    position: absolute;
    top: 25px;
    left: 50%;
    width: 170px;
    height: 100px;
    transform: translateX(-50%);
    z-index: 100;
    animation: hover 2s ease-in-out infinite;
}
.dome {
    position: absolute;
    top: 0;
    left: 55px;
    width: 60px;
    height: 40px;
    border: 2px solid #a5f3fc;
    border-radius: 50% 50% 20% 20%;
    background: linear-gradient(120deg, #dbeafe, #6877dc, #272a65);
    box-shadow: 0 0 22px #22d3ee;
}
.disk {
    position: absolute;
    top: 30px;
    width: 170px;
    height: 42px;
    border-radius: 50%;
    border: 3px solid #c4b5fd;
    background: linear-gradient(#b5c8ff, #626bd7 50%, #20264c);
    box-shadow: 0 0 22px #818cf8;
}
.lights {
    position: absolute;
    top: 49px;
    left: 17px;
    width: 136px;
    display: flex;
    justify-content: space-around;
}
.lights span {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #a5f3fc;
    box-shadow: 0 0 12px #22d3ee;
    animation: blink .5s infinite alternate;
}
.person {
    position: absolute;
    width: 10%;
    max-width: 55px;
    min-width: 25px;
    height: 55px;
    text-align: center;
    transform: translateX(-50%);
}
.head {
    font-size: clamp(17px, 3vw, 27px);
    line-height: 27px;
    filter: drop-shadow(0 0 5px #67e8f9);
}
.body {
    width: 13px;
    height: 19px;
    margin: auto;
    border-radius: 6px;
    border: 1px solid #c4b5fd;
    background: linear-gradient(#8b5cf6, #312e81);
}
.name {
    max-width: 60px;
    margin: auto;
    color: #e0f2fe;
    font-size: 7px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-shadow: 0 0 5px black;
}
.captured {
    position: absolute;
    top: 150px;
    left: 50%;
    width: 120px;
    text-align: center;
    transform: translateX(-50%);
    z-index: 90;
    animation: abduct 3.5s ease-in-out forwards;
}
.beam {
    position: absolute;
    top: -40px;
    left: 15px;
    width: 90px;
    height: 300px;
    clip-path: polygon(40% 0, 60% 0, 100% 100%, 0 100%);
    background: linear-gradient(to bottom,
        rgba(103,232,249,.08),
        rgba(103,232,249,.45),
        transparent);
    animation: flash .35s infinite alternate;
}
.alien {
    position: relative;
    z-index: 2;
    font-size: 48px;
    filter: drop-shadow(0 0 15px #67e8f9);
}
.captured-name {
    position: relative;
    z-index: 3;
    padding: 4px;
    border: 1px solid #67e8f9;
    border-radius: 6px;
    background: #071326;
    font-size: 11px;
    overflow-wrap: anywhere;
}
.ground {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 18px;
    background: linear-gradient(#164e63, #07111f);
    border-top: 2px solid #22d3ee;
}
.caption {
    position: absolute;
    bottom: 25px;
    width: 100%;
    z-index: 120;
    text-align: center;
    color: #a5f3fc;
    font-size: 12px;
    font-weight: bold;
    pointer-events: none;
}
@keyframes hover {
    0%, 100% { margin-top: 0; }
    50% { margin-top: -8px; }
}
@keyframes blink {
    from { opacity: .3; }
    to { opacity: 1; }
}
@keyframes flash {
    from { opacity: .4; }
    to { opacity: 1; }
}
@keyframes abduct {
    0% { top: 410px; opacity: 0; transform: translateX(-50%) scale(.65); }
    15% { opacity: 1; }
    75% { top: 175px; opacity: 1; transform: translateX(-50%) scale(1); }
    100% { top: 80px; opacity: 0; transform: translateX(-50%) scale(.4); }
}
@media(max-width: 600px) {
    .scene { height: 520px; }
    .ufo { transform: translateX(-50%) scale(.8); }
    .person { height: 48px; }
    .name { font-size: 6px; max-width: 36px; }
}
</style>
</head>
<body>
<div class="scene">
    <div class="ufo">
        <div class="dome"></div>
        <div class="disk"></div>
        <div class="lights">
            <span></span><span></span><span></span>
            <span></span><span></span><span></span>
        </div>
    </div>
    <div class="main-beam"></div>
"""

scene_end = r"""
    <div class="ground"></div>
    <div class="caption">🛸 UFO ĐANG QUAN SÁT ĐÁM ĐÔNG 👽</div>
</div>
</body>
</html>
"""

# Nối HTML thành từng phần. Không dùng .format() trên CSS.
scene_html = (
    scene_start
    + crowd_html
    + captured_html
    + scene_end
)

components.html(
    scene_html,
    height=580,
    scrolling=False,
)

# ==================================================
# DANH SÁCH NGƯỜI CHƠI
# ==================================================

with st.expander("📋 XEM TẤT CẢ NGƯỜI CHƠI"):
    for player in st.session_state.players:
        status = (
            "🛸 Đã bị bắt"
            if not player["alive"]
            else "🟢 Còn trên mặt đất"
        )
        st.write(
            f"{player['name']} (ID {player['id']}) — {status}"
        )

st.markdown("---")
st.markdown(
    '<div style="text-align:center;color:#94a3b8;font-size:12px">'
    'UFO HACK NÃO · MINI GAME NGOÀI HÀNH TINH'
    '</div>',
    unsafe_allow_html=True,
)
