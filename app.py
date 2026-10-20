import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

GAME_HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #080d1b;
    color: #ffe66d;
    font-family: Arial, sans-serif;
}

button, input {
    font-family: inherit;
}

.game {
    width: 100%;
    max-width: 1400px;
    margin: auto;
    padding: 12px;
}

.header {
    text-align: center;
    padding: 12px 5px;
    border: 2px solid #ffcf33;
    border-radius: 15px;
    background: linear-gradient(120deg, #101735, #24104b);
    box-shadow: 0 0 18px #ffcf3340;
}

.header h1 {
    margin: 4px;
    font-size: clamp(27px, 5vw, 44px);
    color: #ffe66d;
    text-shadow: 0 0 15px #ffae00;
}

.header p {
    margin: 7px;
    color: #c9d8ff;
}

.stats {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin: 12px 0;
}

.stat {
    flex: 1;
    min-width: 100px;
    text-align: center;
    padding: 12px 5px;
    border: 1px solid #5c70b9;
    border-radius: 12px;
    background: #111a36;
}

.stat b {
    display: block;
    font-size: 22px;
    color: #ffe66d;
    margin-bottom: 4px;
}

.controls {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 10px;
    padding: 12px;
    margin-bottom: 12px;
    background: #101832;
    border: 1px solid #334779;
    border-radius: 12px;
}

.control {
    display: flex;
    flex-direction: column;
    gap: 5px;
    flex: 1;
    min-width: 150px;
}

label {
    font-size: 13px;
    color: #cbd7ff;
}

input[type="number"],
input[type="text"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #6478bd;
    border-radius: 8px;
    background: #080e20;
    color: white;
    outline: none;
}

input[type="range"] {
    width: 100%;
    accent-color: #ffd43b;
}

button {
    padding: 10px 14px;
    border: 1px solid #ffdf5d;
    border-radius: 9px;
    color: #fff4ba;
    background: #38234e;
    cursor: pointer;
    font-weight: bold;
    transition: 0.2s;
}

button:hover {
    transform: translateY(-1px);
    background: #68418a;
}

button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.primary {
    background: linear-gradient(120deg, #f7b928, #ff7a18);
    color: #160d20;
    border: none;
}

.primary:hover {
    background: #ffdb65;
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
    inset: 0 0 42% 0;
    background:
        radial-gradient(circle at 20% 20%, #ffffff 0 1px, transparent 2px),
        radial-gradient(circle at 65% 17%, #ffffff 0 1px, transparent 2px),
        radial-gradient(circle at 83% 30%, #a9d4ff 0 1px, transparent 2px),
        linear-gradient(#080e29, #26365d);
    background-size: 100px 80px, 130px 110px, 160px 120px, auto;
}

.moon {
    position: absolute;
    top: 25px;
    right: 11%;
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: #fff2b0;
    box-shadow: 0 0 35px #ffe9a0;
}

.buildings {
    position: absolute;
    inset: 90px 0 38% 0;
    display: flex;
    align-items: end;
    gap: 5px;
    padding: 0 6px;
}

.building {
    position: relative;
    flex: 1;
    height: var(--height);
    min-width: 35px;
    background: linear-gradient(90deg, #17213d, #263656);
    border: 1px solid #40547a;
}

.windows {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 7px;
    padding: 10px 7px;
}

.window {
    height: 13px;
    background: #ffda69;
    box-shadow: 0 0 8px #ffbb3c55;
    opacity: 0.85;
}

.road {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 43%;
    background: linear-gradient(#424957, #222936);
    border-top: 9px solid #858b9a;
}

.sidewalk {
    position: absolute;
    left: 0;
    right: 0;
    top: 56%;
    height: 6%;
    background: repeating-linear-gradient(
        90deg,
        #858b9a 0 60px,
        #636b7c 60px 63px
    );
}

.road-line {
    position: absolute;
    top: 80%;
    left: 0;
    right: 0;
    height: 4px;
    background: repeating-linear-gradient(
        90deg,
        #ffe59b 0 45px,
        transparent 45px 85px
    );
    opacity: 0.8;
}

.lamp {
    position: absolute;
    top: 20%;
    width: 5px;
    height: 40%;
    background: #66738c;
}

.lamp::before {
    content: "";
    position: absolute;
    width: 34px;
    height: 5px;
    top: 0;
    left: 0;
    background: #66738c;
}

.lamp::after {
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
    height: 70px;
    z-index: 20;
    text-align: center;
    font-size: 55px;
    filter: drop-shadow(0 0 10px #6deaff);
    transition: left 2.4s ease, top 1.4s ease;
    pointer-events: none;
}

.beam {
    position: absolute;
    display: none;
    top: 65px;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 260px;
    background: linear-gradient(
        to bottom,
        #6df9ff99,
        #6df9ff20,
        transparent
    );
    clip-path: polygon(40% 0, 60% 0, 100% 100%, 0 100%);
    animation: beamPulse 0.6s infinite alternate;
}

@keyframes beamPulse {
    from { opacity: 0.5; }
    to { opacity: 1; }
}

.person {
    position: absolute;
    z-index: 10;
    width: 34px;
    height: 100px;
    transform-origin: center bottom;
    cursor: default;
    transition: opacity 0.7s, filter 0.7s;
}

.person .head {
    position: absolute;
    left: 10px;
    top: 0;
    width: 17px;
    height: 19px;
    border-radius: 50%;
    background: var(--skin);
    border: 1px solid #47312a;
}

.person .hair {
    position: absolute;
    z-index: 2;
    left: 9px;
    top: -2px;
    width: 19px;
    height: 8px;
    border-radius: 9px 9px 4px 4px;
    background: var(--hair);
}

.person .body {
    position: absolute;
    left: 7px;
    top: 19px;
    width: 23px;
    height: 38px;
    border-radius: 7px 7px 3px 3px;
    background: var(--shirt);
    border: 1px solid #ffffff40;
}

.person .arm {
    position: absolute;
    top: 23px;
    width: 7px;
    height: 31px;
    border-radius: 6px;
    background: var(--skin);
    transform-origin: top center;
}

.person .arm.left {
    left: 4px;
    animation: armLeft 0.45s infinite alternate;
}

.person .arm.right {
    right: 3px;
    animation: armRight 0.45s infinite alternate;
}

.person .leg {
    position: absolute;
    top: 53px;
    width: 9px;
    height: 37px;
    border-radius: 5px;
    background: var(--pants);
    transform-origin: top center;
}

.person .leg.left {
    left: 9px;
    animation: legLeft 0.4s infinite alternate;
}

.person .leg.right {
    left: 20px;
    animation: legRight 0.4s infinite alternate;
}

.person .shoe {
    position: absolute;
    bottom: 5px;
    width: 13px;
    height: 6px;
    border-radius: 5px;
    background: #111;
}

.person .shoe.left {
    left: 5px;
}

.person .shoe.right {
    left: 17px;
}

@keyframes legLeft {
    from { transform: rotate(-22deg); }
    to { transform: rotate(22deg); }
}

@keyframes legRight {
    from { transform: rotate(22deg); }
    to { transform: rotate(-22deg); }
}

@keyframes armLeft {
    from { transform: rotate(20deg); }
    to { transform: rotate(-20deg); }
}

@keyframes armRight {
    from { transform: rotate(-20deg); }
    to { transform: rotate(20deg); }
}

.person.captured {
    animation: abduct 2.3s forwards ease-in;
    pointer-events: none;
}

.person.captured .leg,
.person.captured .arm {
    animation-play-state: paused;
}

@keyframes abduct {
    0% {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
    50% {
        filter: brightness(2);
    }
    100% {
        opacity: 0;
        transform: translateY(-230px) scale(0.2);
    }
}

.person .nameTag {
    position: absolute;
    top: 90px;
    left: 50%;
    transform: translateX(-50%);
    color: #fff;
    font-size: 10px;
    white-space: nowrap;
    text-shadow: 1px 1px 3px black;
    pointer-events: none;
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
    color: #ffe66d;
    text-align: center;
    font-weight: bold;
    font-size: 13px;
}

#quiz {
    display: none;
    position: absolute;
    z-index: 50;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: min(500px, 92%);
    padding: 20px;
    background: #10142af5;
    border: 2px solid #ffe66d;
    border-radius: 17px;
    box-shadow: 0 0 30px #55eaff77;
    color: #fff;
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
    min-height: 48px;
    background: #202d50;
    border-color: #657fc2;
    color: white;
}

.answers button:hover {
    background: #465b8c;
}

#quizResult {
    margin-top: 12px;
    min-height: 25px;
    font-weight: bold;
    color: #ffe66d;
}

.footer {
    padding: 12px 3px;
    text-align: center;
    color: #aab9e5;
    font-size: 12px;
}

@media (max-width: 600px) {
    #scene {
        height: 480px;
    }

    #ufo {
        font-size: 42px;
        width: 75px;
    }

    .person {
        transform: scale(0.85);
        transform-origin: bottom center;
    }

    #quiz {
        padding: 13px;
    }

    #question {
        font-size: 15px;
    }
}
</style>
</head>

<body>
<div class="game">

    <div class="header">
        <h1>🛸 UFO HACK NÃO 👽</h1>
        <p>UFO đang săn người ngoài phố! Hãy giải câu đố để giành điểm!</p>
    </div>

    <div class="stats">
        <div class="stat">
            <b id="score">0</b>
            Điểm
        </div>
        <div class="stat">
            <b id="saved">0</b>
            Đã giải cứu
        </div>
        <div class="stat">
            <b id="remaining">12</b>
            Người còn lại
        </div>
        <div class="stat">
            <b id="round">0</b>
            Lượt UFO bắt
        </div>
    </div>

    <div class="controls">
        <div class="control">
            <label for="peopleCount">Số người trong thành phố (1–100)</label>
            <input id="peopleCount" type="number" min="1" max="100" value="12">
        </div>

        <button id="applyPeople">👥 Áp dụng số người</button>

        <div class="control">
            <label for="renameSelect">Chọn người để đổi tên</label>
            <select id="renameSelect"
                style="padding:10px;border-radius:8px;background:#080e20;color:white;border:1px solid #6478bd">
            </select>
        </div>

        <div class="control">
            <label for="newName">Tên mới</label>
            <input id="newName" type="text" maxlength="18" placeholder="Nhập tên...">
        </div>

        <button id="renameButton">✏️ Đổi tên</button>
        <button id="startButton" class="primary">🔊 BẮT ĐẦU GAME</button>
        <button id="resetButton">🔄 Chơi lại</button>

        <div class="control" style="max-width:180px">
            <label for="volume">Âm lượng nhạc</label>
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

        <div id="ufo">
            🛸
            <div class="beam" id="beam"></div>
        </div>

        <div id="message">🌃 Đêm xuống... UFO đang tuần tra thành phố!</div>

        <div id="peopleLayer"></div>

        <div id="quiz">
            <h2>🧠 HACK NÃO!</h2>
            <div id="targetText">UFO đã bắt được một người!</div>
            <div id="question"></div>
            <div class="answers" id="answers"></div>
            <div id="quizResult"></div>
        </div>
    </div>

    <div class="footer">
        Mẹo: Bấm “BẮT ĐẦU GAME” để bật âm thanh. Người và UFO sẽ tự động di chuyển.
        Trả lời câu hỏi để ghi điểm!
    </div>
</div>

<script>
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
let nextAbductionTimer = null;
let animationFrame = null;

const shirts = [
    "#e74c3c", "#3498db", "#2ecc71", "#f1c40f",
    "#9b59b6", "#ff8c42", "#ff69b4", "#4ecdc4"
];

const pantsColors = [
    "#202d46", "#353535", "#293b59", "#493b35"
];

const skinColors = [
    "#f4c7a1", "#d99a6c", "#b9754c", "#f0d1b0"
];

const hairColors = [
    "#211914", "#563a25", "#292929", "#a56a32"
];

const questions = [
    {
        q: "Cái gì càng lấy đi thì càng lớn?",
        a: ["Cái túi", "Cái hố", "Ngọn núi", "Cái cây"],
        correct: 1,
        explain: "Chính xác! Càng đào đất đi, cái hố càng lớn."
    },
    {
        q: "Một năm có bao nhiêu tháng có 28 ngày?",
        a: ["1 tháng", "2 tháng", "6 tháng", "12 tháng"],
        correct: 3,
        explain: "Đúng rồi! Tháng nào cũng có ít nhất 28 ngày."
    },
    {
        q: "Có 5 quả táo, bạn lấy đi 2 quả. Bạn có mấy quả?",
        a: ["3 quả", "2 quả", "5 quả", "7 quả"],
        correct: 1,
        explain: "Đúng! Bạn lấy 2 quả nên bạn có 2 quả."
    },
    {
        q: "Cái gì có răng nhưng không biết nhai?",
        a: ["Con cá", "Cái lược", "Con chó", "Cái bát"],
        correct: 1,
        explain: "Chính xác! Đó là cái lược."
    },
    {
        q: "Bạn vượt qua người đứng thứ hai trong cuộc đua. Bạn đứng thứ mấy?",
        a: ["Thứ nhất", "Thứ hai", "Thứ ba", "Thứ tư"],
        correct: 1,
        explain: "Đúng! Bạn chiếm vị trí thứ hai của người đó."
    },
    {
        q: "Cái gì luôn đi tới nhưng không bao giờ đến nơi?",
        a: ["Ngày mai", "Xe buýt", "Con mèo", "Cơn mưa"],
        correct: 0,
        explain: "Đúng! Ngày mai đến thì lại trở thành hôm nay."
    },
    {
        q: "Có 3 con gà đẻ 3 quả trứng trong 3 ngày. 6 con gà đẻ 6 quả trứng trong bao lâu?",
        a: ["1 ngày", "2 ngày", "3 ngày", "6 ngày"],
        correct: 2,
        explain: "Chính xác! Mỗi con gà đẻ 1 quả trong 3 ngày."
    },
    {
        q: "Cái gì có cổ nhưng không có đầu?",
        a: ["Con người", "Cái chai", "Con ngựa", "Cái bàn"],
        correct: 1,
        explain: "Đúng rồi! Đó là cái chai."
    },
    {
        q: "Một bác sĩ cho bạn 3 viên thuốc, cứ 30 phút uống 1 viên. Bao lâu thì uống hết?",
        a: ["30 phút", "60 phút", "90 phút", "120 phút"],
        correct: 1,
        explain: "Đúng! Uống viên đầu ngay, viên hai sau 30 phút, viên ba sau 60 phút."
    },
    {
        q: "Cái gì có mặt và hai kim nhưng không có tay?",
        a: ["Robot", "Đồng hồ", "Con người", "Cái quạt"],
        correct: 1,
        explain: "Chính xác! Đó là đồng hồ."
    },
    {
        q: "Một căn phòng có 4 góc. Mỗi góc có một con mèo. Có tất cả mấy con mèo?",
        a: ["4", "8", "12", "16"],
        correct: 0,
        explain: "Đúng! Mỗi góc một con mèo, tổng cộng 4 con."
    },
    {
        q: "Cái gì có thể đi vòng quanh thế giới mà vẫn nằm nguyên một chỗ?",
        a: ["Máy bay", "Con tem", "Mặt trời", "Con tàu"],
        correct: 1,
        explain: "Đúng! Con tem nằm ở góc phong bì."
    },
    {
        q: "Nếu bạn có một que diêm và vào phòng tối có nến, đèn dầu, bếp củi, bạn thắp gì trước?",
        a: ["Nến", "Đèn dầu", "Bếp củi", "Que diêm"],
        correct: 3,
        explain: "Chính xác! Phải thắp que diêm trước."
    },
    {
        q: "Cái gì càng khô thì càng ướt?",
        a: ["Cái khăn", "Cát", "Đá", "Tờ giấy"],
        correct: 0,
        explain: "Đúng! Khăn lau càng khô thì càng hút nước và trở nên ướt."
    },
    {
        q: "Bạn có thể cầm thứ gì bằng tay trái nhưng không thể cầm bằng tay phải?",
        a: ["Cái cốc", "Khuỷu tay phải", "Quyển sách", "Cái bút"],
        correct: 1,
        explain: "Đúng! Bạn không thể cầm khuỷu tay phải bằng chính tay phải."
    }
];

// Tạo nhà cửa và cửa sổ.
function createBuildings() {
    const container = $("buildings");
    container.innerHTML = "";

    const heights = [65, 90, 75, 100, 68, 86, 72, 94];

    for (let i = 0; i < heights.length; i++) {
        const building = document.createElement("div");
        building.className = "building";
        building.style.setProperty("--height", heights[i] + "%");

        const windows = document.createElement("div");
        windows.className = "windows";

        for (let j = 0; j < 12; j++) {
            const win = document.createElement("div");
            win.className = "window";

            if (Math.random() > 0.25) {
                win.style.opacity = "0.9";
            } else {
                win.style.opacity = "0.15";
            }

            windows.appendChild(win);
        }

        building.appendChild(windows);
        container.appendChild(building);
    }
}

function createPerson(index) {
    const el = document.createElement("div");
    el.className = "person";

    const person = {
        id: index + 1,
        name: "Người " + (index + 1),
        el: el,
        x: Math.random() * 90,
        y: 57 + Math.random() * 23,
        speed: 0.012 + Math.random() * 0.022,
        direction: Math.random() > 0.5 ? 1 : -1,
        alive: true,
        captured: false
    };

    const shirt = shirts[Math.floor(Math.random() * shirts.length)];
    const pants = pantsColors[Math.floor(Math.random() * pantsColors.length)];
    const skin = skinColors[Math.floor(Math.random() * skinColors.length)];
    const hair = hairColors[Math.floor(Math.random() * hairColors.length)];

    el.style.setProperty("--shirt", shirt);
    el.style.setProperty("--pants", pants);
    el.style.setProperty("--skin", skin);
    el.style.setProperty("--hair", hair);

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

    peopleLayer.appendChild(el);

    el.querySelector(".nameTag").textContent = person.name;
    el.style.left = person.x + "%";
    el.style.top = person.y + "%";
    el.style.zIndex = String(Math.floor(person.y));

    person.el.style.transform =
        "scale(" + (0.7 + (person.y - 57) / 23 * 0.45) + ")";

    people.push(person);
    return person;
}

function updateNameTag(person) {
    person.el.querySelector(".nameTag").textContent = person.name;
}

function refreshRenameSelect() {
    const select = $("renameSelect");
    const previous = select.value;

    select.innerHTML = "";

    people.forEach(person => {
        if (!person.alive) return;

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

function setMessage(text) {
    message.textContent = text;
}

function createCity(count) {
    peopleLayer.innerHTML = "";
    people = [];

    for (let i = 0; i < count; i++) {
        createPerson(i);
    }

    score = 0;
    saved = 0;
    round = 0;
    currentTarget = null;
    quizOpen = false;

    quiz.style.display = "none";
    beam.style.display = "none";

    refreshRenameSelect();
    updateStats();

    setMessage("🌃 Đêm xuống... UFO đang tuần tra thành phố!");

    if (gameStarted) {
        scheduleAbduction();
    }
}

function moveUFO() {
    const x = 4 + Math.random() * 78;
    const y = 4 + Math.random() * 15;

    ufo.style.left = x + "%";
    ufo.style.top = y + "%";
}

function animatePeople() {
    if (!document.body.isConnected) return;

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

        person.el.style.left = person.x + "%";
        person.el.style.transform =
            "scale(" + (0.7 + (person.y - 57) / 23 * 0.45) + ")";

        person.el.style.zIndex = String(Math.floor(person.y));

        if (person.direction < 0) {
            person.el.style.filter = "none";
        }
    });

    animationFrame = requestAnimationFrame(animatePeople);
}

function scheduleAbduction() {
    clearTimeout(nextAbductionTimer);

    if (!gameStarted || quizOpen) return;

    const living = people.filter(p => p.alive && !p.captured);

    if (living.length === 0) {
        setMessage("👽 UFO đã bắt hết mọi người! Bấm CHƠI LẠI để tiếp tục.");
        gameStarted = false;
        $("startButton").textContent = "🔊 BẮT ĐẦU GAME";
        return;
    }

    const delay = 5500 + Math.random() * 3500;

    nextAbductionTimer = setTimeout(() => {
        if (!gameStarted || quizOpen) return;
        beginAbduction();
    }, delay);
}

function beginAbduction() {
    const living = people.filter(p => p.alive && !p.captured);

    if (living.length === 0) {
        scheduleAbduction();
        return;
    }

    currentTarget = living[Math.floor(Math.random() * living.length)];
    round++;

    const target = currentTarget;
    const sceneWidth = $("scene").clientWidth;

    const targetX = Math.max(
        0,
        Math.min(85, target.x - 3)
    );

    ufo.style.left = targetX + "%";
    ufo.style.top = "8%";

    beam.style.display = "block";

    setMessage("🛸 UFO đang khóa mục tiêu: " + target.name + "!");

    playSFX(660, 0.3);

    setTimeout(() => {
        if (!target.alive) return;

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
        }, 1200);

    }, 900);
}

function showQuestion(target) {
    quizOpen = true;
    gameStarted = false;

    clearTimeout(nextAbductionTimer);

    const question = questions[
        Math.floor(Math.random() * questions.length)
    ];

    $("targetText").textContent =
        "🛸 UFO đã bắt " + target.name + "! Trả lời để giành điểm.";

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

                playSFX(880, 0.5);
            } else {
                $("quizResult").textContent =
                    "❌ Chưa đúng! " + question.explain;

                playSFX(220, 0.4);
            }

            updateStats();

            const continueButton = document.createElement("button");
            continueButton.className = "primary";
            continueButton.textContent = "▶ TIẾP TỤC";
            continueButton.style.gridColumn = "1 / -1";

            continueButton.addEventListener("click", () => {
                quiz.style.display = "none";
                quizOpen = false;

                if (people.every(p => !p.alive)) {
                    setMessage(
                        "👽 UFO đã bắt hết mọi người! Bấm CHƠI LẠI để chơi tiếp."
                    );
                    gameStarted = false;
                    $("startButton").textContent = "🔊 BẮT ĐẦU GAME";
                    return;
                }

                gameStarted = true;
                $("startButton").textContent = "⏸ TẠM DỪNG GAME";
                setMessage("🌃 UFO tiếp tục tuần tra... Hãy cảnh giác!");

                scheduleAbduction();
            });

            answerBox.appendChild(continueButton);
        });

        answerBox.appendChild(button);
    });

    quiz.style.display = "block";
}

function resetGame() {
    clearTimeout(nextAbductionTimer);

    gameStarted = false;
    quizOpen = false;
    currentTarget = null;

    $("startButton").textContent = "🔊 BẮT ĐẦU GAME";

    const raw = parseInt($("peopleCount").value, 10);
    const count = Math.max(1, Math.min(100, Number.isFinite(raw) ? raw : 12));

    $("peopleCount").value = count;

    createCity(count);
    moveUFO();

    if (gameStarted) {
        scheduleAbduction();
    }
}

// Âm thanh điện tử tự tạo bằng Web Audio API.
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
        setMessage("Trình duyệt này chưa hỗ trợ âm thanh Web Audio.");
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

        const freq = melody[noteIndex % melody.length];

        tone(freq, 0.25, "sawtooth", 0.13);
        tone(freq * 2, 0.15, "square", 0.035);

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

$("startButton").addEventListener("click", () => {
    initAudio();

    if (quizOpen) {
        setMessage("🧠 Hãy trả lời câu hỏi trước khi tiếp tục!");
        return;
    }

    if (gameStarted) {
        gameStarted = false;
        clearTimeout(nextAbductionTimer);
        $("startButton").textContent = "▶ TIẾP TỤC GAME";
        setMessage("⏸ Game đang tạm dừng.");
    } else {
        const living = people.filter(p => p.alive);

        if (living.length === 0) {
            resetGame();
        }

        gameStarted = true;
        $("startButton").textContent = "⏸ TẠM DỪNG GAME";
        setMessage("🛸 UFO đã xuất hiện! Hãy sẵn sàng hack não!");
        scheduleAbduction();
    }
});

$("applyPeople").addEventListener("click", () => {
    resetGame();
});

$("resetButton").addEventListener("click", () => {
    resetGame();
});

$("renameButton").addEventListener("click", () => {
    const id = Number($("renameSelect").value);
    const newName = $("newName").value.trim();

    if (!newName) {
        setMessage("✏️ Hãy nhập tên mới trước nhé!");
        return;
    }

    const person = people.find(p => p.id === id && p.alive);

    if (!person) {
        setMessage("Người này không còn ở trên phố!");
        return;
    }

    person.name = newName.slice(0, 18);
    updateNameTag(person);
    refreshRenameSelect();

    $("renameSelect").value = String(person.id);
    $("newName").value = "";

    setMessage("✨ Đã đổi tên thành " + person.name + "!");
});

$("volume").addEventListener("input", setVolume);

createBuildings();
createCity(12);
moveUFO();
animatePeople();
setVolume();

// UFO bay tuần tra kể cả trước khi người chơi bấm bắt đầu.
setInterval(() => {
    if (!gameStarted || quizOpen) {
        moveUFO();
    }
}, 4500);
</script>
</body>
</html>
"""

st.markdown(
    """
    <style>
    .stApp {
        background: #080d1b;
    }
    [data-testid="stHeader"] {
        background: transparent;
    }
    h1 {
        color: #ffe66d !important;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🛸 UFO HACK NÃO")
st.caption("Thành phố về đêm — UFO tự động săn người — câu đố xuất hiện ngay trong game.")

components.html(
    GAME_HTML,
    height=1050,
    scrolling=True
)
"""

st.components.v1.html(GAME_HTML, height=1050, scrolling=True)
