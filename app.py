import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(page_title="UFO HACK NÃO", page_icon="🛸", layout="wide")

# correct là vị trí đáp án đúng, bắt đầu từ 0
QUESTIONS = {
    "Mức 1 - Đố vui, đố mẹo": [
        {"q":"Một năm có bao nhiêu tháng có 28 ngày?","a":["1 tháng","2 tháng","6 tháng","12 tháng"],"correct":3,"explain":"Cả 12 tháng đều có ít nhất 28 ngày."},
        {"q":"Cái gì càng đào đi thì càng lớn?","a":["Cái túi","Cái hố","Ngọn núi","Cái cây"],"correct":1,"explain":"Càng đào đất đi thì cái hố càng lớn."},
        {"q":"Bạn vượt qua người đứng thứ hai trong cuộc đua. Bạn đứng thứ mấy?","a":["Thứ nhất","Thứ hai","Thứ ba","Thứ tư"],"correct":1,"explain":"Bạn chiếm vị trí thứ hai."},
        {"q":"Cái gì có răng nhưng không biết nhai?","a":["Con cá","Cái lược","Con chó","Cái bát"],"correct":1,"explain":"Đó là cái lược."},
        {"q":"Có 5 quả táo, bạn lấy đi 2 quả. Bạn có mấy quả?","a":["3 quả","2 quả","5 quả","7 quả"],"correct":1,"explain":"Bạn lấy 2 quả nên bạn có 2 quả."},
        {"q":"Cái gì có cổ nhưng không có đầu?","a":["Con người","Cái chai","Con ngựa","Cái bàn"],"correct":1,"explain":"Đó là cái chai."},
        {"q":"Bạn có thể cầm gì bằng tay trái nhưng không thể cầm bằng tay phải?","a":["Cái cốc","Khuỷu tay phải","Quyển sách","Cái bút"],"correct":1,"explain":"Bạn không thể dùng tay phải cầm chính khuỷu tay phải."},
        {"q":"Cái gì luôn đến nhưng không bao giờ trở thành hôm qua?","a":["Ngày mai","Hôm nay","Hôm qua","Buổi sáng"],"correct":0,"explain":"Ngày mai đến thì lại trở thành hôm nay."},
        {"q":"Một căn phòng có 4 góc, mỗi góc có một con mèo. Có bao nhiêu con mèo?","a":["2","4","8","16"],"correct":1,"explain":"Có tổng cộng 4 con mèo."},
        {"q":"Cái gì có mặt và hai kim nhưng không có tay?","a":["Robot","Đồng hồ","Con người","Cái quạt"],"correct":1,"explain":"Đó là đồng hồ."}
    ],
    "Mức 2 - Ca dao, tục ngữ": [
        {"q":"Có công mài sắt, có ngày nên ...","a":["Kim","Dao","Kéo","Búa"],"correct":0,"explain":"Có công mài sắt, có ngày nên kim."},
        {"q":"Uống nước nhớ ...","a":["Cây","Nguồn","Sông","Suối"],"correct":1,"explain":"Uống nước nhớ nguồn."},
        {"q":"Lá lành đùm lá ...","a":["Đỏ","Xanh","Rách","Vàng"],"correct":2,"explain":"Lá lành đùm lá rách."},
        {"q":"Gần mực thì đen, gần đèn thì ...","a":["Sáng","Tối","Nóng","Lạnh"],"correct":0,"explain":"Gần mực thì đen, gần đèn thì sáng."},
        {"q":"Thất bại là mẹ thành ...","a":["Công","Danh","Đạt","Tài"],"correct":0,"explain":"Thất bại là mẹ thành công."},
        {"q":"Ăn quả nhớ kẻ trồng ...","a":["Hoa","Cây","Đất","Rừng"],"correct":1,"explain":"Ăn quả nhớ kẻ trồng cây."},
        {"q":"Một cây làm chẳng nên non, ba cây chụm lại nên hòn núi ...","a":["Đỏ","Cao","Thái Sơn","Lớn"],"correct":2,"explain":"Câu ca dao đề cao tinh thần đoàn kết."},
        {"q":"Câu nào khuyên chúng ta phải biết ơn?","a":["Có chí thì nên","Uống nước nhớ nguồn","Đi một ngày đàng","Tốt gỗ hơn tốt nước sơn"],"correct":1,"explain":"Uống nước nhớ nguồn khuyên ta nhớ ơn cội nguồn."},
        {"q":"Không thầy đố mày làm ...","a":["Giàu","Nên","Quan","Khôn"],"correct":1,"explain":"Không thầy đố mày làm nên."},
        {"q":"Một mặt người bằng mười mặt ...","a":["Đất","Vàng","Bạc","Ngọc"],"correct":1,"explain":"Câu tục ngữ đề cao giá trị con người."}
    ],
    "Mức 3 - Toán lớp 9": [
        {"q":"Giải phương trình x² - 5x + 6 = 0.","a":["x = 1 hoặc x = 6","x = 2 hoặc x = 3","x = -2 hoặc x = -3","x = 0 hoặc x = 5"],"correct":1,"explain":"(x - 2)(x - 3) = 0 nên x = 2 hoặc x = 3."},
        {"q":"Tính √81.","a":["7","8","9","10"],"correct":2,"explain":"√81 = 9."},
        {"q":"Giải phương trình 2x + 6 = 0.","a":["x = 3","x = -3","x = 6","x = -6"],"correct":1,"explain":"2x = -6 nên x = -3."},
        {"q":"Nếu y = 2x + 1, khi x = 3 thì y bằng bao nhiêu?","a":["5","6","7","8"],"correct":2,"explain":"y = 2 × 3 + 1 = 7."},
        {"q":"Phương trình x² = 16 có nghiệm nào?","a":["Chỉ x = 4","Chỉ x = -4","x = ±4","x = 16"],"correct":2,"explain":"Hai nghiệm là x = 4 và x = -4."},
        {"q":"Tính √25 + √9.","a":["8","34","16","2"],"correct":0,"explain":"5 + 3 = 8."},
        {"q":"Đường thẳng y = 3x - 2 có hệ số góc bằng bao nhiêu?","a":["-2","2","3","-3"],"correct":2,"explain":"Hệ số góc là 3."},
        {"q":"Tam giác vuông có hai cạnh góc vuông 3 và 4. Cạnh huyền bằng bao nhiêu?","a":["5","6","7","8"],"correct":0,"explain":"Theo định lý Pythagore, cạnh huyền bằng 5."},
        {"q":"Giải phương trình x² - 9 = 0.","a":["x = 3","x = -3","x = ±3","x = 9"],"correct":2,"explain":"Hai nghiệm là x = 3 và x = -3."},
        {"q":"Nếu sin A = 1/2 và A là góc nhọn thì A bằng bao nhiêu?","a":["30°","45°","60°","90°"],"correct":0,"explain":"sin 30° = 1/2."},
        {"q":"Giải hệ x + y = 7 và x - y = 1.","a":["x = 3, y = 4","x = 4, y = 3","x = 5, y = 2","x = 6, y = 1"],"correct":1,"explain":"Cộng hai phương trình được 2x = 8, nên x = 4, y = 3."},
        {"q":"Biệt thức Δ của x² - 4x + 4 = 0 bằng bao nhiêu?","a":["0","4","8","16"],"correct":0,"explain":"Δ = 16 - 16 = 0."},
        {"q":"Tính √(49/64).","a":["7/8","8/7","7/64","49/8"],"correct":0,"explain":"√(49/64) = 7/8."},
        {"q":"Đồ thị hàm số y = ax² (a khác 0) có hình dạng gì?","a":["Đường thẳng","Đường tròn","Parabol","Hình chữ nhật"],"correct":2,"explain":"Đồ thị hàm số y = ax² là một parabol."},
        {"q":"Đường tròn bán kính 3 cm có đường kính bao nhiêu?","a":["3 cm","6 cm","9 cm","12 cm"],"correct":1,"explain":"Đường kính bằng hai lần bán kính: 6 cm."}
    ]
}
QUESTIONS_JSON = json.dumps(QUESTIONS, ensure_ascii=False)

GAME_HTML = r"""
<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<style>
*{box-sizing:border-box}html,body{margin:0;width:100%;overflow-x:hidden}
body{background:#080d1b;color:#ffe66d;font-family:Arial,sans-serif}
.game{width:100%;max-width:1400px;margin:auto;padding:10px}
.header{text-align:center;padding:12px;border:2px solid #ffcf33;border-radius:15px;background:linear-gradient(120deg,#101735,#24104b);box-shadow:0 0 18px #ffcf3340}
.header h1{margin:5px;font-size:clamp(27px,5vw,43px);text-shadow:0 0 15px #ffae00}
.header p{color:#d5ddff}
.stats{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
.stat{flex:1;min-width:100px;text-align:center;padding:10px;border:1px solid #5c70b9;border-radius:12px;background:#111a36}
.stat b{display:block;font-size:22px;margin-bottom:4px}
.controls{display:flex;flex-wrap:wrap;gap:10px;align-items:end;padding:12px;margin-bottom:12px;background:#101832;border:1px solid #334779;border-radius:12px}
.control{flex:1;min-width:140px;display:flex;flex-direction:column;gap:6px}
label{color:#d2dcff;font-size:13px}
input,select{width:100%;padding:10px;border:1px solid #6478bd;border-radius:8px;background:#080e20;color:white;font-size:16px;min-height:44px}
input[type=range]{accent-color:#ffd43b}
button{padding:10px 13px;min-height:44px;border:1px solid #ffdf5d;border-radius:9px;color:#fff4ba;background:#38234e;cursor:pointer;font-weight:bold;font-size:15px;touch-action:manipulation}
button:hover{filter:brightness(1.2)}button:disabled{opacity:.5;cursor:not-allowed}
.primary{color:#160d20;background:linear-gradient(120deg,#f7b928,#ff7a18);border:none}
#scene{position:relative;width:100%;height:clamp(460px,65vh,650px);min-height:450px;overflow:hidden;border:2px solid #5e78c6;border-radius:15px;background:#10162e;isolation:isolate}
.sky{position:absolute;inset:0 0 42%;background:radial-gradient(circle at 20% 20%,white 0 1px,transparent 2px),radial-gradient(circle at 65% 17%,white 0 1px,transparent 2px),radial-gradient(circle at 83% 30%,#a9d4ff 0 1px,transparent 2px),linear-gradient(#080e29,#26365d);background-size:100px 80px,130px 110px,160px 120px,auto}
.moon{position:absolute;top:25px;right:11%;width:45px;height:45px;border-radius:50%;background:#fff2b0;box-shadow:0 0 30px #ffe9a0}
.buildings{position:absolute;inset:90px 0 38%;display:flex;align-items:end;gap:5px;padding:0 5px}
.building{flex:1;min-width:25px;height:var(--height);background:linear-gradient(90deg,#17213d,#263656);border:1px solid #40547a}
.windows{display:grid;grid-template-columns:repeat(3,1fr);gap:7px;padding:8px 5px}
.window{height:12px;background:#ffda69}
.road{position:absolute;bottom:0;left:0;right:0;height:43%;background:linear-gradient(#424957,#222936);border-top:9px solid #858b9a}
.sidewalk{position:absolute;top:56%;left:0;right:0;height:6%;background:repeating-linear-gradient(90deg,#858b9a 0 60px,#636b7c 60px 63px)}
.road-line{position:absolute;top:80%;left:0;right:0;height:4px;background:repeating-linear-gradient(90deg,#ffe59b 0 45px,transparent 45px 85px)}
.lamp{position:absolute;top:20%;width:5px;height:40%;background:#66738c}.lamp:before{content:"";position:absolute;width:35px;height:5px;background:#66738c}.lamp:after{content:"";position:absolute;top:0;left:25px;width:13px;height:10px;background:#ffe6a0;border-radius:50%;box-shadow:0 0 20px #ffe6a0}
#ufo{position:absolute;top:8%;left:12%;width:100px;text-align:center;font-size:53px;z-index:20;filter:drop-shadow(0 0 10px #6deaff);transition:left .8s ease,top .8s ease;pointer-events:none}
.beam{display:none;position:absolute;top:60px;left:50%;transform:translateX(-50%);width:100px;height:250px;background:linear-gradient(#6df9ff99,#6df9ff20,transparent);clip-path:polygon(40% 0,60% 0,100% 100%,0 100%);animation:pulse .5s infinite alternate;pointer-events:none}
@keyframes pulse{from{opacity:.5}to{opacity:1}}
#peopleLayer{position:absolute;inset:0;z-index:10;pointer-events:none}
.person{position:absolute;width:34px;height:100px;transform-origin:center bottom}
.head{position:absolute;left:10px;top:0;width:17px;height:19px;border-radius:50%;background:var(--skin);border:1px solid #47312a}
.hair{position:absolute;z-index:2;left:9px;top:-2px;width:19px;height:8px;border-radius:9px;background:var(--hair)}
.body{position:absolute;left:7px;top:19px;width:23px;height:38px;border-radius:7px;background:var(--shirt)}
.arm{position:absolute;top:23px;width:7px;height:31px;border-radius:6px;background:var(--skin);transform-origin:top}
.arm.left{left:4px;animation:armL .45s infinite alternate}.arm.right{right:3px;animation:armR .45s infinite alternate}
.leg{position:absolute;top:53px;width:9px;height:37px;border-radius:5px;background:var(--pants);transform-origin:top}
.leg.left{left:9px;animation:legL .4s infinite alternate}.leg.right{left:20px;animation:legR .4s infinite alternate}
.shoe{position:absolute;bottom:5px;width:13px;height:6px;border-radius:5px;background:#111}.shoe.left{left:5px}.shoe.right{left:17px}
@keyframes legL{from{transform:rotate(-22deg)}to{transform:rotate(22deg)}}@keyframes legR{from{transform:rotate(22deg)}to{transform:rotate(-22deg)}}
@keyframes armL{from{transform:rotate(20deg)}to{transform:rotate(-20deg)}}@keyframes armR{from{transform:rotate(-20deg)}to{transform:rotate(20deg)}}
.person.captured{animation:abduct 1.5s forwards}
@keyframes abduct{0%{opacity:1}50%{filter:brightness(2)}100%{opacity:0;translate:0 -220px;scale:.2}}
.nameTag{position:absolute;top:90px;left:50%;transform:translateX(-50%) scaleX(var(--name-direction,1));color:white;font-size:10px;white-space:nowrap;text-shadow:1px 1px 3px black;pointer-events:none}
#message{position:absolute;top:68px;left:50%;transform:translateX(-50%);z-index:30;width:max-content;max-width:90%;padding:9px 15px;border-radius:20px;background:#080d1ddd;border:1px solid #ffe66d;text-align:center;font-size:13px;font-weight:bold}
#ufoButton{position:absolute;top:12px;left:12px;z-index:50;max-width:calc(100% - 24px);padding:10px 12px;color:#160d20;background:linear-gradient(120deg,#ffe66d,#ff9f1c);border:2px solid #fff0a8;box-shadow:0 0 16px #ffe66d99;font-size:14px;font-weight:900}
#ufoButton:disabled{opacity:.8;color:#554b2a;filter:saturate(.65)}
#quiz{display:none;position:absolute;z-index:1000;left:50%;top:50%;transform:translate(-50%,-50%);width:min(520px,calc(100% - 20px));max-height:calc(100% - 20px);overflow-y:auto;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;padding:20px;background:#10142af7;border:2px solid #ffe66d;border-radius:17px;box-shadow:0 0 30px #55eaff77;color:white;text-align:center}
#quiz h2{margin:0 0 10px;color:#ffe66d}#question{font-size:17px;line-height:1.5;margin:14px 0;overflow-wrap:anywhere}
.answers{display:grid;grid-template-columns:1fr 1fr;gap:9px}.answers button{min-height:46px;background:#202d50;border-color:#657fc2;color:white;white-space:normal;overflow-wrap:anywhere}
#quizResult{margin-top:12px;line-height:1.5;color:#ffe66d;font-weight:bold}.footer{padding:12px;text-align:center;color:#aab9e5;font-size:12px}
@media(max-width:600px){#ufoButton{top:10px;left:10px;padding:9px 10px;font-size:12px}#message{top:65px;max-width:calc(100% - 20px)}.game{padding:6px}.header h1{font-size:27px}.controls{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:8px}.control{min-width:0;width:100%}.controls>button{width:100%;min-width:0;padding:10px 6px;font-size:14px}.stat{min-width:calc(50% - 8px)}#scene{height:500px;min-height:450px}#ufo{font-size:42px;width:75px}#quiz{padding:12px}#question{font-size:16px}.answers{grid-template-columns:1fr}}
@media(max-width:360px){.controls{grid-template-columns:1fr}#scene{height:460px}}
</style></head><body><div class="game">
<div class="header"><h1>🛸 UFO HACK NÃO 👽</h1><p>Thành phố ban đêm — bạn điều khiển UFO — thử thách trí tuệ!</p></div>
<div class="stats"><div class="stat"><b id="score">0</b>Điểm</div><div class="stat"><b id="saved">0</b>Giải cứu</div><div class="stat"><b id="remaining">12</b>Người còn lại</div><div class="stat"><b id="round">0</b>Lượt UFO bắt</div></div>
<div class="controls">
<div class="control"><label>🎯 Mức độ câu hỏi</label><select id="difficulty"><option value="Mức 1 - Đố vui, đố mẹo">🟢 Mức 1 - Đố vui</option><option value="Mức 2 - Ca dao, tục ngữ">🟡 Mức 2 - Ca dao tục ngữ</option><option value="Mức 3 - Toán lớp 9">🔴 Mức 3 - Toán lớp 9</option></select></div>
<div class="control"><label>👥 Số người (1–100)</label><input id="peopleCount" type="number" min="1" max="100" value="12"></div><button id="applyPeople">Áp dụng</button>
<div class="control"><label>Chọn người để đổi tên</label><select id="renameSelect"></select></div><div class="control"><label>Tên mới</label><input id="newName" maxlength="18" placeholder="Nhập tên..."></div><button id="renameButton">✏️ Đổi tên</button>
<button id="startButton" class="primary">🔊 BẮT ĐẦU GAME</button><button id="resetButton">🔄 Chơi lại</button>
<div class="control" style="max-width:180px"><label>🔊 Âm lượng</label><input id="volume" type="range" min="0" max="100" value="70"><span id="volumeLabel">70%</span></div></div>
<div id="scene"><div class="sky"></div><div class="moon"></div><div class="buildings" id="buildings"></div><div class="lamp" style="left:8%"></div><div class="lamp" style="left:76%"></div><div class="road"></div><div class="sidewalk"></div><div class="road-line"></div>
<div id="ufo">🛸<div class="beam" id="beam"></div></div><div id="message">🌃 Đêm xuống... Hãy bắt đầu trò chơi!</div><button id="ufoButton" disabled>🛸 UFO BẮT NGƯỜI</button><div id="peopleLayer"></div>
<div id="quiz"><h2>🧠 HACK NÃO!</h2><div id="targetText"></div><div id="question"></div><div class="answers" id="answers"></div><div id="quizResult"></div></div></div>
<div class="footer">Bạn chủ động bấm UFO BẮT NGƯỜI. UFO không tự bắt người.</div></div>
<script>
const QUESTION_BANK=__QUESTIONS__;
const $=id=>document.getElementById(id);
const peopleLayer=$("peopleLayer"),ufo=$("ufo"),beam=$("beam"),quiz=$("quiz"),message=$("message");
let people=[],score=0,saved=0,round=0,gameStarted=false,quizOpen=false,abductionInProgress=false;
let usedQuestions={}; // Riêng từng mức; không lặp cho đến khi chơi lại.
const shirts=["#e74c3c","#3498db","#2ecc71","#f1c40f","#9b59b6","#ff8c42","#ff69b4","#4ecdc4"];
const pantsColors=["#202d46","#353535","#293b59","#493b35"],skinColors=["#f4c7a1","#d99a6c","#b9754c","#f0d1b0"],hairColors=["#211914","#563a25","#292929","#a56a32"];
let audioContext=null,masterGain=null,musicTimer=null,noteIndex=0;
const melody=[523.25,659.25,783.99,659.25,587.33,698.46,880,698.46,493.88,587.33,739.99,587.33,440,554.37,659.25,554.37],bassNotes=[130.81,146.83,123.47,110];
function setVolume(){const v=Number($("volume").value);$("volumeLabel").textContent=v+"%";if(masterGain&&audioContext)masterGain.gain.setTargetAtTime(v/100*.8,audioContext.currentTime,.06)}
function initAudio(){const AC=window.AudioContext||window.webkitAudioContext;if(!AC){setMessage("Trình duyệt không hỗ trợ âm thanh.");return}if(!audioContext){audioContext=new AC();masterGain=audioContext.createGain();masterGain.gain.value=Number($("volume").value)/100*.8;masterGain.connect(audioContext.destination);startMusic()}if(audioContext.state==="suspended")audioContext.resume()}
function tone(f,d,type="sine",v=.2,delay=0){if(!audioContext||!masterGain)return;const t=audioContext.currentTime+delay,o=audioContext.createOscillator(),g=audioContext.createGain(),filter=audioContext.createBiquadFilter();o.type=type;o.frequency.setValueAtTime(f,t);filter.type="lowpass";filter.frequency.setValueAtTime(4200,t);g.gain.setValueAtTime(.0001,t);g.gain.exponentialRampToValueAtTime(Math.max(.0002,v),t+.025);g.gain.exponentialRampToValueAtTime(.0001,t+d);o.connect(filter);filter.connect(g);g.connect(masterGain);o.start(t);o.stop(t+d+.03)}
function playKick(delay=0){if(!audioContext||!masterGain)return;const t=audioContext.currentTime+delay,o=audioContext.createOscillator(),g=audioContext.createGain();o.type="sine";o.frequency.setValueAtTime(120,t);o.frequency.exponentialRampToValueAtTime(45,t+.14);g.gain.setValueAtTime(.07,t);g.gain.exponentialRampToValueAtTime(.001,t+.16);o.connect(g);g.connect(masterGain);o.start(t);o.stop(t+.17)}
function startMusic(){if(!audioContext)return;clearInterval(musicTimer);noteIndex=0;musicTimer=setInterval(()=>{if(!audioContext||audioContext.state!=="running")return;const s=noteIndex%melody.length,n=melody[s],b=bassNotes[Math.floor(s/4)%bassNotes.length];tone(n,.24,"triangle",.035);if(s%2===0)tone(n*1.5,.17,"sine",.012,.035);if(s%4===0){tone(b,.34,"triangle",.045);playKick()}if(s%4===2)tone(1100,.045,"square",.009);noteIndex++},220)}
function playUfoSound(){if(!audioContext)return;tone(440,.45,"sawtooth",.16);tone(660,.5,"triangle",.12,.12);tone(880,.5,"sine",.09,.25)}
function playCorrectSound(){if(!audioContext)return;tone(523.25,.18,"triangle",.62,0);tone(659.25,.18,"triangle",.62,.13);tone(783.99,.20,"triangle",.65,.26);tone(1046.5,.42,"sine",.72,.40);tone(1318.51,.28,"sine",.32,.48)}
function playWrongSound(){if(!audioContext)return;tone(329.63,.22,"triangle",.62,0);tone(277.18,.28,"triangle",.65,.17);tone(220,.38,"sine",.72,.36)}
function setMessage(t){message.textContent=t}
function createBuildings(){const c=$("buildings");c.innerHTML="";[65,90,75,100,68,86,72,94].forEach(h=>{const b=document.createElement("div");b.className="building";b.style.setProperty("--height",h+"%");const w=document.createElement("div");w.className="windows";for(let i=0;i<12;i++){const x=document.createElement("div");x.className="window";if(Math.random()<.25)x.style.opacity=".15";w.appendChild(x)}b.appendChild(w);c.appendChild(b)})}
function createPerson(i){const el=document.createElement("div");el.className="person";const p={id:i+1,name:"Người "+(i+1),el,x:2+Math.random()*90,y:58+Math.random()*20,speed:.012+Math.random()*.02,direction:Math.random()>.5?1:-1,alive:true,captured:false};el.style.setProperty("--shirt",shirts[Math.floor(Math.random()*shirts.length)]);el.style.setProperty("--pants",pantsColors[Math.floor(Math.random()*pantsColors.length)]);el.style.setProperty("--skin",skinColors[Math.floor(Math.random()*skinColors.length)]);el.style.setProperty("--hair",hairColors[Math.floor(Math.random()*hairColors.length)]);el.innerHTML='<div class="hair"></div><div class="head"></div><div class="body"></div><div class="arm left"></div><div class="arm right"></div><div class="leg left"></div><div class="leg right"></div><div class="shoe left"></div><div class="shoe right"></div><div class="nameTag"></div>';el.querySelector(".nameTag").textContent=p.name;peopleLayer.appendChild(el);people.push(p);positionPerson(p)}
function positionPerson(p){p.el.style.left=p.x+"%";p.el.style.top=p.y+"%";p.el.style.zIndex=String(Math.floor(p.y));const scale=.7+((p.y-58)/20)*.45;p.el.style.transform="scale("+scale+") scaleX("+p.direction+")";p.el.querySelector(".nameTag").style.setProperty("--name-direction",p.direction===-1?"-1":"1")}
function refreshRenameSelect(){const s=$("renameSelect"),prev=s.value;s.innerHTML="";people.filter(p=>p.alive).forEach(p=>{const o=document.createElement("option");o.value=p.id;o.textContent=p.name;s.appendChild(o)});if([...s.options].some(o=>o.value===prev))s.value=prev}
function updateStats(){$("score").textContent=score;$("saved").textContent=saved;$("remaining").textContent=people.filter(p=>p.alive).length;$("round").textContent=round}
function createCity(count){gameStarted=false;quizOpen=false;abductionInProgress=false;peopleLayer.innerHTML="";people=[];quiz.style.display="none";beam.style.display="none";score=0;saved=0;round=0;usedQuestions={};for(let i=0;i<count;i++)createPerson(i);refreshRenameSelect();updateStats();$("startButton").textContent="🔊 BẮT ĐẦU GAME";$("ufoButton").disabled=true;setMessage("🌃 Đêm xuống... Hãy bấm BẮT ĐẦU GAME!");ufo.style.left="12%";ufo.style.top="8%"}
function animatePeople(){people.forEach(p=>{if(!p.alive||p.captured||!gameStarted)return;p.x+=p.speed*p.direction;if(p.x>94){p.x=94;p.direction=-1}if(p.x<1){p.x=1;p.direction=1}positionPerson(p)});requestAnimationFrame(animatePeople)}
function beginAbduction(){if(!gameStarted||quizOpen||abductionInProgress)return;const living=people.filter(p=>p.alive&&!p.captured);if(!living.length){gameStarted=false;$("ufoButton").disabled=true;setMessage("👽 Hết người rồi! Hãy bấm CHƠI LẠI.");return}abductionInProgress=true;$("ufoButton").disabled=true;const target=living[Math.floor(Math.random()*living.length)];round++;ufo.style.left=Math.max(0,Math.min(85,target.x-3))+"%";ufo.style.top="7%";beam.style.display="block";setMessage("🛸 UFO đang bắt "+target.name+"!");playUfoSound();setTimeout(()=>{if(!target.alive){abductionInProgress=false;beam.style.display="none";return}target.captured=true;target.el.classList.add("captured");setTimeout(()=>{target.alive=false;target.captured=false;target.el.style.display="none";beam.style.display="none";updateStats();refreshRenameSelect();showQuestion(target)},1100)},800)}
function showQuestion(target){gameStarted=false;quizOpen=true;$("ufoButton").disabled=true;const level=$("difficulty").value,list=QUESTION_BANK[level];if(!usedQuestions[level])usedQuestions[level]=[];const available=list.filter(q=>!usedQuestions[level].includes(q.q));$("targetText").textContent="🛸 UFO đã bắt "+target.name+"! Mức độ: "+level;const answerBox=$("answers");answerBox.innerHTML="";$("quizResult").textContent="";
if(!available.length){$("targetText").textContent="🎉 Bạn đã hoàn thành tất cả câu hỏi của mức này!";$("question").textContent="Hãy chọn mức độ khác để tiếp tục thử thách.";const next=document.createElement("button");next.className="primary";next.textContent="▶ TIẾP TỤC";next.style.gridColumn="1 / -1";next.addEventListener("click",resumeGame);answerBox.appendChild(next);quiz.style.display="block";return}
const q=available[Math.floor(Math.random()*available.length)];usedQuestions[level].push(q.q);$("question").textContent=q.q;
q.a.forEach((answer,index)=>{const b=document.createElement("button");b.textContent=answer;b.addEventListener("click",()=>{[...answerBox.querySelectorAll("button")].forEach(x=>x.disabled=true);if(index===q.correct){score+=10;saved++;$("quizResult").textContent="🎉 Chính xác! +10 điểm. "+q.explain;playCorrectSound()}else{$("quizResult").textContent="❌ Chưa đúng. Đáp án đúng: "+q.a[q.correct]+". "+q.explain;playWrongSound()}updateStats();const next=document.createElement("button");next.className="primary";next.textContent="▶ TIẾP TỤC";next.style.gridColumn="1 / -1";next.addEventListener("click",resumeGame);answerBox.appendChild(next)});answerBox.appendChild(b)});quiz.style.display="block"}
function resumeGame(){quiz.style.display="none";quizOpen=false;abductionInProgress=false;if(people.every(p=>!p.alive)){gameStarted=false;$("startButton").textContent="🔊 BẮT ĐẦU GAME";$("ufoButton").disabled=true;setMessage("👽 Hết người rồi! Hãy bấm CHƠI LẠI.");return}gameStarted=true;$("startButton").textContent="⏸ TẠM DỪNG GAME";$("ufoButton").disabled=false;setMessage("🌃 Bấm 🛸 UFO BẮT NGƯỜI khi bạn muốn bắt tiếp!")}
$("applyPeople").addEventListener("click",resetGame);$("resetButton").addEventListener("click",resetGame);
$("renameButton").addEventListener("click",()=>{const id=Number($("renameSelect").value),name=$("newName").value.trim();if(!name){setMessage("✏️ Hãy nhập tên mới!");return}const p=people.find(x=>x.id===id&&x.alive);if(!p){setMessage("Người này không còn trên phố.");return}p.name=name.slice(0,18);p.el.querySelector(".nameTag").textContent=p.name;refreshRenameSelect();$("renameSelect").value=String(p.id);$("newName").value="";setMessage("✨ Đã đổi tên thành "+p.name+"!")});
$("startButton").addEventListener("click",()=>{initAudio();if(quizOpen||abductionInProgress){setMessage("🧠 Hãy hoàn thành câu hỏi hiện tại trước!");return}if(gameStarted){gameStarted=false;$("startButton").textContent="▶ TIẾP TỤC GAME";$("ufoButton").disabled=true;setMessage("⏸ Game đang tạm dừng.")}else{if(people.every(p=>!p.alive))resetGame();gameStarted=true;$("startButton").textContent="⏸ TẠM DỪNG GAME";$("ufoButton").disabled=false;setMessage("🛸 Game bắt đầu! Hãy tự bấm UFO BẮT NGƯỜI.")}});
$("ufoButton").addEventListener("click",()=>{if(!gameStarted){setMessage("▶ Hãy bấm BẮT ĐẦU GAME trước!");return}if(quizOpen){setMessage("🧠 Hãy trả lời câu hỏi trước!");return}if(abductionInProgress){setMessage("🛸 UFO đang bắt người!");return}beginAbduction()});
$("volume").addEventListener("input",setVolume);
function resetGame(){let count=parseInt($("peopleCount").value,10);if(!Number.isFinite(count))count=12;count=Math.max(1,Math.min(100,count));$("peopleCount").value=count;createCity(count)}
createBuildings();createCity(12);animatePeople();setVolume();
</script></body></html>
"""
GAME_HTML = GAME_HTML.replace("__QUESTIONS__", QUESTIONS_JSON)

st.markdown("""
<style>
.stApp {background-color:#080d1b;}
[data-testid="stHeader"] {background:transparent;}
h1 {color:#ffe66d !important;text-align:center;}
.block-container {padding-top:1rem;padding-bottom:1rem;}
iframe {width:100% !important;}
</style>
""", unsafe_allow_html=True)

st.title("🛸 UFO HACK NÃO")
st.caption("Chọn mức độ câu hỏi, sau đó tự bấm nút UFO BẮT NGƯỜI để chọn ngẫu nhiên một nhân vật.")
components.html(GAME_HTML, height=1450, scrolling=True)
