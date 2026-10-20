import streamlit as st
import random
import html
import streamlit.components.v1 as components

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide"
)

# =========================
# GIAO DIỆN
# =========================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #101b3b, #03050f);
    color: white;
}

.block-container {
    max-width: 1300px;
    padding-top: 1.5rem;
}

h1, h2, h3, p, label {
    color: white !important;
}

.title {
    text-align: center;
    font-size: clamp(30px, 5vw, 55px);
    font-weight: 900;
    color: #67e8f9;
    text-shadow: 0 0 18px #06b6d4;
}

.subtitle {
    text-align: center;
    color: #c4b5fd;
    margin-bottom: 25px;
}

div.stButton > button {
    width: 100%;
    min-height: 44px;
    border-radius: 12px;
    font-weight: bold;
}

.card {
    background: rgba(20, 32, 65, .92);
    border: 1px solid #475569;
    border-radius: 14px;
    padding: 15px;
    margin: 10px 0;
}

.number {
    font-size: 25px;
    color: #67e8f9;
    font-weight: bold;
}

.stat {
    text-align: center;
    border: 1px solid #475569;
    border-radius: 12px;
    padding: 10px;
    background: #111a35;
}
</style>
""", unsafe_allow_html=True)

# =========================
# KHỞI TẠO TRẠNG THÁI
# =========================

if "players" not in st.session_state:
    st.session_state.players = []

    for i in range(20):
        st.session_state.players.append({
            "id": i,
            "name": "Người {}".format(i + 1),
            "alive": True
        })

if "round" not in st.session_state:
    st.session_state.round = 1

if "message" not in st.session_state:
    st.session_state.message = "UFO đang bay quanh Trái Đất!"

if "victim_id" not in st.session_state:
    st.session_state.victim_id = None

# =========================
# TIÊU ĐỀ
# =========================

st.markdown(
    '<div class="title">🛸 UFO HACK NÃO 👽</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Chào mừng đến với trò chơi UFO bắt cóc!'
    '</div>',
    unsafe_allow_html=True
)

# =========================
# NHẠC NỀN
# =========================

st.markdown("## 🔊 NHẠC UFO")

music_enabled = st.toggle("Bật khu vực nhạc", value=True)

if music_enabled:
    components.html("""
    <div style="background:#111a35;color:white;padding:12px;
                border-radius:12px;text-align:center;">
      <button id="play"
       style="padding:12px;border:0;border-radius:8px;
              background:#7c3aed;color:white;font-weight:bold;">
       ▶️ PHÁT NHẠC
      </button>

      <button id="stop"
       style="padding:12px;border:0;border-radius:8px;
              background:#475569;color:white;font-weight:bold;">
       ⏹ TẮT NHẠC
      </button>
    </div>

    <script>
    (() => {
      let ctx = null;
      let timer = null;
      let master = null;
      let drone = null;

      function stopMusic() {
        if (timer) clearInterval(timer);
        timer = null;

        if (ctx) {
          ctx.close().catch(() => {});
        }

        ctx = null;
        master = null;
        drone = null;
      }

      function playMusic() {
        stopMusic();

        const AudioContext =
          window.AudioContext || window.webkitAudioContext;

        if (!AudioContext) {
          alert("Trình duyệt không hỗ trợ âm thanh.");
          return;
        }

        ctx = new AudioContext();

        master = ctx.createGain();
        master.gain.value = 0.18;
        master.connect(ctx.destination);

        drone = ctx.createOscillator();
        const droneGain = ctx.createGain();

        drone.type = "sawtooth";
        drone.frequency.value = 48;
        droneGain.gain.value = 0.08;

        drone.connect(droneGain);
        droneGain.connect(master);
        drone.start();

        let count = 0;

        timer = setInterval(() => {
          if (!ctx || !master) return;

          const sound = ctx.createOscillator();
          const gain = ctx.createGain();

          sound.type = "triangle";
          sound.frequency.value = count % 2 ? 65 : 82;

          gain.gain.setValueAtTime(0.001, ctx.currentTime);
          gain.gain.linearRampToValueAtTime(
            0.06, ctx.currentTime + 0.05
          );
          gain.gain.linearRampToValueAtTime(
            0.001, ctx.currentTime + 0.35
          );

          sound.connect(gain);
          gain.connect(master);

          sound.start();
          sound.stop(ctx.currentTime + 0.4);

          count++;
        }, 600);
      }

      document.getElementById("play").onclick = playMusic;
      document.getElementById("stop").onclick = stopMusic;
    })();
    </script>
    """, height=85)

    st.caption(
        "Nếu chưa nghe thấy nhạc, hãy bấm PHÁT NHẠC. "
        "Giữ âm lượng vừa phải để bảo vệ thính giác."
    )

# =========================
# THÊM NGƯỜI
# =========================

st.markdown("## 👥 NGƯỜI CHƠI")

players = st.session_state.players

st.write("Số người chơi: **{}/100**".format(len(players)))

if st.button("➕ THÊM 10 NGƯỜI"):
    amount = min(10, 100 - len(players))
    next_id = max([p["id"] for p in players], default=-1) + 1

    for i in range(amount):
        players.append({
            "id": next_id + i,
            "name": "Người {}".format(next_id + i + 1),
            "alive": True
        })

    if amount:
        st.session_state.message = "Đã thêm {} người.".format(amount)
    else:
        st.session_state.message = "Đã đủ 100 người."

    st.rerun()

# =========================
# ĐỔI TÊN
# =========================

with st.expander("✏️ ĐỔI TÊN NHÂN VẬT"):
    if players:
        options = {}

        for player in players:
            label = "{} (ID {})".format(
                player["name"], player["id"]
            )
            options[label] = player["id"]

        selected_label = st.selectbox(
            "Chọn nhân vật",
            list(options.keys())
        )

        selected_id = options[selected_label]

        new_name = st.text_input(
            "Nhập tên mới",
            max_chars=24
        )

        if st.button("💾 LƯU TÊN"):
            new_name = new_name.strip()

            if not new_name:
                st.warning("Bạn hãy nhập tên mới.")
            else:
                for player in players:
                    if player["id"] == selected_id:
                        player["name"] = new_name
                        break

                st.session_state.message = (
                    "Đã đổi tên thành {}.".format(new_name)
                )
                st.rerun()

# =========================
# CÂU ĐỐ
# =========================

riddles = [
    {
        "q": "Cái gì càng lấy đi thì càng lớn?",
        "options": ["Cái hố", "Cái cây", "Ngọn núi", "Dòng sông"],
        "answer": "Cái hố"
    },
    {
        "q": "Tháng nào có 28 ngày?",
        "options": ["Tháng 2", "Tháng 4", "Tất cả các tháng", "Tháng 6"],
        "answer": "Tất cả các tháng"
    },
    {
        "q": "Cái gì có cổ nhưng không có đầu?",
        "options": ["Cái chai", "Cái bàn", "Con mèo", "Cái ghế"],
        "answer": "Cái chai"
    },
    {
        "q": "Bạn vượt qua người đứng thứ hai. Bạn đứng thứ mấy?",
        "options": ["Thứ nhất", "Thứ hai", "Thứ ba", "Thứ tư"],
        "answer": "Thứ hai"
    },
    {
        "q": "Cái gì có răng nhưng không cắn?",
        "options": ["Cá mập", "Cái lược", "Cá sấu", "Con chó"],
        "answer": "Cái lược"
    }
]

st.markdown("## 🧠 CÂU ĐỐ HACK NÃO")

riddle = riddles[(st.session_state.round - 1) % len(riddles)]

st.markdown(
    '<div class="card"><b>CÂU {}</b><h3>{}</h3></div>'.format(
        st.session_state.round,
        html.escape(riddle["q"])
    ),
    unsafe_allow_html=True
)

answer = st.radio(
    "Chọn đáp án:",
    riddle["options"],
    key="answer_{}".format(st.session_state.round)
)

col_a, col_b = st.columns(2)

with col_a:
    if st.button("✅ KIỂM TRA ĐÁP ÁN"):
        if answer == riddle["answer"]:
            st.success("🎉 Chính xác!")
        else:
            st.error("Chưa đúng! Đáp án là: " + riddle["answer"])

with col_b:
    if st.button("➡️ CÂU TIẾP"):
        st.session_state.round += 1
        st.rerun()

# =========================
# UFO BẮT NGƯỜI
# =========================

st.markdown("## 🛸 UFO BẮT NGƯỜI")

alive = [p for p in players if p["alive"]]
captured_count = len(players) - len(alive)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        '<div class="stat"><div class="number">{}</div>'
        'Tổng người</div>'.format(len(players)),
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        '<div class="stat"><div class="number">{}</div>'
        'Còn trên mặt đất</div>'.format(len(alive)),
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        '<div class="stat"><div class="number">{}</div>'
        'Đã bị bắt</div>'.format(captured_count),
        unsafe_allow_html=True
    )

if st.button("🚨 CHO UFO BẮT NGẪU NHIÊN"):
    if alive:
        victim = random.choice(alive)
        victim["alive"] = False
        st.session_state.victim_id = victim["id"]
        st.session_state.message = (
            "🚨 UFO đã bắt {}!".format(victim["name"])
        )
    else:
        st.session_state.message = (
            "Tất cả người chơi đã bị bắt! Hãy chơi lại."
        )

    st.rerun()

if st.button("🔄 CHƠI LẠI TỪ ĐẦU"):
    for player in players:
        player["alive"] = True

    st.session_state.victim_id = None
    st.session_state.round = 1
    st.session_state.message = "UFO đã quay lại!"
    st.rerun()

st.markdown(
    '<div class="card" style="text-align:center;font-size:20px;">'
    + html.escape(st.session_state.message)
    + '</div>',
    unsafe_allow_html=True
)

# =========================
# CẢNH UFO
# =========================

st.markdown("## 🌌 CẢNH UFO VÀ ĐÁM ĐÔNG")

crowd = ""

for index, player in enumerate(players):
    if not player["alive"]:
        continue

    row = index // 10
    col = index % 10

    left = 5 + col * 10 + random.uniform(-2, 2)
    bottom = 8 + row * 7

    crowd += """
    <div class="person" title="{name}"
         style="left:{left}%;bottom:{bottom}%;z-index:{z};">
        <div class="head">👽</div>
        <div class="body"></div>
        <div class="name">{name}</div>
    </div>
    """.format(
        name=html.escape(player["name"]),
        left=left,
        bottom=bottom,
        z=10 + row
    )

captured = ""

if st.session_state.victim_id is not None:
    victim = next(
        (
            p for p in players
            if p["id"] == st.session_state.victim_id
        ),
        None
    )

    if victim:
        captured = """
        <div class="captured">
            <div class="beam"></div>
            <div class="alien">👽</div>
            <div class="captured-name">{}</div>
        </div>
        """.format(html.escape(victim["name"]))

# Truyền HTML trực tiếp bằng f-string không an toàn với CSS có dấu {}.
# Dùng format() để tránh lỗi định dạng.

scene = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing:border-box; }

body {
    margin:0;
    background:#02040d;
    color:white;
    font-family:Arial,sans-serif;
    overflow:hidden;
}

.scene {
    position:relative;
    height:560px;
    overflow:hidden;
    border:1px solid #475569;
    border-radius:16px;
    background:
      radial-gradient(circle at 15% 15%,white 1px,transparent 2px),
      radial-gradient(circle at 80% 22%,white 1px,transparent 2px),
      radial-gradient(ellipse at bottom,#123847,#071326 50%,#02040d);
    background-size:100px 100px,140px 140px,auto;
}

.ufo {
    position:absolute;
    left:50%;
    top:25px;
    transform:translateX(-50%);
    width:160px;
    height:90px;
    z-index:100;
    animation:hover 2s infinite ease-in-out;
}

.dome {
    position:absolute;
    left:52px;
    top:0;
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

.captured {
    position:absolute;
    left:50%;
    top:160px;
    z-index:90;
    width:110px;
    text-align:center;
    transform:translateX(-50%);
    animation:abduct 3s ease-in-out forwards;
}

.beam {
    position:absolute;
    top:-60px;
    left:10px;
    width:90px;
    height:300px;
    clip-path:polygon(40% 0,60% 0,100% 100%,0 100%);
    background:linear-gradient(to top,rgba(34,211,238,.05),
                                rgba(103,232,249,.5),transparent);
}

.alien {
    position:relative;
    font-size:48px;
    z-index:2;
}

.captured-name {
    position:relative;
    z-index:3;
    font-size:11px;
    padding:4px;
    background:#071326;
    border:1px solid #67e8f9;
    border-radius:6px;
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
    75% { top:170px; opacity:1; }
    100% { top:80px; opacity:0; }
}

@media(max-width:600px) {
    .scene { height:520px; }
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
    scrolling=False
)

# =========================
# DANH SÁCH
# =========================

with st.expander("📋 XEM DANH SÁCH NGƯỜI CHƠI"):
    for player in players:
        status = "🛸 Đã bị bắt" if not player["alive"] else "🟢 Còn trên mặt đất"
        st.write("{} — {}".format(player["name"], status))

st.markdown("---")
st.caption("UFO HACK NÃO · Mini game ngoài hành tinh")
