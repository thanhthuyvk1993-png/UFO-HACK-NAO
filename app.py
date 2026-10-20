import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="UFO HACK NÃO 🛸",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background: #100c2b;
        color: white;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1400px;
        padding: 1rem 1rem 0.5rem;
    }

    h1 {
        text-align: center;
        color: #ffe66d;
        font-weight: 900;
    }

    .stMarkdown, label {
        color: white !important;
    }

    div[data-testid="stNumberInput"] input {
        text-align: center;
    }

    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1>🛸 UFO HACK NÃO 🧠</h1>"
    "<p style='text-align:center'>"
    "👽 UFO săn người · ✨ Nhân vật phép thuật · 🎵 Nhạc vũ trụ"
    "</p>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    player_count = st.number_input(
        "👥 Số người chơi",
        min_value=1,
        max_value=100,
        value=20,
        step=1
    )

with col2:
    level = st.selectbox(
        "🧠 Cấp độ",
        ["Dễ", "Trung bình", "Hack não"]
    )

with col3:
    speed = st.select_slider(
        "🛸 Tốc độ UFO",
        options=["Chậm", "Vừa", "Nhanh"],
        value="Vừa"
    )

# Toàn bộ game chạy trong một khung HTML độc lập.
# Nhạc và hoạt ảnh được xử lý trực tiếp bằng JavaScript.

game_html = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport"
 content="width=device-width, initial-scale=1, maximum-scale=1,
 user-scalable=no">

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
    font-family: Arial, Helvetica, sans-serif;
    background: #100c2b;
    color: white;
}

#game {
    width: 100%;
    height: 590px;
    max-height: 85vh;
    min-height: 430px;
    overflow: hidden;
    position: relative;
    border: 2px solid #8067ff;
    border-radius: 20px;
    background:
        radial-gradient(ellipse at 50% 0%,
        #493a8d 0%, #17113b 50%, #09091c 100%);
    display: flex;
    flex-direction: column;
}

#topbar {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 12px;
    gap: 5px;
    background: rgba(10, 7, 35, .8);
    border-bottom: 1px solid #54449c;
}

.badge {
    background: #2a215c;
    color: #ffe66d;
    padding: 7px 9px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: bold;
    white-space: nowrap;
}

#arena {
    width: 100%;
    flex: 1;
    min-height: 0;
    position: relative;
    overflow: hidden;
}

canvas {
    display: block;
    width: 100%;
    height: 100%;
    touch-action: manipulation;
}

#bottom {
    flex-shrink: 0;
    background: rgba(10, 7, 35, .94);
    border-top: 1px solid #54449c;
    padding: 8px;
}

.buttons {
    display: flex;
    gap: 6px;
    justify-content: center;
    flex-wrap: wrap;
}

button {
    border: 0;
    border-radius: 12px;
    padding: 10px 12px;
    font-size: 12px;
    font-weight: bold;
    color: white;
    background: #6845df;
    cursor: pointer;
    touch-action: manipulation;
}

button:active {
    transform: scale(.96);
}

.primary {
    background: linear-gradient(135deg, #ff4fa0, #8c4dff);
}

.music {
    background: #26345d;
}

#message {
    color: #ffe99a;
    text-align: center;
    font-size: 12px;
    min-height: 16px;
    margin-top: 6px;
}

#quiz {
    display: none;
    position: absolute;
    inset: 8px;
    z-index: 10;
    border: 2px solid #bba5ff;
    border-radius: 18px;
    background: rgba(20, 14, 57, .97);
    padding: 16px;
    text-align: center;
    overflow-y: auto;
}

#quiz h3 {
    color: #ffe66d;
}

#question {
    font-size: 17px;
    line-height: 1.5;
    font-weight: bold;
}

#answer {
    width: 100%;
    max-width: 300px;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #9480ff;
    background: #171033;
    color: white;
    font-size: 16px;
    margin: 10px auto;
}

#result {
    color: #a5ffca;
    font-weight: bold;
    line-height: 1.5;
}

.quizbuttons {
    display: flex;
    gap: 8px;
    justify-content: center;
    flex-wrap: wrap;
}

@media (max-width: 500px) {
    #game {
        height: 590px;
        max-height: 78vh;
        min-height: 400px;
        border-radius: 14px;
    }

    .badge {
        padding: 6px;
        font-size: 10px;
    }

    button {
        padding: 9px;
        font-size: 11px;
    }

    #question {
        font-size: 15px;
    }
}
</style>
</head>

<body>
<div id="game">

    <div id="topbar">
        <div class="badge">🛸 UFO HACK NÃO</div>
        <div class="badge" id="counter">👥 0/20</div>
        <div class="badge" id="levelBadge">🧠 DỄ</div>
    </div>

    <div id="arena">
        <canvas id="canvas"></canvas>

        <div id="quiz">
            <h3>🛸 UFO ĐÃ CHỌN BẠN!</h3>
            <div id="chosenName"></div>
            <p id="question"></p>

            <input id="answer"
                   type="text"
                   autocomplete="off"
                   placeholder="Nhập câu trả lời...">

            <div class="quizbuttons">
                <button class="primary" onclick="checkAnswer()">
                    ✨ Trả lời
                </button>
                <button onclick="closeQuiz()">
                    Đóng
                </button>
            </div>

            <p id="result"></p>
        </div>
    </div>

    <div id="bottom">
        <div class="buttons">
            <button class="primary" onclick="startGame()">
                🚀 BẮT ĐẦU
            </button>

            <button onclick="choosePerson()">
                👽 UFO CHỌN NGƯỜI
            </button>

            <button class="music" id="musicBtn"
                    onclick="toggleMusic()">
                🎵 BẬT NHẠC
            </button>
        </div>

        <div class="buttons" style="margin-top:6px">
            <button onclick="changeVolume(-1)">🔉 Giảm nhạc</button>
            <button onclick="changeVolume(1)">🔊 Tăng nhạc</button>
        </div>

        <div id="message">
            Nhấn BẮT ĐẦU để triệu hồi UFO! ✨
        </div>
    </div>
</div>

<script>
"use strict";

const CONFIG = {
    players: __PLAYERS__,
    level: "__LEVEL__",
    speed: "__SPEED__"
};

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let W = 800;
let H = 400;
let frame = 0;
let running = false;
let beam = 0;
let selected = -1;
let playerList = [];
let stars = [];
let score = 0;
let currentQuestion = null;
let answered = new Set();

let music = false;
let audio = null;
let musicTimer = null;
let musicVolume = 0.10;

const names = [
    "Thỏ Hồng", "Minh Huy", "Phương Mai",
    "Tuấn Minh", "Quỳnh Anh", "Trúc Mai",
    "Hải", "Thanh Thảo", "Huy Khánh",
    "Dũng", "Mạnh", "Bảo Ngọc",
    "Khánh Linh", "Gia Huy", "Minh Anh",
    "Đức Anh", "Phương Linh", "Hoàng",
    "Nhật Minh", "Tuấn Anh"
];

const quizzes = {
    "Dễ": [
        {q:"Có 3 quả táo, lấy đi 2 quả. Bạn có mấy quả?",
         a:["2","hai"]},
        {q:"Một tuần có bao nhiêu ngày?",
         a:["7","bảy"]},
        {q:"Số tiếp theo: 2, 4, 6, 8, ...?",
         a:["10","mười"]},
        {q:"Con gì có 4 chân nhưng không tự đi?",
         a:["cái bàn","bàn"]},
        {q:"1 kg bông và 1 kg sắt, cái nào nặng hơn?",
         a:["bằng nhau","như nhau","bang nhau"]}
    ],

    "Trung bình": [
        {q:"Số tiếp theo: 1, 1, 2, 3, 5, 8, ...?",
         a:["13","mười ba"]},
        {q:"Có 5 người, mỗi người bắt tay tất cả người còn lại. Có bao nhiêu cái bắt tay?",
         a:["10","mười"]},
        {q:"Một chiếc đồng hồ điểm 6 tiếng trong 5 giây. Điểm 12 tiếng mất bao lâu?",
         a:["11 giây","11","mười một giây"]},
        {q:"Tôi càng lấy đi, tôi càng lớn. Tôi là gì?",
         a:["cái hố","hố","cai ho"]},
        {q:"Số nào nhân với số nào cũng bằng chính nó?",
         a:["0","không"]}
    ],

    "Hack não": [
        {q:"Một người có 2 đồng tiền tổng cộng 15 nghìn đồng. Một đồng không phải 5 nghìn. Đó là hai đồng nào?",
         a:["10 và 5","5 và 10","mười nghìn và năm nghìn"]},
        {q:"Có 10 con cá trong bể, 2 con chết. Còn mấy con cá trong bể?",
         a:["10","mười"]},
        {q:"Bạn vượt người đứng thứ hai trong cuộc đua. Bạn đứng thứ mấy?",
         a:["thứ hai","2","hai"]},
        {q:"Số tiếp theo: 1, 4, 9, 16, 25, ...?",
         a:["36","ba mươi sáu"]},
        {q:"Một căn phòng có 4 góc, mỗi góc có một con mèo. Mỗi con mèo nhìn thấy 3 con còn lại. Có bao nhiêu con mèo?",
         a:["4","bốn"]}
    ]
};

function resizeCanvas() {
    const rect = canvas.getBoundingClientRect();

    if (rect.width <= 0 || rect.height <= 0) return;

    const dpr = Math.min(window.devicePixelRatio || 1, 2);

    W = rect.width;
    H = rect.height;

    canvas.width = Math.round(W * dpr);
    canvas.height = Math.round(H * dpr);

    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    stars = Array.from({length: 55}, () => ({
        x: Math.random() * W,
        y: Math.random() * H,
        r: Math.random() * 1.7 + .3,
        phase: Math.random() * 6
    }));

    makePlayers();
    draw();
}

function makePlayers() {
    playerList = [];

    const count = CONFIG.players;
    const cols = Math.max(3, Math.floor(W / 65));
    const rows = Math.ceil(count / cols);

    for (let i = 0; i < count; i++) {
        const col = i % cols;
        const row = Math.floor(i / cols);

        playerList.push({
            name: names[i % names.length] +
                  (i >= names.length ? " " + (i + 1) : ""),
            x: (col + 0.5) * W / cols,
            y: H * 0.43 + row * Math.min(45, H * 0.13),
            type: i % 5,
            phase: Math.random() * 6,
            visible: true,
            captured: false
        });
    }

    document.getElementById("counter").textContent =
        "👥 " + count + " người";

    document.getElementById("levelBadge").textContent =
        "🧠 " + CONFIG.level.toUpperCase();
}

function roundedRect(x, y, w, h, r, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.roundRect(x, y, w, h, r);
    ctx.fill();
}

function drawBackground() {
    const gradient = ctx.createLinearGradient(0, 0, 0, H);

    gradient.addColorStop(0, "#201547");
    gradient.addColorStop(1, "#111c37");

    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, W, H);

    for (const s of stars) {
        const alpha = .45 + Math.sin(frame * .04 + s.phase) * .4;

        ctx.globalAlpha = alpha;
        ctx.fillStyle = "#ffffff";
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
        ctx.fill();
    }

    ctx.globalAlpha = 1;

    // Mặt đất
    ctx.fillStyle = "#263956";
    ctx.fillRect(0, H * .77, W, H * .23);

    // Thành phố
    const buildingW = Math.max(40, W / 12);

    for (let x = 0; x < W; x += buildingW) {
        const bh = H * (.12 + ((Math.floor(x) % 4) * .035));

        ctx.fillStyle = "#39345f";
        ctx.fillRect(x, H * .77 - bh, buildingW - 3, bh);

        for (let wy = H * .77 - bh + 8; wy < H * .75; wy += 13) {
            ctx.fillStyle = "#ffe69b";

            for (let wx = x + 7; wx < x + buildingW - 6; wx += 13) {
                ctx.fillRect(wx, wy, 4, 5);
            }
        }
    }

    ctx.fillStyle = "#131a35";
    ctx.fillRect(0, H * .77, W, H * .035);
}

function drawUFO() {
    const ux = W / 2;
    const uy = H * .20 + Math.sin(frame * .04) * 4;

    // Luồng sáng
    if (beam > 0) {
        const grad = ctx.createLinearGradient(
            ux, uy + 15, ux, H * .83
        );

        grad.addColorStop(0, "rgba(115,255,230,.48)");
        grad.addColorStop(1, "rgba(115,255,230,0)");

        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.moveTo(ux - 18, uy + 10);
        ctx.lineTo(ux - 65 - beam, H * .84);
        ctx.lineTo(ux + 65 + beam, H * .84);
        ctx.lineTo(ux + 18, uy + 10);
        ctx.closePath();
        ctx.fill();
    }

    // Vòm UFO
    ctx.fillStyle = "#83f9f1";
    ctx.beginPath();
    ctx.ellipse(ux, uy - 10, 26, 18, 0, Math.PI, Math.PI * 2);
    ctx.fill();

    // Thân tàu
    const g = ctx.createLinearGradient(ux - 75, uy, ux + 75, uy);

    g.addColorStop(0, "#b8c7ff");
    g.addColorStop(.5, "#ffffff");
    g.addColorStop(1, "#9a8bff");

    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.ellipse(ux, uy, 77, 19, 0, 0, Math.PI * 2);
    ctx.fill();

    // Viền
    ctx.strokeStyle = "#91e7ff";
    ctx.lineWidth = 2;
    ctx.stroke();

    // Đèn
    for (let i = -2; i <= 2; i++) {
        ctx.fillStyle = frame % 30 < 15 ? "#ffe66d" : "#ff75ce";
        ctx.beginPath();
        ctx.arc(ux + i * 27, uy + 7, 3.5, 0, Math.PI * 2);
        ctx.fill();
    }

    ctx.fillStyle = "#a3fff4";
    ctx.beginPath();
    ctx.ellipse(ux, uy + 19, 24, 5, 0, 0, Math.PI * 2);
    ctx.fill();
}

function drawCharacter(p, i) {
    if (!p.visible) return;

    let x = p.x;
    let y = p.y + Math.sin(frame * .04 + p.phase) * 2;

    if (p.captured) {
        y -= beam * 1.25;
    }

    ctx.save();
    ctx.translate(x, y);

    const scale = Math.min(1, W / 650);
    ctx.scale(scale, scale);

    // Bóng
    ctx.fillStyle = "rgba(0,0,0,.2)";
    ctx.beginPath();
    ctx.ellipse(0, 22, 13, 4, 0, 0, Math.PI * 2);
    ctx.fill();

    // Chân
    ctx.strokeStyle = "#392c40";
    ctx.lineWidth = 4;
    ctx.lineCap = "round";
    ctx.beginPath();
    ctx.moveTo(-5, 8);
    ctx.lineTo(-7, 21);
    ctx.moveTo(5, 8);
    ctx.lineTo(7, 21);
    ctx.stroke();

    if (p.type === 0) {
        // Thỏ hồng
        ctx.fillStyle = "#f6a8ca";
        ctx.strokeStyle = "#573447";
        ctx.lineWidth = 2.5;

        ctx.beginPath();
        ctx.ellipse(-7, -26, 6, 17, -.15, 0, Math.PI * 2);
        ctx.ellipse(7, -26, 6, 17, .15, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.roundRect(-11, -4, 22, 24, 7);
        ctx.arc(0, -13, 15, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#573447";
        ctx.beginPath();
        ctx.arc(-5, -15, 2, 0, Math.PI * 2);
        ctx.arc(5, -15, 2, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = "#573447";
        ctx.beginPath();
        ctx.moveTo(-3, -8);
        ctx.lineTo(0, -6);
        ctx.lineTo(3, -8);
        ctx.stroke();

        ctx.fillStyle = "#ff759f";
        ctx.beginPath();
        ctx.arc(-10, -10, 3, 0, Math.PI * 2);
        ctx.arc(10, -10, 3, 0, Math.PI * 2);
        ctx.fill();

    } else if (p.type === 1) {
        // Cậu bé áo đỏ
        ctx.fillStyle = "#ffe64f";
        ctx.strokeStyle = "#30212b";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.roundRect(-13, 2, 26, 15, 4);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#e62c46";
        ctx.beginPath();
        ctx.moveTo(-12, -16);
        ctx.lineTo(12, -16);
        ctx.lineTo(15, 7);
        ctx.lineTo(-15, 7);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#ffc09d";
        ctx.beginPath();
        ctx.ellipse(0, -21, 16, 17, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#111015";
        ctx.beginPath();
        ctx.arc(0, -29, 17, Math.PI, Math.PI * 2);
        ctx.lineTo(15, -21);
        ctx.lineTo(5, -27);
        ctx.lineTo(-4, -23);
        ctx.lineTo(-15, -18);
        ctx.closePath();
        ctx.fill();

        ctx.strokeStyle = "#111015";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(-11, -23);
        ctx.lineTo(-3, -20);
        ctx.moveTo(11, -23);
        ctx.lineTo(3, -20);
        ctx.stroke();

    } else if (p.type === 2) {
        // Pháp sư hoàng gia
        ctx.fillStyle = "#fff4df";
        ctx.strokeStyle = "#c69b59";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(-11, -12);
        ctx.lineTo(11, -12);
        ctx.lineTo(19, 19);
        ctx.lineTo(-19, 19);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#90a992";
        ctx.strokeStyle = "#29372e";
        ctx.beginPath();
        ctx.arc(0, -22, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#e9b04f";
        ctx.beginPath();
        ctx.moveTo(-15, -33);
        ctx.lineTo(-12, -44);
        ctx.lineTo(-4, -37);
        ctx.lineTo(0, -47);
        ctx.lineTo(5, -37);
        ctx.lineTo(13, -44);
        ctx.lineTo(16, -33);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#18291f";
        ctx.beginPath();
        ctx.arc(-5, -23, 2, 0, Math.PI * 2);
        ctx.arc(5, -23, 2, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = "#8b553a";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(18, -3);
        ctx.lineTo(22, 21);
        ctx.stroke();

        ctx.fillStyle = "#ffe56b";
        ctx.beginPath();
        ctx.arc(17, -7, 4, 0, Math.PI * 2);
        ctx.fill();

    } else if (p.type === 3) {
        // Pháp sư tóc tím
        ctx.fillStyle = "#8250bd";
        ctx.strokeStyle = "#402454";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(-11, -12);
        ctx.lineTo(11, -12);
        ctx.lineTo(19, 19);
        ctx.lineTo(-19, 19);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#91a992";
        ctx.strokeStyle = "#29372e";
        ctx.beginPath();
        ctx.arc(0, -21, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#9958e5";
        ctx.strokeStyle = "#56306f";
        ctx.beginPath();

        for (let k = 0; k < 11; k++) {
            const angle = Math.PI + k * Math.PI / 10;
            const radius = k % 2 === 0 ? 23 : 15;
            const px = Math.cos(angle) * radius;
            const py = -24 + Math.sin(angle) * radius;

            if (k === 0) ctx.moveTo(px, py);
            else ctx.lineTo(px, py);
        }

        ctx.lineTo(13, -30);
        ctx.lineTo(5, -34);
        ctx.lineTo(-4, -30);
        ctx.lineTo(-13, -32);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#18291f";
        ctx.beginPath();
        ctx.arc(-5, -21, 2, 0, Math.PI * 2);
        ctx.arc(5, -21, 2, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = "#6f4ad1";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(18, -3);
        ctx.lineTo(22, 21);
        ctx.stroke();

        ctx.fillStyle = "#71f5ff";
        ctx.beginPath();
        ctx.arc(17, -7, 4, 0, Math.PI * 2);
        ctx.fill();

    } else {
        // Cô bé tóc hồng
        ctx.fillStyle = "#ff83b6";
        ctx.strokeStyle = "#9c326b";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(-11, -12);
        ctx.lineTo(11, -12);
        ctx.lineTo(19, 19);
        ctx.lineTo(-19, 19);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#91a992";
        ctx.strokeStyle = "#29372e";
        ctx.beginPath();
        ctx.arc(0, -22, 16, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#ff64ac";
        ctx.beginPath();
        ctx.arc(0, -28, 18, Math.PI, Math.PI * 2);
        ctx.lineTo(18, -16);
        ctx.lineTo(10, -20);
        ctx.lineTo(4, -16);
        ctx.lineTo(-4, -20);
        ctx.lineTo(-12, -16);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = "#ff3e91";
        ctx.beginPath();
        ctx.arc(-12, -35, 5, 0, Math.PI * 2);
        ctx.arc(12, -35, 5, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = "#17261e";
        ctx.beginPath();
        ctx.arc(-5, -22, 2, 0, Math.PI * 2);
        ctx.arc(5, -22, 2, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = "#ffe76c";
        ctx.beginPath();
        ctx.arc(0, -6, 4, 0, Math.PI * 2);
        ctx.fill();
    }

    // Hiệu ứng lấp lánh
    if (p.captured) {
        for (let k = 0; k < 5; k++) {
            const angle = frame * .09 + k * Math.PI * 2 / 5;

            ctx.fillStyle = k % 2 ? "#ffe66d" : "#77f8ff";
            ctx.beginPath();
            ctx.arc(
                Math.cos(angle) * 22,
                Math.sin(angle) * 20 - 10,
                2.5, 0, Math.PI * 2
            );
            ctx.fill();
        }
    }

    ctx.restore();

    // Nhãn tên
    ctx.font = "bold 10px Arial";

    const labelWidth = Math.min(
        ctx.measureText(p.name).width + 10, 100
    );

    roundedRect(
        x - labelWidth / 2,
        y - 52,
        labelWidth,
        15,
        4,
        p.captured ? "#ffe66d" : "#ffffff"
    );

    ctx.fillStyle = "#29203e";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(p.name, x, y - 44, labelWidth - 5);
}

function draw() {
    drawBackground();

    // UFO ở trung tâm
    drawUFO();

    // Nhân vật
    playerList.forEach(drawCharacter);

    // Hướng dẫn
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.font = "bold 12px Arial";
    ctx.fillStyle = "#d6d0ff";

    if (!running) {
        ctx.fillText(
            "NHẤN BẮT ĐẦU ĐỂ TRIỆU HỒI UFO",
            W / 2,
            H * .37
        );
    }
}

function animate() {
    frame++;

    if (running && selected >= 0) {
        beam = Math.min(beam + 1.5, 30);

        const p = playerList[selected];

        if (p) {
            p.captured = true;
            p.y = Math.max(p.y - .4, H * .38);
        }
    }

    draw();
    requestAnimationFrame(animate);
}

function setMessage(message) {
    document.getElementById("message").textContent = message;
}

function startGame() {
    running = true;
    selected = -1;
    beam = 0;

    playerList.forEach(p => {
        p.visible = true;
        p.captured = false;
    });

    setMessage("🚀 UFO đã xuất hiện! Hãy chọn người chơi.");

    draw();
}

function choosePerson() {
    if (selected >= 0 && playerList[selected]) {
        playerList[selected].captured = false;
        playerList[selected].visible = true;
    }

    const available = playerList
        .map((p, i) => ({p, i}))
        .filter(item => !answered.has(item.i));

    if (available.length === 0) {
        answered.clear();
    }

    const candidates = playerList
        .map((p, i) => ({p, i}))
        .filter(item => !answered.has(item.i));

    const chosen = candidates[
        Math.floor(Math.random() * candidates.length)
    ];

    selected = chosen.i;
    running = true;
    beam = 0;

    playerList.forEach(p => p.captured = false);

    const p = playerList[selected];
    p.captured = true;

    document.getElementById("chosenName").textContent =
        "👤 Người chơi: " + p.name;

    const bank = quizzes[CONFIG.level];
    currentQuestion = bank[Math.floor(Math.random() * bank.length)];

    document.getElementById("question").textContent =
        "🧠 " + currentQuestion.q;

    document.getElementById("answer").value = "";
    document.getElementById("result").textContent = "";

    document.getElementById("quiz").style.display = "block";

    setMessage("🛸 UFO đã chọn " + p.name + "!");

    setTimeout(() => {
        document.getElementById("answer").focus();
    }, 100);
}

function checkAnswer() {
    if (!currentQuestion || selected < 0) return;

    const value = document.getElementById("answer")
        .value.trim().toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/đ/g, "d")
        .replace(/[^a-z0-9 ]/g, "")
        .replace(/\s+/g, " ");

    const valid = currentQuestion.a.map(a =>
        a.toLowerCase()
         .normalize("NFD")
         .replace(/[\u0300-\u036f]/g, "")
         .replace(/đ/g, "d")
         .replace(/[^a-z0-9 ]/g, "")
         .replace(/\s+/g, " ")
    );

    if (valid.includes(value)) {
        score++;

        document.getElementById("result").textContent =
            "🎉 Chính xác! Bạn đã giải được câu đố! Điểm: " + score;

        answered.add(selected);

        setMessage("✨ " + playerList[selected].name +
                   " trả lời đúng! Điểm: " + score);
    } else {
        document.getElementById("result").textContent =
            "🤔 Chưa đúng rồi! Hãy thử lại nhé.";

        setMessage("🧠 Hãy suy nghĩ thêm một chút!");
    }
}

function closeQuiz() {
    document.getElementById("quiz").style.display = "none";

    if (selected >= 0 && playerList[selected]) {
        playerList[selected].captured = false;
    }

    selected = -1;
    beam = 0;
    running = false;
    draw();
}

function toggleMusic() {
    if (!music) {
        const AudioContextClass =
            window.AudioContext || window.webkitAudioContext;

        if (!AudioContextClass) {
            setMessage("Trình duyệt chưa hỗ trợ âm thanh.");
            return;
        }

        audio = new AudioContextClass();
        music = true;

        document.getElementById("musicBtn").textContent =
            "🔇 TẮT NHẠC";

        audio.resume().then(playMagicMusic);

        setMessage("🎵 Nhạc vũ trụ đang phát!");
    } else {
        music = false;
        clearTimeout(musicTimer);

        if (audio) {
            audio.close();
            audio = null;
        }

        document.getElementById("musicBtn").textContent =
            "🎵 BẬT NHẠC";

        setMessage("🔇 Đã tắt nhạc.");
    }
}

function playMagicMusic() {
    if (!music || !audio) return;

    const melody = [
        523.25, 659.25, 783.99, 659.25,
        587.33, 698.46, 880.00, 698.46,
        523.25, 783.99, 1046.50, 783.99,
        659.25, 587.33, 523.25, 392.00
    ];

    let index = 0;

    function playNote() {
        if (!music || !audio) return;

        const now = audio.currentTime;
        const frequency = melody[index % melody.length];

        const osc = audio.createOscillator();
        const gain = audio.createGain();

        osc.type = "triangle";
        osc.frequency.value = frequency;

        gain.gain.setValueAtTime(.0001, now);
        gain.gain.exponentialRampToValueAtTime(
            musicVolume, now + .04
        );
        gain.gain.exponentialRampToValueAtTime(
            .0001, now + .32
        );

        osc.connect(gain);
        gain.connect(audio.destination);

        osc.start(now);
        osc.stop(now + .35);

        if (index % 4 === 0) {
            const bass = audio.createOscillator();
            const bg = audio.createGain();

            bass.type = "sine";
            bass.frequency.value = 130.81;

            bg.gain.setValueAtTime(.0001, now);
            bg.gain.exponentialRampToValueAtTime(
                musicVolume * .4, now + .04
            );
            bg.gain.exponentialRampToValueAtTime(
                .0001, now + .28
            );

            bass.connect(bg);
            bg.connect(audio.destination);

            bass.start(now);
            bass.stop(now + .3);
        }

        index++;
        musicTimer = setTimeout(playNote, 280);
    }

    playNote();
}

function changeVolume(direction) {
    musicVolume = Math.max(
        .01,
        Math.min(.20, musicVolume + direction * .02)
    );

    setMessage(
        "🔊 Âm lượng: " +
        Math.round(musicVolume / .20 * 100) + "%"
    );
}

document.getElementById("answer").addEventListener(
    "keydown",
    event => {
        if (event.key === "Enter") checkAnswer();
    }
);

window.addEventListener("resize", resizeCanvas);

if ("ResizeObserver" in window) {
    new ResizeObserver(resizeCanvas).observe(
        document.getElementById("arena")
    );
}

makePlayers();
resizeCanvas();
animate();
</script>
</body>
</html>
"""

# Đưa cài đặt Streamlit vào game.
game_html = (
    game_html
    .replace("__PLAYERS__", str(int(player_count)))
    .replace("__LEVEL__", level)
    .replace("__SPEED__", speed)
)

components.html(
    game_html,
    height=610,
    scrolling=False
)

st.markdown(
    "<p style='text-align:center;color:#bdb6e9;font-size:12px'>"
    "🛸 UFO HACK NÃO · Chơi vui vẻ, thử thách trí thông minh!"
    "</p>",
    unsafe_allow_html=True
)
