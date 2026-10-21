import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide"
)

QUESTIONS = {
    "Mức 1 - Đố vui, đố mẹo": [
        {
            "q": "Một năm có bao nhiêu tháng có 28 ngày?",
            "a": ["1 tháng", "2 tháng", "6 tháng", "12 tháng"],
            "correct": 3,
            "explain": "Cả 12 tháng đều có ít nhất 28 ngày."
        },
        {
            "q": "Cái gì càng đào đi thì càng lớn?",
            "a": ["Cái túi", "Cái hố", "Ngọn núi", "Cái cây"],
            "correct": 1,
            "explain": "Càng đào đất đi thì cái hố càng lớn."
        },
        {
            "q": "Bạn vượt qua người đứng thứ hai trong cuộc đua. Bạn đứng thứ mấy?",
            "a": ["Thứ nhất", "Thứ hai", "Thứ ba", "Thứ tư"],
            "correct": 1,
            "explain": "Bạn chiếm vị trí thứ hai của người đó."
        },
        {
            "q": "Cái gì có răng nhưng không biết nhai?",
            "a": ["Con cá", "Cái lược", "Con chó", "Cái bát"],
            "correct": 1,
            "explain": "Đó là cái lược."
        },
        {
            "q": "Có 5 quả táo, bạn lấy đi 2 quả. Bạn có mấy quả?",
            "a": ["3 quả", "2 quả", "5 quả", "7 quả"],
            "correct": 1,
            "explain": "Bạn lấy 2 quả nên bạn có 2 quả."
        },
        {
            "q": "Cái gì có cổ nhưng không có đầu?",
            "a": ["Con người", "Cái chai", "Con ngựa", "Cái bàn"],
            "correct": 1,
            "explain": "Đó là cái chai."
        },
        {
            "q": "Bạn có thể cầm gì bằng tay trái nhưng không thể cầm bằng tay phải?",
            "a": ["Cái cốc", "Khuỷu tay phải", "Quyển sách", "Cái bút"],
            "correct": 1,
            "explain": "Bạn không thể dùng tay phải cầm chính khuỷu tay phải."
        },
        {
            "q": "Cái gì luôn đến nhưng không bao giờ trở thành hôm qua?",
            "a": ["Ngày mai", "Hôm nay", "Hôm qua", "Buổi sáng"],
            "correct": 0,
            "explain": "Ngày mai đến thì lại trở thành hôm nay."
        },
        {
            "q": "Một căn phòng có 4 góc, mỗi góc có một con mèo. Có bao nhiêu con mèo?",
            "a": ["2", "4", "8", "16"],
            "correct": 1,
            "explain": "Có tổng cộng 4 con mèo."
        },
        {
            "q": "Cái gì có mặt và hai kim nhưng không có tay?",
            "a": ["Robot", "Đồng hồ", "Con người", "Cái quạt"],
            "correct": 1,
            "explain": "Đó là đồng hồ."
        }
    ],

    "Mức 2 - Ca dao, tục ngữ": [
        {
            "q": "Có công mài sắt, có ngày nên ...",
            "a": ["Kim", "Dao", "Kéo", "Búa"],
            "correct": 0,
            "explain": "Có công mài sắt, có ngày nên kim."
        },
        {
            "q": "Uống nước nhớ ...",
            "a": ["Cây", "Nguồn", "Sông", "Suối"],
            "correct": 1,
            "explain": "Uống nước nhớ nguồn."
        },
        {
            "q": "Lá lành đùm lá ...",
            "a": ["Đỏ", "Xanh", "Rách", "Vàng"],
            "correct": 2,
            "explain": "Lá lành đùm lá rách."
        },
        {
            "q": "Gần mực thì đen, gần đèn thì ...",
            "a": ["Sáng", "Tối", "Nóng", "Lạnh"],
            "correct": 0,
            "explain": "Câu tục ngữ nói về ảnh hưởng của môi trường."
        },
        {
            "q": "Thất bại là mẹ thành ...",
            "a": ["Công", "Danh", "Đạt", "Tài"],
            "correct": 0,
            "explain": "Thất bại là mẹ thành công."
        },
        {
            "q": "Ăn quả nhớ kẻ trồng ...",
            "a": ["Hoa", "Cây", "Đất", "Rừng"],
            "correct": 1,
            "explain": "Ăn quả nhớ kẻ trồng cây."
        },
        {
            "q": "Một cây làm chẳng nên non, ba cây chụm lại nên hòn núi ...",
            "a": ["Đỏ", "Cao", "Thái Sơn", "Lớn"],
            "correct": 2,
            "explain": "Câu tục ngữ đề cao tinh thần đoàn kết."
        },
        {
            "q": "Câu nào khuyên chúng ta phải biết ơn?",
            "a": [
                "Có chí thì nên",
                "Uống nước nhớ nguồn",
                "Đi một ngày đàng",
                "Tốt gỗ hơn tốt nước sơn"
            ],
            "correct": 1,
            "explain": "Uống nước nhớ nguồn khuyên ta nhớ ơn cội nguồn."
        },
        {
            "q": "Không thầy đố mày làm ...",
            "a": ["Giàu", "Nên", "Quan", "Khôn"],
            "correct": 3,
            "explain": "Không thầy đố mày làm nên."
        },
        {
            "q": "Một mặt người bằng mười mặt ...",
            "a": ["Đất", "Vàng", "Bạc", "Ngọc"],
            "correct": 1,
            "explain": "Câu tục ngữ đề cao giá trị con người."
        }
    ],

    "Mức 3 - Toán lớp 9": [
        {
            "q": "Giải phương trình x² - 5x + 6 = 0.",
            "a": [
                "x = 1 hoặc x = 6",
                "x = 2 hoặc x = 3",
                "x = -2 hoặc x = -3",
                "x = 0 hoặc x = 5"
            ],
            "correct": 1,
            "explain": "(x - 2)(x - 3) = 0 nên x = 2 hoặc x = 3."
        },
        {
            "q": "Tính √81.",
            "a": ["7", "8", "9", "10"],
            "correct": 2,
            "explain": "√81 = 9."
        },
        {
            "q": "Giải phương trình 2x + 6 = 0.",
            "a": ["x = 3", "x = -3", "x = 6", "x = -6"],
            "correct": 1,
            "explain": "2x = -6 nên x = -3."
        },
        {
            "q": "Nếu y = 2x + 1, khi x = 3 thì y bằng bao nhiêu?",
            "a": ["5", "6", "7", "8"],
            "correct": 2,
            "explain": "y = 2 × 3 + 1 = 7."
        },
        {
            "q": "Phương trình x² = 16 có nghiệm nào?",
            "a": ["Chỉ x = 4", "Chỉ x = -4", "x = ±4", "x = 16"],
            "correct": 2,
            "explain": "Hai nghiệm là x = 4 và x = -4."
        },
        {
            "q": "Tính √25 + √9.",
            "a": ["8", "34", "16", "2"],
            "correct": 0,
            "explain": "5 + 3 = 8."
        },
        {
            "q": "Đường thẳng y = 3x - 2 có hệ số góc bằng bao nhiêu?",
            "a": ["-2", "2", "3", "-3"],
            "correct": 2,
            "explain": "Hệ số góc là 3."
        },
        {
            "q": "Tam giác vuông có hai cạnh góc vuông 3 và 4. Cạnh huyền bằng bao nhiêu?",
            "a": ["5", "6", "7", "8"],
            "correct": 0,
            "explain": "Theo định lý Pythagore, cạnh huyền bằng 5."
        },
        {
            "q": "Giải phương trình x² - 9 = 0.",
            "a": ["x = 3", "x = -3", "x = ±3", "x = 9"],
            "correct": 2,
            "explain": "Hai nghiệm là x = 3 và x = -3."
        },
        {
            "q": "Nếu sin A = 1/2 và A là góc nhọn thì A bằng bao nhiêu?",
            "a": ["30°", "45°", "60°", "90°"],
            "correct": 0,
            "explain": "sin 30° = 1/2."
        },
        {
            "q": "Giải hệ x + y = 7 và x - y = 1.",
            "a": [
                "x = 3, y = 4",
                "x = 4, y = 3",
                "x = 5, y = 2",
                "x = 6, y = 1"
            ],
            "correct": 1,
            "explain": "Cộng hai phương trình được 2x = 8, nên x = 4, y = 3."
        },
        {
            "q": "Biệt thức Δ của x² - 4x + 4 = 0 bằng bao nhiêu?",
            "a": ["0", "4", "8", "16"],
            "correct": 0,
            "explain": "Δ = 16 - 16 = 0."
        },
        {
            "q": "Tính √(49/64).",
            "a": ["7/8", "8/7", "7/64", "49/8"],
            "correct": 0,
            "explain": "√(49/64) = 7/8."
        },
        {
            "q": "Đồ thị hàm số y = ax² (a khác 0) có hình dạng gì?",
            "a": ["Đường thẳng", "Đường tròn", "Parabol", "Hình chữ nhật"],
            "correct": 2,
            "explain": "Đồ thị là một parabol."
        },
        {
            "q": "Đường tròn bán kính 3 cm có đường kính bao nhiêu?",
            "a": ["3 cm", "6 cm", "9 cm", "12 cm"],
            "correct": 1,
            "explain": "Đường kính bằng hai lần bán kính: 6 cm."
        }
    ]
}

QUESTIONS_JSON = json.dumps(QUESTIONS, ensure_ascii=False)

GAME_HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    background: #080d1b;
    color: #ffe66d;
    font-family: Arial, sans-serif;
}

.game {
    width: 100%;
    max-width: 1400px;
    margin: auto;
    padding: 10px;
}

.header {
    text-align: center;
    padding: 12px;
    border: 2px solid #ffcf33;
    border-radius: 15px;
    background: linear-gradient(120deg, #101735, #24104b);
    box-shadow: 0 0 18px #ffcf3340;
}

.header h1 {
    margin: 5px;
    font-size: clamp(27px, 5vw, 43px);
    text-shadow: 0 0 15px #ffae00;
}

.header p { color: #d5ddff; }

.stats {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 12px 0;
}

.stat {
    flex: 1;
    min-width: 100px;
    text-align: center;
    padding: 10px;
    border: 1px solid #5c70b9;
    border-radius: 12px;
    background: #111a36;
}

.stat b {
    display: block;
    font-size: 22px;
    margin-bottom: 4px;
}

.controls {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: end;
    padding: 12px;
    margin-bottom: 12px;
    background: #101832;
    border: 1px solid #334779;
    border-radius: 12px;
}

.control {
    flex: 1;
    min-width: 150px;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

label {
    color: #d2dcff;
    font-size: 13px;
}

input, select {
    width: 100%;
    padding: 10px;
    border: 1px solid #6478bd;
    border-radius: 8px;
    background: #080e20;
    color: white;
}

input[type=range] { accent-color: #ffd43b; }

button {
    padding: 10px 13px;
    border: 1px solid #ffdf5d;
    border-radius: 9px;
    color: #fff4ba;
    background: #38234e;
    cursor: pointer;
    font-weight: bold;
}

button:hover { background: #68418a; }

button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.primary {
    color: #160d20;
    background: linear-gradient(120deg, #f7b928, #ff7a18);
    border: none;
}

#ufoButton {
    background: linear-gradient(120deg, #00d4ff, #3975ff);
    color: #07132b;
    border: none;
}

#scene {
    position: relative;
    height: 560px;
    overflow: hidden;
    border: 2px solid #5e78c6;
    border-radius: 15px;
    background: #10162e;
    isolation: isolate;
}

.sky {
    position: absolute;
    inset: 0 0 42%;
    background:
        radial-gradient(circle at 20% 20%, white 0 1px, transparent 2px),
        radial-gradient(circle at 65% 17%, white 0 1px, transparent 2px),
        radial-gradient(circle at 83% 30%, #a9d4ff 0 1px, transparent 2px),
        linear-gradient(#080e29, #26365d);
    background-size: 100px 80px, 130px 110px, 160px 120px, auto;
}

.moon {
    position: absolute;
    top: 25px;
    right: 11%;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: #fff2b0;
    box-shadow: 0 0 30px #ffe9a0;
}

.buildings {
    position: absolute;
    inset: 90px 0 38%;
    display: flex;
    align-items: end;
    gap: 5px;
    padding: 0 5px;
}

.building {
    position: relative;
    flex: 1;
    min-width: 25px;
    height: var(--height);
    background: linear-gradient(90deg, #17213d, #263656);
    border: 1px solid #40547a;
}

.windows {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 7px;
    padding: 8px 5px;
}

.window {
    height: 12px;
    background: #ffda69;
    box-shadow: 0 0 8px #ffbb3c55;
}

.road {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 43%;
    background: linear-gradient(#424957, #222936);
    border-top: 9px solid #858b9a;
}

.sidewalk {
    position: absolute;
    top: 56%;
    left: 0;
    right: 0;
    height: 6%;
    background: repeating-linear-gradient(
        90deg, #858b9a 0 60px, #636b7c 60px 63px
    );
}

.road-line {
    position: absolute;
    top: 80%;
    left: 0;
    right: 0;
    height: 4px;
    background: repeating-linear-gradient(
        90deg, #ffe59b 0 45px, transparent 45px 85px
    );
}

.lamp {
    position: absolute;
    top: 20%;
    width: 5px;
    height: 40%;
    background: #66738c;
}

.lamp:before {
    content: "";
    position: absolute;
    width: 35px;
    height: 5px;
    background: #66738c;
}

.lamp:after {
    content: "";
    position: absolute;
    top: 0;
    left: 25px;
    width: 13px;
    height: 10px;
    background: #ffe6a0;
    border-radius: 50%;
    box-shadow: 0 0 20px #ffe6a0;
}

#ufo {
    position: absolute;
    top: 8%;
    left: 12%;
    width: 100px;
    text-align: center;
    font-size: 53px;
    z-index: 20;
    filter: drop-shadow(0 0 10px #6deaff);
    transition: left 0.8s ease, top 0.8s ease;
    pointer-events: none;
}

.beam {
    display: none;
    position: absolute;
    top: 60px;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 250px;
    background: linear-gradient(#6df9ff99, #6df9ff20, transparent);
    clip-path: polygon(40% 0, 60% 0, 100% 100%, 0 100%);
    animation: pulse 0.5s infinite alternate;
    pointer-events: none;
}

@keyframes pulse {
    from { opacity: 0.5; }
    to { opacity: 1; }
}

#peopleLayer {
    position: absolute;
    inset: 0;
    z-index: 10;
    pointer-events: none;
}

.person {
    position: absolute;
    width: 34px;
    height: 100px;
    transform-origin: center bottom;
    transition: opacity 0.7s;
}

.head {
    position: absolute;
    left: 10px;
    top: 0;
    width: 17px;
    height: 19px;
    border-radius: 50%;
    background: var(--skin);
    border: 1px solid #47312a;
}

.hair {
    position: absolute;
    z-index: 2;
    left: 9px;
    top: -2px;
    width: 19px;
    height: 8px;
    border-radius: 9px;
    background: var(--hair);
}

.body {
    position: absolute;
    left: 7px;
    top: 19px;
    width: 23px;
    height: 38px;
    border-radius: 7px 7px 3px 3px;
    background: var(--shirt);
}

.arm {
    position: absolute;
    top: 23px;
    width: 7px;
    height: 31px;
    border-radius: 6px;
    background: var(--skin);
    transform-origin: top;
}

.arm.left {
    left: 4px;
    animation: armL .45s infinite alternate;
}

.arm.right {
    right: 3px;
    animation: armR .45s infinite alternate;
}

.leg {
    position: absolute;
    top: 53px;
    width: 9px;
    height: 37px;
    border-radius: 5px;
    background: var(--pants);
    transform-origin: top;
}

.leg.left {
    left: 9px;
    animation: legL .4s infinite alternate;
}

.leg.right {
    left: 20px;
    animation: legR .4s infinite alternate;
}

.shoe {
    position: absolute;
    bottom: 5px;
    width: 13px;
    height: 6px;
    border-radius: 5px;
    background: #111;
}

.shoe.left { left: 5px; }
.shoe.right { left: 17px; }

@keyframes legL {
    from { transform: rotate(-22deg); }
    to { transform: rotate(22deg); }
}

@keyframes legR {
    from { transform: rotate(22deg); }
    to { transform: rotate(-22deg); }
}

@keyframes armL {
    from { transform: rotate(20deg); }
    to { transform: rotate(-20deg); }
}

@keyframes armR {
    from { transform: rotate(-20deg); }
    to { transform: rotate(20deg); }
}

.person.captured {
    animation: abduct 1.8s forwards;
}

@keyframes abduct {
    0% { opacity: 1; transform: translateY(0) scale(1); }
    50% { filter: brightness(2); }
    100% { opacity: 0; transform: translateY(-220px) scale(.2); }
}

.nameTag {
    position: absolute;
    top: 90px;
    left: 50%;
    transform: translateX(-50%);
    color: white;
    font-size: 10px;
    white-space: nowrap;
    text-shadow: 1px 1px 3px black;
}

#message {
    position: absolute;
    top: 12px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 30;
    width: max-content;
    max-width: 90%;
    padding: 9px 15px;
    border-radius: 20px;
    background: #080d1ddd;
    border: 1px solid #ffe66d;
    text-align: center;
    font-size: 13px;
    font-weight: bold;
}

#quiz {
    display: none;
    position: absolute;
    z-index: 1000;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: min(520px, 94%);
    max-height: 85%;
    overflow-y: auto;
    padding: 20px;
    background: #10142af7;
    border: 2px solid #ffe66d;
    border-radius: 17px;
    box-shadow: 0 0 30px #55eaff77;
    color: white;
    text-align: center;
}

#quiz h2 {
    margin: 0 0 10px;
    color: #ffe66d;
}

#question {
    font-size: 17px;
    line-height: 1.5;
    margin: 14px 0;
}

.answers {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 9px;
}

.answers button {
    min-height: 46px;
    background: #202d50;
    border-color: #657fc2;
    color: white;
}

#quizResult {
    margin-top: 12px;
    line-height: 1.5;
    color: #ffe66d;
    font-weight: bold;
}

.footer {
    padding: 12px;
    text-align: center;
    color: #aab9e5;
    font-size: 12px;
}

@media(max-width:600px) {
    #scene { height: 480px; }
    #ufo { font-size: 42px; width: 75px; }
    #quiz { padding: 12px; }
    #question { font-size: 15px; }
    .answers { grid-template-columns: 1fr; }
}
</style>
</head>

<body>
<div class="game">

    <div class="header">
        <h1>🛸 UFO HACK NÃO 👽</h1>
        <p>Thành phố ban đêm — bạn điều khiển UFO — thử thách trí tuệ!</p>
    </div>

    <div class="stats">
        <div class="stat"><b id="score">0</b>Điểm</div>
        <div class="stat"><b id="saved">0</b>Giải cứu</div>
        <div class="stat"><b id="remaining">12</b>Người còn lại</div>
        <div class="stat"><b id="round">0</b>Lượt UFO bắt</div>
    </div>

    <div class="controls">
        <div class="control">
            <label for="difficulty">🎯 Chọn mức độ câu hỏi</label>
            <select id="difficulty">
                <option value="Mức 1 - Đố vui, đố mẹo">🟢 Mức 1 - Đố vui, đố mẹo</option>
                <option value="Mức 2 - Ca dao, tục ngữ">🟡 Mức 2 - Ca dao, tục ngữ</option>
                <option value="Mức 3 - Toán lớp 9">🔴 Mức 3 - Toán lớp 9</option>
            </select>
        </div>

        <div class="control">
            <label for="peopleCount">👥 Số người (1–100)</label>
            <input id="peopleCount" type="number" min="1" max="100" value="12">
        </div>

        <button id="applyPeople">Áp dụng</button>

        <div class="control">
            <label for="renameSelect">Chọn người</label>
            <select id="renameSelect"></select>
        </div>

        <div class="control">
            <label for="newName">Tên mới</label>
            <input id="newName" type="text" maxlength="18" placeholder="Nhập tên...">
        </div>

        <button id="renameButton">✏️ Đổi tên</button>
        <button id="startButton" class="primary">🔊 BẮT ĐẦU GAME</button>
        <button id="ufoButton">🛸 UFO BẮT NGƯỜI</button>
        <button id="resetButton">🔄 Chơi lại</button>

        <div class="control" style="max-width:180px">
            <label for="volume">🔊 Âm lượng</label>
            <input id="volume" type="range" min="0" max="100" value="45">
            <span id="volumeLabel">45%</span>
        </div>
    </div>

    <div id="scene">
        <div class="sky"></div>
        <div class="moon"></div>
        <div class="buildings" id="buildings"></div>
        <div class="lamp" style="left:8%"></div>
        <div class="lamp" style="left:76%"></div>
        <div class="road"></div>
        <div class="sidewalk"></div>
        <div class="road-line"></div>

        <div id="ufo">🛸<div class="beam" id="beam"></div></div>
        <div id="message">🌃 Đêm xuống... Hãy bắt đầu trò chơi!</div>
        <div id="peopleLayer"></div>

        <div id="quiz">
            <h2>🧠 HACK NÃO!</h2>
            <div id="targetText"></div>
            <div id="question"></div>
            <div class="answers" id="answers"></div>
            <div id="quizResult"></div>
        </div>
    </div>

    <div class="footer">
        Chọn mức độ, bấm BẮT ĐẦU GAME, sau đó tự bấm UFO BẮT NGƯỜI
        mỗi khi bạn muốn bắt người tiếp theo.
    </div>
</div>

<script>
const QUESTION_BANK = __QUESTIONS__;
const $ = id => document.getElementById(id);

const peopleLayer = $("peopleLayer");
const ufo = $("ufo");
const beam = $("beam");
const quiz = $("quiz");
const message = $("message");

let people = [];
let score = 0;
let saved = 0;
let round = 0;
let currentTarget = null;
let gameStarted = false;
let quizOpen = false;
let abductionInProgress = false;
let lastQuestion = null;

const shirts = [
    "#e74c3c", "#3498db", "#2ecc71", "#f1c40f",
    "#9b59b6", "#ff8c42", "#ff69b4", "#4ecdc4"
];

const pantsColors = ["#202d46", "#353535", "#293b59", "#493b35"];
const skinColors = ["#f4c7a1", "#d99a6c", "#b9754c", "#f0d1b0"];
const hairColors = ["#211914", "#563a25", "#292929", "#a56a32"];

function setMessage(text) {
    message.textContent = text;
}

function createBuildings() {
    const container = $("buildings");
    container.innerHTML = "";

    const heights = [65, 90, 75, 100, 68, 86, 72, 94];

    heights.forEach(height => {
        const building = document.createElement("div");
        building.className = "building";
        building.style.setProperty("--height", height + "%");

        const windows = document.createElement("div");
        windows.className = "windows";

        for (let i = 0; i < 12; i++) {
            const win = document.createElement("div");
            win.className = "window";

            if (Math.random() < 0.25) {
                win.style.opacity = "0.15";
            }

            windows.appendChild(win);
        }

        building.appendChild(windows);
        container.appendChild(building);
    });
}

function createPerson(index) {
    const el = document.createElement("div");
    el.className = "person";

    const person = {
        id: index + 1,
        name: "Người " + (index + 1),
        el: el,
        x: 2 + Math.random() * 90,
        y: 58 + Math.random() * 20,
        speed: 0.012 + Math.random() * 0.02,
        direction: Math.random() > 0.5 ? 1 : -1,
        alive: true,
        captured: false
    };

    el.style.setProperty(
        "--shirt",
        shirts[Math.floor(Math.random() * shirts.length)]
    );

    el.style.setProperty(
        "--pants",
        pantsColors[Math.floor(Math.random() * pantsColors.length)]
    );

    el.style.setProperty(
        "--skin",
        skinColors[Math.floor(Math.random() * skinColors.length)]
    );

    el.style.setProperty(
        "--hair",
        hairColors[Math.floor(Math.random() * hairColors.length)]
    );

    el.innerHTML = `
        <div class="hair"></div>
        <div class="head"></div>
        <div class="body"></div>
        <div class="arm left"></div>
        <div class="arm right"></div>
        <div class="leg left"></div>
        <div class="leg right"></div>
        <div class="shoe left"></div>
        <div class="shoe right"></div>
        <div class="nameTag"></div>
    `;

    el.querySelector(".nameTag").textContent = person.name;
    peopleLayer.appendChild(el);
    people.push(person);
    positionPerson(person);

    return person;
}

function positionPerson(person) {
    person.el.style.left = person.x + "%";
    person.el.style.top = person.y + "%";
    person.el.style.zIndex = String(Math.floor(person.y));

    const scale = 0.7 + ((person.y - 58) / 20) * 0.45;

    person.el.style.transform =
        "scale(" + scale + ") scaleX(" + person.direction + ")";
}

function refreshRenameSelect() {
    const select = $("renameSelect");
    const previous = select.value;
    select.innerHTML = "";

    people.filter(p => p.alive).forEach(person => {
        const option = document.createElement("option");
        option.value = person.id;
        option.textContent = person.name;
        select.appendChild(option);
    });

    if ([...select.options].some(o => o.value === previous)) {
        select.value = previous;
    }
}

function updateStats() {
    $("score").textContent = score;
    $("saved").textContent = saved;
    $("remaining").textContent = people.filter(p => p.alive).length;
    $("round").textContent = round;
}

function createCity(count) {
    gameStarted = false;
    quizOpen = false;
    abductionInProgress = false;
    currentTarget = null;

    peopleLayer.innerHTML = "";
    people = [];

    quiz.style.display = "none";
    beam.style.display = "none";

    score = 0;
    saved = 0;
    round = 0;
    lastQuestion = null;

    for (let i = 0; i < count; i++) {
        createPerson(i);
    }

    refreshRenameSelect();
    updateStats();

    $("startButton").textContent = "🔊 BẮT ĐẦU GAME";
    $("ufoButton").disabled = true;

    setMessage("🌃 Đêm xuống... Hãy bấm BẮT ĐẦU GAME!");
    moveUFO();
}

function moveUFO() {
    ufo.style.left = (3 + Math.random() * 78) + "%";
    ufo.style.top = (4 + Math.random() * 15) + "%";
}

function animatePeople() {
    people.forEach(person => {
        if (!person.alive || person.captured) return;

        person.x += person.speed * person.direction;

        if (person.x > 94) {
            person.x = 94;
            person.direction = -1;
        }

        if (person.x < 1) {
            person.x = 1;
            person.direction = 1;
        }

        positionPerson(person);
    });

    requestAnimationFrame(animatePeople);
}

function beginAbduction() {
    if (!gameStarted || quizOpen || abductionInProgress) {
        return;
    }

    const living = people.filter(p => p.alive && !p.captured);

    if (living.length === 0) {
        gameStarted = false;
        $("ufoButton").disabled = true;
        setMessage("👽 Hết người rồi! Hãy bấm CHƠI LẠI.");
        return;
    }

    abductionInProgress = true;
    $("ufoButton").disabled = true;

    const target = living[Math.floor(Math.random() * living.length)];
    currentTarget = target;
    round++;

    ufo.style.left = Math.max(0, Math.min(85, target.x - 3)) + "%";
    ufo.style.top = "7%";

    beam.style.display = "block";
    setMessage("🛸 UFO đang bắt " + target.name + "!");
    playSFX(660, 0.3);

    setTimeout(() => {
        if (!target.alive) {
            abductionInProgress = false;
            beam.style.display = "none";
            return;
        }

        target.captured = true;
        target.el.classList.add("captured");

        setTimeout(() => {
            target.alive = false;
            target.captured = false;
            target.el.style.display = "none";

            beam.style.display = "none";
            updateStats();
            refreshRenameSelect();

            showQuestion(target);
        }, 1100);
    }, 800);
}

function showQuestion(target) {
    gameStarted = false;
    quizOpen = true;
    $("ufoButton").disabled = true;

    const level = $("difficulty").value;
    const list = QUESTION_BANK[level];

    const available = list.filter(q => q.q !== lastQuestion);
    const pool = available.length ? available : list;
    const question = pool[Math.floor(Math.random() * pool.length)];

    lastQuestion = question.q;

    $("targetText").textContent =
        "🛸 UFO đã bắt " + target.name + "! Mức độ: " + level;

    $("question").textContent = question.q;
    $("quizResult").textContent = "";

    const answerBox = $("answers");
    answerBox.innerHTML = "";

    question.a.forEach((answer, index) => {
        const button = document.createElement("button");
        button.textContent = answer;

        button.addEventListener("click", () => {
            [...answerBox.querySelectorAll("button")].forEach(b => {
                b.disabled = true;
            });

            if (index === question.correct) {
                score += 10;
                saved += 1;

                $("quizResult").textContent =
                    "🎉 Chính xác! +10 điểm. " + question.explain;

                playSFX(880, 0.45);
            } else {
                $("quizResult").textContent =
                    "❌ Chưa đúng. Đáp án đúng: " +
                    question.a[question.correct] +
                    ". " + question.explain;

                playSFX(220, 0.4);
            }

            updateStats();

            const next = document.createElement("button");
            next.className = "primary";
            next.textContent = "▶ TIẾP TỤC";
            next.style.gridColumn = "1 / -1";

            next.addEventListener("click", () => {
                quiz.style.display = "none";
                quizOpen = false;
                abductionInProgress = false;

                if (people.every(p => !p.alive)) {
                    gameStarted = false;
                    $("startButton").textContent = "🔊 BẮT ĐẦU GAME";
                    $("ufoButton").disabled = true;
                    setMessage("👽 Hết người rồi! Hãy bấm CHƠI LẠI.");
                    return;
                }

                gameStarted = true;
                $("startButton").textContent = "⏸ TẠM DỪNG GAME";
                $("ufoButton").disabled = false;

                setMessage(
                    "🌃 Hãy bấm 🛸 UFO BẮT NGƯỜI khi bạn muốn bắt tiếp!"
                );
            });

            answerBox.appendChild(next);
        });

        answerBox.appendChild(button);
    });

    quiz.style.display = "block";
}

function resetGame() {
    let count = parseInt($("peopleCount").value, 10);

    if (!Number.isFinite(count)) count = 12;

    count = Math.max(1, Math.min(100, count));
    $("peopleCount").value = count;

    createCity(count);
}

$("applyPeople").addEventListener("click", resetGame);
$("resetButton").addEventListener("click", resetGame);

$("renameButton").addEventListener("click", () => {
    const id = Number($("renameSelect").value);
    const name = $("newName").value.trim();

    if (!name) {
        setMessage("✏️ Hãy nhập tên mới!");
        return;
    }

    const person = people.find(p => p.id === id && p.alive);

    if (!person) {
        setMessage("Người này không còn ở trên phố.");
        return;
    }

    person.name = name.slice(0, 18);
    person.el.querySelector(".nameTag").textContent = person.name;

    refreshRenameSelect();
    $("renameSelect").value = String(person.id);
    $("newName").value = "";

    setMessage("✨ Đã đổi tên thành " + person.name + "!");
});

$("difficulty").addEventListener("change", () => {
    setMessage("🎯 Đã chọn " + $("difficulty").value + ".");
});

$("startButton").addEventListener("click", () => {
    initAudio();

    if (quizOpen || abductionInProgress) {
        setMessage("🧠 Hãy hoàn thành lượt bắt người hiện tại trước!");
        return;
    }

    if (gameStarted) {
        gameStarted = false;
        $("startButton").textContent = "▶ TIẾP TỤC GAME";
        $("ufoButton").disabled = true;
        setMessage("⏸ Game đang tạm dừng.");
    } else {
        if (people.every(p => !p.alive)) {
            resetGame();
        }

        gameStarted = true;
        $("startButton").textContent = "⏸ TẠM DỪNG GAME";
        $("ufoButton").disabled = false;

        setMessage(
            "🛸 Game bắt đầu! Bạn hãy tự bấm nút UFO BẮT NGƯỜI."
        );
    }
});

$("ufoButton").addEventListener("click", () => {
    if (!gameStarted) {
        setMessage("▶ Hãy bấm BẮT ĐẦU GAME trước!");
        return;
    }

    if (quizOpen) {
        setMessage("🧠 Hãy trả lời câu hỏi trước!");
        return;
    }

    if (abductionInProgress) {
        setMessage("🛸 UFO đang bắt người!");
        return;
    }

    beginAbduction();
});

let audioContext = null;
let masterGain = null;
let musicTimer = null;
let noteIndex = 0;

function setVolume() {
    const value = Number($("volume").value);
    $("volumeLabel").textContent = value + "%";

    if (masterGain && audioContext) {
        masterGain.gain.setTargetAtTime(
            value / 100 * 0.45,
            audioContext.currentTime,
            0.08
        );
    }
}

function initAudio() {
    if (audioContext) {
        if (audioContext.state === "suspended") {
            audioContext.resume();
        }
        return;
    }

    const AudioCtx = window.AudioContext || window.webkitAudioContext;

    if (!AudioCtx) {
        setMessage("Trình duyệt không hỗ trợ âm thanh.");
        return;
    }

    audioContext = new AudioCtx();

    masterGain = audioContext.createGain();
    masterGain.gain.value = Number($("volume").value) / 100 * 0.45;
    masterGain.connect(audioContext.destination);

    startMusic();
}

function tone(frequency, duration, type = "sawtooth", volume = 0.15) {
    if (!audioContext || !masterGain) return;

    const oscillator = audioContext.createOscillator();
    const gain = audioContext.createGain();

    oscillator.type = type;
    oscillator.frequency.value = frequency;

    gain.gain.setValueAtTime(volume, audioContext.currentTime);
    gain.gain.exponentialRampToValueAtTime(
        0.001,
        audioContext.currentTime + duration
    );

    oscillator.connect(gain);
    gain.connect(masterGain);

    oscillator.start();
    oscillator.stop(audioContext.currentTime + duration);
}

function startMusic() {
    if (!audioContext) return;

    clearInterval(musicTimer);

    const melody = [
        110, 165, 220, 165,
        130, 196, 261, 196,
        98, 147, 196, 147,
        123, 185, 247, 185
    ];

    musicTimer = setInterval(() => {
        if (!audioContext || audioContext.state !== "running") return;

        const frequency = melody[noteIndex % melody.length];

        tone(frequency, 0.25, "sawtooth", 0.13);
        tone(frequency * 2, 0.15, "square", 0.035);

        if (noteIndex % 4 === 0) {
            tone(55, 0.32, "triangle", 0.12);
        }

        noteIndex++;
    }, 260);
}

function playSFX(frequency = 600, duration = 0.3) {
    if (!audioContext) return;

    tone(frequency, duration, "square", 0.18);
    tone(frequency * 1.5, duration * 0.7, "triangle", 0.1);
}

$("volume").addEventListener("input", setVolume);

createBuildings();
createCity(12);
animatePeople();
setVolume();
</script>
</body>
</html>
"""

GAME_HTML = GAME_HTML.replace("__QUESTIONS__", QUESTIONS_JSON)

st.markdown("""
<style>
.stApp {
    background-color: #080d1b;
}
[data-testid="stHeader"] {
    background: transparent;
}
h1 {
    color: #ffe66d !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("🛸 UFO HACK NÃO")
st.caption(
    "Chọn mức độ câu hỏi, sau đó tự bấm nút UFO BẮT NGƯỜI "
    "để chọn ngẫu nhiên một nhân vật."
)

components.html(
    GAME_HTML,
    height=1200,
    scrolling=True
)
