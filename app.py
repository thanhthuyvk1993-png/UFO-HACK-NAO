import random
import time
import html
import streamlit as st
import streamlit.components.v1 as components

# ==================================================
# UFO HACK NÃO
# ==================================================

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# GIAO DIỆN
# ==================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.stApp {
    background: radial-gradient(
        ellipse at top,
        #243b80 0%,
        #10132f 55%,
        #080b1c 100%
    );
    color: white;
}

.block-container {
    max-width: 1200px;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

h1, h2, h3, p, label {
    color: white !important;
}

.ufo-title {
    text-align: center;
    font-size: clamp(30px, 5vw, 55px);
    font-weight: 900;
    color: #a9f7ff;
    text-shadow: 0 0 12px #00d9ff, 0 0 30px #8657ff;
}

.ufo-subtitle {
    text-align: center;
    color: #e3dcff;
    margin-bottom: 22px;
}

div.stButton > button {
    width: 100%;
    min-height: 48px;
    border: 0;
    border-radius: 14px;
    background: linear-gradient(135deg, #ff45c8, #7957ff);
    color: white;
    font-weight: 900;
    font-size: 16px;
}

div.stButton > button:hover {
    color: white;
    box-shadow: 0 0 20px #b45cff;
}

.panel {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 18px;
    padding: 18px;
    margin-bottom: 16px;
}

.result {
    text-align: center;
    padding: 22px 12px;
    background: linear-gradient(135deg, #fc43c5, #765cff);
    border-radius: 20px;
    color: white;
    font-size: clamp(20px, 3vw, 28px);
    font-weight: 900;
    overflow-wrap: anywhere;
    box-shadow: 0 0 28px rgba(218, 75, 255, 0.4);
}

div[data-testid="stTextInput"] input {
    border-radius: 10px;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# DỮ LIỆU
# ==================================================

DEFAULT_NAMES = [
    "Thành Thỏ", "Minh Huy", "Phương Mai", "Tuấn Minh",
    "Quỳnh Anh", "Hải", "Mạnh", "Trúc Mai",
    "Huy Khánh", "Đồng An"
]

CHARACTERS = ["🐰", "😎", "👑", "🧙", "💖", "👽", "🐸", "🦊"]

RIDDLES = {
    "Dễ": [
        {
            "q": "Cái gì có nhiều răng nhưng không cắn được?",
            "a": "Cái lược",
            "hint": "Dùng để chải tóc."
        },
        {
            "q": "Càng lấy đi thì nó càng lớn. Là cái gì?",
            "a": "Cái hố",
            "hint": "Thường xuất hiện khi đào đất."
        },
        {
            "q": "Cái gì có cổ nhưng không có đầu?",
            "a": "Cái chai",
            "hint": "Có thể đựng nước."
        }
    ],
    "Trung bình": [
        {
            "q": "Một năm có bao nhiêu tháng có 28 ngày?",
            "a": "12 tháng",
            "hint": "Đừng chỉ nghĩ đến tháng 2."
        },
        {
            "q": "Bạn lấy 2 quả táo từ 3 quả. Bạn có mấy quả?",
            "a": "2 quả",
            "hint": "Bạn đã lấy bao nhiêu quả?"
        },
        {
            "q": "Cái gì luôn ở phía trước bạn nhưng không thể nhìn thấy?",
            "a": "Tương lai",
            "hint": "Nó chưa xảy ra."
        }
    ],
    "Hack não": [
        {
            "q": "Bố của Nam có 5 người con: Nana, Nene, Nini, Nono. Người con thứ 5 tên gì?",
            "a": "Nam",
            "hint": "Đọc câu đầu tiên thật kỹ."
        },
        {
            "q": "Bạn vượt qua người đứng thứ hai trong cuộc đua. Bạn đứng thứ mấy?",
            "a": "Thứ hai",
            "hint": "Bạn thay thế vị trí của người đó."
        },
        {
            "q": "Một người đi dưới mưa không mang ô, tóc không ướt. Vì sao?",
            "a": "Vì người đó bị hói",
            "hint": "Hãy nghĩ đến mái tóc."
        },
        {
            "q": "Có 10 con cá trong bể, 2 con chết. Còn bao nhiêu con cá trong bể?",
            "a": "10 con",
            "hint": "Cá chết vẫn ở trong bể."
        }
    ]
}

# ==================================================
# TRẠNG THÁI
# ==================================================

if "players" not in st.session_state:
    st.session_state.players = DEFAULT_NAMES.copy()

if "selected" not in st.session_state:
    st.session_state.selected = None

if "riddle" not in st.session_state:
    st.session_state.riddle = None

if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

if "rounds" not in st.session_state:
    st.session_state.rounds = 0

if "volume" not in st.session_state:
    st.session_state.volume = 35

if "music_on" not in st.session_state:
    st.session_state.music_on = False

# ==================================================
# TIÊU ĐỀ
# ==================================================

st.markdown(
    '<div class="ufo-title">🛸 UFO HACK NÃO 🛸</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="ufo-subtitle">'
    '🌌 Vũ trụ bí ẩn • Thử thách trí tuệ • Ai sẽ bị UFO bắt?'
    '</div>',
    unsafe_allow_html=True
)

# ==================================================
# CÀI ĐẶT NGƯỜI CHƠI
# ==================================================

st.markdown("## ⚙️ Cài đặt trò chơi")

col1, col2 = st.columns(2)

with col1:
    player_count = st.number_input(
        "👥 Số lượng người chơi",
        min_value=2,
        max_value=100,
        value=len(st.session_state.players),
        step=1
    )

with col2:
    difficulty = st.selectbox(
        "🧠 Chọn cấp độ",
        ["Dễ", "Trung bình", "Hack não"]
    )

# Đồng bộ số lượng người chơi
names = list(st.session_state.players)

while len(names) < player_count:
    names.append(f"Người chơi {len(names) + 1}")

names = names[:player_count]
st.session_state.players = names

# ==================================================
# ĐỔI TÊN NHÂN VẬT
# ==================================================

with st.expander("✏️ ĐỔI TÊN TỪNG NHÂN VẬT", expanded=False):

    st.caption("Nhập tên mới cho từng người rồi bấm Lưu tên.")

    with st.form("rename_form"):

        edited_names = []

        for start in range(0, int(player_count), 3):
            cols = st.columns(3)

            for j in range(3):
                index = start + j

                if index >= player_count:
                    break

                with cols[j]:
                    new_name = st.text_input(
                        f"Nhân vật {index + 1}",
                        value=st.session_state.players[index],
                        key=f"rename_{index}"
                    )
                    edited_names.append(new_name)

        save_names = st.form_submit_button("💾 LƯU TÊN")

    if save_names:
        st.session_state.players = [
            name.strip() or f"Người chơi {i + 1}"
            for i, name in enumerate(edited_names)
        ]

        st.session_state.selected = None
        st.session_state.riddle = None
        st.session_state.show_answer = False

        st.success("Đã lưu tên nhân vật!")
        st.rerun()

# ==================================================
# NHẠC NỀN HỒI HỘP
# ==================================================

st.markdown("## 🎵 Nhạc nền")

st.caption(
    "Bấm phát nhạc để nghe nhạc điện tử hồi hộp. "
    "Âm thanh được tạo trực tiếp trong trình duyệt."
)

music_col1, music_col2 = st.columns([2, 1])

with music_col1:
    music_on = st.toggle(
        "🎶 Bật nhạc nền",
        value=st.session_state.music_on,
        key="music_toggle"
    )
    st.session_state.music_on = music_on

with music_col2:
    volume = st.slider(
        "🔊 Âm lượng",
        min_value=0,
        max_value=100,
        value=st.session_state.volume,
        key="music_volume"
    )
    st.session_state.volume = volume

# Trình phát nhạc riêng trong iframe.
# Trạng thái bật/tắt được truyền vào iframe.
music_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    margin: 0;
    background: transparent;
    color: white;
    font-family: Arial, sans-serif;
    text-align: center;
}
button {
    border: 0;
    border-radius: 12px;
    padding: 12px 20px;
    font-size: 15px;
    font-weight: bold;
    color: white;
    background: linear-gradient(135deg,#ff45c8,#7957ff);
}
</style>
</head>
<body>
<div style="padding:8px">
    <div style="font-size:28px">🎼 🛸 🎼</div>
    <button id="btn">▶ PHÁT NHẠC</button>
    <div id="status" style="margin-top:8px;font-size:12px">
        Bấm nút để bắt đầu âm thanh
    </div>
</div>
<script>
let ctx = null;
let master = null;
let timer = null;
let playing = false;
let noteIndex = 0;

function note(freq, duration, type, vol) {
    if (!ctx || !master) return;

    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = type;
    osc.frequency.value = freq;

    gain.gain.setValueAtTime(0.0001, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(
        Math.max(0.0002, vol),
        ctx.currentTime + 0.04
    );
    gain.gain.exponentialRampToValueAtTime(
        0.0001,
        ctx.currentTime + duration
    );

    osc.connect(gain);
    gain.connect(master);

    osc.start();
    osc.stop(ctx.currentTime + duration + 0.05);
}

function loop() {
    if (!playing) return;

    const notes = [110,130.81,164.81,146.83,98,123.47,185,146.83];
    const n = notes[noteIndex % notes.length];

    note(n, 0.6, "triangle", 0.15);
    note(n * 2, 0.25, "sine", 0.055);

    if (noteIndex % 2 === 0) {
        note(55, 0.25, "sine", 0.16);
    }

    if (noteIndex % 4 === 3) {
        note(n * 4, 0.4, "sine", 0.035);
    }

    noteIndex++;
}

async function toggleMusic() {
    if (!ctx) {
        ctx = new (window.AudioContext || window.webkitAudioContext)();
        master = ctx.createGain();
        master.gain.value = 0.7;
        master.connect(ctx.destination);
    }

    if (ctx.state === "suspended") {
        await ctx.resume();
    }

    if (!playing) {
        playing = true;
        loop();
        timer = setInterval(loop, 380);
        document.getElementById("btn").innerText = "⏸ TẮT NHẠC";
        document.getElementById("status").innerText = "🎵 Nhạc đang phát";
    } else {
        playing = false;
        clearInterval(timer);
        document.getElementById("btn").innerText = "▶ PHÁT NHẠC";
        document.getElementById("status").innerText = "Nhạc đã tắt";
    }
}

document.getElementById("btn").addEventListener("click", toggleMusic);
</script>
</body>
</html>
"""

components.html(music_html, height=110)

st.info(
    "Lưu ý: trình phát nhạc chạy trong khung riêng. "
    "Bạn cần bấm nút phát nhạc trong khung đó; "
    "âm thanh có thể dừng khi trang được tải lại."
)

# ==================================================
# UFO CHỌN NGƯỜI
# ==================================================

st.markdown("---")
st.markdown("## 🛸 UFO ĐANG QUÉT TÍN HIỆU")

st.markdown(
    f"""
    <div class="panel" style="text-align:center;">
        <div style="font-size:clamp(55px,10vw,100px);">🛸</div>
        <div style="font-size:20px;font-weight:900;color:#a9f7ff;">
            HỆ THỐNG UFO SẴN SÀNG
        </div>
        <div style="margin-top:8px;">
            👥 {len(st.session_state.players)} người chơi
            &nbsp; | &nbsp; 🧠 {difficulty}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col_start, col_reset = st.columns(2)

with col_start:
    start_game = st.button(
        "🚀 KÍCH HOẠT UFO",
        use_container_width=True
    )

with col_reset:
    reset_game = st.button(
        "🔄 VÁN MỚI",
        use_container_width=True
    )

if reset_game:
    st.session_state.selected = None
    st.session_state.riddle = None
    st.session_state.show_answer = False
    st.rerun()

if start_game:
    animation = st.empty()

    for i in range(10):
        random_name = random.choice(st.session_state.players)

        animation.markdown(
            f"""
            <div class="result">
                🛸 UFO ĐANG QUÉT...
                <br><br>
                📡 {html.escape(random_name)}
                <br><br>
                ✨ ĐANG KHÓA MỤC TIÊU ✨
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.1 + i * 0.025)

    st.session_state.selected = random.choice(
        st.session_state.players
    )

    st.session_state.riddle = random.choice(
        RIDDLES[difficulty]
    )

    st.session_state.show_answer = False
    st.session_state.rounds += 1

    st.rerun()

# ==================================================
# KẾT QUẢ UFO
# ==================================================

if st.session_state.selected:

    selected = st.session_state.selected

    st.markdown(
        f"""
        <div class="result">
            🛸 UFO ĐÃ BẮT ĐƯỢC!
            <br><br>
            🌟 {html.escape(selected)} 🌟
            <br><br>
            😈 CHUẨN BỊ GIẢI MÃ!
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🧠 THỬ THÁCH DÀNH CHO NGƯỜI BỊ BẮT")

    riddle = st.session_state.riddle

    st.markdown(
        f"""
        <div class="panel" style="text-align:center;">
            <div style="font-size:17px;color:#c7c4ff;">
                CẤP ĐỘ: {html.escape(difficulty.upper())}
            </div>
            <div style="
                font-size:clamp(19px,3vw,27px);
                font-weight:900;
                margin-top:15px;
            ">
                {html.escape(riddle["q"])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.expander("💡 GỢI Ý BÍ MẬT"):
        st.write(riddle["hint"])

    if st.button("🔓 GIẢI MÃ ĐÁP ÁN"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        st.success(f"🎯 Đáp án: {riddle['a']}")

        if st.button("🛸 CHỌN NGƯỜI TIẾP THEO"):
            st.session_state.selected = None
            st.session_state.riddle = None
            st.session_state.show_answer = False
            st.rerun()

# ==================================================
# DANH SÁCH NHÂN VẬT RESPONSIVE
# ==================================================

st.markdown("---")
st.markdown("## 👾 PHI ĐỘI NGƯỜI CHƠI")

names = st.session_state.players
selected = st.session_state.selected

st.markdown(
    f"""
    <div class="panel" style="text-align:center;">
        <div style="font-size:20px;font-weight:900;">
            👥 ĐANG CÓ {len(names)} NGƯỜI CHƠI
        </div>
        <div style="margin-top:8px;overflow-wrap:anywhere;">
            🛸 UFO ĐÃ CHỌN:
            {html.escape(selected) if selected else "CHƯA CHỌN"}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

cards = []

for index, name in enumerate(names):
    avatar = CHARACTERS[index % len(CHARACTERS)]
    safe_name = html.escape(name)

    if name == selected:
        card = f"""
        <div class="player-card selected-card">
            <div class="player-avatar">🛸</div>
            <div class="player-avatar">{avatar}</div>
            <div class="player-name">{safe_name}</div>
            <div class="status">🎯 ĐÃ BỊ BẮT</div>
        </div>
        """
    else:
        card = f"""
        <div class="player-card">
            <div class="player-avatar">{avatar}</div>
            <div class="player-name">{safe_name}</div>
            <div class="status">👾 SẴN SÀNG</div>
        </div>
        """

    cards.append(card)

cards_html = "".join(cards)

# Khung độc lập, tự đổi số cột theo độ rộng màn hình.
# Chiều cao được tính theo số hàng trên điện thoại.
players_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {{
    box-sizing: border-box;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    background: transparent;
    color: white;
    font-family: Arial, sans-serif;
}}

.players-grid {{
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 8px;
    width: 100%;
}}

.player-card {{
    min-width: 0;
    min-height: 90px;
    padding: 8px 3px;
    text-align: center;
    overflow-wrap: anywhere;
    word-break: break-word;
    border: 1px solid #8b78ff;
    border-radius: 12px;
    background: linear-gradient(135deg, #282d65, #46286d);
}}

.player-avatar {{
    font-size: clamp(20px, 4vw, 32px);
    line-height: 1.35;
}}

.player-name {{
    font-size: clamp(10px, 1.5vw, 14px);
    font-weight: bold;
    overflow-wrap: anywhere;
}}

.status {{
    margin-top: 4px;
    font-size: 10px;
    color: #d8d0ff;
}}

.selected-card {{
    background: linear-gradient(135deg, #ff42c8, #ff8b5e);
    border: 2px solid #fff3a3;
    box-shadow: 0 0 15px #ff45c8;
}}

@media (max-width: 600px) {{
    .players-grid {{
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 5px;
    }}

    .player-card {{
        min-height: 80px;
        padding: 6px 2px;
        border-radius: 9px;
    }}

    .player-avatar {{
        font-size: 24px;
    }}

    .player-name {{
        font-size: 11px;
    }}

    .status {{
        font-size: 9px;
    }}
}}

@media (min-width: 601px) and (max-width: 900px) {{
    .players-grid {{
        grid-template-columns: repeat(4, minmax(0, 1fr));
    }}
}}
</style>
</head>
<body>
    <div class="players-grid">
        {cards_html}
    </div>
</body>
</html>
"""

# 3 cột trên điện thoại, 4 trên máy tính bảng,
# 5 trên máy tính. Ước lượng chiều cao theo số hàng.
if len(names) <= 0:
    rows = 1
else:
    rows = (len(names) + 2) // 3

components.html(
    players_html,
    height=max(100, rows * 95 + 15),
    scrolling=False
)

# ==================================================
# CHÂN TRANG
# ==================================================

st.markdown("---")

st.markdown(
    f"""
    <div style="text-align:center;color:#c6c2ff;padding:15px;">
        🛸 UFO HACK NÃO
        <br>
        🌌 Số ván đã chơi: {st.session_state.rounds}
        <br>
        ✨ Chúc bạn chơi vui vẻ!
    </div>
    """,
    unsafe_allow_html=True
)
