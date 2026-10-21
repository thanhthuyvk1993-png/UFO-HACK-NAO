import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="UFO HACK NÃO",
    page_icon="🛸",
    layout="wide"
)

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background: #070b19;
    }
    .block-container {
        padding-top: 1rem;
        max-width: 1500px;
    }
    header, footer, #MainMenu {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

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
    background: #070b19;
    color: white;
    font-family: Arial, sans-serif;
}

#game-container {
    position: relative;
    width: 100%;
    height: 620px;
    overflow: hidden;
    border: 2px solid #607bd4;
    border-radius: 16px;
    background: linear-gradient(
        #0c1430 0%,
        #17264b 58%,
        #89909f 58%,
        #252d3c 64%,
        #202735 100%
    );
}

#sky {
    position: absolute;
    inset: 0 0 42% 0;
    overflow: hidden;
}

.star {
    position: absolute;
    width: 3px;
    height: 3px;
    background: white;
    border-radius: 50%;
}

.moon {
    position: absolute;
    right: 12%;
    top: 25px;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: #fff2a3;
    box-shadow: 0 0 25px #ffe9a0;
}

.building {
    position: absolute;
    bottom: 0;
    background: #1b2946;
    border: 1px solid #526183;
}

.window {
    position: absolute;
    width: 17%;
    height: 10px;
    background: #ffdf69;
    box-shadow: 0 0 5px #ffcf43;
}

#sidewalk {
    position: absolute;
    left: 0;
    right: 0;
    top: 56%;
    height: 34px;
    background: #89909f;
    border-bottom: 4px solid #555f70;
}

#road {
    position: absolute;
    left: 0;
    right: 0;
    top: 62%;
    bottom: 0;
    background: linear-gradient(#3c4351, #202735);
}

.lane {
    position: absolute;
    left: 0;
    right: 0;
    top: 81%;
    height: 4px;
    background: repeating-linear-gradient(
        90deg,
        #ffe6a0 0 46px,
        transparent 46px 86px
    );
}

#ufo {
    position: absolute;
    right: 9%;
    top: 60px;
    font-size: 40px;
    z-index: 6;
    filter: drop-shadow(0 0 12px #68eaff);
    animation: hoverUfo 2s ease-in-out infinite;
}

@keyframes hoverUfo {
    50% {
        transform: translateY(-9px) rotate(-3deg);
    }
}

#beam {
    display: none;
    position: absolute;
    top: 35px;
    left: 50%;
    transform: translateX(-50%);
    width: 65px;
    height: 110px;
    background: linear-gradient(#7df9ff99, #7df9ff05);
    clip-path: polygon(40% 0, 60% 0, 100% 100%, 0 100%);
    z-index: -1;
}

.person {
    position: absolute;
    z-index: 4;
    width: 36px;
    height: 85px;
    text-align: center;
    transform: translateX(-50%);
}

.person .hair {
    position: relative;
    top: 4px;
    margin: auto;
    width: 16px;
    height: 6px;
    background: #38291f;
    border-radius: 6px 6px 0 0;
    z-index: 1;
}

.person .head {
    width: 16px;
    height: 17px;
    border-radius: 45%;
    background: #f2c49a;
    margin: auto;
    border: 1px solid #8d6147;
}

.person .body {
    width: 22px;
    height: 28px;
    margin: 0 auto;
    border-radius: 6px 6px 3px 3px;
    background: var(--shirt);
}

.person .legs {
    display: flex;
    justify-content: center;
    gap: 4px;
}

.person .legs span {
    width: 8px;
    height: 24px;
    background: #263044;
    border-radius: 0 0 5px 5px;
}

.person .label {
    font-size: 9px;
    font-weight: bold;
    text-shadow: 0 1px 3px black;
    white-space: nowrap;
}

.person.captured {
    animation: abduct 0.8s ease-in forwards;
}

@keyframes abduct {
    to {
        transform: translate(-50%, -140px) scale(0.2);
        opacity: 0;
    }
}

#topbar {
    position: absolute;
    top: 12px;
    left: 12px;
    z-index: 10;
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.pill {
    padding: 8px 12px;
    border: 1px solid #657cc3;
    border-radius: 20px;
    background: #0b122be8;
    font-size: 13px;
    font-weight: bold;
}

#status {
    position: absolute;
    top: 58px;
    left: 12px;
    z-index: 10;
    color: #ffe45c;
    font-size: 13px;
    font-weight: bold;
    text-shadow: 0 2px 5px black;
    max-width: 65%;
}

#ufo-catch-btn {
    position: absolute;
    top: 12px;
    right: 12px;
    z-index: 20;
    padding: 12px 16px;
    border: 2px solid #ffe34d;
    border-radius: 25px;
    background: linear-gradient(135deg, #6554ff, #251c64);
    color: white;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 0 15px #ffe34d88;
}

#ufo-catch-btn:hover {
    background: linear-gradient(135deg, #ffca28, #ff7b00);
}

#ufo-catch-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

#question-card {
    position: absolute;
    z-index: 30;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: min(520px, calc(100% - 24px));
    padding: 18px;
    border: 2px solid #ffdf48;
    border-radius: 20px;
    background: #101426f5;
    box-shadow: 0 0 28px #ffd83c66;
    text-align: center;
}

#question-card h2 {
    font-size: 24px;
    color: #ffe34d;
    margin: 0 0 12px;
}

#question-meta {
    font-size: 14px;
    line-height: 1.5;
    margin-bottom: 14px;
}

#question {
    font-size: 17px;
    line-height: 1.45;
    margin-bottom: 16px;
}

#answers {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 9px;
}

.answer {
    min-height: 46px;
    padding: 10px;
    border: 1px solid #6682d0;
    border-radius: 10px;
    background: #202d50;
    color: white;
    font-weight: bold;
    font-size: 14px;
    cursor: pointer;
}

.answer:hover:not(:disabled) {
    background: #354a7b;
}

#feedback {
    min-height: 24px;
    font-weight: bold;
    margin-top: 12px;
}

#next-btn, #start-btn, #restart-btn,
#start-overlay-btn {
    border: 0;
    border-radius: 9px;
    padding: 11px 17px;
    font-weight: bold;
    cursor: pointer;
    background: #ffdf48;
    color: #15192a;
    margin: 5px;
}

#controls {
    position: absolute;
    left: 12px;
    bottom: 10px;
    z-index: 12;
    display: flex;
    gap: 7px;
    align-items: center;
    flex-wrap: wrap;
}

#controls label {
    font-size: 12px;
    background: #101426ed;
    padding: 8px;
    border-radius: 8px;
}

#controls select {
    margin-left: 5px;
    max-width: 125px;
}

#start-screen {
    position: absolute;
    z-index: 25;
    inset: 0;
    background: #080d20c9;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 20px;
}

#start-box {
    max-width: 450px;
    background: #101426f5;
    border: 2px solid #ffdf48;
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 0 25px #ffdf4844;
}

#start-box h1 {
    color: #ffe34d;
}

#start-box p {
    line-height: 1.5;
}

#mute-btn {
    position: absolute;
    bottom: 12px;
    right: 12px;
    z-index: 15;
    border: 1px solid #8094d6;
    border-radius: 18px;
    padding: 8px 12px;
    background: #111a36;
    color: white;
    cursor: pointer;
}

@media(max-width:600px) {
    #game-container {
        height: 650px;
    }

    #question-card {
        padding: 12px;
    }

    #question-card h2 {
        font-size: 21px;
    }

    #question {
        font-size: 15px;
    }

    #ufo-catch-btn {
        font-size: 11px;
        padding: 9px;
        top: 50px;
    }

    #topbar {
        top: 10px;
    }

    #status {
        top: 92px;
    }

    .answer {
        font-size: 12px;
    }
}
</style>
</head>

<body>

<div id="game-container">

    <div id="sky">
        <div class="moon"></div>
    </div>

    <div id="sidewalk"></div>
    <div id="road"></div>
    <div class="lane"></div>

    <div id="ufo">
        <div id="beam"></div>
        🛸
    </div>

    <div id="topbar">
        <div class="pill">⭐ Điểm: <span id="score">0</span></div>
        <div class="pill">🧠 Câu: <span id="qcount">0/10</span></div>
        <div class="pill">👥 Còn: <span id="remaining">12</span></div>
    </div>

    <div id="status">
        Chọn mức độ rồi bấm BẮT ĐẦU GAME.
    </div>

    <!-- NÚT UFO NẰM BÊN TRONG GIAO DIỆN GAME -->
    <button id="ufo-catch-btn" onclick="catchRandomPerson()">
        🛸 UFO BẮT NGƯỜI
    </button>

    <div id="people"></div>

    <div id="controls">
        <label>
            Mức độ
            <select id="difficulty">
                <option value="easy">Mức 1 - Dễ vui</option>
                <option value="medium">Mức 2 - Hack não</option>
                <option value="hard">Mức 3 - Siêu khó</option>
            </select>
        </label>

        <label>
            Số người
            <select id="people-count">
                <option value="8">8</option>
                <option value="12" selected>12</option>
                <option value="16">16</option>
                <option value="20">20</option>
            </select>
        </label>

        <button id="start-btn" onclick="startGame()">
            ▶ BẮT ĐẦU GAME
        </button>

        <button id="restart-btn"
                onclick="restartGame()"
                style="display:none">
            ↻ Chơi lại
        </button>
    </div>

    <button id="mute-btn" onclick="toggleMute()">
        🔊 Âm thanh: Bật
    </button>

    <div id="question-card" style="display:none">
        <h2>🧠 HACK NÃO!</h2>
        <div id="question-meta"></div>
        <div id="question"></div>
        <div id="answers"></div>
        <div id="feedback"></div>

        <button id="next-btn"
                onclick="nextQuestion()"
                style="display:none">
            Câu tiếp theo ➜
        </button>
    </div>

    <div id="start-screen">
        <div id="start-box">
            <h1>🛸 UFO HACK NÃO</h1>

            <p>
                Hãy tự bấm nút
                <b>UFO BẮT NGƯỜI</b>
                trong giao diện để chọn ngẫu nhiên một người.
            </p>

            <p>
                Mỗi lần UFO bắt một người, một câu đố sẽ xuất hiện.
                Trả lời đúng để nhận điểm!
            </p>

            <button id="start-overlay-btn" onclick="startGame()">
                ▶ BẮT ĐẦU GAME
            </button>
        </div>
    </div>

</div>

<script>
const questionBank = {
easy: [
{q:"Cái gì có răng nhưng không biết nhai?",a:["Con cá","Cái lược","Con chó","Cái bát"],c:1},
{q:"Càng lấy đi thì càng lớn là cái gì?",a:["Cái hố","Ngọn núi","Cái cây","Đám mây"],c:0},
{q:"Thứ gì có cổ nhưng không có đầu?",a:["Con hươu","Cái áo","Cái chai","Cái bàn"],c:2},
{q:"Cái gì có mặt, có kim nhưng không có tay?",a:["Đồng hồ","Con mèo","Quyển sách","Cái quạt"],c:0},
{q:"Tháng nào có 28 ngày?",a:["Tháng 2","Tháng 4","Chỉ tháng 2","Tất cả các tháng"],c:3},
{q:"Cái gì đi lên đi xuống nhưng vẫn đứng yên?",a:["Cầu thang","Thang máy","Con dốc","Con chim"],c:0},
{q:"Cái gì càng lau càng ướt?",a:["Cái khăn","Cái bàn","Cửa kính","Đôi giày"],c:0},
{q:"Có thành phố nhưng không có nhà, có sông nhưng không có nước là gì?",a:["Bản đồ","Bức tranh","Cuốn truyện","Tivi"],c:0},
{q:"Cái gì có nhiều phím nhưng không mở được cửa?",a:["Bàn phím","Chùm chìa khóa","Cái kéo","Cái hộp"],c:0},
{q:"Bạn có thể giữ thứ gì sau khi đã trao nó cho người khác?",a:["Quả bóng","Lời hứa","Cái cốc","Chiếc ô"],c:1},
{q:"Cái gì luôn ở trước mặt nhưng không thể nhìn thấy?",a:["Quá khứ","Tương lai","Cái mũ","Cái bóng"],c:1},
{q:"Cái gì có chân mà không biết đi?",a:["Con chó","Cái bàn","Con vịt","Con người"],c:1}
],

medium: [
{q:"Một gia đình có 4 người con trai, mỗi người có một em gái chung. Hỏi có mấy người con?",a:["4","5","8","9"],c:1},
{q:"Bạn vượt qua người đứng thứ hai trong cuộc đua. Bạn đứng thứ mấy?",a:["Thứ nhất","Thứ hai","Thứ ba","Cuối cùng"],c:1},
{q:"Hai người cha và hai người con đi câu, bắt được 3 con cá, mỗi người một con. Vì sao?",a:["Có người không câu","Họ là ông, bố và con","Một con cá giả","Chia không đều"],c:1},
{q:"Có 5 quả táo, bạn lấy 2 quả. Bạn có mấy quả?",a:["3","2","5","0"],c:1},
{q:"Một kg sắt và một kg bông, cái nào nặng hơn?",a:["Sắt","Bông","Bằng nhau","Không so được"],c:2},
{q:"Một chiếc đồng hồ điểm 6 tiếng trong 5 giây. Điểm 12 tiếng mất bao lâu?",a:["10 giây","11 giây","12 giây","5 giây"],c:1},
{q:"Có 10 cây nến đang cháy, gió thổi tắt 2 cây. Cuối cùng còn mấy cây nến?",a:["8","2","10","0"],c:1},
{q:"Một người có 3 chiếc áo và 2 chiếc quần. Có bao nhiêu cách phối một áo với một quần?",a:["5","6","8","9"],c:1},
{q:"Nếu hôm kia là ngày trước thứ Sáu, hôm nay là thứ mấy?",a:["Thứ Tư","Thứ Năm","Thứ Sáu","Thứ Bảy"],c:2},
{q:"Có 3 công tắc ngoài phòng và một bóng đèn trong phòng kín. Bạn chỉ được vào phòng một lần. Làm sao biết công tắc nào bật đèn?",a:["Bật thử từng cái","Dùng nhiệt bóng đèn","Đoán","Không thể"],c:1},
{q:"Một con ốc sên leo cột 10 m, ban ngày lên 3 m, ban đêm tụt 2 m. Bao lâu lên tới đỉnh?",a:["8 ngày","10 ngày","7 ngày","5 ngày"],c:0},
{q:"Bạn có 6 quả trứng, làm vỡ 2, chiên 2, ăn 2. Còn lại mấy quả?",a:["2","4","6","0"],c:1}
],

hard: [
{q:"Dãy số: 2, 3, 5, 8, 12, 17, ... số tiếp theo là?",a:["21","22","23","24"],c:2},
{q:"Một cây gậy và quả bóng giá 110 nghìn. Gậy đắt hơn bóng 100 nghìn. Quả bóng giá bao nhiêu?",a:["10 nghìn","5 nghìn","15 nghìn","20 nghìn"],c:1},
{q:"Có 8 viên bi giống nhau, một viên nặng hơn. Ít nhất cần cân bao nhiêu lần để tìm ra viên nặng?",a:["1","2","3","4"],c:2},
{q:"Nếu 5 máy làm 5 món đồ trong 5 phút, 100 máy làm 100 món đồ trong bao lâu?",a:["100 phút","20 phút","5 phút","1 phút"],c:2},
{q:"Một số có hai chữ số. Tổng hai chữ số bằng 9; đảo vị trí thì số mới lớn hơn số cũ 27. Số ban đầu là?",a:["36","45","54","27"],c:0},
{q:"Dãy số: 1, 1, 2, 3, 5, 8, ... số tiếp theo?",a:["11","12","13","15"],c:2},
{q:"Một căn phòng có 4 góc, mỗi góc có một con mèo. Mỗi con mèo nhìn thấy 3 con mèo. Có tất cả mấy con mèo?",a:["4","8","12","16"],c:0},
{q:"Nếu 3 con mèo bắt 3 con chuột trong 3 phút, 100 con mèo bắt 100 con chuột trong bao lâu?",a:["100 phút","3 phút","30 phút","1 phút"],c:1},
{q:"Bạn có hai sợi dây, mỗi sợi cháy hết đúng 60 phút nhưng cháy không đều. Đốt dây thế nào để đo 45 phút?",a:["Không thể","Đốt dây 1 hai đầu, dây 2 một đầu; khi dây 1 hết thì đốt đầu kia dây 2","Đốt cả hai một đầu","Đốt một dây"],c:1},
{q:"Một người nhìn ảnh và nói: 'Tôi không có anh chị em, nhưng cha người trong ảnh là con trai của cha tôi.' Người trong ảnh là ai?",a:["Cha anh ấy","Con trai anh ấy","Anh họ","Chính anh ấy"],c:1},
{q:"Một số nhân với chính nó bằng 144. Tổng các chữ số của số dương đó là?",a:["6","9","12","18"],c:1},
{q:"Bạn có 9 đồng xu, một đồng giả nhẹ hơn. Ít nhất cần cân bao nhiêu lần để tìm đồng giả?",a:["1","2","3","4"],c:1}
]
};

let people = [];
let score = 0;
let questionsAsked = 0;
const totalQuestions = 10;

let gameStarted = false;
let questionActive = false;
let answered = false;
let currentQuestion = null;

let audioCtx = null;
let bgGain = null;
let bgTimer = null;
let muted = false;

const colors = [
    "#f26c4f", "#31c48d", "#f5b82e",
    "#a78bfa", "#ec72b7", "#55b8f2",
    "#ff875a"
];

function makeCity() {
    const sky = document.getElementById("sky");

    sky.querySelectorAll(".star, .building").forEach(
        e => e.remove()
    );

    for (let i = 0; i < 75; i++) {
        const star = document.createElement("div");
        star.className = "star";
        star.style.left = Math.random() * 100 + "%";
        star.style.top = Math.random() * 95 + "%";
        star.style.opacity = 0.35 + Math.random() * 0.65;
        sky.appendChild(star);
    }

    for (let i = 0; i < 9; i++) {
        const building = document.createElement("div");
        building.className = "building";
        building.style.left = (i * 11.5 - 1) + "%";
        building.style.width = (8 + Math.random() * 4) + "%";
        building.style.height = (110 + Math.random() * 135) + "px";

        for (let row = 0; row < 5; row++) {
            for (let col = 0; col < 3; col++) {
                const win = document.createElement("div");
                win.className = "window";
                win.style.left = (8 + col * 29) + "%";
                win.style.top = (8 + row * 18) + "px";

                if (Math.random() > 0.25) {
                    win.style.background = "#ffdf69";
                } else {
                    win.style.background = "#414b60";
                }

                building.appendChild(win);
            }
        }

        sky.appendChild(building);
    }
}

function makePeople(count) {
    const root = document.getElementById("people");
    root.innerHTML = "";
    people = [];

    for (let i = 0; i < count; i++) {
        const person = document.createElement("div");
        person.className = "person";
        person.dataset.caught = "0";

        person.style.left = (5 + Math.random() * 90) + "%";
        person.style.top = (63 + Math.random() * 18) + "%";
        person.style.setProperty(
            "--shirt",
            colors[i % colors.length]
        );

        person.innerHTML = `
            <div class="hair"></div>
            <div class="head"></div>
            <div class="body"></div>
            <div class="legs">
                <span></span><span></span>
            </div>
            <div class="label">Người ${i + 1}</div>
        `;

        root.appendChild(person);
        people.push(person);
    }

    updateHUD();
}

function updateHUD() {
    document.getElementById("score").textContent = score;

    document.getElementById("qcount").textContent =
        questionsAsked + "/" + totalQuestions;

    document.getElementById("remaining").textContent =
        people.filter(p => p.dataset.caught === "0").length;
}

/* ÂM THANH */

function initAudio() {
    if (!audioCtx) {
        audioCtx = new (
            window.AudioContext ||
            window.webkitAudioContext
        )();
    }

    if (audioCtx.state === "suspended") {
        audioCtx.resume();
    }

    if (!bgGain) {
        bgGain = audioCtx.createGain();

        // Nhạc nền nhỏ hơn hiệu ứng đúng/sai.
        bgGain.gain.value = muted ? 0 : 0.045;
        bgGain.connect(audioCtx.destination);

        const notes = [
            220, 261.63, 329.63, 293.66,
            246.94, 293.66, 349.23, 329.63
        ];

        let noteIndex = 0;

        bgTimer = setInterval(() => {
            if (!audioCtx || muted) return;

            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();

            osc.type = "sine";
            osc.frequency.value =
                notes[noteIndex++ % notes.length];

            gain.gain.setValueAtTime(
                0.0001, audioCtx.currentTime
            );

            gain.gain.exponentialRampToValueAtTime(
                0.10, audioCtx.currentTime + 0.06
            );

            gain.gain.exponentialRampToValueAtTime(
                0.0001, audioCtx.currentTime + 0.45
            );

            osc.connect(gain);
            gain.connect(bgGain);

            osc.start();
            osc.stop(audioCtx.currentTime + 0.48);

        }, 520);
    }
}

function tone(freq, duration, volume, type = "sine", delay = 0) {
    if (muted) return;

    initAudio();

    const now = audioCtx.currentTime + delay;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    osc.type = type;
    osc.frequency.setValueAtTime(freq, now);

    gain.gain.setValueAtTime(0.0001, now);

    gain.gain.exponentialRampToValueAtTime(
        Math.max(0.001, volume),
        now + 0.015
    );

    gain.gain.exponentialRampToValueAtTime(
        0.0001,
        now + duration
    );

    osc.connect(gain);
    gain.connect(audioCtx.destination);

    osc.start(now);
    osc.stop(now + duration + 0.03);
}

function playCorrect() {
    // Âm thanh đúng to và sáng rõ.
    tone(880, 0.22, 0.90, "triangle");
    tone(1175, 0.30, 0.85, "triangle", 0.16);
    tone(1480, 0.38, 0.80, "sine", 0.34);
}

function playWrong() {
    // Âm thanh sai to, trầm và dễ nhận biết.
    tone(260, 0.30, 0.90, "sawtooth");
    tone(190, 0.42, 0.85, "square", 0.22);
}

function playUfo() {
    tone(620, 0.22, 0.40, "sine");
    tone(820, 0.30, 0.32, "sine", 0.16);
}

function toggleMute() {
    muted = !muted;

    document.getElementById("mute-btn").textContent =
        muted ? "🔇 Âm thanh: Tắt" : "🔊 Âm thanh: Bật";

    if (bgGain && audioCtx) {
        bgGain.gain.setTargetAtTime(
            muted ? 0 : 0.045,
            audioCtx.currentTime,
            0.05
        );
    }
}

/* BẮT ĐẦU GAME */

function startGame() {
    initAudio();

    score = 0;
    questionsAsked = 0;
    gameStarted = true;
    questionActive = false;
    answered = false;

    const count = parseInt(
        document.getElementById("people-count").value,
        10
    );

    makePeople(count);
    updateHUD();

    document.getElementById("start-screen").style.display = "none";
    document.getElementById("question-card").style.display = "none";
    document.getElementById("start-btn").style.display = "none";
    document.getElementById("restart-btn").style.display = "inline-block";

    document.getElementById("ufo-catch-btn").disabled = false;

    document.getElementById("status").textContent =
        "Bấm nút UFO BẮT NGƯỜI để chọn ngẫu nhiên một người!";
}

function restartGame() {
    startGame();
}

/* UFO BẮT NGƯỜI */

function catchRandomPerson() {
    if (!gameStarted) {
        document.getElementById("status").textContent =
            "Hãy bấm BẮT ĐẦU GAME trước nhé!";
        return;
    }

    if (questionActive) {
        document.getElementById("status").textContent =
            "Hãy trả lời câu hỏi hiện tại trước nhé!";
        return;
    }

    if (questionsAsked >= totalQuestions) {
        document.getElementById("status").textContent =
            "Bạn đã hoàn thành 10 câu! Bấm Chơi lại để tiếp tục.";
        return;
    }

    const available = people.filter(
        p => p.dataset.caught === "0"
    );

    if (available.length === 0) {
        document.getElementById("status").textContent =
            "Không còn người nào để bắt. Hãy bấm Chơi lại!";
        return;
    }

    const target = available[
        Math.floor(Math.random() * available.length)
    ];

    target.dataset.caught = "1";
    target.classList.add("captured");

    document.getElementById("beam").style.display = "block";

    playUfo();

    setTimeout(() => {
        document.getElementById("beam").style.display = "none";
    }, 650);

    questionsAsked++;
    updateHUD();
    showQuestion();
}

/* CÂU HỎI */

function showQuestion() {
    questionActive = true;
    answered = false;

    const level = document.getElementById("difficulty").value;
    const questions = questionBank[level];

    currentQuestion = questions[
        Math.floor(Math.random() * questions.length)
    ];

    const levelName = {
        easy: "Mức 1 - Dễ vui",
        medium: "Mức 2 - Hack não",
        hard: "Mức 3 - Siêu khó"
    }[level];

    document.getElementById("question-meta").textContent =
        "🛸 UFO đã bắt người! | " +
        levelName +
        " | Câu " +
        questionsAsked +
        "/" +
        totalQuestions;

    document.getElementById("question").textContent =
        currentQuestion.q;

    const answers = document.getElementById("answers");
    answers.innerHTML = "";

    currentQuestion.a.forEach((answer, index) => {
        const button = document.createElement("button");

        button.className = "answer";
        button.textContent = answer;

        button.onclick = () => {
            answerQuestion(index, button);
        };

        answers.appendChild(button);
    });

    document.getElementById("feedback").textContent = "";
    document.getElementById("next-btn").style.display = "none";
    document.getElementById("question-card").style.display = "block";

    document.getElementById("status").textContent =
        "Hãy chọn một đáp án trong bảng câu hỏi!";
}

function answerQuestion(index, button) {
    if (answered) return;

    answered = true;

    const buttons = [
        ...document.querySelectorAll(".answer")
    ];

    buttons.forEach(b => {
        b.disabled = true;
    });

    const feedback = document.getElementById("feedback");

    if (index === currentQuestion.c) {
        score += 10;

        button.style.background = "#16794b";

        feedback.textContent = "✅ Chính xác! +10 điểm";
        feedback.style.color = "#64ffab";

        playCorrect();

    } else {
        button.style.background = "#a52e43";

        buttons[currentQuestion.c].style.background = "#16794b";

        feedback.textContent =
            "❌ Chưa đúng! Đáp án: " +
            currentQuestion.a[currentQuestion.c];

        feedback.style.color = "#ff929f";

        playWrong();
    }

    updateHUD();

    const nextButton = document.getElementById("next-btn");

    nextButton.style.display = "inline-block";

    nextButton.textContent =
        questionsAsked >= totalQuestions
        ? "Xem kết quả"
        : "Câu tiếp theo ➜";
}

function nextQuestion() {
    document.getElementById("question-card").style.display = "none";

    questionActive = false;

    if (questionsAsked >= totalQuestions) {
        gameStarted = false;

        document.getElementById("status").textContent =
            "🎉 Hoàn thành! Điểm của bạn: " +
            score +
            " / " +
            (totalQuestions * 10) +
            ". Bấm Chơi lại để chơi lần nữa.";

        document.getElementById("ufo-catch-btn").disabled = true;

    } else {
        document.getElementById("status").textContent =
            "Bấm 🛸 UFO BẮT NGƯỜI để chọn người tiếp theo!";
    }
}

makeCity();
makePeople(12);
</script>

</body>
</html>
"""

components.html(
    GAME_HTML,
    height=650,
    scrolling=False
)
