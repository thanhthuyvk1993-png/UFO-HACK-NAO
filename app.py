import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        margin: 0;
        padding: 0;
        background: #080d20;
    }

    #MainMenu, footer, header,
    [data-testid="stHeader"],
    [data-testid="stToolbar"] {
        display: none !important;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    iframe {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

GAME = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, initial-scale=1,
maximum-scale=1, user-scalable=no">

<style>
* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #080d20;
    color: white;
    font-family: Arial, sans-serif;
}

#game {
    width: 100%;
    height: 100dvh;
    max-width: 1200px;
    margin: auto;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.header {
    flex: 0 0 auto;
    text-align: center;
    padding: 7px 4px;
    background: linear-gradient(120deg, #101d46, #36165a);
    border-bottom: 1px solid #5ff5ff;
}

.logo {
    font-size: clamp(20px, 4vw, 32px);
    font-weight: 900;
    color: #70f7ff;
    text-shadow: 0 0 12px #13bfff;
    letter-spacing: 2px;
}

.subtitle {
    font-size: 10px;
    color: #d7e6ff;
    margin-top: 3px;
}

.hud {
    flex: 0 0 auto;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 4px;
    padding: 5px 3px;
    background: #101831;
}

.stat {
    padding: 5px 7px;
    background: #1b2850;
    border: 1px solid #5268a5;
    border-radius: 8px;
    font-size: clamp(10px, 2vw, 13px);
}

#scene {
    display: block;
    width: 100%;
    flex: 1 1 auto;
    min-height: 100px;
    height: 100%;
    background: #a7e7ff;
    touch-action: manipulation;
}

.controls {
    flex: 0 0 auto;
    padding: 5px 8px;
    background: #0d1530;
}

.row {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 5px;
    margin: 4px 0;
}

button, input, select {
    font: inherit;
}

button {
    border: 1px solid #68f4ff;
    background: linear-gradient(120deg, #164a80, #53328d);
    color: white;
    border-radius: 8px;
    padding: 8px 10px;
    cursor: pointer;
    font-size: 12px;
    font-weight: bold;
}

button:active {
    transform: scale(.97);
}

input, select {
    max-width: 48%;
    padding: 7px;
    color: white;
    background: #172344;
    border: 1px solid #566a9d;
    border-radius: 8px;
    font-size: 12px;
}

#message {
    padding: 6px 8px;
    background: #121d3b;
    border: 1px solid #40568d;
    border-radius: 8px;
    margin: 4px 0;
    font-size: 12px;
    line-height: 1.4;
}

#quiz {
    display: none;
    position: absolute;
    z-index: 5;
    left: 4%;
    width: 92%;
    top: 50%;
    transform: translateY(-50%);
    max-height: 78%;
    overflow-y: auto;
    padding: 13px;
    background: rgba(13, 22, 53, .97);
    border: 2px solid #70f7ff;
    border-radius: 14px;
    box-shadow: 0 0 30px #13bfff;
}

#question {
    font-size: 17px;
    font-weight: bold;
    line-height: 1.45;
    margin-bottom: 10px;
}

.answers {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 7px;
}

.answers button {
    min-height: 38px;
    overflow-wrap: anywhere;
}

#hint {
    color: #ffe89b;
    margin-top: 8px;
    font-size: 13px;
}

.note {
    font-size: 10px;
    color: #b9c9ed;
    text-align: center;
    margin: 3px 0;
}

@media(max-width: 500px) {
    .answers {
        grid-template-columns: 1fr 1fr;
    }

    button {
        padding: 8px 7px;
        font-size: 11px;
    }

    .logo {
        font-size: 22px;
    }

    .subtitle {
        font-size: 9px;
    }
}

@media(max-height: 650px) {
    .header {
        padding: 3px;
    }

    .logo {
        font-size: 19px;
    }

    .subtitle {
        display: none;
    }

    .hud {
        padding: 3px;
    }

    .stat {
        padding: 3px 5px;
    }

    .controls {
        padding: 3px 6px;
    }

    button {
        padding: 5px 7px;
    }

    #message {
        padding: 4px 6px;
        margin: 2px 0;
    }

    .note {
        display: none;
    }
}
</style>
</head>

<body>
<div id="game">

    <div class="header">
        <div class="logo">🛸 UFO HACK NÃO</div>
        <div class="subtitle">
            PHIÊU LƯU VŨ TRỤ · BẮT NGƯỜI · GIẢI ĐỐ
        </div>
    </div>

    <div class="hud">
        <div class="stat">⭐ Điểm: <b id="score">0</b></div>
        <div class="stat">👨‍🚀 <b id="playerName">Khách</b></div>
        <div class="stat">🧠 Cấp: <b id="level">1</b></div>
        <div class="stat">👥 Còn: <b id="count">12</b></div>
    </div>

    <canvas id="scene" width="800" height="480"></canvas>

    <div class="controls">
        <div class="row">
            <input id="name" maxlength="20"
                   placeholder="Tên của bạn">
            <button onclick="saveName()">Lưu tên</button>
            <button onclick="toggleAuto()" id="autoBtn">
                ▶ UFO tự chọn
            </button>
        </div>

        <div class="row">
            <select id="maxPlayers" aria-label="Số nhân vật">
                <option value="12">12 nhân vật</option>
                <option value="20">20 nhân vật</option>
                <option value="30">30 nhân vật</option>
                <option value="50">50 nhân vật</option>
                <option value="100" selected>100 nhân vật</option>
            </select>

            <button onclick="newGame()">🔄 Chơi lại</button>
            <button onclick="toggleMusic()" id="musicBtn">
                🎵 Bật nhạc
            </button>
        </div>

        <div id="message">
            🛸 Nhấn “UFO tự chọn” để bắt đầu khảo bài!
        </div>

        <p class="note">
            UFO chọn ngẫu nhiên · Trả lời đúng để ghi điểm
        </p>
    </div>

    <div id="quiz">
        <div id="question"></div>
        <div class="answers" id="answers"></div>
        <div id="hint"></div>
        <div class="row">
            <button onclick="showHint()">💡 Gợi ý</button>
        </div>
    </div>

</div>

<script>
const canvas = document.getElementById("scene");
const ctx = canvas.getContext("2d");

let score = 0;
let player = "Khách";
let selected = -1;
let beam = 0;
let level = 1;
let completed = 0;
let frame = 0;
let music = false;
let audio = null;
let musicTimer = null;
let autoMode = false;
let autoTimer = null;
let busy = false;
let currentPuzzle = null;

const names = [
    "Minh Huy", "Phương Mai", "Tuấn Minh",
    "Thanh Thảo", "Quỳnh Anh", "Huy Khánh",
    "Trúc Mai", "Đình Trọng", "Bảo Ngọc",
    "Gia Huy", "Minh Anh", "Hoàng Nam",
    "Khánh Linh", "Bảo An", "Đức Anh",
    "Ngọc Mai", "Tuấn Anh", "Hải Đăng",
    "Phương Linh", "Minh Khang", "Anh Thư",
    "Quốc Bảo", "Thảo Vy", "Gia Bảo",
    "Hà My", "Nhật Minh", "Thiên An",
    "Quỳnh Như", "Đăng Khoa", "Bảo Trân"
];

let students = [];
let answered = {};

const puzzles = [
    {
        q: "Càng đào thì thứ gì càng lớn?",
        a: ["Cái hố", "Ngọn núi", "Chiếc hộp", "Đám mây"],
        correct: 0,
        hint: "Nghĩ đến việc đào đất.",
        points: 100,
        level: 1
    },
    {
        q: "Một năm có bao nhiêu tháng có 28 ngày?",
        a: ["1 tháng", "2 tháng", "6 tháng", "12 tháng"],
        correct: 3,
        hint: "Đọc kỹ câu hỏi.",
        points: 100,
        level: 1
    },
    {
        q: "Dãy số 2, 6, 12, 20, 30, ... Số tiếp theo?",
        a: ["36", "40", "42", "44"],
        correct: 2,
        hint: "Hiệu lần lượt là 4, 6, 8, 10.",
        points: 100,
        level: 1
    },
    {
        q: "Dãy Fibonacci: 1, 1, 2, 3, 5, 8, ...",
        a: ["11", "12", "13", "15"],
        correct: 2,
        hint: "Cộng hai số đứng trước.",
        points: 150,
        level: 2
    },
    {
        q: "5 robot, mỗi robot có 5 mắt. Có bao nhiêu mắt?",
        a: ["10", "20", "25", "30"],
        correct: 2,
        hint: "Nhân số robot với số mắt mỗi robot.",
        points: 150,
        level: 2
    },
    {
        q: "Số tiếp theo: 3, 6, 12, 24, ...",
        a: ["30", "36", "42", "48"],
        correct: 3,
        hint: "Mỗi số gấp đôi số trước.",
        points: 150,
        level: 2
    },
    {
        q: "12 tiếng chuông cách nhau 1 giây. Từ tiếng đầu đến tiếng cuối mất bao lâu?",
        a: ["10 giây", "11 giây", "12 giây", "13 giây"],
        correct: 1,
        hint: "Có 11 khoảng giữa 12 tiếng chuông.",
        points: 200,
        level: 3
    },
    {
        q: "Nếu hôm qua là thứ Hai thì ngày mai là thứ mấy?",
        a: ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm"],
        correct: 2,
        hint: "Hôm nay là thứ Ba.",
        points: 200,
        level: 3
    },
    {
        q: "Có 3 quả táo, bạn lấy đi 2 quả. Bạn có mấy quả?",
        a: ["1", "2", "3", "5"],
        correct: 1,
        hint: "Bạn lấy đi bao nhiêu quả?",
        points: 150,
        level: 2
    },
    {
        q: "Số nào khác biệt: 2, 4, 8, 16, 31, 64?",
        a: ["4", "16", "31", "64"],
        correct: 2,
        hint: "Các số đều là lũy thừa của 2, trừ một số.",
        points: 200,
        level: 3
    }
];

function resetStudents() {
    const count = Number(
        document.getElementById("maxPlayers").value || 100
    );

    students = [];

    for (let i = 0; i < count; i++) {
        const name = names[i % names.length];

        students.push({
            name: i < names.length
                ? name
                : name + " " + (Math.floor(i / names.length) + 1),
            x: 25 + Math.random() * 750,
            y: 335 + Math.random() * 115,
            phase: Math.random() * 6,
            color: ["#f6d5b5", "#ffd8c2", "#e8bd96"][i % 3],
            shirt: ["#ffffff", "#8de3ff", "#ffda7a", "#ffc2dc"][i % 4],
            visible: true,
            captured: false
        });
    }

    document.getElementById("count").textContent = students.length;
}

function rect(x, y, w, h, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, w, h);
}

function rounded(x, y, w, h, r, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.roundRect(x, y, w, h, r);
    ctx.fill();
}

function text(str, x, y, size, color, align = "center") {
    ctx.fillStyle = color;
    ctx.font = "bold " + size + "px Arial";
    ctx.textAlign = align;
    ctx.fillText(str, x, y);
}

function drawSky() {
    const sky = ctx.createLinearGradient(0, 0, 0, 480);
    sky.addColorStop(0, "#5bc6ff");
    sky.addColorStop(1, "#e5f8ff");
    rect(0, 0, 800, 480, sky);

    ctx.fillStyle = "rgba(255,255,255,.8)";

    for (let i = 0; i < 4; i++) {
        const x = ((i * 225 + frame * .15) % 950) - 70;
        ctx.beginPath();
        ctx.arc(x, 70 + i % 2 * 30, 24, 0, Math.PI * 2);
        ctx.arc(x + 28, 58 + i % 2 * 30, 32, 0, Math.PI * 2);
        ctx.arc(x + 59, 72 + i % 2 * 30, 24, 0, Math.PI * 2);
        ctx.fill();
    }
}

function drawBuildings() {
    const buildings = [
        {x: 0, w: 145, c: "#ffe0b9", name: "BÁNH MÌ"},
        {x: 145, w: 140, c: "#e9d6ff", name: "TRÀ SỮA"},
        {x: 285, w: 155, c: "#fff1d3", name: "HỚT TÓC"},
        {x: 440, w: 135, c: "#d8e7ff", name: "BÚN CHẢ"},
        {x: 575, w: 125, c: "#ffe0b9", name: "KEM"},
        {x: 700, w: 100, c: "#e8d9ff", name: "CÀ PHÊ"}
    ];

    buildings.forEach((b) => {
        rect(b.x, 130, b.w, 170, b.c);
        rect(b.x, 125, b.w, 10, "#f8fafc");

        for (let wx = b.x + 14; wx < b.x + b.w - 12; wx += 42) {
            rect(wx, 151, 25, 35, "#83cafa");
            rect(wx - 2, 149, 29, 4, "#ffffff");
            rect(wx + 10, 151, 3, 35, "#ffffff");
            rect(wx, 205, 25, 32, "#8ad0ff");
            rect(wx - 2, 203, 29, 4, "#ffffff");
        }

        rect(b.x, 240, b.w, 7, "#c8a27b");
        rect(b.x, 250, b.w, 50, "#f6b64b");
        rect(b.x, 250, b.w, 8, "#ffffff");

        text(b.name, b.x + b.w / 2, 275, 11, "#26324a");

        for (let sx = b.x + 6; sx < b.x + b.w; sx += 20) {
            rect(sx, 288, 12, 12, "#fff7dc");
        }
    });
}

function drawStreet() {
    rect(0, 300, 800, 55, "#6b7b8c");
    rect(0, 355, 800, 125, "#d7c6a9");

    for (let x = 0; x < 800; x += 100) {
        rect(x, 324, 48, 4, "#ffffff");
    }

    rect(0, 352, 800, 6, "#f4eee1");

    for (let x = 15; x < 800; x += 120) {
        rect(x, 360, 2, 120, "#c2b198");
    }
}

function drawTree(x, y) {
    rect(x - 5, y, 10, 35, "#8d5c3a");

    ctx.fillStyle = "#329b61";
    ctx.beginPath();
    ctx.arc(x, y - 10, 24, 0, Math.PI * 2);
    ctx.arc(x - 15, y, 17, 0, Math.PI * 2);
    ctx.arc(x + 15, y, 17, 0, Math.PI * 2);
    ctx.fill();
}

function drawScooter(x, y, color) {
    ctx.strokeStyle = "#27364c";
    ctx.lineWidth = 4;

    ctx.beginPath();
    ctx.arc(x - 17, y, 9, 0, Math.PI * 2);
    ctx.arc(x + 20, y, 9, 0, Math.PI * 2);
    ctx.stroke();

    rounded(x - 12, y - 15, 30, 8, 3, color);

    ctx.beginPath();
    ctx.moveTo(x - 8, y - 10);
    ctx.lineTo(x - 17, y);
    ctx.lineTo(x + 20, y);
    ctx.stroke();
}

function drawStudent(s, i) {
    if (!s.visible) return;

    let x = s.x;
    let y = s.y + Math.sin(frame * .045 + s.phase) * 2;

    if (s.captured) {
        y -= beam * 1.8;
        x += Math.sin(frame * .05) * 5;
    }

    if (i % 3 === 0) {
        drawScooter(x, y + 12, i % 2 ? "#4e96ef" : "#ef6c70");
    }

    ctx.strokeStyle = "#344c7a";
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(x - 5, y + 13);
    ctx.lineTo(x - 8, y + 27);
    ctx.moveTo(x + 5, y + 13);
    ctx.lineTo(x + 10, y + 27);
    ctx.stroke();

    rounded(x - 10, y - 7, 20, 23, 5, s.shirt);

    ctx.strokeStyle = s.color;
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(x - 8, y - 2);
    ctx.lineTo(x - 15, y + 8);
    ctx.moveTo(x + 8, y - 2);
    ctx.lineTo(x + 15, y + 7);
    ctx.stroke();

    ctx.fillStyle = s.color;
    ctx.beginPath();
    ctx.arc(x, y - 15, 10, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "#342b2a";
    ctx.beginPath();
    ctx.arc(x, y - 19, 10, Math.PI, Math.PI * 2);
    ctx.fill();

    ctx.font = "bold 9px Arial";
    const label = s.name;
    const width = Math.min(ctx.measureText(label).width + 10, 100);

    rounded(x - width / 2, y - 43, width, 16, 4, "#ffffff");
    text(label, x, y - 32, 9, "#26334b");

    if (s.captured) {
        ctx.strokeStyle = "#80ffff";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(x, y - 4, 19, 0, Math.PI * 2);
        ctx.stroke();
    }
}

function drawUFO() {
    const x = 400;
    const y = 78 + Math.sin(frame * .035) * 5;

    const glow = ctx.createRadialGradient(x, y, 5, x, y, 105);
    glow.addColorStop(0, "rgba(110,255,255,.3)");
    glow.addColorStop(1, "rgba(110,255,255,0)");

    ctx.fillStyle = glow;
    ctx.beginPath();
    ctx.arc(x, y, 105, 0, Math.PI * 2);
    ctx.fill();

    if (selected >= 0 && students[selected]) {
        const s = students[selected];
        const sy = s.y - beam * 1.8;

        ctx.fillStyle = "rgba(100,255,220,.25)";
        ctx.beginPath();
        ctx.moveTo(x - 27, y + 12);
        ctx.lineTo(s.x - 25, sy);
        ctx.lineTo(s.x + 25, sy);
        ctx.lineTo(x + 27, y + 12);
        ctx.closePath();
        ctx.fill();
    }

    ctx.fillStyle = "#baf6ff";
    ctx.beginPath();
    ctx.ellipse(x, y - 9, 39, 26, 0, Math.PI, 0);
    ctx.fill();

    ctx.fillStyle = "#5b94bd";
    ctx.beginPath();
    ctx.ellipse(x, y - 9, 26, 15, 0, Math.PI, 0);
    ctx.fill();

    const metal = ctx.createLinearGradient(x - 100, y, x + 100, y + 30);
    metal.addColorStop(0, "#c7d7e6");
    metal.addColorStop(.5, "#ffffff");
    metal.addColorStop(1, "#7189b1");

    ctx.fillStyle = metal;
    ctx.beginPath();
    ctx.ellipse(x, y + 5, 105, 23, 0, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "#64f7ff";
    ctx.beginPath();
    ctx.ellipse(x, y + 14, 57, 7, 0, 0, Math.PI * 2);
    ctx.fill();

    for (let i = -3; i <= 3; i++) {
        ctx.fillStyle = i % 2 ? "#fff49b" : "#7cffff";
        ctx.beginPath();
        ctx.arc(x + i * 25, y + 7, 4, 0, Math.PI * 2);
        ctx.fill();
    }

    rounded(x - 35, y - 32, 70, 19, 5, "#132442");
    text(selected >= 0 ? "HÚT!" : "UFO", x, y - 18, 11, "#83ffff");
}

function render() {
    frame++;

    // Khung cảnh co giãn theo canvas, không cuộn.
    const rectCanvas = canvas.getBoundingClientRect();
    const dpr = Math.min(window.devicePixelRatio || 1, 2);

    const targetW = Math.max(1, Math.round(rectCanvas.width * dpr));
    const targetH = Math.max(1, Math.round(rectCanvas.height * dpr));

    if (canvas.width !== targetW || canvas.height !== targetH) {
        canvas.width = targetW;
        canvas.height = targetH;
    }

    ctx.setTransform(
        canvas.width / 800, 0,
        0, canvas.height / 480, 0, 0
    );

    drawSky();
    drawBuildings();
    drawStreet();
    drawTree(110, 325);
    drawTree(685, 326);

    students.forEach(drawStudent);
    drawUFO();

    requestAnimationFrame(render);
}

function saveName() {
    const input = document.getElementById("name").value.trim();

    if (input) {
        player = input;
        document.getElementById("playerName").textContent = player;
        document.getElementById("message").textContent =
            "Xin chào " + player + "! Sẵn sàng khảo bài chưa?";
    }
}

function showQuiz(index) {
    const available = puzzles.filter(p => p.level <= level);
    currentPuzzle = available[Math.floor(Math.random() * available.length)];

    const p = currentPuzzle;

    document.getElementById("quiz").style.display = "block";
    document.getElementById("question").textContent = p.q;
    document.getElementById("hint").textContent = "";
    document.getElementById("hint").dataset.hint = p.hint;

    const container = document.getElementById("answers");
    container.innerHTML = "";

    p.a.forEach((answer, i) => {
        const btn = document.createElement("button");
        btn.textContent = answer;

        btn.onclick = () => {
            if (selected < 0 || answered[selected]) return;

            if (i === p.correct) {
                score += p.points;
                completed++;
                answered[selected] = true;

                document.getElementById("score").textContent = score;

                students[selected].visible = false;
                students[selected].captured = false;

                document.getElementById("message").textContent =
                    "🎉 Chính xác! +" + p.points + " điểm!";

                selected = -1;
                beam = 0;
                busy = false;

                if (completed >= 3) level = 2;
                if (completed >= 6) level = 3;

                document.getElementById("level").textContent = level;
                document.getElementById("quiz").style.display = "none";

                if (autoMode) {
                    clearTimeout(autoTimer);
                    autoTimer = setTimeout(randomPick, 1500);
                }
            } else {
                document.getElementById("message").textContent =
                    "❌ Chưa đúng! Hãy thử lại nhé.";
            }
        };

        container.appendChild(btn);
    });
}

function showHint() {
    const hint = document.getElementById("hint");
    hint.textContent = "💡 " + hint.dataset.hint;
}

function randomPick() {
    if (busy || selected >= 0) return;

    const available = students
        .map((student, index) => ({student, index}))
        .filter(item =>
            item.student.visible &&
            !item.student.captured &&
            !answered[item.index]
        );

    if (available.length === 0) {
        autoMode = false;
        document.getElementById("autoBtn").textContent = "▶ UFO tự chọn";

        document.getElementById("message").textContent =
            "🏆 Đã khảo bài hết nhân vật! Nhấn Chơi lại để bắt đầu mới.";
        return;
    }

    busy = true;

    const chosen = available[Math.floor(Math.random() * available.length)];
    selected = chosen.index;

    const student = students[selected];
    student.captured = true;
    beam = 0;

    document.getElementById("message").textContent =
        "🛸 UFO đã chọn ngẫu nhiên " + student.name + "!";

    const start = performance.now();
    const duration = 1100;

    function animateBeam(now) {
        beam = Math.min(100, ((now - start) / duration) * 100);

        if (now - start < duration) {
            requestAnimationFrame(animateBeam);
        } else {
            beam = 100;
            showQuiz(selected);
        }
    }

    requestAnimationFrame(animateBeam);
}

function toggleAuto() {
    autoMode = !autoMode;

    document.getElementById("autoBtn").textContent =
        autoMode ? "⏸ Dừng UFO" : "▶ UFO tự chọn";

    if (autoMode) {
        document.getElementById("message").textContent =
            "🛸 UFO đang tìm người ngẫu nhiên...";

        if (selected < 0 && !busy) {
            randomPick();
        }
    } else {
        clearTimeout(autoTimer);
        document.getElementById("message").textContent =
            "UFO đã dừng chế độ tự chọn.";
    }
}

function newGame() {
    score = 0;
    selected = -1;
    beam = 0;
    level = 1;
    completed = 0;
    answered = {};
    busy = false;

    clearTimeout(autoTimer);
    autoMode = false;

    document.getElementById("autoBtn").textContent = "▶ UFO tự chọn";
    document.getElementById("score").textContent = "0";
    document.getElementById("level").textContent = "1";
    document.getElementById("quiz").style.display = "none";

    resetStudents();

    document.getElementById("message").textContent =
        "🛸 Game mới! Nhấn UFO tự chọn để bắt đầu.";
}

document.getElementById("maxPlayers").addEventListener("change", () => {
    newGame();

    document.getElementById("message").textContent =
        "Đã tạo " + students.length +
        " nhân vật trong bản đồ. Đây chưa phải số người chơi trực tuyến.";
});

function toggleMusic() {
    if (!music) {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;

        if (!AudioContextClass) {
            document.getElementById("message").textContent =
                "Trình duyệt chưa hỗ trợ nhạc.";
            return;
        }

        audio = new AudioContextClass();
        music = true;

        const notes = [261.63, 329.63, 392.00, 329.63];
        let noteIndex = 0;

        function playNote() {
            if (!music || !audio) return;

            const osc = audio.createOscillator();
            const gain = audio.createGain();

            osc.type = "sine";
            osc.frequency.value = notes[noteIndex % notes.length];

            gain.gain.setValueAtTime(.0001, audio.currentTime);
            gain.gain.exponentialRampToValueAtTime(.025, audio.currentTime + .05);
            gain.gain.exponentialRampToValueAtTime(.0001, audio.currentTime + .35);

            osc.connect(gain);
            gain.connect(audio.destination);

            osc.start();
            osc.stop(audio.currentTime + .4);

            noteIndex++;
            musicTimer = setTimeout(playNote, 420);
        }

        audio.resume().then(playNote);
        document.getElementById("musicBtn").textContent = "🔇 Tắt nhạc";
    } else {
        music = false;
        clearTimeout(musicTimer);

        if (audio) {
            audio.close();
            audio = null;
        }

        document.getElementById("musicBtn").textContent = "🎵 Bật nhạc";
    }
}

resetStudents();
render();
</script>
</body>
</html>
"""

components.html(
    GAME,
    height=900,
    scrolling=False
)
