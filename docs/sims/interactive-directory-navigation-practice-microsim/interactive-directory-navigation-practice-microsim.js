const tree = {
  '/': ['docs', 'skills', 'src'],
  '/docs': ['chapters', 'sims', 'learning-graph'],
  '/docs/chapters': ['01-intro', '02-setup', '13-dev-tools'],
  '/docs/sims': ['mkdocs-build-process', 'dependency-mapping-workflow']
};

let cwd = '/';
let target = '/docs/sims';
let inputBox, feedback = 'Enter a command (cd, ls, pwd).';

function runCommand(cmd) {
  const parts = cmd.trim().split(/\s+/);
  if (!parts[0]) return;
  if (parts[0] === 'pwd') {
    feedback = cwd;
  } else if (parts[0] === 'ls') {
    feedback = (tree[cwd] || []).join('  ');
  } else if (parts[0] === 'cd') {
    const arg = parts[1] || '/';
    let next = arg.startsWith('/') ? arg : (cwd === '/' ? `/${arg}` : `${cwd}/${arg}`);
    if (arg === '..') {
      const seg = cwd.split('/').filter(Boolean);
      seg.pop();
      next = '/' + seg.join('/');
      if (next === '') next = '/';
    }
    if (tree[next]) {
      cwd = next;
      feedback = `Changed directory to ${cwd}`;
    } else {
      feedback = `No such directory: ${next}`;
    }
  } else {
    feedback = `Unknown command: ${parts[0]}`;
  }
}

function setup() {
  const c = createCanvas(980, 640);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  inputBox = createInput('pwd');
  inputBox.position(30, 530); inputBox.size(560, 30);
  createButton('Run').position(600, 530).mousePressed(() => runCommand(inputBox.value()));
  createButton('Reset').position(650, 530).mousePressed(() => { cwd = '/'; feedback = 'Reset to root directory.'; });
}

function drawTree(x, y, path, depth = 0) {
  fill('#0f172a'); textSize(13); text('  '.repeat(depth) + path.split('/').pop() || '/', x, y);
  const kids = tree[path] || [];
  let yy = y + 20;
  kids.forEach((k) => {
    const child = path === '/' ? `/${k}` : `${path}/${k}`;
    fill(child === cwd ? '#1d4ed8' : '#334155');
    text('  '.repeat(depth + 1) + k, x, yy);
    yy += 20;
  });
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('Interactive Directory Navigation Practice', 16, 30);

  fill('#ffffff'); stroke('#cbd5e1'); rect(16, 48, 620, 460, 10);
  noStroke(); fill('#0f172a'); textSize(14); text('File Tree', 30, 74);
  drawTree(30, 100, '/');
  drawTree(30, 200, '/docs');
  drawTree(30, 300, '/docs/chapters');
  drawTree(30, 380, '/docs/sims');

  fill('#ffffff'); stroke('#cbd5e1'); rect(650, 48, 314, 560, 10);
  noStroke(); fill('#0f172a'); textSize(16); text('Terminal', 664, 78);
  textSize(13); text(`Target: ${target}`, 664, 108);
  text(`Current Directory: ${cwd}`, 664, 132);
  fill(cwd === target ? '#166534' : '#334155');
  text(cwd === target ? 'Success: reached target directory.' : 'Goal: navigate to /docs/sims', 664, 158, 290, 40);

  fill('#111827'); rect(664, 188, 286, 300, 8);
  fill('#a7f3d0'); textSize(12); text(`user@book ${cwd} % ${inputBox.value()}`, 674, 212, 270, 40);
  fill('#e5e7eb'); text(feedback, 674, 252, 270, 220);
}
