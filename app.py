import random
import html
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide",
)

# ===================== GIAO DIỆN =====================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #111b3d, #03050d);
    color: white;
}
.block-container {
    max-width: 1350px;
    padding-top: 1.5rem;
}
h1, h2, h3, p, label {
    color: white !important;
}
.hero {
    text-align: center;
    font-size: clamp(32px, 5vw, 56px);
    font-weight: 900;
    color: #67e8f9;
    text-shadow: 0 0 18px #06b6d4;
}
.subtitle {
    text-align: center;
    color: #c4b5fd;
    margin-bottom: 25px;
}
.card {
    background: #111a35;
    border: 1px solid #475569;
    border-radius: 14px;
    padding: 15px;
    margin: 10px 0;
}
.stat {
    text-align: center;
    background: #111a35;
    border: 1px solid #475569;
    border-radius: 12px;
    padding: 12px 4px;
}
.number {
    font-size: 27px;
    color: #67e8f9;
    font-weight: 900;
}
div.stButton > button {
    width: 100%;
    min-height: 43px;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ===================== KHỞI TẠO GAME =====================

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

# ===================== TIÊU ĐỀ =====================

st.markdown(
    '<div class="hero">🛸 UFO HACK NÃO 👽</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="subtitle">'
    'THỬ THÁCH TRÍ TUỆ · UFO BẮT CÓC · SINH TỒN NGOÀI HÀNH TINH'
    '</div>',
    unsafe_allow_html=True,
)

# ===================== NHẠC =====================

st.markdown("## 🔊 NHẠC UFO")

volume = st.slider(
    "Âm lượng",
    min_value=0.0,
    max_value=0.6,
    value=0.2,
    step=0.05,
)

components.html(
    """
    <div style="background:#111a35;padding:12px;border-radius:12px;
                text-align:center;color:white;font-family:Arial">
      <button id="play" style="padding:12px;background:#7c3aed;
        color:white;border:0;border-radius:8px;font-weight:bold">
        ▶️ PHÁT NHẠC
      </button>
      <button id="stop" style="padding:12px;background:#475569;
        color:white;border:0;border-radius:8px;font-weight:bold">
        ⏹ DỪNG NHẠC
      </button>
    </div>
    <script>
    (() => {
      let ctx = null, timer = null, master = null;
      const volume = VOLUME;

      function stop() {
        if (timer) clearInterval(timer);
        timer = null;
        if (ctx) ctx.close().catch(() => {});
        ctx = null;
        master = null;
      }

      function play() {
        stop();
        const AC = window.AudioContext || window.webkitAudioContext;
        if (!AC) {
          alert("Trình duyệt không hỗ trợ âm thanh.");
          return;
        }

        ctx = new AC();
        master = ctx.createGain();
        master.gain.value = volume;
        master.connect(ctx.destination);

        const drone = ctx.createOscillator();
        const droneGain = ctx.createGain();
        drone.type = "sawtooth";
        drone.frequency.value = 48;
        droneGain.gain.value = 0.05;
        drone.connect(droneGain);
        droneGain.connect(master);
        drone.start();

        let count = 0;
        timer = setInterval(() => {
          if (!ctx || !master) return;
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = "triangle";
          osc.frequency.value = count % 2 ? 65 : 82;
          gain.gain.setValueAtTime(0.001, ctx.currentTime);
          gain.gain.linearRampToValueAtTime(0.07, ctx.currentTime + 0.05);
          gain.gain.linearRampToValueAtTime(0.001, ctx.currentTime + 0.35);
          osc.connect(gain);
          gain.connect(master);
          osc.start();
          osc.stop(ctx.currentTime + 0.4);
          count++;
        }, 600);
      }

      document.getElementById("play").onclick = play;
      document.getElementById("stop").onclick = stop;
    })();
    </script>
    """.replace("VOLUME", str(volume)),
    height=85,
)

st.caption("Bấm PHÁT NHẠC để nghe. Hãy giữ âm lượng ở mức dễ chịu.")

# ===================== NGƯỜI CHƠI =====================

st.markdown("## 👥 QUẢN LÝ NGƯỜI CHƠI")

players = st.session_state.players
st.write(f"Số người chơi: **{len(players)}/100**")

if st.button("➕ THÊM 10 NGƯỜI"):
    amount = min(10, 100 - len(st.session_state.players))
    next_id = max(
        (p.get("id", -1) for p in st.session_state.players),
        default=-1,
    ) + 1

    for i in range(amount):
        st.session_state.players.append({
            "id": next_id + i,
            "name": f"Người {next_id + i + 1}",
            "alive": True,
        })

    st.session_state.message = (
        f"Đã thêm {amount} người."
        if amount
        else "Đã đủ 100 người!"
    )
    st.rerun()

with st.expander("✏️ ĐỔI TÊN NHÂN VẬT"):
    players = st.session_state.players

    if players:
        # Dùng ID làm giá trị lựa chọn để tránh lỗi trùng tên.
        ids = [p.get("id", i) for i, p in enumerate(players)]

        selected_id = st.selectbox(
            "Chọn nhân vật",
            ids,
            format_func=lambda pid: next(
                (
                    f"{p.get('name', 'Người chơi')} (ID {pid})"
                    for p in players
                    if p.get("id") == pid
                ),
                f"Người chơi (ID {pid})",
            ),
        )

        new_name = st.text_input("Tên mới", max_chars=24)

        if st.button("💾 LƯU TÊN"):
            cleaned = new_name.strip()

            if not cleaned:
                st.warning("Bạn hãy nhập tên mới.")
            else:
                for p in st.session_state.players:
                    if p.get("id") == selected_id:
                        p["name"] = cleaned
                        break

                st.session_state.message = f"Đã đổi tên thành {cleaned}."
                st.rerun()

# ===================== CÂU ĐỐ =====================

riddles = [
    {
        "q": "Cái gì càng lấy đi thì càng lớn?",
        "options": ["Cái hố", "Cái cây", "Ngọn núi", "Dòng sông"],
        "answer": "Cái hố",
    },
    {
        "q": "Tháng nào có 28 ngày?",
        "options": ["Tháng 2", "Tháng 4", "Tất cả các tháng", "Tháng 6"],
        "answer": "Tất cả các tháng",
    },
    {
        "q": "Cái gì có cổ nhưng không có đầu?",
        "options": ["Cái chai", "Cái bàn", "Con mèo", "Cái ghế"],
        "answer": "Cái chai",
    },
    {
        "q": "Bạn vượt qua người đứng thứ hai. Bạn đứng thứ mấy?",
        "options": ["Thứ nhất", "Thứ hai", "Thứ ba", "Thứ tư"],
        "answer": "Thứ hai",
    },
    {
        "q": "Cái gì có răng nhưng không cắn?",
        "options": ["Cá mập", "Cái lược", "Cá sấu", "Con chó"],
        "answer": "Cái lược",
    },
    {
        "q": "Có 5 quả táo, bạn lấy 2 quả. Bạn có mấy quả?",
        "options": ["2", "3", "5", "7"],
        "answer": "2",
    },
    {
        "q": "Cái gì càng lau càng ướt?",
        "options": ["Cái khăn", "Cái bàn", "Cái ghế", "Quyển sách"],
        "answer": "Cái khăn",
    },
    {
        "q": "Cái gì luôn đến nhưng không bao giờ là hôm nay?",
        "options": ["Ngày mai", "Hôm qua", "Buổi sáng", "Mặt trời"],
        "answer": "Ngày mai",
    },
]

st.markdown("## 🧠 CÂU ĐỐ HACK NÃO")

riddle = riddles[(st.session_state.round - 1) % len(riddles)]

st.markdown(
    '<div class="card"><b>CÂU {}</b><h3>{}</h3></div>'.format(
        st.session_state.round,
        html.escape(riddle["q"]),
    ),
    unsafe_allow_html=True,
)

answer = st.radio(
    "Chọn đáp án:",
    riddle["options"],
    key=f"answer_{st.session_state.round}",
)

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ KIỂM TRA ĐÁP ÁN"):
        current_round = st.session_state.round

        if current_round in st.session_state.answered:
            st.info("Bạn đã trả lời câu này rồi.")
        elif answer == riddle["answer"]:
            st.session_state.score += 1
            st.session_state.answered.append(current_round)
            st.success("🎉 Chính xác!")
        else:
            st.session_state.answered.append(current_round)
            st.error(f"Chưa đúng! Đáp án: {riddle['answer']}")

with col2:
    if st.button("➡️ CÂU TIẾP THEO"):
        st.session_state.round += 1
        st.rerun()

st.write(f"🏆 Điểm số: **{st.session_state.score}**")

# ===================== UFO BẮT NGƯỜI =====================

st.markdown("## 🛸 UFO ĐANG SĂN NGƯỜI")

players = st.session_state.players
alive = [p for p in players if p.get("alive", True)]
captured_count = len(players) - len(alive)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        f'<div class="stat"><div class="number">{len(players)}</div>'
        '<div>Tổng người</div></div>',
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f'<div class="stat"><div class="number">{len(alive)}</div>'
        '<div>Còn trên mặt đất</div></div>',
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f'<div class="stat"><div class="number">{captured_count}</div>'
        '<div>Đã bị bắt</div></div>',
        unsafe_allow_html=True,
    )

if st.button("🚨 CHO UFO BẮT NGẪU NHIÊN", type="primary"):
    alive = [
        p for p in st.session_state.players
        if p.get("alive", True)
    ]

    if alive:
        victim = random.choice(alive)
        victim["alive"] = False
        st.session_state.victim_id = victim.get("id")
        st.session_state.message = f"🚨 UFO đã bắt {victim['name']}!"
    else:
        st.session_state.message = "Tất cả người chơi đã bị bắt!"

    st.rerun()

if st.button("🔄 CHƠI LẠI TỪ ĐẦU"):
    for p in st.session_state.players:
        p["alive"] = True

    st.session_state.victim_id = None
    st.session_state.round = 1
    st.session_state.score = 0
    st.session_state.answered = []
    st.session_state.message = "UFO đã quay lại!"
    st.rerun()

st.markdown(
    '<div class="card" style="text-align:center;font-size:20px">'
    + html.escape(st.session_state.message)
    + '</div>',
    unsafe_allow_html=True,
)

# ===================== CẢNH UFO =====================

st.markdown("## 🌌 CẢNH UFO BẮT CÓC")

crowd = ""

for index, p in enumerate(st.session_state.players):
    if not p.get("alive", True):
        continue

    row = index // 10
    col = index % 10

    left = 5 + col * 10 + random.uniform(-2, 2)
    bottom = 7 + row * 7

    crowd += """
    <div class="person"
         style="left:{:.2f}%;bottom:{:.2f}%;z-index:{}"
         title="{}">
        <div class="head">👽</div>
        <div class="body"></div>
        <div class="name">{}</div>
    </div>
    """.format(
        left,
        bottom,
        10 + row,
        html.escape(p["name"]),
        html.escape(p["name"]),
    )

captured = ""

if st.session_state.victim_id is not None:
    victim = next(
        (
            p for p in st.session_state.players
            if p.get("id") == st.session_state.victim_id
        ),
        None,
    )

    if victim:
        captured = """
        <div class="captured">
            <div class="beam"></div>
            <div class="alien">👽</div>
            <div class="captured-name">{}</div>
        </div>
        """.format(html.escape(victim["name"]))

scene = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing:border-box; }

body {
    margin:0;
    overflow:hidden;
    font-family:Arial,sans-serif;
    color:white;
    background:#02040d;
}

.scene {
    position:relative;
    height:560px;
    width:100%;
    overflow:hidden;
    border:1px solid #475569;
    border-radius:15px;
    background:
        radial-gradient(circle at 15% 15%,white 1px,transparent 2px),
        radial-gradient(circle at 80% 20%,white 1px,transparent 2px),
        radial-gradient(ellipse at bottom,#123847,#071326 50%,#02040d);
    background-size:100px 100px,140px 120px,auto;
}

.ufo {
    position:absolute;
    left:50%;
    top:25px;
    width:160px;
    height:90px;
    transform:translateX(-50%);
    z-index:100;
    animation:hover 2s infinite ease-in-out;
}

.dome {
    position:absolute;
    top:0;
    left:52px;
    width:56px;
    height:40px;
    border-radius:50% 50% 20% 20%;
    border:2px solid #a5f3fc;
    background:linear-gradient(#dbeafe,#565fc8);
    box-shadow:0 0 20px #22d3ee;
}

.disk {
    position:absolute;
    top:30px;
    width:160px;
    height:40px;
    border-radius:50%;
    border:3px solid #c4b5fd;
    background:linear-gradient(#b7c7ff,#555fc7,#20264c);
    box-shadow:0 0 22px #818cf8;
}

.person {
    position:absolute;
    width:10%;
    max-width:55px;
    min-width:25px;
    height:55px;
    text-align:center;
    transform:translateX(-50%);
}

.head {
    font-size:clamp(17px,3vw,27px);
    line-height:27px;
    filter:drop-shadow(0 0 5px #67e8f9);
}

.body {
    width:13px;
    height:19px;
    margin:auto;
    border-radius:6px;
    background:linear-gradient(#8b5cf6,#312e81);
}

.name {
    font-size:7px;
    max-width:60px;
    margin:auto;
    color:#e0f2fe;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
}

.beam {
    position:absolute;
    top:-55px;
    left:10px;
    width:90px;
    height:300px;
    clip-path:polygon(40% 0,60% 0,100% 100%,0 100%);
    background:linear-gradient(to top,rgba(34,211,238,.05),
        rgba(103,232,249,.5),transparent);
}

.captured {
    position:absolute;
    left:50%;
    top:150px;
    width:110px;
    text-align:center;
    transform:translateX(-50%);
    z-index:90;
    animation:abduct 3.5s ease-in-out forwards;
}

.alien {
    position:relative;
    font-size:48px;
    z-index:2;
    filter:drop-shadow(0 0 15px #67e8f9);
}

.captured-name {
    position:relative;
    z-index:3;
    padding:4px;
    background:#071326;
    border:1px solid #67e8f9;
    border-radius:6px;
    font-size:11px;
    overflow-wrap:anywhere;
}

.ground {
    position:absolute;
    bottom:0;
    width:100%;
    height:18px;
    background:#164e63;
    border-top:2px solid #22d3ee;
}

@keyframes hover {
    0%,100% { margin-top:0; }
    50% { margin-top:-8px; }
}

@keyframes abduct {
    0% { top:410px; opacity:0; }
    15% { opacity:1; }
    75% { top:175px; opacity:1; }
    100% { top:80px; opacity:0; }
}

@media(max-width:600px) {
    .scene { height:520px; }
    .ufo { transform:translateX(-50%) scale(.8); }
    .person { height:48px; }
    .name { font-size:6px; max-width:36px; }
}
</style>
</head>
<body>
<div class="scene">
    <div class="ufo">
        <div class="dome"></div>
        <div class="disk"></div>
    </div>
    {crowd}
    {captured}
    <div class="ground"></div>
</div>
</body>
</html>
"""

components.html(
    scene.format(crowd=crowd, captured=captured),
    height=580,
    scrolling=False,
)

# ===================== DANH SÁCH CHI TIẾT =====================

with st.expander("📋 DANH SÁCH NGƯỜI CHƠI"):
    for p in st.session_state.players:
        status = (
            "🛸 Đã bị bắt"
            if not p.get("alive", True)
            else "🟢 Còn trên mặt đất"
        )
        st.write(
            "{} (ID {}) — {}".format(
                p.get("name", "Người chơi"),
                p.get("id", 0),
                status,
            )
        )

st.markdown("---")
st.caption("🛸 UFO HACK NÃO — Mini game ngoài hành tinh")
