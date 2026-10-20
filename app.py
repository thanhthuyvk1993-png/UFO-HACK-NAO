import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide"
)

st.title("🛸 UFO HACK NÃO")
st.write("Điều khiển UFO, chọn người ngẫu nhiên và trả lời câu hỏi!")

# =========================
# NGÂN HÀNG CÂU HỎI
# =========================

QUESTIONS = {
    "Mức 1 - Đố vui": [
        {
            "q": "Cái gì có răng nhưng không có miệng?",
            "a": ["Cái lược", "Con cá", "Cái bàn", "Quyển sách"],
            "correct": 0
        },
        {
            "q": "Càng lau càng ướt là cái gì?",
            "a": ["Cái chổi", "Cái khăn", "Cái quạt", "Cái ghế"],
            "correct": 1
        },
        {
            "q": "Cái gì có cổ nhưng không có đầu?",
            "a": ["Cái áo", "Cái chai", "Cái bàn", "Cái kéo"],
            "correct": 1
        },
        {
            "q": "Một năm có bao nhiêu tháng có 28 ngày?",
            "a": ["1 tháng", "2 tháng", "6 tháng", "12 tháng"],
            "correct": 3
        },
        {
            "q": "Cái gì càng kéo càng ngắn?",
            "a": ["Điếu thuốc", "Sợi dây", "Cái thước", "Con đường"],
            "correct": 0
        },
        {
            "q": "Con gì đầu dê mình ốc?",
            "a": ["Con dê", "Con ốc", "Con dốc", "Con cua"],
            "correct": 2
        },
        {
            "q": "Cái gì có mặt mà không có miệng?",
            "a": ["Cái đồng hồ", "Con mèo", "Cái cốc", "Cái ghế"],
            "correct": 0
        },
        {
            "q": "Cái gì đi khắp thế giới nhưng vẫn đứng một chỗ?",
            "a": ["Mặt trời", "Con tem", "Máy bay", "Con tàu"],
            "correct": 1
        },
        {
            "q": "Có 3 quả táo, bạn lấy đi 2 quả. Bạn có mấy quả?",
            "a": ["1 quả", "2 quả", "3 quả", "5 quả"],
            "correct": 1
        },
        {
            "q": "Cái gì có nhiều phím nhưng không mở được cửa?",
            "a": ["Chùm chìa khóa", "Đàn piano", "Cái kéo", "Cái hộp"],
            "correct": 1
        },
    ],

    "Mức 2 - Ca dao tục ngữ": [
        {
            "q": "Điền vào chỗ trống: Có công mài sắt, có ngày ...",
            "a": ["Nên kim", "Nên vàng", "Nên bạc", "Nên đồng"],
            "correct": 0
        },
        {
            "q": "Điền vào chỗ trống: Uống nước nhớ ...",
            "a": ["Bạn bè", "Nguồn", "Nhà", "Sông"],
            "correct": 1
        },
        {
            "q": "Điền vào chỗ trống: Ăn quả nhớ kẻ ...",
            "a": [
                "Trồng cây",
                "Hái hoa",
                "Tưới nước",
                "Bắt sâu"
            ],
            "correct": 0
        },
        {
            "q": "Điền vào chỗ trống: Lá lành đùm lá ...",
            "a": ["Xanh", "Vàng", "Rách", "Non"],
            "correct": 2
        },
        {
            "q": "Điền vào chỗ trống: Thất bại là mẹ của ...",
            "a": ["Khó khăn", "Thành công", "Thất vọng", "Lo lắng"],
            "correct": 1
        },
        {
            "q": "Điền vào chỗ trống: Một cây làm chẳng nên non, ba cây chụm lại nên hòn ...",
            "a": ["Đá to", "Núi cao", "Đồi xanh", "Đất lớn"],
            "correct": 1
        },
        {
            "q": "Điền vào chỗ trống: Gần mực thì đen, gần đèn thì ...",
            "a": ["Sáng", "Tối", "Nóng", "Lạnh"],
            "correct": 0
        },
        {
            "q": "Điền vào chỗ trống: Có chí thì ...",
            "a": ["Có tiền", "Nên", "Có bạn", "Có nhà"],
            "correct": 1
        },
        {
            "q": "Điền vào chỗ trống: Đi một ngày đàng, học một sàng ...",
            "a": ["Cơm", "Khôn", "Sách", "Chữ"],
            "correct": 1
        },
        {
            "q": "Điền vào chỗ trống: Thương người như thể thương ...",
            "a": ["Bạn bè", "Gia đình", "Thương thân", "Anh em"],
            "correct": 2
        },
    ],

    "Mức 3 - Toán lớp 9": [
        {
            "q": "Giải phương trình: 2x + 6 = 0",
            "a": ["x = 3", "x = -3", "x = 6", "x = -6"],
            "correct": 1
        },
        {
            "q": "Căn bậc hai số học của 81 là bao nhiêu?",
            "a": ["8", "9", "-9", "18"],
            "correct": 1
        },
        {
            "q": "Giải phương trình: x² = 25",
            "a": ["x = 5", "x = -5", "x = ±5", "x = 25"],
            "correct": 2
        },
        {
            "q": "Phân tích x² - 9 thành nhân tử.",
            "a": [
                "(x - 3)(x + 3)",
                "(x - 9)(x + 1)",
                "(x - 3)²",
                "(x + 9)(x - 1)"
            ],
            "correct": 0
        },
        {
            "q": "Nếu y = 2x + 1 và x = 3 thì y bằng bao nhiêu?",
            "a": ["5", "6", "7", "8"],
            "correct": 2
        },
        {
            "q": "Nghiệm của phương trình x - 7 = 0 là gì?",
            "a": ["x = -7", "x = 0", "x = 1", "x = 7"],
            "correct": 3
        },
        {
            "q": "Tổng hai nghiệm của x² - 5x + 6 = 0 là bao nhiêu?",
            "a": ["2", "3", "5", "6"],
            "correct": 2
        },
        {
            "q": "Tam giác vuông có hai cạnh góc vuông dài 3 và 4. Cạnh huyền bằng?",
            "a": ["5", "6", "7", "8"],
            "correct": 0
        },
        {
            "q": "Đường tròn bán kính 3 có chu vi bằng bao nhiêu?",
            "a": ["3π", "6π", "9π", "12π"],
            "correct": 1
        },
        {
            "q": "Giải phương trình: 3x - 12 = 0",
            "a": ["x = 3", "x = 4", "x = 6", "x = 12"],
            "correct": 1
        },
        {
            "q": "Biệt thức Δ của phương trình x² - 4x + 4 = 0 bằng bao nhiêu?",
            "a": ["0", "4", "8", "16"],
            "correct": 0
        },
        {
            "q": "Hàm số y = ax² có đồ thị là hình gì khi a khác 0?",
            "a": ["Đường thẳng", "Đường tròn", "Parabol", "Hình chữ nhật"],
            "correct": 2
        },
        {
            "q": "Nếu sin A = 1/2 và A là góc nhọn thì A bằng bao nhiêu?",
            "a": ["30°", "45°", "60°", "90°"],
            "correct": 0
        },
        {
            "q": "Giải phương trình: x² - 4 = 0",
            "a": ["x = 2", "x = -2", "x = ±2", "x = 4"],
            "correct": 2
        },
        {
            "q": "Một hình tròn bán kính 2 có diện tích bằng bao nhiêu?",
            "a": ["2π", "4π", "6π", "8π"],
            "correct": 1
        },
    ]
}

# =========================
# CÀI ĐẶT GAME
# =========================

st.sidebar.header("⚙️ Cài đặt game")

player_name = st.sidebar.text_input(
    "Tên người chơi",
    value="Người điều khiển UFO"
)

level = st.sidebar.selectbox(
    "Chọn mức câu hỏi",
    list(QUESTIONS.keys())
)

people_count = st.sidebar.slider(
    "Số lượng nhân vật",
    min_value=1,
    max_value=100,
    value=20
)

if "score" not in st.session_state:
    st.session_state.score = 0

if "round" not in st.session_state:
    st.session_state.round = 0

if "used_questions" not in st.session_state:
    st.session_state.used_questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "current_person" not in st.session_state:
    st.session_state.current_person = None

if "answered" not in st.session_state:
    st.session_state.answered = False

if "message" not in st.session_state:
    st.session_state.message = ""

# =========================
# KHU PHỐ VÀ NHÂN VẬT
# =========================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(#dff4ff, #f5fff1);
}

.game-title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
}

.question-box {
    background: white;
    padding: 24px;
    border: 3px solid #3987ff;
    border-radius: 18px;
    margin-top: 15px;
    margin-bottom: 15px;
}

div.stButton > button {
    border-radius: 12px;
    font-weight: bold;
    min-height: 45px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="game-title">🌆 KHU PHỐ UFO HACK NÃO 🛸</div>',
    unsafe_allow_html=True
)

# Cảnh đường phố có nhân vật đi bộ.
# Nút bắt người nằm ngoài cảnh để không che nhân vật.

GAME_HTML = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    margin: 0;
    font-family: Arial, sans-serif;
}}

.scene {{
    height: 390px;
    position: relative;
    overflow: hidden;
    border: 4px solid #333;
    border-radius: 16px;
    background: linear-gradient(
        to bottom,
        #77d5ff 0%,
        #d8f5ff 58%,
        #8bd17c 58%,
        #8bd17c 68%,
        #666 68%,
        #666 100%
    );
}}

.sun {{
    position: absolute;
    top: 20px;
    right: 45px;
    font-size: 48px;
}}

.building {{
    position: absolute;
    bottom: 32%;
    width: 90px;
    height: 145px;
    background: #f3b66e;
    border: 3px solid #a46a3e;
}}

.building.one {{ left: 4%; }}
.building.two {{
    left: 19%;
    height: 110px;
    background: #ffb8c9;
}}
.building.three {{
    right: 15%;
    height: 160px;
    background: #d0c2ff;
}}
.building.four {{
    right: 1%;
    height: 120px;
    background: #ffe29b;
}}

.window {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 9px;
    padding: 12px;
}}

.window span {{
    height: 17px;
    background: #9ee7ff;
    border: 2px solid white;
}}

.road-line {{
    position: absolute;
    bottom: 38px;
    left: 0;
    width: 100%;
    border-top: 5px dashed white;
}}

.people {{
    position: absolute;
    bottom: 43px;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: end;
}}

.person {{
    font-size: 34px;
    animation: walk 0.7s infinite alternate ease-in-out;
}}

.person:nth-child(even) {{
    animation-delay: 0.3s;
}}

@keyframes walk {{
    from {{ transform: translateY(0) rotate(-5deg); }}
    to {{ transform: translateY(-8px) rotate(5deg); }}
}}

.cloud {{
    position: absolute;
    top: 40px;
    left: 10%;
    font-size: 45px;
}}

.cloud.two {{
    left: 42%;
    top: 65px;
}}
</style>
</head>

<body>
<div class="scene">
    <div class="sun">☀️</div>
    <div class="cloud">☁️</div>
    <div class="cloud two">☁️</div>

    <div class="building one">
        <div class="window">
            <span></span><span></span>
            <span></span><span></span>
            <span></span><span></span>
        </div>
    </div>

    <div class="building two">
        <div class="window">
            <span></span><span></span>
            <span></span><span></span>
        </div>
    </div>

    <div class="building three">
        <div class="window">
            <span></span><span></span>
            <span></span><span></span>
            <span></span><span></span>
        </div>
    </div>

    <div class="building four">
        <div class="window">
            <span></span><span></span>
            <span></span><span></span>
        </div>
    </div>

    <div class="road-line"></div>

    <div class="people">
"""

people_icons = [
    "🚶", "🚶‍♀️", "🚶‍♂️", "🧍",
    "🧍‍♀️", "🧍‍♂️", "🏃", "🏃‍♀️",
    "🏃‍♂️", "🚶"
]

for i in range(people_count):
    GAME_HTML += (
        f'<span class="person" title="Nhân vật {i+1}">'
        f'{people_icons[i % len(people_icons)]}</span>'
    )

GAME_HTML += """
    </div>
</div>
</body>
</html>
"""

components.html(GAME_HTML, height=410, scrolling=False)

# =========================
# NÚT ĐIỀU KHIỂN UFO
# =========================

st.subheader("🛸 Điều khiển UFO")

col1, col2 = st.columns(2)

with col1:
    st.metric("⭐ Điểm số", st.session_state.score)

with col2:
    st.metric("🎯 Số lượt chơi", st.session_state.round)

if st.button(
    "🛸 UFO BẮT NGƯỜI NGẪU NHIÊN",
    type="primary",
    use_container_width=True
):
    import random

    question_list = QUESTIONS[level]

    available = [
        i for i in range(len(question_list))
        if i not in st.session_state.used_questions
    ]

    if not available:
        st.session_state.used_questions = []
        available = list(range(len(question_list)))

    selected = random.choice(available)

    st.session_state.used_questions.append(selected)
    st.session_state.current_question = question_list[selected]
    st.session_state.current_person = random.randint(1, people_count)
    st.session_state.answered = False
    st.session_state.message = ""

    st.rerun()

# =========================
# HIỂN THỊ CÂU HỎI RIÊNG
# =========================

if st.session_state.current_question is not None:

    question = st.session_state.current_question

    st.markdown("---")

    st.success(
        f"🛸 UFO đã chọn ngẫu nhiên nhân vật số "
        f"{st.session_state.current_person}!"
    )

    st.markdown(
        f"""
        <div class="question-box">
            <h2>❓ CÂU HỎI HACK NÃO</h2>
            <h3>{question["q"]}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    if not st.session_state.answered:

        answer = st.radio(
            "Chọn một đáp án:",
            question["a"],
            key=f"answer_{st.session_state.round}_"
                f"{st.session_state.current_person}_"
                f"{len(st.session_state.used_questions)}"
        )

        if st.button(
            "✅ XÁC NHẬN ĐÁP ÁN",
            use_container_width=True
        ):
            selected_answer = question["a"].index(answer)

            st.session_state.round += 1
            st.session_state.answered = True

            if selected_answer == question["correct"]:
                st.session_state.score += 10
                st.session_state.message = (
                    "🎉 Chính xác! Bạn được cộng 10 điểm!"
                )
            else:
                correct_answer = question["a"][
                    question["correct"]
                ]
                st.session_state.message = (
                    f"❌ Chưa đúng! Đáp án đúng là: "
                    f"{correct_answer}"
                )

            st.rerun()

    else:
        st.info(st.session_state.message)

        if st.button(
            "➡️ TIẾP TỤC CHƠI",
            use_container_width=True
        ):
            st.session_state.current_question = None
            st.session_state.current_person = None
            st.session_state.answered = False
            st.session_state.message = ""
            st.rerun()

# =========================
# CHƠI LẠI
# =========================

st.markdown("---")

if st.button("🔄 CHƠI LẠI TỪ ĐẦU", use_container_width=True):
    st.session_state.score = 0
    st.session_state.round = 0
    st.session_state.used_questions = []
    st.session_state.current_question = None
    st.session_state.current_person = None
    st.session_state.answered = False
    st.session_state.message = ""
    st.rerun()

st.caption(
    f"🎮 Người chơi: {player_name} | "
    f"📚 Mức hiện tại: {level}"
)
