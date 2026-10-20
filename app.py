import streamlit as st
import streamlit.components.v1 as components
import random
import html

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
    background: radial-gradient(
        ellipse at top,
        #192b50 0%,
        #080d20 55%,
        #02040b 100%
    );
    color: white;
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
}

h1, h2, h3, p, label {
    color: white !important;
}

.game-title {
    text-align: center;
    font-size: clamp(30px, 5vw, 55px);
    font-weight: 1000;
    color: #a5f3fc;
    text-shadow: 0 0 15px #06b6d4, 0 0 30px #7c3aed;
}

.game-subtitle {
    text-align: center;
    color: #c4b5fd;
    margin-bottom: 25px;
}

.panel {
    background: rgba(17, 24, 55, .9);
    border: 1px solid #46558a;
    border-radius: 15px;
    padding: 16px;
    margin: 12px 0;
}

div.stButton > button {
    border-radius: 12px;
    min-height: 44px;
    font-weight: bold;
}

.stat {
    background: rgba(30, 41, 80, .8);
    border: 1px solid #46558a;
    border-radius: 12px;
    padding: 12px 5px;
    text-align: center;
}

.stat-number {
    font-size: 26px;
    font-weight: bold;
    color: #67e8f9;
}

.stat-label {
    font-size: 12px;
    color: #cbd5e1;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 10px;
        padding-right: 10px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# TRẠNG THÁI
# =========================

if "players" not in st.session_state:
    st.session_state.players = [
        {
            "id": i,
            "name": "Người {}".format(i + 1),
            "alive": True
        }
        for i in range(10)
    ]

if "round" not in st.session_state:
    st.session_state.round = 1

if "message" not in st.session_state:
    st.session_state.message = "🛸 UFO đang bay quanh Trái Đất!"

if "last_abducted" not in st.session_state:
    st.session_state.last_abducted = None

if "music_on" not in st.session_state:
    st.session_state.music_on = True

if "music_volume" not in st.session_state:
    st.session_state.music_volume = 0.25

# =========================
# TIÊU ĐỀ
# =========================

st.markdown(
    '<div class="game-title">🛸 UFO HACK NÃO 👽</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="game-subtitle">'
    'Ai sẽ là người tiếp theo bị UFO bắt cóc?'
    '</div>',
    unsafe_allow_html=True
)

# =========================
# NHẠC NỀN
# =========================

st.markdown("## 🔊 NHẠC HỒI HỘP")

music_col1, music_col2 = st.columns(2)

with music_col1:
    st.session_state.music_on = st.toggle(
        "Bật nhạc UFO",
        value=st.session_state.music_on,
        key="music_switch"
    )

with music_col2:
    st.session_state.music_volume = st.slider(
        "Âm lượng",
        min_value=0.0,
        max_value=1.0,
        value=st.session_state.music_volume,
        step=0.05,
        help="Nên tăng từ từ và tránh nghe ở mức quá lớn."
    )

# Phát âm thanh trong iframe riêng.
# Bấm nút phát trong khung để trình duyệt cho phép âm thanh.

if st.session_state.music_on:
    volume = st.session_state.music_volume

    components.html(
        """
        <div style="background:#111a35;color:white;padding:12px;
                    border-radius:12px;text-align:center;">
            <button id="play"
                style="padding:10px 18px;border:0;border-radius:8px;
                       background:#7c3aed;color:white;font-weight:bold;">
                ▶️ PHÁT NHẠC UFO
            </button>
            <button id="stop"
                style="padding:10px 18px;border:0;border-radius:8px;
                       background:#334155;color:white;font-weight:bold;">
                ⏹ TẮT NHẠC
            </button>
            <div style="font-size:12px;margin-top:8px;">
                Nhấn Phát nhạc nếu trình duyệt chưa phát âm thanh.
            </div>
        </div>

        <script>
        (() => {
            let ctx = null;
            let timer = null;
            let nodes = [];

            const volume = VOLUME_PLACEHOLDER;

            function stopMusic() {
                if (timer) {
                    clearInterval(timer);
                    timer = null;
                }

                nodes.forEach(node => {
                    try { node.stop(); } catch (e) {}
                });

                nodes = [];

                if (ctx) {
                    ctx.close().catch(() => {});
                    ctx = null;
                }
            }

            function playMusic() {
                stopMusic();

                const AC = window.AudioContext ||
                           window.webkitAudioContext;

                if (!AC) {
                    alert("Trình duyệt không hỗ trợ âm thanh.");
                    return;
                }

                ctx = new AC();

                const master = ctx.createGain();
                master.gain.value = volume;
                master.connect(ctx.destination);

                const drone = ctx.createOscillator();
                const droneGain = ctx.createGain();

                drone.type = "sawtooth";
                drone.frequency.value = 48;
                droneGain.gain.value = 0.07;

                drone.connect(droneGain);
                droneGain.connect(master);
                drone.start();

                nodes.push(drone);

                let beat = 0;

                timer = setInterval(() => {
                    if (!ctx) return;

                    const pulse = ctx.createOscillator();
                    const gain = ctx.createGain();

                    pulse.type = "triangle";
                    pulse.frequency.value =
                        beat % 2 === 0 ? 72 : 55;

                    gain.gain.setValueAtTime(
                        0.0001, ctx.currentTime
                    );

                    gain.gain.exponentialRampToValueAtTime(
                        0.08, ctx.currentTime + 0.04
                    );

                    gain.gain.exponentialRampToValueAtTime(
                        0.0001, ctx.currentTime + 0.35
                    );

                    pulse.connect(gain);
                    gain.connect(master);

                    pulse.start();
                    pulse.stop(ctx.currentTime + 0.4);

                    beat++;
                }, 600);
            }

            document.getElementById("play").onclick = playMusic;
            document.getElementById("stop").onclick = stopMusic;
        })();
        </script>
        """.replace("VOLUME_PLACEHOLDER", str(volume)),
        height=105
    )
else:
    st.info("Nhạc đang tắt.")

# =========================
# QUẢN LÝ NGƯỜI CHƠI
# =========================

st.markdown("## 👥 QUẢN LÝ NGƯỜI CHƠI")

st.write(
    "Số người chơi: **{}/100**".format(
        len(st.session_state.players)
    )
)

add_col, reset_col = st.columns(2)

with add_col:
    if st.button("➕ THÊM 10 NGƯỜI", use_container_width=True):
        players = st.session_state.players
        amount = min(10, 100 - len(players))

        existing_ids = [p["id"] for p in players]
        next_id = max(existing_ids, default=-1) + 1

        for i in range(amount):
            players.append({
                "id": next_id + i,
                "name": "Người {}".format(next_id + i + 1),
                "alive": True
            })

        if amount:
            st.session_state.message = (
                "Đã thêm {} người chơi!".format(amount)
            )
        else:
            st.session_state.message = "Đã đủ 100 người chơi!"

        st.rerun()

with reset_col:
    if st.button("🔄 CHƠI LẠI TỪ ĐẦU", use_container_width=True):
        for player in st.session_state.players:
            player["alive"] = True

        st.session_state.last_abducted = None
        st.session_state.round = 1
        st.session_state.message = "UFO đã quay lại!"

        st.rerun()

# =========================
# ĐỔI TÊN
# =========================

with st.expander("✏️ ĐỔI TÊN NHÂN VẬT"):
    players = st.session_state.players

    if players:
        # Dùng format() để tránh lỗi cú pháp f-string.
        player_options = {
            "{} (ID {})".format(p["name"], p["id"]): p["id"]
            for p in players
        }

        selected_label = st.selectbox(
            "Chọn nhân vật",
            list(player_options.keys()),
            key="rename_player_select"
        )

        selected_id = player_options[selected_label]

        new_name = st.text_input(
            "Nhập tên mới",
            max_chars=24,
            key="rename_player_text"
        )

        if st.button("💾 LƯU TÊN"):
            cleaned_name = new_name.strip()

            if cleaned_name:
                for player in players:
                    if player["id"] == selected_id:
                        player["name"] = cleaned_name
                        break

                st.session_state.message = (
                    "Đã đổi tên thành {}!".format(cleaned_name)
                )
                st.rerun()
            else:
                st.warning("Bạn hãy nhập tên mới trước.")

# =========================
# CÂU ĐỐ
# =========================

riddles = [
    {
        "q": "Cái gì càng lấy đi thì càng lớn?",
        "a": ["Cái hố", "Ngọn núi", "Cái cây", "Dòng sông"],
        "correct": "Cái hố",
        "explain": "Càng đào đất đi thì cái hố càng lớn."
    },
    {
        "q": "Tháng nào có 28 ngày?",
        "a": ["Tháng 2", "Tháng 4", "Tất cả các tháng", "Tháng 6"],
        "correct": "Tất cả các tháng",
        "explain": "Tất cả các tháng đều có ít nhất 28 ngày."
    },
    {
        "q": "Cái gì có cổ nhưng không có đầu?",
        "a": ["Cái chai", "Con hươu", "Cái bàn", "Cái quạt"],
        "correct": "Cái chai",
        "explain": "Cái chai có cổ chai."
    },
    {
        "q": "Bạn vượt qua người đứng thứ hai. Bạn đứng thứ mấy?",
        "a": ["Thứ nhất", "Thứ hai", "Thứ ba", "Thứ tư"],
        "correct": "Thứ hai",
        "explain": "Bạn chiếm vị trí của người đứng thứ hai."
    },
    {
        "q": "Cái gì có nhiều răng nhưng không cắn được?",
        "a": ["Cá mập", "Cái lược", "Cá sấu", "Con mèo"],
        "correct": "Cái lược",
        "explain": "Cái lược có răng lược."
    },
    {
        "q": "Có 5 quả táo, bạn lấy 2 quả. Bạn có mấy quả?",
        "a": ["2", "3", "5", "7"],
        "correct": "2",
        "explain": "Bạn lấy 2 quả nên bạn có 2 quả."
    },
    {
        "q": "Cái gì càng lau càng ướt?",
        "a": ["Cái khăn", "Cái bàn", "Cái ghế", "Quyển sách"],
        "correct": "Cái khăn",
        "explain": "Khăn thấm nước khi lau."
    },
    {
        "q": "Cái gì luôn đến nhưng không bao giờ là hôm nay?",
        "a": ["Ngày mai", "Hôm qua", "Buổi sáng", "Mặt trời"],
        "correct": "Ngày mai",
        "explain": "Ngày mai đến thì lại trở thành hôm nay."
    }
]

st.markdown("## 🧠 CÂU ĐỐ HACK NÃO")

riddle_index = (st.session_state.round - 1) % len(riddles)
riddle = riddles[riddle_index]

st.markdown(
    '<div class="panel"><b>CÂU ĐỐ SỐ {}</b><h3>{}</h3></div>'.format(
        st.session_state.round,
        html.escape(riddle["q"])
    ),
    unsafe_allow_html=True
)

answer = st.radio(
    "Chọn đáp án:",
    riddle["a"],
    key="answer_round_{}".format(st.session_state.round)
)

check_col, next_col = st.columns(2)

with check_col:
    if st.button("✅ KIỂM TRA", use_container_width=True):
        if answer == riddle["correct"]:
            st.success("🎉 Chính xác! " + riddle["explain"])
        else:
            st.error("Chưa đúng! Đáp án: " + riddle["correct"])

with next_col:
    if st.button("➡️ CÂU TIẾP THEO", use_container_width=True):
        st.session_state.round += 1
        st.rerun()

# =========================
# UFO BẮT NGƯỜI
# =========================

st.markdown("## 🛸 UFO ĐANG SĂN NGƯỜI")

players = st.session_state.players
alive_players = [p for p in players if p["alive"]]
captured_count = len(players) - len(alive_players)

s1, s2, s3 = st.columns(3)

with s1:
    st.markdown(
        '<div class="stat"><div class="stat-number">{}</div>'
        '<div class="stat-label">Tổng người chơi</div></div>'.format(
            len(players)
        ),
        unsafe_allow_html=True
    )

with s2:
    st.markdown(
        '<div class="stat"><div class="stat-number">{}</div>'
        '<div class="stat-label">Còn trên mặt đất</div></div>'.format(
            len(alive_players)
        ),
        unsafe_allow_html=True
    )

with s3:
    st.markdown(
        '<div class="stat"><div class="stat-number">{}</div>'
        '<div class="stat-label">Đã bị bắt</div></div>'.format(
            captured_count
        ),
        unsafe_allow_html=True
    )

if st.button(
    "🚨 CHO UFO BẮT NGẪU NHIÊN",
    type="primary",
    use_container_width=True
):
    if alive_players:
        victim = random.choice(alive_players)
        victim["alive"] = False

        st.session_state.last_abducted = victim["id"]
        st.session_state.message = (
            "🚨 UFO đã bắt {}!".format(victim["name"])
        )
    else:
        st.session_state.message = (
            "Tất cả người chơi đã bị bắt! Hãy chơi lại."
        )

    st.rerun()

st.markdown(
    '<div class="panel" style="text-align:center;font-size:20px;">'
    + html.escape(st.session_state.message)
    + '</div>',
    unsafe_allow_html=True
)

# =========================
# CẢNH UFO VÀ ĐÁM ĐÔNG
# =========================

st.markdown("### 🌌 CẢNH UFO BẮT CÓC")

crowd_html = ""

# Nhân vật đứng chen chúc trong 10 cột.
# Mỗi hàng được đặt cao thấp khác nhau để tạo cảm giác đông người.

for index, player in enumerate(players):
    if not player["alive"]:
        continue

    row = index // 10
    col = index % 10

    left = 5 + col * 10 + random.uniform(-2, 2)
    bottom = 7 + row * 7 + random.uniform(-1, 1)

    name = html.escape(player["name"])

    crowd_html += """
    <div class="person"
         title="{name}"
         style="left:{left:.1f}%;bottom:{bottom:.1f}%;
                z-index:{z};">
        <div class="head">👽</div>
        <div class="body"></div>
        <div class="name">{name}</div>
    </div>
    """.format(
        name=name,
        left=left,
        bottom=bottom,
        z=10 + row
    )

captured_html = ""

if st.session_state.last_abducted is not None:
    victim = next(
        (
            p for p in players
            if p["id"] == st.session_state.last_abducted
        ),
        None
    )

    if victim:
        captured_html = """
        <div class="captured">
            <div class="captured-beam"></div>
            <div class="captured-alien">👽</div>
            <div class="captured-name">{}</div>
        </div>
        """.format(html.escape(victim["name"]))

components.html(
    """
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
            height:570px;
            width:100%;
            position:relative;
            overflow:hidden;
            border:1px solid #5365a0;
            border-radius:16px;
            background:
                radial-gradient(circle at 10% 12%,white 1px,transparent 2px),
                radial-gradient(circle at 80% 20%,white 1px,transparent 2px),
                radial-gradient(circle at 45% 8%,white 1px,transparent 2px),
                radial-gradient(ellipse at bottom,#123847,#071326 50%,#02040d);
            background-size:100px 100px,130px 130px,170px 170px,auto;
        }

        .moon {
            position:absolute;
            right:8%;
            top:20px;
            font-size:35px;
        }

        .ufo {
            position:absolute;
            top:28px;
            left:50%;
            transform:translateX(-50%);
            width:170px;
            height:95px;
            z-index:100;
            animation:hover 2s infinite ease-in-out;
        }

        .ufo-dome {
            position:absolute;
            top:0;
            left:55px;
            width:60px;
            height:40px;
            border:2px solid #a5f3fc;
            border-radius:50% 50% 20% 20%;
            background:linear-gradient(135deg,#dbeafe,#5b65d8,#252c63);
            box-shadow:0 0 20px #22d3ee;
        }

        .ufo-disk {
            position:absolute;
            top:30px;
            width:170px;
            height:42px;
            border:3px solid #c4b5fd;
            border-radius:50%;
            background:linear-gradient(#b7c7ff,#555fc7,#20264c);
            box-shadow:0 0 22px #818cf8;
        }

        .lights {
            position:absolute;
            top:49px;
            left:18px;
            width:134px;
            display:flex;
            justify-content:space-around;
        }

        .lights span {
            height:8px;
            width:8px;
            border-radius:50%;
            background:#a5f3fc;
            box-shadow:0 0 10px #22d3ee;
            animation:blink .5s infinite alternate;
        }

        .general-beam {
            position:absolute;
            top:95px;
            left:50%;
            transform:translateX(-50%);
            width:240px;
            height:390px;
            clip-path:polygon(40% 0,60% 0,100% 100%,0 100%);
            background:linear-gradient(
                to bottom,
                rgba(103,232,249,.28),
                rgba(103,232,249,.04),
                transparent
            );
        }

        .person {
            position:absolute;
            width:10%;
            max-width:55px;
            min-width:25px;
            height:58px;
            transform:translateX(-50%);
            text-align:center;
            animation:sway 2s infinite alternate ease-in-out;
        }

        .head {
            font-size:clamp(17px,3vw,27px);
            line-height:28px;
            filter:drop-shadow(0 0 5px #67e8f9);
        }

        .body {
            width:13px;
            height:19px;
            margin:-1px auto 0;
            border:1px solid #c4b5fd;
            border-radius:6px;
            background:linear-gradient(#8b5cf6,#312e81);
        }

        .name {
            font-size:7px;
            color:#e0f2fe;
            max-width:60px;
            margin:auto;
            white-space:nowrap;
            overflow:hidden;
            text-overflow:ellipsis;
            text-shadow:0 0 5px black;
        }

        .captured {
            position:absolute;
            left:50%;
            top:150px;
            width:120px;
            transform:translateX(-50%);
            z-index:90;
            text-align:center;
            animation:abduct 3.5s ease-in-out forwards;
        }

        .captured-beam {
            position:absolute;
            left:15px;
            top:-30px;
            width:90px;
            height:300px;
            clip-path:polygon(40% 0,60% 0,100% 100%,0 100%);
            background:linear-gradient(
                to top,
                rgba(34,211,238,.04),
                rgba(103,232,249,.48),
                rgba(34,211,238,.08)
            );
            animation:flash .35s infinite alternate;
        }

        .captured-alien {
            position:relative;
            z-index:2;
            font-size:48px;
            filter:drop-shadow(0 0 15px #67e8f9);
        }

        .captured-name {
            position:relative;
            z-index:3;
            padding:4px;
            font-size:12px;
            background:#071326;
            border:1px solid #67e8f9;
            border-radius:6px;
            overflow-wrap:anywhere;
        }

        .ground {
            position:absolute;
            bottom:0;
            height:20px;
            width:100%;
            background:linear-gradient(#164e63,#07111f);
            border-top:2px solid #22d3ee;
        }

        .caption {
            position:absolute;
            bottom:25px;
            width:100%;
            text-align:center;
            z-index:120;
            font-size:12px;
            font-weight:bold;
            color:#a5f3fc;
            text-shadow:0 0 7px #0891b2;
        }

        @keyframes hover {
            0%,100% { margin-top:0; }
            50% { margin-top:-9px; }
        }

        @keyframes blink {
            from { opacity:.3; }
            to { opacity:1; }
        }

        @keyframes sway {
            from { margin-left:-1px; }
            to { margin-left:1px; }
        }

        @keyframes flash {
            from { opacity:.4; }
            to { opacity:1; }
        }

        @keyframes abduct {
            0% {
                top:405px;
                opacity:0;
                transform:translateX(-50%) scale(.65);
            }
            15% { opacity:1; }
            75% {
                top:175px;
                opacity:1;
                transform:translateX(-50%) scale(1);
            }
            100% {
                top:85px;
                opacity:0;
                transform:translateX(-50%) scale(.4);
            }
        }

        @media(max-width:600px) {
            .scene { height:520px; }
            .ufo { transform:translateX(-50%) scale(.8); }
            .person { height:48px; }
            .name { font-size:6px; max-width:36px; }
            .moon { font-size:28px; }
        }
    </style>
    </head>
    <body>
        <div class="scene">
            <div class="moon">🌙</div>

            <div class="ufo">
                <div class="ufo-dome"></div>
                <div class="ufo-disk"></div>
                <div class="lights">
                    <span></span><span></span><span></span>
                    <span></span><span></span><span></span>
                </div>
            </div>

            <div class="general-beam"></div>

            {crowd}

            {captured}

            <div class="ground"></div>
            <div class="caption">🛸 UFO ĐANG QUAN SÁT ĐÁM ĐÔNG 👽</div>
        </div>
    </body>
    </html>
    """.format(
        crowd=crowd_html,
        captured=captured_html
    ),
    height=590,
    scrolling=False
)

# =========================
# DANH SÁCH ĐẦY ĐỦ
# =========================

with st.expander("📋 XEM DANH SÁCH NGƯỜI CHƠI"):
    for player in st.session_state.players:
        status = (
            "🛸 Đã bị bắt"
            if not player["alive"]
            else "🟢 Còn trên mặt đất"
        )

        st.write(
            "{} — {}".format(player["name"], status)
        )

st.markdown("---")

st.markdown(
    '<div style="text-align:center;color:#94a3b8;font-size:12px;">'
    'UFO HACK NÃO · Mini game ngoài hành tinh'
    '</div>',
    unsafe_allow_html=True
)
