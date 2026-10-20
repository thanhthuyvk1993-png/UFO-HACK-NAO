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
    #MainMenu, footer, header {
        visibility: hidden;
    }

    .stApp {
        background: #080d20;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
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

body {
    margin: 0;
    background: #080d20;
    color: white;
    font-family: Arial, sans-serif;
    overflow-x: hidden;
}

#game {
    width: 100%;
    max-width: 1200px;
    margin: auto;
}

.header {
    text-align: center;
    padding: 15px 8px;
    background: linear-gradient(120deg, #101d46, #36165a);
    border-bottom: 2px solid #5ff5ff;
}

.logo {
    font-size: clamp(25px, 5vw, 43px);
    font-weight: 900;
    color: #70f7ff;
    text-shadow: 0 0 18px #13bfff;
    letter-spacing: 2px;
}

.subtitle {
    margin-top: 6px;
    color: #d7e6ff;
    font-size: 13px;
}

.hud {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 8px;
    padding: 12px;
    background: #101831;
}

.stat {
    padding: 9px 12px;
    background: #1b2850;
    border: 1px solid #5268a5;
    border-radius: 12px;
    font-size: 13px;
}

#scene {
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 800 / 480;
    background: #a7e7ff;
    touch-action: manipulation;
    cursor: pointer;
}

.controls {
    padding: 12px;
    background: #0d1530;
}

button, select, input {
    font: inherit;
}

button {
    border: 1px solid #68f4ff;
    background: linear-gradient(120deg, #164a80, #53328d);
    color: white;
    border-radius: 11px;
    padding: 11px 15px;
    cursor: pointer;
    font-weight: bold;
}

button:active {
    transform: scale(.97);
}

.row {
    display: flex;
    flex-wrap: wrap;
    gap: 9px;
    margin: 8px 0;
}

input, select {
    min-width: 0;
    padding: 10px;
    color: white;
    background: #172344;
    border: 1px solid #566a9d;
    border-radius: 9px;
}

#message {
    padding: 12px;
    background: #121d3b;
    border: 1px solid #40568d;
    border-radius: 12px;
    margin: 10px 0;
    line-height: 1.6;
}

#quiz {
    display: none;
    padding: 16px;
    background: linear-gradient(135deg, #192954, #311b52);
    border: 1px solid #70f7ff;
    border-radius: 15px;
    margin-top: 10px;
}

#question {
    font-size: 18px;
    font-weight: bold;
    line-height: 1.5;
    margin-bottom: 12px;
}

.answers {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 9px;
}

.answers button {
    min-height: 46px;
    overflow-wrap: anywhere;
}

#hint {
    color: #ffe89b;
    margin-top: 10px;
}

.note {
    color: #b9c9ed;
    font-size: 12px;
    line-height: 1.6;
}

@media(max-width: 500px) {
    .answers {
        grid-template-columns: 1fr;
    }

    .stat {
        padding: 8px;
        font-size: 12px;
    }

    .controls {
        padding: 9px;
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
        <div class="stat">👨‍🚀 Phi hành gia: <b id="playerName">Khách</b></div>
        <div class="stat">🧠 Cấp độ: <b id="level">1</b></div>
        <div class="stat">👥 Nhân vật: <b id="count">12</b></div>
    </div>

    <canvas id="scene" width="800" height="480"></canvas>

    <div class="controls">
        <div class="row">
            <input id="name" maxlength="20"
                   placeholder="Tên phi hành gia"
                   aria-label="Tên phi hành gia">

            <button onclick="saveName()">Lưu tên</button>
        </div>

        <div class="row">
            <label for="maxPlayers">Số người tối đa:</label>
            <select id="maxPlayers">
                <option>10</option>
                <option>20</option>
                <option>30</option>
                <option>50</option>
                <option selected>100</option>
            </select>

            <button onclick="newGame()">🔄 Chơi lại</button>
            <button onclick="toggleMusic()" id="musicBtn">
                🎵 Bật nhạc
            </button>
        </div>

        <div id="message">
            🛸 Chạm vào một học sinh trên bản đồ để UFO hút lên
            và bắt đầu khảo bài!
        </div>

        <div id="quiz">
            <div id="question"></div>
            <div class="answers" id="answers"></div>
            <div id="hint"></div>
            <div class="row">
                <button onclick="showHint()">💡 Gợi ý</button>
            </div>
        </div>

        <p class="note">
            Cách chơi: Chạm vào học sinh → UFO hút lên →
            trả lời câu đố để nhận điểm.
            Nhạc bắt đầu phát sau khi bạn bật nhạc.
        </p>
    </div>
</div>

<script>
const canvas = document.getElementById("scene");
const ctx = canvas.getContext("2d");

const W = 800;
const H = 480;

let score = 0;
let player = "Khách";
let selected = -1;
let beam = 0;
let moving = true;
let level = 1;
let answered = {};
let music = false;
let audio = null;
let musicTimer = null;
let frame = 0;
let completed = 0;

const names = [
    "Minh Huy", "Phương Mai", "Tuấn Minh",
    "Thanh Thảo", "Quỳnh Anh", "Huy Khánh",
    "Trúc Mai", "Đình Trọng", "Bảo Ngọc",
    "Gia Huy", "Minh Anh", "Hoàng Nam"
];

let students = [];

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
        hint: "Đọc kỹ câu hỏi nhé!",
        points: 100,
        level: 1
    },
    {
        q: "Dãy số 2, 6, 12, 20, 30, ... Số tiếp theo?",
        a: ["36", "40", "42", "44"],
        correct: 2,
        hint: "Hiệu giữa các số lần lượt là 4, 6, 8, 10.",
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
        hint: "Mỗi số gấp đôi số đứng trước.",
        points: 150,
        level: 2
    },
    {
        q: "12 tiếng chuông cách nhau 1 giây. Từ tiếng đầu đến tiếng cuối mất bao lâu?",
        a: ["10 giây", "11 giây", "12 giây", "13 giây"],
        correct: 1,
        hint: "12 tiếng chuông tạo ra 11 khoảng.",
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
    }
];

function resetStudents() {
    students = names.map((name, i) => ({
        name,
        x: 35 + (i % 6) * 135,
        y: 340 + Math.floor(i / 6) * 55,
        phase: Math.random() * 6,
        color: ["#f6d5b5", "#ffd8c2", "#e8bd96"][i % 3],
        shirt: ["#ffffff", "#8de3ff", "#ffda7a", "#ffc2dc"][i % 4],
        visible: true,
        captured: false
    }));
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

function text(str, x, y, size, color, align="center") {
    ctx.fillStyle = color;
    ctx.font = "bold " + size + "px Arial";
    ctx.textAlign = align;
    ctx.fillText(str, x, y);
}

function drawSky() {
    const sky = ctx.createLinearGradient(0, 0, 0, H);
    sky.addColorStop(0, "#5bc6ff");
    sky.addColorStop(1, "#e5f8ff");
    rect(0, 0, W, H, sky);

    // Mây
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
        {x:0, w:145, c:"#ffe0b9"},
        {x:145, w:140, c:"#e9d6ff"},
        {x:285, w:155, c:"#fff1d3"},
        {x:440, w:135, c:"#d8e7ff"},
        {x:575, w:125, c:"#ffe0b9"},
        {x:700, w:100, c:"#e8d9ff"}
    ];

    buildings.forEach((b, i) => {
        rect(b.x, 130, b.w, 170, b.c);
        rect(b.x, 125, b.w, 10, "#f8fafc");

        for (let wx = b.x + 14; wx < b.x + b.w - 12; wx += 42) {
            rect(wx, 151, 25, 35, "#83cafa");
            rect(wx - 2, 149, 29, 4, "#ffffff");
            rect(wx + 10, 151, 3, 35, "#ffffff");

            rect(wx, 205, 25, 32, "#8ad0ff");
            rect(wx - 2, 203, 29, 4, "#ffffff");
        }

        // Mái nhà
        rect(b.x, 240, b.w, 7, "#c8a27b");

        // Cửa hàng
        const shopColors = ["#f6b64b", "#fa746d", "#62b8aa"];
        rect(b.x, 250, b.w, 50, shopColors[i % 3]);

        rect(b.x, 250, b.w, 8, "#ffffff");

        const label = [
            "BÁNH MÌ", "TRÀ SỮA", "HỚT TÓC",
            "BÚN CHẢ", "KEM", "CÀ PHÊ"
        ][i];

        text(label, b.x + b.w / 2, 274, 11, "#26324a");

        for (let sx = b.x + 6; sx < b.x + b.w; sx += 20) {
            rect(sx, 288, 12, 12, "#fff7dc");
        }
    });
}

function drawStreet() {
    rect(0, 300, W, 55, "#6b7b8c");
    rect(0, 355, W, 125, "#d7c6a9");

    // Vạch đường
    for (let x = 0; x < W; x += 100) {
        rect(x, 324, 48, 4, "#ffffff");
    }

    // Vỉa hè
    rect(0, 352, W, 6, "#f4eee1");

    for (let x = 15; x < W; x += 120) {
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
    let y = s.y;

    if (s.captured) {
        y -= beam * 0.7;
        x += Math.sin(frame * .05) * 8;
    } else {
        y += Math.sin(frame * .045 + s.phase) * 2;
    }

    if (i % 3 === 0) {
        drawScooter(x, y + 12, i % 2 ? "#4e96ef" : "#ef6c70");
    }

    // Chân
    ctx.strokeStyle = "#344c7a";
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(x - 5, y + 13);
    ctx.lineTo(x - 8, y + 27);
    ctx.moveTo(x + 5, y + 13);
    ctx.lineTo(x + 10, y + 27);
    ctx.stroke();

    // Áo
    rounded(x - 10, y - 7, 20, 23, 5, s.shirt);

    // Tay
    ctx.strokeStyle = s.color;
    ctx.lineWidth = 5;
    ctx.beginPath();
    ctx.moveTo(x - 8, y - 2);
    ctx.lineTo(x - 15, y + 8);
    ctx.moveTo(x + 8, y - 2);
    ctx.lineTo(x + 15, y + 7);
    ctx.stroke();

    // Đầu
    ctx.fillStyle = s.color;
    ctx.beginPath();
    ctx.arc(x, y - 15, 10, 0, Math.PI * 2);
    ctx.fill();

    // Tóc
    ctx.fillStyle = "#342b2a";
    ctx.beginPath();
    ctx.arc(x, y - 19, 10, Math.PI, Math.PI * 2);
    ctx.fill();

    // Tên
    ctx.font = "bold 10px Arial";
    const width = ctx.measureText(s.name).width + 12;

    rounded(x - width / 2, y - 43, width, 17, 5, "#ffffff");
    text(s.name, x, y - 31, 9, "#26334b");

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
    const y = selected >= 0 ? 90 + beam * .2 : 75 + Math.sin(frame * .04) * 7;

    // Ánh sáng
    const glow = ctx.createRadialGradient(x, y, 5, x, y, 110);
    glow.addColorStop(0, "rgba(110,255,255,.30)");
    glow.addColorStop(1, "rgba(110,255,255,0)");
    ctx.fillStyle = glow;
    ctx.beginPath();
    ctx.arc(x, y, 110, 0, Math.PI * 2);
    ctx.fill();

    // Tia hút
    if (selected >= 0 && students[selected]) {
        const s = students[selected];
        const sy = s.y - beam * .7;

        ctx.fillStyle = "rgba(100,255,220,.23)";
        ctx.beginPath();
        ctx.moveTo(x - 27, y + 12);
        ctx.lineTo(s.x - 25, sy);
        ctx.lineTo(s.x + 25, sy);
        ctx.lineTo(x + 27, y + 12);
        ctx.closePath();
        ctx.fill();
    }

    // Vòm kính
    ctx.fillStyle = "#baf6ff";
    ctx.beginPath();
    ctx.ellipse(x, y - 9, 39, 26, 0, Math.PI, 0);
    ctx.fill();

    ctx.fillStyle = "#5b94bd";
    ctx.beginPath();
    ctx.ellipse(x, y - 9, 26, 15, 0, Math.PI, 0);
    ctx.fill();

    // Thân đĩa bay
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
            "Chào phi hành gia " + player +
            "! Chạm vào học sinh để bắt đầu nhiệm vụ.";
    }
}

function showQuiz(index) {
    const available = puzzles.filter(p => p.level <= level);
    const p = available[index % available.length];

    document.getElementById("quiz").style.display = "block";
    document.getElementById("question").textContent = p.q;
    document.getElementById("hint").textContent = "";

    const container = document.getElementById("answers");
    container.innerHTML = "";

    p.a.forEach((answer, i) => {
        const btn = document.createElement("button");
        btn.textContent = answer;

        btn.onclick = () => {
            if (answered[selected]) return;

            if (i === p.correct) {
                score += p.points;
                completed++;

                answered[selected] = true;

                document.getElementById("score").textContent = score;
                document.getElementById("message").textContent =
                    "🎉 Chính xác! +" + p.points +
                    " điểm. Bạn đã giải mã thành công!";

                students[selected].visible = false;
                selected = -1;
                beam = 0;

                if (completed >= 3) level = 2;
                if (completed >= 6) level = 3;

                document.getElementById("level").textContent = level;
                document.getElementById("quiz").style.display = "none";
            } else {
                document.getElementById("message").textContent =
                    "❌ Chưa đúng! Hãy thử đáp án khác.";
            }
        };

        container.appendChild(btn);
    });

    document.getElementById("hint").dataset.hint = p.hint;
}

function showHint() {
    const hint = document.getElementById("hint");
    hint.textContent = "💡 " + hint.dataset.hint;
}

canvas.addEventListener("click", function(event) {
    const rect = canvas.getBoundingClientRect();

    const x = (event.clientX - rect.left) * W / rect.width;
    const y = (event.clientY - rect.top) * H / rect.height;

    // Chạm UFO để biết cách chơi
    if (y < 130 && x > 280 && x < 520) {
        document.getElementById("message").textContent =
            "🛸 Hãy chạm vào một học sinh ở phía dưới UFO!";
        return;
    }

    let closest = -1;
    let distance = Infinity;

    students.forEach((s, i) => {
        if (!s.visible || s.captured) return;

        const d = Math.hypot(x - s.x, y - s.y);

        if (d < distance && d < 55) {
            distance = d;
            closest = i;
        }
    });

    if (closest >= 0) {
        selected = closest;
        beam = 0;

        students[closest].captured = true;

        document.getElementById("message").textContent =
            "🛸 UFO đang hút " + students[closest].name +
            " lên phi thuyền! Chuẩn bị khảo bài...";

        const start = performance.now();
        const duration = 1000;

        function animateBeam(now) {
            beam = Math.min(100, (now - start) / duration * 100);

            if (now - start < duration) {
                requestAnimationFrame(animateBeam);
            } else {
                showQuiz(closest);
            }
        }

        requestAnimationFrame(animateBeam);
    } else {
        document.getElementById("message").textContent =
            "Hãy chạm gần nhân vật có tên trên bản đồ nhé!";
    }
});

function newGame() {
    score = 0;
    selected = -1;
    beam = 0;
    level = 1;
    completed = 0;
    answered = {};

    resetStudents();

    document.getElementById("score").textContent = "0";
    document.getElementById("level").textContent = "1";
    document.getElementById("quiz").style.display = "none";

    document.getElementById("message").textContent =
        "🛸 Nhiệm vụ mới bắt đầu! Chọn một học sinh để khảo bài.";

    document.getElementById("count").textContent = students.length;
}

function toggleMusic() {
    if (!music) {
        const AudioContextClass =
            window.AudioContext || window.webkitAudioContext;

        if (!AudioContextClass) {
            document.getElementById("message").textContent =
                "Trình duyệt này chưa hỗ trợ phát nhạc.";
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
            gain.gain.exponentialRampToValueAtTime(
                .035, audio.currentTime + .05
            );
            gain.gain.exponentialRampToValueAtTime(
                .0001, audio.currentTime + .35
            );

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

document.getElementById("maxPlayers").addEventListener("change", function() {
    document.getElementById("message").textContent =
        "Đã đặt giới hạn cấu hình: " + this.value +
        " người. Bản hiện tại là game đơn trên mỗi thiết bị; " +
        "chưa có hệ thống phòng trực tuyến đồng bộ.";
});

resetStudents();
render();
</script>
</body>
</html>
"""

components.html(GAME, height=950, scrolling=True)

components.html(GAME, height=950, scrolling=True)
