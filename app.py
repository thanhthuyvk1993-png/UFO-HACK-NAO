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

st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden;}
.stApp {
    background:#050817;
    color:white;
}
.block-container {
    max-width:1500px;
    padding:8px 12px 20px;
}
.game {
    background:linear-gradient(140deg,#111d43,#070b1a);
    border:1px solid #5266a3;
    border-radius:18px;
    padding:12px;
    box-shadow:0 0 25px #312e8155;
}
.title {
    text-align:center;
    font-size:clamp(24px,4vw,42px);
    font-weight:900;
    color:#a5f3fc;
    text-shadow:0 0 14px #06b6d4;
}
.subtitle {
    text-align:center;
    color:#c4b5fd;
    font-size:12px;
    margin-bottom:10px;
}
.stat {
    background:#111a35;
    border:1px solid #475569;
    border-radius:10px;
    padding:7px;
    text-align:center;
    font-size:12px;
}
.stat b {
    color:#67e8f9;
    font-size:20px;
}
.stButton button {
    width:100%;
    min-height:38px;
    font-weight:bold;
    border-radius:9px;
}
div[data-testid="stVerticalBlock"] {
    gap:.45rem;
}
@media(max-width:600px) {
    .block-container {padding:4px;}
    .game {padding:6px;}
}
</style>
""", unsafe_allow_html=True)

# ---------- TRẠNG THÁI GAME ----------
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

for i, p in enumerate(st.session_state.players):
    p.setdefault("id", i)
    p.setdefault("name", f"Người {i+1}")
    p.setdefault("alive", True)

# ---------- MỘT KHUNG GAME ----------
st.markdown('<div class="game">', unsafe_allow_html=True)
st.markdown('<div class="title">🛸 UFO HACK NÃO 👽</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">THỬ THÁCH TRÍ TUỆ · UFO BẮT CÓC</div>',
    unsafe_allow_html=True
)

players = st.session_state.players
alive = [p for p in players if p["alive"]]
captured_count = len(players) - len(alive)

a, b, c, d = st.columns(4)
for col, value, label in [
    (a, len(players), "👥 Người chơi"),
    (b, len(alive), "🟢 Còn lại"),
    (c, captured_count, "🛸 Bị bắt"),
    (d, st.session_state.score, "🏆 Điểm"),
]:
    with col:
        st.markdown(
            f'<div class="stat"><b>{value}</b><br>{label}</div>',
            unsafe_allow_html=True,
        )

# ---------- CHIA KHUNG THÀNH 2 CỘT ----------
left, right = st.columns([1.8, 1], gap="small")

with left:
    st.markdown("#### 🌌 SÂN CHƠI UFO")

    # Vẽ đám đông và UFO trong cùng một cảnh HTML.
    crowd = []
    for i, p in enumerate(players):
        if not p["alive"]:
            continue
        row = i // 10
        col = i % 10
        x = 5 + col * 10 + random.uniform(-1.8, 1.8)
        y = 5 + row * 7.0
        name = html.escape(p["name"])
        crowd.append(
            f'<div class="person" style="left:{x:.1f}%;bottom:{y:.1f}%">'
            f'<span>👽</span><small>{name}</small></div>'
        )

    victim = next(
        (p for p in players if p["id"] == st.session_state.victim_id),
        None,
    )
    beam_person = ""
    if victim:
        beam_person = (
            '<div class="beam"></div>'
            '<div class="fly">👽<small>'
            + html.escape(victim["name"])
            + '</small></div>'
        )

    scene = r"""
    <!DOCTYPE html><html><head>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <style>
    *{box-sizing:border-box}
    body{margin:0;background:#050817;font-family:Arial;color:white}
    .scene{
      position:relative;height:390px;overflow:hidden;border-radius:13px;
      border:1px solid #5266a3;
      background:
      radial-gradient(circle at 15% 15%,white 1px,transparent 2px),
      radial-gradient(circle at 80% 25%,white 1px,transparent 2px),
      linear-gradient(#101b3a,#07111f 75%,#123b43);
      background-size:70px 70px,90px 90px,auto;
    }
    .ufo{
      position:absolute;z-index:100;top:13px;left:50%;
      width:115px;height:65px;transform:translateX(-50%);
      animation:hover 2s infinite ease-in-out;
    }
    .dome{
      position:absolute;top:0;left:39px;width:38px;height:28px;
      border:2px solid #a5f3fc;border-radius:50% 50% 20% 20%;
      background:#6278df;box-shadow:0 0 15px #22d3ee;
    }
    .disk{
      position:absolute;top:22px;width:115px;height:29px;
      border:2px solid #c4b5fd;border-radius:50%;
      background:linear-gradient(#c7d2fe,#4f46a5,#20264c);
      box-shadow:0 0 20px #818cf8;
    }
    .lights{position:absolute;top:34px;left:12px;width:91px;
      display:flex;justify-content:space-around}
    .lights i{width:5px;height:5px;border-radius:50%;background:#67e8f9;
      box-shadow:0 0 7px #67e8f9;animation:blink .4s infinite alternate}
    .person{
      position:absolute;width:10%;height:42px;text-align:center;
      transform:translateX(-50%);z-index:10;
    }
    .person span{display:block;font-size:clamp(13px,2.5vw,22px);
      line-height:22px;filter:drop-shadow(0 0 4px #67e8f9)}
    .person small{display:block;max-width:50px;margin:auto;font-size:6px;
      overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
    .beam{
      position:absolute;z-index:80;top:47px;left:40%;width:20%;height:280px;
      clip-path:polygon(40% 0,60% 0,100% 100%,0 100%);
      background:linear-gradient(#67e8f988,#67e8f922,transparent);
      animation:blink .4s infinite alternate;
    }
    .fly{
      position:absolute;z-index:90;top:55px;left:50%;transform:translateX(-50%);
      text-align:center;font-size:32px;animation:abduct 3s ease-in-out forwards;
      filter:drop-shadow(0 0 8px #67e8f9);
    }
    .fly small{display:block;font-size:9px;background:#071326;padding:2px}
    .ground{position:absolute;bottom:0;width:100%;height:9px;
      background:#164e63;border-top:2px solid #22d3ee}
    @keyframes hover{50%{margin-top:-6px}}
    @keyframes blink{from{opacity:.3}to{opacity:1}}
    @keyframes abduct{
      0%{top:300px;opacity:0}
      15%{opacity:1}
      75%{top:90px;opacity:1}
      100%{top:35px;opacity:0}
    }
    @media(max-width:500px){.scene{height:330px}.person small{font-size:5px}}
    </style></head><body>
    <div class="scene">
      <div class="ufo"><div class="dome"></div><div class="disk"></div>
      <div class="lights"><i></i><i></i><i></i><i></i><i></i></div></div>
    __CROWD__
    __VICTIM__
    <div class="ground"></div>
    </div></body></html>
    """
    scene = scene.replace("__CROWD__", "".join(crowd))
    scene = scene.replace("__VICTIM__", beam_person)
    components.html(scene, height=400, scrolling=False)

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

with right:
    st.markdown("#### 🧠 CÂU ĐỐ HACK NÃO")

    riddles = [
        ("Cái gì càng lấy đi càng lớn?", ["Cái hố", "Cái cây", "Dòng sông"], "Cái hố"),
        ("Tháng nào có 28 ngày?", ["Tháng 2", "Tất cả các tháng", "Tháng 6"], "Tất cả các tháng"),
        ("Cái gì có cổ nhưng không có đầu?", ["Cái chai", "Cái bàn", "Cái ghế"], "Cái chai"),
        ("Vượt qua người đứng thứ hai thì bạn đứng thứ mấy?", ["Thứ nhất", "Thứ hai", "Thứ ba"], "Thứ hai"),
        ("Cái gì có răng nhưng không cắn?", ["Cái lược", "Con chó", "Cá mập"], "Cái lược"),
        ("Bạn lấy 2 quả trong 5 quả táo. Bạn có mấy quả?", ["2", "3", "5"], "2"),
        ("Cái gì càng lau càng ướt?", ["Cái khăn", "Cái bàn", "Cái ghế"], "Cái khăn"),
    ]

    idx = (st.session_state.round - 1) % len(riddles)
    question, options, correct = riddles[idx]
    st.caption(f"Câu số {st.session_state.round}")
    st.write(question)

    chosen = st.radio(
        "Đáp án",
        options,
        key=f"answer_{st.session_state.round}",
        label_visibility="collapsed",
    )

    if st.button("✅ KIỂM TRA"):
        if st.session_state.round in st.session_state.answered:
            st.warning("Bạn đã trả lời câu này rồi.")
        else:
            st.session_state.answered.append(st.session_state.round)
            if chosen == correct:
                st.session_state.score += 1
                st.success("Chính xác! 🎉")
            else:
                st.error(f"Đáp án đúng: {correct}")

    if st.button("➡️ CÂU TIẾP"):
        st.session_state.round += 1
        st.rerun()

    st.markdown("---")
    st.markdown("#### 👥 NGƯỜI CHƠI")

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
    chosen_id = st.selectbox(
        "Chọn người để đổi tên",
        ids,
        format_func=lambda pid: next(
            f"{p['name']} (ID {pid})" for p in players if p["id"] == pid
        ),
    )
    new_name = st.text_input("Tên mới", max_chars=24)

    if st.button("✏️ ĐỔI TÊN"):
        if new_name.strip():
            target = next(p for p in players if p["id"] == chosen_id)
            target["name"] = new_name.strip()
            st.rerun()
        else:
            st.warning("Nhập tên mới trước nhé.")

    if st.button("🔄 CHƠI LẠI"):
        for p in players:
            p["alive"] = True
        st.session_state.victim_id = None
        st.session_state.round = 1
        st.session_state.score = 0
        st.session_state.answered = []
        st.session_state.notice = "UFO đã quay lại!"
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
