const rows = [
  ['rwx------', '700', 'Owner full, group/others none'],
  ['rwxr-x---', '750', 'Owner full, group read+execute'],
  ['rw-r-----', '640', 'Owner read+write, group read'],
  ['rw-r--r--', '644', 'Common file mode'],
  ['rwxr-xr-x', '755', 'Common executable mode']
];

function setup() {
  const c = createCanvas(980, 680);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function drawBits(bits, x, y) {
  const labels = ['Owner', 'Group', 'Others'];
  for (let i = 0; i < 3; i++) {
    const seg = bits.slice(i * 3, i * 3 + 3);
    fill('#e2e8f0'); stroke('#cbd5e1'); rect(x + i * 190, y, 180, 54, 8);
    noStroke(); fill('#1e3a8a'); textSize(12); text(labels[i], x + 12 + i * 190, y + 18);
    fill('#0f172a'); textSize(20); text(seg, x + 12 + i * 190, y + 44);
  }
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('Permission Bits Visual Infographic', 16, 32);

  fill('#334155'); textSize(13); text('r = read (4), w = write (2), x = execute (1). Each triplet sums to an octal digit.', 16, 56);

  let y = 90;
  rows.forEach((r) => {
    fill('#ffffff'); stroke('#cbd5e1'); rect(16, y, 948, 104, 10);
    noStroke(); fill('#0f172a'); textSize(14); text(`Symbolic: ${r[0]}    Octal: ${r[1]}`, 30, y + 24);
    fill('#334155'); textSize(12); text(r[2], 30, y + 44);
    drawBits(r[0], 240, y + 20);
    y += 116;
  });
}
