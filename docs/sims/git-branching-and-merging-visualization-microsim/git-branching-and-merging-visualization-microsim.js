let branches = {};
let activeBranch = 'main';
let commitCount = 0;
let branchOrder = ['main'];
let mergeTargetSelect;

function resetScenario() {
  branches = {
    main: {
      y: 210,
      active: true,
      commits: [
        { id: ++commitCount, msg: 'init repo' },
        { id: ++commitCount, msg: 'add docs structure' },
        { id: ++commitCount, msg: 'chapter baseline' }
      ]
    }
  };
  activeBranch = 'main';
  branchOrder = ['main'];
  syncBranchSelect();
}

function syncBranchSelect() {
  if (!mergeTargetSelect) return;
  mergeTargetSelect.elt.innerHTML = '';
  branchOrder.forEach((b) => {
    if (b !== activeBranch && branches[b].active) {
      mergeTargetSelect.option(b);
    }
  });
}

function addCommit(msg) {
  branches[activeBranch].commits.push({ id: ++commitCount, msg });
}

function createBranch() {
  const name = prompt('Branch name:', `feature-${branchOrder.length}`);
  if (!name || branches[name]) return;
  const base = branches[activeBranch];
  const offset = branchOrder.length % 2 === 0 ? 90 : -90;
  branches[name] = {
    y: base.y + offset,
    active: true,
    commits: base.commits.slice(0),
    parent: activeBranch
  };
  branchOrder.push(name);
  activeBranch = name;
  syncBranchSelect();
}

function mergeBranch() {
  const target = mergeTargetSelect.value();
  if (!target || !branches[target] || !branches[target].active) return;
  addCommit(`merge ${target} into ${activeBranch}`);
  branches[target].active = false;
  syncBranchSelect();
}

function setup() {
  const c = createCanvas(940, 620);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  const b1 = createButton('Create Branch');
  b1.position(16, 520);
  b1.mousePressed(createBranch);

  const b2 = createButton('Make Commit');
  b2.position(122, 520);
  b2.mousePressed(() => {
    const msg = prompt('Commit message:', `commit ${commitCount + 1}`) || `commit ${commitCount + 1}`;
    addCommit(msg);
  });

  const b3 = createButton('Switch Branch');
  b3.position(220, 520);
  b3.mousePressed(() => {
    const next = prompt('Switch to branch:', activeBranch);
    if (next && branches[next] && branches[next].active) {
      activeBranch = next;
      syncBranchSelect();
    }
  });

  mergeTargetSelect = createSelect();
  mergeTargetSelect.position(326, 520);
  mergeTargetSelect.size(150);

  const b4 = createButton('Merge Branch');
  b4.position(486, 520);
  b4.mousePressed(mergeBranch);

  const b5 = createButton('Reset Scenario');
  b5.position(592, 520);
  b5.mousePressed(() => {
    commitCount = 0;
    resetScenario();
  });

  resetScenario();
}

function commitPos(i) {
  return 80 + i * 90;
}

function drawBranch(name, data) {
  if (!data.active && name !== activeBranch) {
    stroke('#94a3b8');
  } else if (name === activeBranch) {
    stroke('#f59e0b');
  } else {
    stroke('#2563eb');
  }

  strokeWeight(name === activeBranch ? 4 : 2);
  noFill();
  line(commitPos(0), data.y, commitPos(data.commits.length - 1), data.y);

  for (let i = 0; i < data.commits.length; i++) {
    const x = commitPos(i);
    const c = data.commits[i];
    fill(name === activeBranch ? '#f59e0b' : '#3b82f6');
    if (!data.active && name !== activeBranch) fill('#94a3b8');
    noStroke();
    circle(x, data.y, i === data.commits.length - 1 ? 14 : 10);

    if (dist(mouseX, mouseY, x, data.y) < 9) {
      fill('#111827');
      rect(mouseX + 10, mouseY - 26, 220, 24, 4);
      fill('#f8fafc');
      textSize(11);
      text(`${name}: ${c.msg}`, mouseX + 16, mouseY - 10);
    }
  }
}

function draw() {
  background('#f8fafc');
  fill('#0f172a');
  noStroke();
  textSize(22);
  text('Git Branching and Merging Visualization', 16, 30);

  textSize(13);
  fill('#334155');
  text(`Active branch: ${activeBranch}`, 16, 54);
  text(`Total commits: ${commitCount}`, 180, 54);
  text(`Active branches: ${branchOrder.filter((b) => branches[b].active).length}`, 300, 54);

  stroke('#e2e8f0');
  line(16, 480, 924, 480);

  branchOrder.forEach((b) => drawBranch(b, branches[b]));

  fill('#1e293b');
  noStroke();
  textSize(12);
  text('Use controls to branch, commit, switch, and merge. Hover a commit for details.', 16, 500);
}
