import streamlit as st
import random

# ==========================
# 🛸 UFO HACK NÃO
# ==========================

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide"
)

# ==========================
# GIAO DIỆN
# ==========================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;800&family=Orbitron:wght@600;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at top left, #202b65, transparent 40%),
        linear-gradient(135deg, #070b1b, #151238, #071827);
    color: white;
    font-family: 'Be Vietnam Pro', sans-serif;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.hero {
    padding: 30px;
    border-radius: 25px;
    border: 1px solid #65f3ff;
    background: linear-gradient(135deg, #171e49, #27154b);
    box-shadow: 0 0 30px #00d9ff22;
    text-align: center;
}

.logo {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(30px, 5vw, 55px);
    font-weight: 800;
    color: #65f3ff;
    text-shadow: 0 0 20px #00d9ff66;
}

.card {
    padding: 20px;
    margin: 10px 0;
    border-radius: 18px;
    border: 1px solid #5666a0;
    background: #111a38;
}

.question {
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #65f3ff;
    background: linear-gradient(135deg, #15234a, #251647);
    font-size: 22px;
    font-weight: bold;
}

div.stButton > button {
    width: 100%;
    min-height: 45px;
    border-radius: 12px;
    background: linear-gradient(90deg, #254a83, #583c94);
    color: white;
    border: 1px solid #65f3ff;
    font-weight: bold;
}

div.stButton > button:hover {
    border-color: white;
    color: #65f3ff;
}

@media(max-width:600px) {
    .block-container {
        padding-left: 12px;
        padding-right: 12px;
    }

    .hero {
        padding: 18px;
    }

    .question {
        padding: 18px;
        font-size: 19px;
    }
}
</style>
""", unsafe_allow_html=True)

# ==========================
# TIÊU ĐỀ GAME
# ==========================

st.markdown("""
<div class="hero">
    <div class="logo">🛸 UFO HACK NÃO</div>
    <h3>GIẢI MÃ BÍ ẨN VŨ TRỤ</h3>
    <p>🧠 Thử thách trí tuệ · 🚀 Chinh phục cấp độ</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================
# CÂU ĐỐ
# ==========================

PUZZLES = [
    {
        "level": 1,
        "question": "Càng lấy đi thì thứ đó càng lớn. Đó là gì?",
        "options": [
            "Cái hố",
            "Ngọn núi",
            "Đám mây",
            "Chiếc hộp"
        ],
        "answer": "Cái hố",
        "hint": "Hãy nghĩ đến việc đào đất.",
        "points": 100
    },
    {
        "level": 1,
        "question": "Dãy số: 2, 6, 12, 20, 30, ?",
        "options": [
            "36",
            "40",
            "42",
            "44"
        ],
        "answer": "42",
        "hint": "Hiệu giữa các số tăng dần.",
        "points": 100
    },
    {
        "level": 1,
        "question": "Một năm có bao nhiêu tháng có 28 ngày?",
        "options": [
            "1 tháng",
            "2 tháng",
            "6 tháng",
            "12 tháng"
        ],
        "answer": "12 tháng",
        "hint": "Đọc kỹ câu hỏi!",
        "points": 100
    },
    {
        "level": 2,
        "question": "Người đi dưới mưa không ô nhưng tóc không ướt. Vì sao?",
        "options": [
            "Người đó hói",
            "Mưa giả",
            "Người đó chạy nhanh",
            "Trời không mưa"
        ],
        "answer": "Người đó hói",
        "hint": "Câu đố liên quan đến tóc.",
        "points": 150
    },
    {
        "level": 2,
        "question": "5 người có 5 robot mỗi người. Mỗi robot có 5 mắt. Có bao nhiêu mắt?",
        "options": [
            "25",
            "50",
            "100",
            "125"
        ],
        "answer": "125",
        "hint": "Hãy nhân ba số 5.",
        "points": 150
    },
    {
        "level": 2,
        "question": "Số tiếp theo: 1, 1, 2, 3, 5, 8, ?",
        "options": [
            "11",
            "12",
            "13",
            "15"
        ],
        "answer": "13",
        "hint": "Cộng hai số đứng trước.",
        "points": 150
    },
    {
        "level": 3,
        "question": "6 tiếng chuông cách nhau tạo thành 5 khoảng. Nếu mỗi khoảng 1 giây, 12 tiếng mất bao lâu?",
        "options": [
            "10 giây",
            "11 giây",
            "12 giây",
            "15 giây"
        ],
        "answer": "11 giây",
        "hint": "Đếm khoảng cách giữa các tiếng.",
        "points": 200
    },
    {
        "level": 3,
        "question": "Một con số tăng gấp đôi từ 3. Kết quả là bao nhiêu?",
        "options": [
            "5",
            "6",
            "9",
            "12"
        ],
        "answer": "6",
        "hint": "Nhân số đó với 2.",
        "points": 200
    },
    {
        "level": 3,
        "question": "Số tiếp theo: 3, 6, 12, 24, ?",
        "options": [
            "30",
            "36",
            "42",
            "48"
        ],
        "answer": "48",
        "hint": "Mỗi số gấp đôi số trước.",
        "points": 250
    }
]

# ==========================
# TRẠNG THÁI GAME
# ==========================

if "index" not in st.session_state:
    st.session_state.index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "hint" not in st.session_state:
    st.session_state.hint = False

if "answered" not in st.session_state:
    st.session_state.answered = False

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "player" not in st.session_state:
    st.session_state.player = ""

# ==========================
# THÔNG TIN NGƯỜI CHƠI
# ==========================

st.markdown("## 👨‍🚀 Phi hành gia")

st.session_state.player = st.text_input(
    "Nhập tên của bạn",
    value=st.session_state.player,
    max_chars=24
)

col1, col2 = st.columns(2)

with col1:
    st.metric("⭐ Điểm số", st.session_state.score)

with col2:
    st.metric(
        "🔐 Số câu",
        f"{min(st.session_state.index + 1, len(PUZZLES))}/{len(PUZZLES)}"
    )

# ==========================
# HIỂN THỊ CÂU ĐỐ
# ==========================

if st.session_state.index < len(PUZZLES):

    p = PUZZLES[st.session_state.index]

    level_name = {
        1: "TÂN BINH VŨ TRỤ",
        2: "THỢ SĂN TÍN HIỆU",
        3: "CHỈ HUY UFO"
    }

    st.markdown(
        f"""
        <div class="question">
            🛸 CẤP {p['level']} — {level_name[p['level']]}
            <br><br>
            {p['question']}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if not st.session_state.answered:

        answer = st.radio(
            "Chọn đáp án:",
            p["options"],
            index=None,
            key=f"answer_{st.session_state.index}"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("💡 GỢI Ý"):

                st.session_state.hint = True

        with col2:
            if st.button("🔓 KIỂM TRA"):

                if not st.session_state.player.strip():
                    st.warning("Hãy nhập tên của bạn trước!")

                elif answer is None:
                    st.warning("Hãy chọn một đáp án!")

                elif answer == p["answer"]:

                    earned = p["points"]

                    if st.session_state.hint:
                        earned = max(25, earned - 50)

                    st.session_state.score += earned

                    st.session_state.answered = True

                    st.session_state.feedback = (
                        f"Đúng rồi! Bạn nhận được {earned} điểm."
                    )

                    st.rerun()

                else:

                    st.session_state.feedback = "wrong"

                    st.rerun()

        if st.session_state.hint:
            st.info("💡 Gợi ý: " + p["hint"])

        if st.session_state.feedback == "wrong":
            st.error("Chưa chính xác! Hãy thử lại.")

    else:

        st.success(st.session_state.feedback)

        if st.button("➡️ CÂU TIẾP THEO"):

            st.session_state.index += 1
            st.session_state.hint = False
            st.session_state.answered = False
            st.session_state.feedback = ""

            st.rerun()

# ==========================
# KẾT THÚC GAME
# ==========================

else:

    st.balloons()

    st.markdown("""
    <div class="hero">
        <div class="logo">🏆 CHIẾN THẮNG!</div>
        <h3>Bạn đã hoàn thành nhiệm vụ UFO.</h3>
    </div>
    """, unsafe_allow_html=True)

    st.metric("TỔNG ĐIỂM", st.session_state.score)

    if st.button("🔁 CHƠI LẠI"):

        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.hint = False
        st.session_state.answered = False
        st.session_state.feedback = ""

        st.rerun()

st.divider()

st.markdown("""
<div style="text-align:center">
    🛸 UFO HACK NÃO
    <br>
    🌌 Hãy sẵn sàng cho nhiệm vụ tiếp theo!
</div>
""", unsafe_allow_html=True)
