import html
import random
import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# CẤU HÌNH
# =====================================================

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =====================================================
# CSS GIAO DIỆN
# =====================================================

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(ellipse at top, #172650 0%, #080d20 52%, #02040b 100%);
        color: #ffffff;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3, p, label {
        color: #ffffff !important;
    }

    .hero-title {
        text-align: center;
        font-size: clamp(32px, 5vw, 58px);
        font-weight: 1000;
        color: #a5f3fc;
        text-shadow: 0 0 14px #06b6d4, 0 0 35px #7c3aed;
        margin-bottom: 4px;
    }

    .hero-subtitle {
        text-align: center;
        color: #c4b5fd;
        margin-bottom: 24px;
    }

    .game-card {
        background: rgba(17, 24, 55, 0.92);
        border: 1px solid #46558a;
        border-radius: 15px;
        padding: 16px;
        margin: 10px 0;
    }

    .stat-card {
        background: rgba(20, 32, 65, 0.95);
        border: 1px solid #475569;
        border-radius: 12px;
        padding: 12px 5px;
        text-align: center;
        min-height: 82px;
    }

    .stat-number {
        color: #67e8f9;
        font-size: 27px;
        font-weight: 900;
    }

    .stat-label {
        color: #cbd5e1;
        font-size: 12px;
    }

    div.stButton > button {
        min-height: 43px;
        border-radius: 11px;
        font-weight: bold;
    }

    div[data-testid="stTextInput"] input {
        background: #111a35;
        color: white;
    }

    @media (max-width: 600px) {
        .block-container {
            padding-left: 10px;
            padding-right: 10px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# KHỞI TẠO TRẠNG THÁI GAME
# =====================================================

if "players" not in st.session_state:
    st.session_state.players = [
        {
            "id": i,
            "name": "Người {}".format(i + 1),
            "alive": True,
        }
        for i in range(20)
    ]

if "round" not in st.session_state:
    st.session_state.round = 1

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered_rounds" not in st.session_state:
    st.session_state.answered_rounds = []

if "message" not in st.session_state:
    st.session_state.message = "🛸 UFO đang bay quanh Trái Đất!"

if "victim_id" not in st.session_state:
    st.session_state.victim_id = None

if "abduction_event" not in st.session_state:
    st.session_state.abduction_event = 0

if "music_volume" not in st.session_state:
    st.session_state.music_volume = 0.20

# =====================================================
# TIÊU ĐỀ
# =====================================================

st.markdown(
    '<div class="hero-title">🛸 UFO HACK NÃO 👽</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero-subtitle">'
    'THỬ THÁCH TRÍ TUỆ · UFO BẮT CÓC · SINH TỒN NGOÀI HÀNH TINH'
    '</div>',
    unsafe_allow_html=True,
)

# =====================================================
# ÂM NHẠC KHOA HỌC VIỄN TƯỞNG
# =====================================================

st.markdown("## 🔊 NHẠC UFO")

music_col1, music_col2 = st.columns([1, 2])

with music_col1:
    music_enabled = st.toggle(
        "Bật khung nhạc",
        value=True,
        key="music_enabled",
    )

with music_col2:
    st.session_state.music_volume = st.slider(
        "Âm lượng nhạc",
        min_value=0.0,
        max_value=0.60,
        value=float(st.session_state.music_volume),
        step=0.05,
        help="Nên bắt đầu nhỏ rồi tăng dần đến mức nghe thoải mái.",
    )

if music_enabled:
    components.html(
        """
        <div style="
            padding:12px;
            background:#111a35;
            color:white;
            border-radius:12px;
            text-align:center;
            font-family:Arial,sans-serif;
        ">
            <button id="ufo-play" style="
                padding:11px 18px;
                border:0;
                border-radius:9px;
                background:#7c3aed;
                color:white;
                font-weight:bold;
                cursor:pointer;
            ">▶️ PHÁT NHẠC</button>

            <button id="ufo-stop" style="
                padding:11px 18px;
                border:0;
                border-radius:9px;
                background:#334155;
                color:white;
                font-weight:bold;
                cursor:pointer;
            ">⏹ DỪNG NHẠC</button>

            <div style="font-size:12px;margin-top:8px;color:#cbd5e1">
                Bấm PHÁT NHẠC để bắt đầu âm thanh.
            </div>
        </div>

        <script>
        (() => {
            let ctx = null;
            let timer = null;
            let master = null;
            let drone = null;

            const volume = VOLUME_VALUE;

            function stopMusic() {
                if (timer !== null) {
                    clearInterval(timer);
                    timer = null;
                }

                if (ctx !== null) {
                    try {
                        ctx.close();
                    } catch (e) {}
                    ctx = null;
                }

                master = null;
                drone = null;
            }

            function playMusic() {
                stopMusic();

                const AudioContext =
                    window.AudioContext || window.webkitAudioContext;

                if (!AudioContext) {
                    alert("Trình duyệt không hỗ trợ Web Audio.");
                    return;
                }

                ctx = new AudioContext();
                master = ctx.createGain();
                master.gain.value = volume;
                master.connect(ctx.destination);

                drone = ctx.createOscillator();
                const droneGain = ctx.createGain();

                drone.type = "sawtooth";
                drone.frequency.value = 48;
                droneGain.gain.value = 0.055;

                drone.connect(droneGain);
                droneGain.connect(master);
                drone.start();

                let count = 0;

                timer = setInterval(() => {
                    if (!ctx || !master) return;

                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();

                    osc.type = "triangle";
                    osc.frequency.value =
                        count % 2 === 0 ? 74 : 58;

                    gain.gain.setValueAtTime(
                        0.0001,
                        ctx.currentTime
                    );

                    gain.gain.exponentialRampToValueAtTime(
                        0.075,
                        ctx.currentTime + 0.04
                    );

                    gain.gain.exponentialRampToValueAtTime(
                        0.0001,
                        ctx.currentTime + 0.4
                    );

                    osc.connect(gain);
                    gain.connect(master);

                    osc.start();
                    osc.stop(ctx.currentTime + 0.42);

                    count++;
                }, 620);
            }

            document.getElementById("ufo-play").onclick = playMusic;
            document.getElementById("ufo-stop").onclick = stopMusic;
        })();
        </script>
        """.replace(
            "VOLUME_VALUE",
            str(float(st.session_state.music_volume)),
        ),
        height=100,
        scrolling=False,
    )

    st.caption(
        "Nếu chưa có tiếng, hãy bấm PHÁT NHẠC trong khung. "
        "Không nên nghe ở âm lượng quá lớn."
    )

# =====================================================
# QUẢN LÝ NGƯỜI CHƠI
# =====================================================

st.markdown("## 👥 QUẢN LÝ NGƯỜI CHƠI")

players = st.session_state.players

st.write("Số người chơi: **{}/100**".format(len(players)))

add_col, rename_col = st.columns(2)

with add_col:
    if st.button("➕ THÊM 10 NGƯỜI", use_container_width=True):
        current_count = len(st.session_state.players)
        amount = min(10, 100 - current_count)

        next_id = max(
            [p["id"] for p in st.session_state.players],
            default=-1,
        ) + 1

        for i in range(amount):
            st.session_state.players.append(
                {
                    "id": next_id + i,
                    "name": "Người {}".format(next_id + i + 1),
                    "alive": True,
                }
            )

        if amount > 0:
            st.session_state.message = (
                "Đã thêm {} người chơi.".format(amount)
            )
        else:
            st.session_state.message = "Đã đủ 100 người chơi."

        st.rerun()

with rename_col:
    st.write("Bạn có thể đổi tên bất kỳ nhân vật nào trong mục bên dưới.")

with st.expander("✏️ ĐỔI TÊN NHÂN VẬT", expanded=False):
    players = st.session_state.players

    if players:
        player_labels = [
            "{} (ID {})".format(p["name"], p["id"])
            for p in players
        ]

        selected_label = st.selectbox(
            "Chọn nhân vật",
            player_labels,
            key="rename_select",
        )

        selected_index = player_labels.index(selected_label)
        selected_id = players[selected_index]["id"]

        new_name = st.text_input(
            "Nhập tên mới",
            max_chars=24,
            key="rename_input",
        )

        if st.button("💾 LƯU TÊN MỚI", use_container_width=True):
            cleaned = new_name.strip()

            if not cleaned:
                st.warning("Bạn hãy nhập tên trước khi lưu.")
            else:
                for player in st.session_state.players:
                    if player["id"] == selected_id:
                        player["name"] = cleaned
                        break

                st.session_state.message = (
                    "Đã đổi tên nhân vật thành {}.".format(cleaned)
                )
                st.rerun()

# =====================================================
# CÂU ĐỐ HACK NÃO
# =====================================================

riddles = [
    {
        "question": "Cái gì càng lấy đi thì càng lớn?",
        "options": ["Cái hố", "Ngọn núi", "Cái cây", "Dòng sông"],
        "answer": "Cái hố",
        "explanation": "Càng đào đất đi thì cái hố càng lớn.",
    },
    {
        "question": "Tháng nào có 28 ngày?",
        "options": [
            "Tháng 2",
            "Tháng 4",
            "Tất cả các tháng",
            "Tháng 6",
        ],
        "answer": "Tất cả các tháng",
        "explanation": "Tất cả các tháng đều có ít nhất 28 ngày.",
    },
    {
        "question": "Cái gì có cổ nhưng không có đầu?",
        "options": ["Cái chai", "Con hươu", "Cái bàn", "Cái quạt"],
        "answer": "Cái chai",
        "explanation": "Cái chai có cổ chai.",
    },
    {
        "question": "Bạn vượt qua người đứng thứ hai. Bạn đứng thứ mấy?",
        "options": ["Thứ nhất", "Thứ hai", "Thứ ba", "Thứ tư"],
        "answer": "Thứ hai",
        "explanation": "Bạn chiếm vị trí của người đứng thứ hai.",
    },
    {
        "question": "Cái gì có nhiều răng nhưng không cắn được?",
        "options": ["Cá mập", "Cái lược", "Cá sấu", "Con mèo"],
        "answer": "Cái lược",
        "explanation": "Cái lược có răng lược.",
    },
    {
        "question": "Có 5 quả táo, bạn lấy 2 quả. Bạn có mấy quả?",
        "options": ["2", "3", "5", "7"],
        "answer": "2",
        "explanation": "Bạn lấy 2 quả nên bạn có 2 quả.",
    },
    {
        "question": "Cái gì càng lau càng ướt?",
        "options": ["Cái khăn", "Cái bàn", "Cái ghế", "Quyển sách"],
        "answer": "Cái khăn",
        "explanation": "Khăn thấm nước khi lau.",
    },
    {
        "question": "Cái gì luôn đến nhưng không bao giờ là hôm nay?",
        "options": ["Ngày mai", "Hôm qua", "Buổi sáng", "Mặt trời"],
        "answer": "Ngày mai",
        "explanation": "Ngày mai đến thì lại trở thành hôm nay.",
    },
    {
        "question": "Một tuần có bao nhiêu ngày?",
        "options": ["5", "6", "7", "8"],
        "answer": "7",
        "explanation": "Một tuần có 7 ngày.",
    },
    {
        "question": "Cái gì có mặt nhưng không có mũi, miệng?",
        "options": ["Đồng hồ", "Cái ghế", "Cái bàn", "Cái bút"],
        "answer": "Đồng hồ",
        "explanation": "Đồng hồ có mặt đồng hồ.",
    },
]

st.markdown("## 🧠 THỬ THÁCH HACK NÃO")

riddle_index = (st.session_state.round - 1) % len(riddles)
riddle = riddles[riddle_index]

st.markdown(
    """
    <div class="game-card">
        <div style="color:#67e8f9;font-weight:bold">CÂU ĐỐ SỐ {}</div>
        <h3>{}</h3>
    </div>
    """.format(
        st.session_state.round,
        html.escape(riddle["question"]),
    ),
    unsafe_allow_html=True,
)

answer = st.radio(
    "Chọn đáp án:",
    riddle["options"],
    key="answer_round_{}".format(st.session_state.round),
)

answer_col, next_col = st.columns(2)

with answer_col:
    if st.button("✅ KIỂM TRA ĐÁP ÁN", use_container_width=True):
        if st.session_state.round in st.session_state.answered_rounds:
            st.info("Bạn đã trả lời câu này rồi.")
        elif answer == riddle["answer"]:
            st.session_state.score += 1
            st.session_state.answered_rounds.append(
                st.session_state.round
            )
            st.success("🎉 Chính xác! " + riddle["explanation"])
        else:
            st.session_state.answered_rounds.append(
                st.session_state.round
            )
            st.error("Chưa đúng! Đáp án là: " + riddle["answer"])

with next_col:
    if st.button("➡️ CÂU TIẾP THEO", use_container_width=True):
        st.session_state.round += 1
        st.rerun()

st.write("🏆 **Điểm số:** {}".format(st.session_state.score))

# =====================================================
# UFO BẮT NGƯỜI
# =====================================================

st.markdown("## 🛸 UFO ĐANG SĂN NGƯỜI")

players = st.session_state.players
alive_players = [p for p in players if p["alive"]]
captured_count = len(players) - len(alive_players)

stat1, stat2, stat3 = st.columns(3)

with stat1:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">{}</div>
            <div class="stat-label">Tổng người chơi</div>
        </div>
        """.format(len(players)),
        unsafe_allow_html=True,
    )

with stat2:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">{}</div>
            <div class="stat-label">Còn trên mặt đất</div>
        </div>
        """.format(len(alive_players)),
        unsafe_allow_html=True,
    )

with stat3:
    st.markdown(
        """
        <div class="stat-card">
            <div class="stat-number">{}</div>
            <div class="stat-label">Đã bị UFO bắt</div>
        </div>
        """.format(captured_count),
        unsafe_allow_html=True,
    )

if st.button(
    "🚨 CHO UFO BẮT NGẪU NHIÊN",
    type="primary",
    use_container_width=True,
):
    alive_players = [
        p for p in st.session_state.players if p["alive"]
    ]

    if alive_players:
        victim = random.choice(alive_players)
        victim["alive"] = False

        st.session_state.victim_id = victim["id"]
        st.session_state.abduction_event += 1
        st.session_state.message = (
            "🚨 UFO đã bắt {}!".format(victim["name"])
        )
    else:
        st.session_state.message = (
            "Tất cả người chơi đã bị bắt. Hãy chơi lại!"
        )

    st.rerun()

if st.button("🔄 CHƠI LẠI TỪ ĐẦU", use_container_width=True):
    for player in st.session_state.players:
        player["alive"] = True

    st.session_state.victim_id = None
    st.session_state.abduction_event += 1
    st.session_state.round = 1
    st.session_state.score = 0
    st.session_state.answered_rounds = []
    st.session_state.message = "UFO đã quay lại!"

    st.rerun()

st.markdown(
    """
    <div class="game-card" style="text-align:center;font-size:20px">
        {}
    </div>
    """.format(html.escape(st.session_state.message)),
    unsafe_allow_html=True,
)

# =====================================================
# TẠO ĐÁM ĐÔNG VÀ CẢNH UFO
# =====================================================

st.markdown("## 🌌 CẢNH UFO BẮT CÓC")

crowd_html = ""

players = st.session_state.players

# Xếp người thành 10 cột, nhiều hàng.
# Các hàng được đặt gần nhau để tạo cảnh đông đúc.

for index, player in enumerate(players):
    if not player["alive"]:
        continue

    row = index // 10
    col = index % 10

    left = 5 + col * 10 + random.uniform(-2, 2)
    bottom = 7 + row * 7 + random.uniform(-1, 1)

    crowd_html += """
    <div class="person"
         title="{name}"
         style="left:{left:.2f}%;bottom:{bottom:.2f}%;z-index:{z}">
        <div class="person-head">👽</div>
        <div class="person-body"></div>
        <div class="person-name">{name}</div>
    </div>
    """.format(
        name=html.escape(player["name"]),
        left=left,
        bottom=bottom,
        z=10 + row,
    )

captured_html = ""

if st.session_state.victim_id is not None:
    victim = next(
        (
            p for p in players
            if p["id"] == st.session_state.victim_id
        ),
        None,
    )

    if victim:
        captured_html = """
        <div class="captured-person">
            <div class="abduction-beam"></div>
            <div class="abduction-alien">👽</div>
            <div class="abduction-name">{}</div>
        </div>
        """.format(html.escape(victim["name"]))

scene_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    overflow: hidden;
    background: #02040d;
    font-family: Arial, sans-serif;
    color: white;
}

.scene {
    position: relative;
    height: 570px;
    width: 100%;
    overflow: hidden;
    border-radius: 16px;
    border: 1px solid #52639c;
    background:
        radial-gradient(circle at 12% 13%, #fff 1px, transparent 2px),
        radial-gradient(circle at 78% 19%, #fff 1px, transparent 2px),
        radial-gradient(circle at 50% 7%, #fff 1px, transparent 2px),
        radial-gradient(ellipse at bottom, #123847, #071326 48%, #02040d);
    background-size: 100px 100px, 140px 120px, 170px 170px, auto;
}

.moon {
    position: absolute;
    top: 18px;
    right: 7%;
    font-size: 36px;
    filter: drop-shadow(0 0 12px #dbeafe);
}

.ufo {
    position: absolute;
    top: 25px;
    left: 50%;
    width: 170px;
    height: 100px;
    transform: translateX(-50%);
    z-index: 100;
    animation: ufoHover 2s ease-in-out infinite;
}

.ufo-dome {
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

.ufo-disk {
    position: absolute;
    top: 30px;
    width: 170px;
    height: 42px;
    border-radius: 50%;
    border: 3px solid #c4b5fd;
    background: linear-gradient(#b5c8ff, #626bd7 50%, #20264c);
    box-shadow: 0 0 22px #818cf8;
}

.ufo-lights {
    position: absolute;
    top: 49px;
    left: 17px;
    width: 136px;
    display: flex;
    justify-content: space-around;
}

.ufo-lights span {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #a5f3fc;
    box-shadow: 0 0 12px #22d3ee;
    animation: blink .5s infinite alternate;
}

.main-beam {
    position: absolute;
    top: 105px;
    left: 50%;
    transform: translateX(-50%);
    width: 230px;
    height: 360px;
    clip-path: polygon(40% 0, 60% 0, 100% 100%, 0 100%);
    background: linear-gradient(
        to bottom,
        rgba(103, 232, 249, .28),
        rgba(103, 232, 249, .08),
        transparent
    );
    pointer-events: none;
}

.person {
    position: absolute;
    width: 10%;
    max-width: 55px;
    min-width: 25px;
    height: 57px;
    text-align: center;
    transform: translateX(-50%);
}

.person-head {
    font-size: clamp(17px, 3vw, 27px);
    line-height: 27px;
    filter: drop-shadow(0 0 5px #67e8f9);
}

.person-body {
    width: 13px;
    height: 19px;
    margin: auto;
    border-radius: 6px;
    border: 1px solid #c4b5fd;
    background: linear-gradient(#8b5cf6, #312e81);
}

.person-name {
    font-size: 7px;
    color: #e0f2fe;
    max-width: 60px;
    margin: auto;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    text-shadow: 0 0 5px #000;
}

.captured-person {
    position: absolute;
    top: 150px;
    left: 50%;
    width: 120px;
    transform: translateX(-50%);
    text-align: center;
    z-index: 90;
    animation: abduct 3.5s ease-in-out forwards;
}

.abduction-beam {
    position: absolute;
    top: -40px;
    left: 15px;
    width: 90px;
    height: 300px;
    clip-path: polygon(40% 0, 60% 0, 100% 100%, 0 100%);
    background: linear-gradient(
        to top,
        rgba(34, 211, 238, .05),
        rgba(103, 232, 249, .50),
        rgba(34, 211, 238, .08)
    );
    animation: beamFlash .35s infinite alternate;
}

.abduction-alien {
    position: relative;
    z-index: 2;
    font-size: 48px;
    filter: drop-shadow(0 0 15px #67e8f9);
}

.abduction-name {
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
    height: 18px;
    width: 100%;
    background: linear-gradient(#164e63, #07111f);
    border-top: 2px solid #22d3ee;
}

.caption {
    position: absolute;
    bottom: 25px;
    width: 100%;
    text-align: center;
    z-index: 120;
    font-size: 12px;
    font-weight: bold;
    color: #a5f3fc;
    text-shadow: 0 0 7px #0891b2;
    pointer-events: none;
}

@keyframes ufoHover {
    0%, 100% { margin-top: 0; }
    50% { margin-top: -8px; }
}

@keyframes blink {
    from { opacity: .3; }
    to { opacity: 1; }
}

@keyframes beamFlash {
    from { opacity: .4; }
    to { opacity: 1; }
}

@keyframes abduct {
    0% {
        top: 410px;
        opacity: 0;
        transform: translateX(-50%) scale(.65);
    }
    15% { opacity: 1; }
    75% {
        top: 175px;
        opacity: 1;
        transform: translateX(-50%) scale(1);
    }
    100% {
        top: 80px;
        opacity: 0;
        transform: translateX(-50%) scale(.4);
    }
}

@media(max-width: 600px) {
    .scene { height: 520px; }
    .ufo { transform: translateX(-50%) scale(.8); }
    .person { height: 48px; }
    .person-name { font-size: 6px; max-width: 36px; }
    .moon { font-size: 28px; }
}
</style>
</head>
<body>
    <div class="scene">
        <div class="moon">🌙</div>

        <div class="ufo">
            <div class="ufo-dome"></div>
            <div class="ufo-disk"></div>
            <div class="ufo-lights">
                <span></span><span></span><span></span>
                <span></span><span></span><span></span>
            </div>
        </div>

        <div class="main-beam"></div>

        {crowd}

        {captured}

        <div class="ground"></div>
        <div class="caption">🛸 UFO ĐANG QUAN SÁT ĐÁM ĐÔNG 👽</div>
    </div>
</body>
</html>
"""

components.html(
    scene_html.format(
        crowd=crowd_html,
        captured=captured_html,
    ),
    height=590,
    scrolling=False,
)

# =====================================================
# DANH SÁCH NGƯỜI CHƠI
# =====================================================

with st.expander("📋 XEM TẤT CẢ NGƯỜI CHƠI"):
    for player in st.session_state.players:
        status = (
            "🛸 Đã bị bắt"
            if not player["alive"]
            else "🟢 Còn trên mặt đất"
        )

        st.write("{} — {}".format(player["name"], status))

# =====================================================
# CHÂN TRANG
# =====================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;color:#94a3b8;font-size:12px;">
        UFO HACK NÃO · MINI GAME NGOÀI HÀNH TINH
    </div>
    """,
    unsafe_allow_html=True,
)
