const levels = ['Junior High', 'Senior High', 'College', 'Graduate'];
const questions = [
  { text: 'Target: middle-school coding club. Prereqs: none. Focus: basic loops and variables.', ans: 0, hint: 'Look at age and prerequisites.' },
  { text: 'Target: AP Computer Science students. Prereqs: algebra and prior coding class.', ans: 1, hint: 'AP courses are secondary education.' },
  { text: 'Target: IT professionals and sysadmins. Prereqs: SQL and data modeling.', ans: 2, hint: 'Professional upskilling is post-secondary.' },
  { text: 'Target: PhD students in AI policy. Prereqs: research methods and statistics.', ans: 3, hint: 'Research-focused, specialized audience.' }
];

let idx = 0, selected = -1, feedback = '', score = 0, total = 0, streak = 0, hint = '';

function nextQ() { idx = (idx + 1) % questions.length; selected = -1; feedback = ''; hint = ''; }

function setup() {
  const c = createCanvas(920, 700);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  const submit = createButton('Submit Answer'); submit.position(640, 330); submit.mousePressed(() => {
    if (selected < 0) return;
    total++;
    const ok = selected === questions[idx].ans;
    if (ok) { score++; streak++; feedback = 'Correct. Indicators match this reading level.'; }
    else { streak = 0; feedback = `Not quite. Correct level: ${levels[questions[idx].ans]}.`; }
  });

  const showHint = createButton('Show Hint'); showHint.position(760, 330); showHint.mousePressed(() => hint = questions[idx].hint);
  const next = createButton('Next Example'); next.position(640, 365); next.mousePressed(nextQ);
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('Interactive Exercise Generator', 16, 30);
  fill('#334155'); textSize(13); text('Practice determining reading level from course descriptions.', 16, 52);

  fill('#ffffff'); stroke('#cbd5e1'); rect(16, 80, 600, 590, 10);
  noStroke(); fill('#0f172a'); textSize(16); text('Course Description', 30, 108);
  fill('#1f2937'); textSize(14); text(questions[idx].text, 30, 136, 570, 160);

  fill('#ffffff'); stroke('#cbd5e1'); rect(632, 80, 272, 590, 10);
  noStroke(); fill('#0f172a'); textSize(16); text('Choose Reading Level', 646, 108);

  levels.forEach((l, i) => {
    const y = 140 + i * 44;
    fill(selected === i ? '#bfdbfe' : '#e2e8f0'); rect(646, y, 238, 34, 8);
    fill('#0f172a'); textSize(14); text(l, 660, y + 22);
  });

  fill('#0f172a'); textSize(13); text(`Score: ${score}/${total}`, 646, 430);
  text(`Streak: ${streak}`, 646, 452);
  fill(feedback.startsWith('Correct') ? '#166534' : '#991b1b'); text(feedback || 'Submit an answer to get feedback.', 646, 480, 238, 80);
  fill('#1d4ed8'); text(hint ? `Hint: ${hint}` : '', 646, 560, 238, 80);
}

function mousePressed() {
  for (let i = 0; i < levels.length; i++) {
    const y = 140 + i * 44;
    if (mouseX > 646 && mouseX < 884 && mouseY > y && mouseY < y + 34) selected = i;
  }
}
