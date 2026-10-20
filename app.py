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
# CẤU HÌNH
# =========================

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(ellipse at top, #18264d 0%, #070b1b 55%, #02040c 100%);
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

.block-container {
    padding-top: 1.2rem;
    max-width: 1400px;
}

div.stButton > button {
    border-radius: 12px;
    font-weight: bold;
    min-height: 44px;
}

div.stButton > button[kind="primary"] {
    background: #7c3aed;
    border: 1px solid #c4b5fd;
}

.game-title {
    text-align: center;
    font-size: clamp(30px, 5vw, 56px);
    font-weight: 1000;
    color: #a5f3fc;
    text-shadow: 0 0 18px #06b6d4, 0 0 35px #7c3aed;
    margin-bottom: 4px;
}

.game-subtitle {
    text-align: center;
    color: #c4b5fd;
    margin-bottom: 22px;
}

.panel {
    background: rgba(17, 24, 55, 0.88);
    border: 1px solid rgba(129, 140, 248, 0.55);
    border-radius: 16px;
    padding: 16px;
    margin: 10px 0;
    box-shadow: 0 0 20px rgba(99, 102, 241, 0.12);
}

.stat {
    text-align: center;
    background: rgba(30, 41, 80, 0.8);
    border-radius: 12px;
    padding: 12px 5px;
    border: 1px solid #394875;
}

.stat-number {
    color: #67e8f9;
    font-size: 26px;
    font-weight: 900;
}

.stat-label {
    font-size: 13px;
    color: #cbd5e1;
}

.small-note {
    color: #cbd5e1;
    font-size: 13px;
}

div[data-testid="stTextInput"] input {
    background: #111a35;
    color: white;
}

div[data-testid="stNumberInput"] input {
    background: #111a35;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TRẠNG THÁI GAME
# =========================

if "players" not in st.session_state:
    st.session_state.players = [
        {"id": i, "name": f"Người {i + 1}", "alive": True}
        for i in range(20)
    ]

if "selected_id" not in st.session_state:
    st.session_state.selected_id = None

if "round" not in st.session_state:
    st.session_state.round = 1

if "message" not in st.session_state:
    st.session_state.message = "UFO đang bay quanh Trái Đất..."

if "music_on" not in st.session_state:
    st.session_state.music_on = True

if "volume" not in st.session_state:
    st.session_state.volume = 0.35

if "music_started" not in st.session_state:
    st.session_state.music_started = False

if "last_abducted" not in st.session_state:
    st.session_state.last_abducted = None

# =========================
# TIÊU ĐỀ
# =========================

st.markdown(
    '<div class="game-title">🛸 UFO HACK NÃO 👽</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="game-subtitle">Bầu trời đang có biến... Ai sẽ bị UFO bắt tiếp theo?</div>',
    unsafe_allow_html=True
)

# =========================
# NHẠC HỒI HỘP
# =========================

with st.expander("🔊 CÀI ĐẶT NHẠC HỒI HỘP", expanded=True):
    music_col1, music_col2 = st.columns([1, 2])

    with music_col1:
        st.session_state.music_on = st.toggle(
            "Bật nhạc nền",
            value=st.session_state.music_on,
            key="music_toggle"
        )

    with music_col2:
        st.session_state.volume = st.slider(
            "Âm lượng",
            min_value=0.0,
            max_value=1.0,
            value=float(st.session_state.volume),
            step=0.05,
            help="Nên bắt đầu ở mức thấp rồi tăng từ từ để bảo vệ thính giác."
        )

    st.caption(
        "Lưu ý: Trình duyệt có thể yêu cầu bạn bấm nút bên dưới trước khi phát nhạc."
    )

    if st.button("▶️ KÍCH HOẠT NHẠC", use_container_width=True):
        st.session_state.music_started = True

    # Âm thanh được tạo trực tiếp trong trình duyệt.
    # Nhạc chỉ bắt đầu sau thao tác bấm nút của người dùng.
    if st.session_state.music_started and st.session_state.music_on:
        volume_value = float(st.session_state.volume)

        components.html(
            f"""
            <div style="font-family:Arial;color:white;background:#111a35;
                        border-radius:12px;padding:10px;text-align:center;">
              <span>🎵 Nhạc nền UFO đang hoạt động trong khung này</span>
              <br>
              <button id="startMusic"
                style="margin-top:8px;padding:10px 16px;border-radius:9px;
                       border:0;background:#7c3aed;color:white;font-weight:bold;">
                BẬT / PHÁT NHẠC
              </button>
              <button id="stopMusic"
                style="margin-top:8px;padding:10px 16px;border-radius:9px;
                       border:0;background:#334155;color:white;font-weight:bold;">
                TẮT NHẠC
              </button>
            </div>

            <script>
            (() => {{
                let ctx = null;
                let master = null;
                let oscillators = [];
                let timer = null;

                function stopAudio() {{
                    if (timer) {{
                        clearInterval(timer);
                        timer = null;
                    }}

                    oscillators.forEach(o => {{
                        try {{ o.stop(); }} catch(e) {{}}
                    }});
                    oscillators = [];

                    if (ctx) {{
                        try {{ ctx.close(); }} catch(e) {{}}
                        ctx = null;
                    }}
                }}

                function startAudio() {{
                    stopAudio();

                    const AudioContext =
                        window.AudioContext || window.webkitAudioContext;

                    if (!AudioContext) {{
                        alert("Trình duyệt không hỗ trợ phát âm thanh.");
                        return;
                    }}

                    ctx = new AudioContext();
                    master = ctx.createGain();
                    master.gain.value = {volume_value};
                    master.connect(ctx.destination);

                    const drone = ctx.createOscillator();
                    const droneGain = ctx.createGain();

                    drone.type = "sawtooth";
                    drone.frequency.value = 48;
                    droneGain.gain.value = 0.10;

                    drone.connect(droneGain);
                    droneGain.connect(master);
                    drone.start();

                    oscillators.push(drone);

                    const bass = ctx.createOscillator();
                    const bassGain = ctx.createGain();

                    bass.type = "sine";
                    bass.frequency.value = 42;
                    bassGain.gain.value = 0.16;

                    bass.connect(bassGain);
                    bassGain.connect(master);
                    bass.start();

                    oscillators.push(bass);

                    let beat = 0;

                    timer = setInterval(() => {{
                        if (!ctx || !master) return;

                        beat++;

                        const note = beat % 2 === 0 ? 72 : 58;
                        const pulse = ctx.createOscillator();
                        const pulseGain = ctx.createGain();

                        pulse.type = "triangle";
                        pulse.frequency.value = note;
                        pulseGain.gain.setValueAtTime(
                            0.0001, ctx.currentTime
                        );
                        pulseGain.gain.exponentialRampToValueAtTime(
                            0.12, ctx.currentTime + 0.03
                        );
                        pulseGain.gain.exponentialRampToValueAtTime(
                            0.0001, ctx.currentTime + 0.35
                        );

                        pulse.connect(pulseGain);
                        pulseGain.connect(master);
                        pulse.start();
                        pulse.stop(ctx.currentTime + 0.4);
                    }}, 650);
                }}

                document.getElementById("startMusic").onclick = startAudio;
                document.getElementById("stopMusic").onclick = stopAudio;
            }})();
            </script>
            """,
            height=95
        )

    elif not st.session_state.music_on:
        st.info("Nhạc nền đang tắt.")

# =========================
# QUẢN LÝ NGƯỜI CHƠI
# =========================

st.markdown("## 👥 QUẢN LÝ NGƯỜI CHƠI")

col_count, col_add = st.columns([1, 1])

with col_count:
    st.write(f"**Số người hiện tại: {len(st.session_state.players)}/100**")

with col_add:
    if st.button("➕ THÊM 10 NGƯỜI", use_container_width=True):
        current_count = len(st.session_state.players)
        amount = min(10, 100 - current_count)

        for _ in range(amount):
            new_id = max(
                [p["id"] for p in st.session_state.players],
                default=-1
            ) + 1

            st.session_state.players.append({
                "id": new_id,
                "name": f"Người {new_id + 1}",
                "alive": True
            })

        if amount > 0:
            st.session_state.message = f"Đã thêm {amount} người chơi."
        else:
            st.session_state.message = "Đã đủ 100 người chơi."

st.caption("Bạn có thể đổi tên người chơi ở bên dưới.")

with st.expander("✏️ ĐỔI TÊN NHÂN VẬT", expanded=False):
    if st.session_state.players:
        player_options = {
            f'{p["name"]} (ID {p["id"]})': p["id"]
            for p in st.session_state.players
        }

        selected_label = st.selectbox(
            "Chọn nhân vật",
            list(player_options.keys())
        )

        rename_id = player_options[selected_label]

        new_name = st.text_input(
            "Tên mới",
            max_chars=24,
            key=f"rename_{rename_id}"
        )

        if st.button("LƯU TÊN MỚI"):
            cleaned = new_name.strip()

            if cleaned:
                for p in st.session_state.players:
                    if p["id"] == rename_id:
                        p["name"] = cleaned
                        break

                st.session_state.message = f"Đã đổi tên thành {cleaned}."
                st.rerun()
            else:
                st.warning("Hãy nhập tên trước khi lưu.")

# =========================
# CÂU ĐỐ HACK NÃO
# =========================

riddles = [
    {
        "question": "Cái gì càng lấy đi thì càng lớn?",
        "options": ["Cái hố", "Ngọn núi", "Cái cây", "Dòng sông"],
        "answer": "Cái hố",
        "explain": "Càng đào đất đi thì cái hố càng lớn."
    },
    {
        "question": "Tháng nào có 28 ngày?",
        "options": ["Tháng 2", "Tháng 4", "Tất cả các tháng", "Tháng 6"],
        "answer": "Tất cả các tháng",
        "explain": "Tháng nào cũng có ít nhất 28 ngày."
    },
    {
        "question": "Cái gì có cổ nhưng không có đầu?",
        "options": ["Cái chai", "Con hươu", "Cái bàn", "Cái quạt"],
        "answer": "Cái chai",
        "explain": "Cái chai có phần cổ chai nhưng không có đầu."
    },
    {
        "question": "Bạn vượt qua người đứng thứ hai trong cuộc đua. Bạn đứng thứ mấy?",
        "options": ["Thứ nhất", "Thứ hai", "Thứ ba", "Thứ tư"],
        "answer": "Thứ hai",
        "explain": "Bạn chiếm vị trí của người đứng thứ hai."
    },
    {
        "question": "Cái gì có nhiều răng nhưng không cắn được?",
        "options": ["Con cá mập", "Cái lược", "Con cá sấu", "Con mèo"],
        "answer": "Cái lược",
        "explain": "Cái lược có răng lược nhưng không thể cắn."
    },
    {
        "question": "Một con vịt đi trước hai con vịt, một con đi sau hai con vịt. Có mấy con vịt?",
        "options": ["2", "3", "4", "5"],
        "answer": "3",
        "explain": "Ba con vịt đi thành một hàng."
    },
    {
        "question": "Cái gì luôn đi tới nhưng không bao giờ tới nơi?",
        "options": ["Ngày mai", "Hôm qua", "Buổi sáng", "Mặt trời"],
        "answer": "Ngày mai",
        "explain": "Ngày mai đến thì lại trở thành hôm nay."
    },
    {
        "question": "Có 5 quả táo, bạn lấy 2 quả. Bạn có mấy quả?",
        "options": ["2", "3", "5", "7"],
        "answer": "2",
        "explain": "Bạn lấy 2 quả nên bạn có 2 quả."
    },
    {
        "question": "Cái gì càng lau càng ướt?",
        "options": ["Cái khăn", "Cái bàn", "Cái ghế", "Quyển sách"],
        "answer": "Cái khăn",
        "explain": "Khăn thấm nước khi lau nên trở nên ướt."
    },
    {
        "question": "Một năm có bao nhiêu tháng có 30 ngày trở lên?",
        "options": ["4", "6", "11", "12"],
        "answer": "11",
        "explain": "Tất cả trừ tháng 2 đều có ít nhất 30 ngày."
    }
]

st.markdown("## 🧠 THỬ THÁCH HACK NÃO")

riddle = riddles[(st.session_state.round - 1) % len(riddles)]

st.markdown(
    f"""
    <div class="panel">
      <div style="color:#a5f3fc;font-weight:bold;">
        CÂU ĐỐ SỐ {st.session_state.round}
      </div>
      <h3>{html.escape(riddle["question"])}</h3>
    </div>
    """,
    unsafe_allow_html=True
)

answer = st.radio(
    "Chọn đáp án:",
    riddle["options"],
    key=f"riddle_{st.session_state.round}"
)

answer_col1, answer_col2 = st.columns(2)

with answer_col1:
    if st.button("✅ KIỂM TRA ĐÁP ÁN", use_container_width=True):
        if answer == riddle["answer"]:
            st.success("🎉 Chính xác! " + riddle["explain"])
        else:
            st.error("👾 Chưa đúng! Đáp án là: " + riddle["answer"])

with answer_col2:
    if st.button("➡️ CÂU TIẾP THEO", use_container_width=True):
        st.session_state.round += 1
        st.rerun()

# =========================
# UFO BẮT NGƯỜI
# =========================

st.markdown("## 🛸 UFO ĐANG SĂN NGƯỜI")

alive_players = [
    p for p in st.session_state.players if p["alive"]
]

stat1, stat2, stat3 = st.columns(3)

with stat1:
    st.markdown(
        f"""
        <div class="stat">
          <div class="stat-number">{len(st.session_state.players)}</div>
          <div class="stat-label">Tổng người chơi</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with stat2:
    st.markdown(
        f"""
        <div class="stat">
          <div class="stat-number">{len(alive_players)}</div>
          <div class="stat-label">Còn trên mặt đất</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with stat3:
    st.markdown(
        f"""
        <div class="stat">
          <div class="stat-number">{len(st.session_state.players) - len(alive_players)}</div>
          <div class="stat-label">Đã bị UFO bắt</div>
        </div>
        """,
        unsafe_allow_html=True
    )

ufo_col1, ufo_col2 = st.columns(2)

with ufo_col1:
    if st.button(
        "🛸 CHO UFO BẮT NGẪU NHIÊN",
        type="primary",
        use_container_width=True
    ):
        if alive_players:
            victim = random.choice(alive_players)
            victim["alive"] = False

            st.session_state.selected_id = victim["id"]
            st.session_state.last_abducted = victim["id"]
            st.session_state.message = (
                f'🚨 UFO đã bắt {victim["name"]}!'
            )
        else:
            st.session_state.message = (
                "Không còn ai trên mặt đất! Hãy chơi lại."
            )

with ufo_col2:
    if st.button("🔄 CHƠI LẠI TỪ ĐẦU", use_container_width=True):
        for p in st.session_state.players:
            p["alive"] = True

        st.session_state.selected_id = None
        st.session_state.last_abducted = None
        st.session_state.round = 1
        st.session_state.message = "UFO quay lại săn người!"
        st.rerun()

st.markdown(
    f"""
    <div class="panel" style="text-align:center;font-size:20px;">
      {html.escape(st.session_state.message)}
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# CẢNH UFO VÀ ĐÁM ĐÔNG
# =========================

players = st.session_state.players
abducted_id = st.session_state.last_abducted

crowd_html = ""

for index, p in enumerate(players):
    # Xếp thành nhiều hàng nhỏ, nhân vật hơi chồng lên nhau.
    row = index // 10
    col = index % 10

    left = 3 + col * 9.5 + random.uniform(-1.8, 1.8)
    bottom = 8 + row * 7.1 + random.uniform(-1.2, 1.2)

    if not p["alive"]:
        # Người đã bị bắt nằm trên UFO, không xuất hiện trong đám đông.
        continue

    safe_name = html.escape(p["name"])

    crowd_html += f"""
    <div class="person"
         title="{safe_name}"
         style="left:{left:.2f}%;bottom:{bottom:.2f}%;
                z-index:{10 + row};">
        <div class="person-head">👽</div>
        <div class="person-body"></div>
        <div class="person-name">{safe_name}</div>
    </div>
    """

abducted_html = ""

if abducted_id is not None:
    victim = next(
        (p for p in players if p["id"] == abducted_id),
        None
    )

    if victim:
        abducted_html = f"""
        <div class="captured">
          <div class="captured-beam"></div>
          <div class="captured-person">👽</div>
          <div class="captured-label">
            {html.escape(victim["name"])}
          </div>
        </div>
        """

st.markdown("### 🌌 CẢNH UFO BẮT CÓC")

components.html(
    f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      * {{ box-sizing:border-box; }}

      body {{
        margin:0;
        background:#030615;
        font-family:Arial,sans-serif;
        color:white;
        overflow:hidden;
      }}

      .scene {{
        position:relative;
        width:100%;
        height:570px;
        overflow:hidden;
        border-radius:18px;
        border:1px solid #5666a6;
        background:
          radial-gradient(circle at 20% 18%, #ffffff 0 1px, transparent 2px),
          radial-gradient(circle at 78% 27%, #ffffff 0 1px, transparent 2px),
          radial-gradient(circle at 60% 14%, #ffffff 0 1px, transparent 2px),
          radial-gradient(ellipse at bottom, #123a46 0%, #071326 43%, #02040e 100%);
        background-size:100px 100px, 140px 120px, 190px 170px, auto;
      }}

      .moon {{
        position:absolute;
        top:55px;
        right:7%;
        font-size:44px;
        filter:drop-shadow(0 0 14px #dbeafe);
      }}

      .ufo {{
        position:absolute;
        top:35px;
        left:50%;
        transform:translateX(-50%);
        z-index:100;
        width:170px;
        height:100px;
        animation:hover 2s ease-in-out infinite;
      }}

      .ufo-top {{
        position:absolute;
        top:0;
        left:50%;
        transform:translateX(-50%);
        width:65px;
        height:38px;
        border-radius:50% 50% 20% 20%;
        background:linear-gradient(120deg,#b7f7ff,#6877dc,#272a65);
        border:2px solid #a5f3fc;
        box-shadow:0 0 22px #22d3ee;
      }}

      .ufo-base {{
        position:absolute;
        top:28px;
        left:0;
        width:170px;
        height:42px;
        border-radius:50%;
        border:3px solid #b8c7ff;
        background:linear-gradient(#b5c8ff,#626bd7 50%,#20264c);
        box-shadow:0 0 22px #818cf8;
      }}

      .ufo-light {{
        position:absolute;
        top:54px;
        left:12px;
        width:146px;
        display:flex;
        justify-content:space-around;
      }}

      .ufo-light span {{
        width:9px;
        height:9px;
        background:#a5f3fc;
        border-radius:50%;
        box-shadow:0 0 12px #22d3ee;
        animation:blink .6s infinite alternate;
      }}

      .beam {{
        position:absolute;
        top:110px;
        left:50%;
        transform:translateX(-50%);
        width:240px;
        height:380px;
        background:linear-gradient(
          to bottom,
          rgba(103,232,249,.4),
          rgba(103,232,249,.12) 55%,
          transparent
        );
        clip-path:polygon(38% 0,62% 0,100% 100%,0 100%);
        opacity:.8;
        pointer-events:none;
      }}

      .ground {{
        position:absolute;
        bottom:0;
        left:0;
        width:100%;
        height:24px;
        background:linear-gradient(#164e63,#07111f);
        border-top:2px solid #22d3ee;
      }}

      .person {{
        position:absolute;
        width:10%;
        min-width:25px;
        max-width:56px;
        height:62px;
        text-align:center;
        transform:translateX(-50%);
        animation:personWiggle 2s ease-in-out infinite alternate;
      }}

      .person-head {{
        font-size:clamp(17px,3vw,28px);
        line-height:28px;
        filter:drop-shadow(0 0 5px #67e8f9);
      }}

      .person-body {{
        width:14px;
        height:22px;
        margin:-1px auto 0;
        background:linear-gradient(#8b5cf6,#312e81);
        border:1px solid #c4b5fd;
        border-radius:7px 7px 4px 4px;
      }}

      .person-name {{
        font-size:8px;
        white-space:nowrap;
        overflow:hidden;
        text-overflow:ellipsis;
        color:#e0f2fe;
        max-width:62px;
        margin:1px auto 0;
        text-shadow:0 0 5px #000;
      }}

      .captured {{
        position:absolute;
        top:135px;
        left:50%;
        transform:translateX(-50%);
        z-index:90;
        width:120px;
        text-align:center;
        animation:beamUp 3.5s ease-in-out forwards;
      }}

      .captured-person {{
        position:relative;
        z-index:2;
        font-size:48px;
        filter:drop-shadow(0 0 15px #67e8f9);
      }}

      .captured-label {{
        background:rgba(2,6,23,.8);
        border:1px solid #67e8f9;
        border-radius:7px;
        padding:4px;
        font-size:12px;
        overflow-wrap:anywhere;
      }}

      .captured-beam {{
        position:absolute;
        top:0;
        left:50%;
        transform:translateX(-50%);
        height:300px;
        width:90px;
        background:linear-gradient(
          to top,
          rgba(34,211,238,.05),
          rgba(103,232,249,.5),
          rgba(34,211,238,.08)
        );
        clip-path:polygon(40% 0,60% 0,100% 100%,0 100%);
        animation:beamFlash .35s infinite alternate;
      }}

      .scene-title {{
        position:absolute;
        left:0;
        right:0;
        bottom:30px;
        z-index:120;
        text-align:center;
        font-weight:bold;
        font-size:13px;
        color:#a5f3fc;
        text-shadow:0 0 8px #0891b2;
        pointer-events:none;
      }}

      @keyframes hover {{
        0%,100% {{ margin-top:0; }}
        50% {{ margin-top:-10px; }}
      }}

      @keyframes blink {{
        from {{ opacity:.3; }}
        to {{ opacity:1; }}
      }}

      @keyframes personWiggle {{
        from {{ margin-left:-1px; }}
        to {{ margin-left:1px; }}
      }}

      @keyframes beamFlash {{
        from {{ opacity:.5; }}
        to {{ opacity:1; }}
      }}

      @keyframes beamUp {{
        0% {{ top:410px; opacity:0; transform:translateX(-50%) scale(.7); }}
        12% {{ opacity:1; }}
        75% {{ top:170px; opacity:1; transform:translateX(-50%) scale(1); }}
        100% {{ top:88px; opacity:0; transform:translateX(-50%) scale(.45); }}
      }}

      @media(max-width:600px) {{
        .scene {{ height:520px; }}
        .ufo {{ transform:translateX(-50%) scale(.8); }}
        .moon {{ font-size:32px; }}
        .person {{ height:48px; }}
        .person-name {{ font-size:6px; max-width:38px; }}
        .captured-person {{ font-size:40px; }}
      }}
    </style>
    </head>

    <body>
      <div class="scene">
        <div class="moon">🌙</div>

        <div class="ufo">
          <div class="ufo-top"></div>
          <div class="ufo-base"></div>
          <div class="ufo-light">
            <span></span><span></span><span></span>
            <span></span><span></span><span></span>
          </div>
        </div>

        <div class="beam"></div>

        {crowd_html}

        {abducted_html}

        <div class="ground"></div>
        <div class="scene-title">
          🛸 UFO ĐANG QUAN SÁT ĐÁM ĐÔNG 👽
        </div>
      </div>
    </body>
    </html>
    """,
    height=590,
    scrolling=False
)

# =========================
# DANH SÁCH NGƯỜI CHƠI
# =========================

st.markdown("## 📋 DANH SÁCH NGƯỜI CHƠI")

with st.expander("Xem danh sách đầy đủ", expanded=False):
    for p in st.session_state.players:
        status = "🛸 Đã bị bắt" if not p["alive"] else "🟢 Còn trên mặt đất"
        st.write(f'**{p["name"]}** — {status}')

# =========================
# CHÂN TRANG
# =========================

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;color:#94a3b8;font-size:12px;">
      UFO HACK NÃO · Trò chơi câu đố và bắt người ngoài hành tinh
    </div>
    """,
    unsafe_allow_html=True
)
