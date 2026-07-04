/* docker-lab.js — shared runtime for all Docker Python labs.
 *
 * Single-lab pages use suffix "1":
 *   id="docker-lab-1"  id="docker-code-1"  id="docker-output-1"
 *   Buttons: onclick="runDocker('1')"   onclick="resetDocker('1')"
 *
 * Multi-lab pages add more suffixes ("2", "3", …):
 *   id="docker-lab-2"  id="docker-code-2"  id="docker-output-2"
 *   Buttons: onclick="runDocker('2')"   onclick="resetDocker('2')"
 *
 * The timed lab uses runDockerTimed('4') / resetDockerTimed('4')
 * and expects the timing-table elements from the Lab 4 HTML template.
 *
 * CSS counterpart: docs/css/docker-lab.css
 * Service:         scripts/run-python-docker.sh  (port 5001)
 */

var _DOCKER_SERVICE_URL = 'http://127.0.0.1:5001/run';

/* ── Helpers ───────────────────────────────────────────────────────────────── */

function _dockerEsc(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function _dockerIsConnectError(err) {
  return err.message.includes('Failed to fetch') ||
         err.message.includes('NetworkError') ||
         err.message.includes('net::ERR');
}

function _dockerShowResult(outputEl, data) {
  outputEl.className = 'docker-output';
  if (data.returncode !== 0 && data.stderr) {
    outputEl.innerHTML =
      (data.stdout ? _dockerEsc(data.stdout) + '\n' : '') +
      '<span class="docker-error">' + _dockerEsc(data.stderr) + '</span>';
  } else if (data.stdout || data.stderr) {
    outputEl.textContent = (data.stdout + (data.stderr || '')).replace(/\n$/, '');
  } else {
    outputEl.textContent = '(program finished with no output)';
  }
}

function _dockerShowConnectError(outputEl, err) {
  outputEl.className = 'docker-output';
  outputEl.innerHTML = _dockerIsConnectError(err)
    ? '<span class="docker-error">' +
      'Cannot connect to the Python Docker service.\n\n' +
      'Please open a terminal and run:\n' +
      '  bash scripts/run-python-docker.sh\n\n' +
      'Then reload this page and try again.' +
      '</span>'
    : '<span class="docker-error">Error: ' + _dockerEsc(err.message) + '</span>';
}

/* ── Standard lab (runDocker / resetDocker) ────────────────────────────────── */

async function runDocker(suffix) {
  var codeEl   = document.getElementById('docker-code-'   + suffix);
  var outputEl = document.getElementById('docker-output-' + suffix);
  var runBtn   = document.getElementById('docker-run-'    + suffix);
  if (!codeEl || !outputEl) return;

  runBtn.disabled = true;
  outputEl.className = 'docker-output docker-running';
  outputEl.textContent = 'Running…';

  try {
    var resp = await fetch(_DOCKER_SERVICE_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code: codeEl.value }),
    });
    if (!resp.ok) throw new Error('Service returned status ' + resp.status);
    _dockerShowResult(outputEl, await resp.json());
  } catch (err) {
    _dockerShowConnectError(outputEl, err);
  } finally {
    runBtn.disabled = false;
  }
}

function resetDocker(suffix) {
  var codeEl   = document.getElementById('docker-code-'   + suffix);
  var outputEl = document.getElementById('docker-output-' + suffix);
  var key = '_dockerOrig' + suffix;
  if (codeEl && window[key] !== undefined) codeEl.value = window[key];
  if (outputEl) { outputEl.className = 'docker-output'; outputEl.textContent = ''; }
}

/* ── Timed lab (runDockerTimed / resetDockerTimed) ─────────────────────────── *
 *                                                                               *
 * Requires the timing-table HTML block in the page (see Lab 4 template).       *
 * The suffix defaults to '4' to match the standard Lab 4 element IDs.          *
 * ────────────────────────────────────────────────────────────────────────────── */

async function runDockerTimed(suffix) {
  suffix = suffix || '4';
  var codeEl   = document.getElementById('docker-code-'   + suffix);
  var outputEl = document.getElementById('docker-output-' + suffix);
  var runBtn   = document.getElementById('docker-run-'    + suffix);
  var display  = document.getElementById('docker-timing-display');
  if (!codeEl || !outputEl) return;

  runBtn.disabled = true;
  outputEl.className = 'docker-output docker-running';
  outputEl.textContent = 'Running…';
  if (display) display.style.display = 'none';

  var t0 = performance.now();

  try {
    var resp = await fetch(_DOCKER_SERVICE_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code: codeEl.value, show_timing: true }),
    });
    var t_total = performance.now() - t0;
    if (!resp.ok) throw new Error('Service returned status ' + resp.status);
    var data = await resp.json();
    var tm   = data.timing || {};

    /* Break the round-trip into four phases. */
    var docker_total    = tm.docker_total_ms      || 0;
    var server_overhead = tm.server_overhead_ms   || 0;
    var startup         = tm.container_startup_ms != null ? tm.container_startup_ms : docker_total;
    var exec            = tm.python_exec_ms       || 0;
    var network_total   = Math.max(0, t_total - server_overhead - docker_total);
    var net_send        = network_total / 2;
    var net_recv        = network_total / 2;

    var phases = [
      { id: 'network-send',   ms: net_send },
      { id: 'startup',        ms: startup  },
      { id: 'exec',           ms: exec     },
      { id: 'network-return', ms: net_recv },
    ];
    var maxMs = Math.max.apply(null, phases.map(function(p) { return p.ms; }).concat([1]));

    phases.forEach(function(p) {
      var td  = document.getElementById('td-'  + p.id);
      var bar = document.getElementById('bar-' + p.id);
      if (td)  td.textContent    = p.ms.toFixed(1);
      if (bar) bar.style.width   = Math.max(2, (p.ms / maxMs) * 200) + 'px';
    });

    var tdTotal = document.getElementById('td-total');
    if (tdTotal) tdTotal.textContent = t_total.toFixed(1) + ' ms';

    var noteEl = document.getElementById('docker-timing-note');
    if (noteEl) {
      noteEl.textContent = (tm.python_exec_ms != null)
        ? 'Your Python code ran for ' + exec.toFixed(3) + ' ms — ' +
          ((exec / t_total) * 100).toFixed(1) + '% of the total round-trip time.'
        : '';
    }

    if (display) display.style.display = 'block';
    _dockerShowResult(outputEl, data);

  } catch (err) {
    if (display) display.style.display = 'none';
    _dockerShowConnectError(outputEl, err);
  } finally {
    runBtn.disabled = false;
  }
}

function resetDockerTimed(suffix) {
  suffix = suffix || '4';
  var codeEl   = document.getElementById('docker-code-'   + suffix);
  var outputEl = document.getElementById('docker-output-' + suffix);
  var display  = document.getElementById('docker-timing-display');
  var key = '_dockerOrig' + suffix;
  if (codeEl && window[key] !== undefined) codeEl.value = window[key];
  if (outputEl) { outputEl.className = 'docker-output'; outputEl.textContent = ''; }
  if (display)  display.style.display = 'none';
}

/* ── Editor auto-initialisation ────────────────────────────────────────────── *
 *                                                                               *
 * Runs once on DOMContentLoaded. For every textarea whose id starts with       *
 * "docker-code-" it:                                                            *
 *   1. Saves the original code so resetDocker() can restore it without a       *
 *      per-page defaults dictionary.                                            *
 *   2. Auto-sizes the textarea to show all initial code without scrolling.     *
 *   3. Maps the Tab key to four spaces (Python indentation).                   *
 * ────────────────────────────────────────────────────────────────────────────── */

function _initDockerEditors() {
  document.querySelectorAll('textarea[id^="docker-code-"]').forEach(function (ta) {
    var suffix = ta.id.slice('docker-code-'.length);

    /* Save original content for Reset. */
    window['_dockerOrig' + suffix] = ta.value;

    /* Auto-size: trim trailing newlines so the blank line before </textarea>
       in the markdown source doesn't add a wasted empty row at the bottom. */
    var saved = ta.value;
    ta.value = saved.replace(/\n+$/, '');
    ta.style.height = '0px';
    ta.style.height = Math.max(80, ta.scrollHeight + 4) + 'px';
    ta.value = saved;

    /* Tab → 4 spaces */
    ta.addEventListener('keydown', function (e) {
      if (e.key === 'Tab') {
        e.preventDefault();
        var s = ta.selectionStart;
        ta.value = ta.value.substring(0, s) + '    ' + ta.value.substring(ta.selectionEnd);
        ta.selectionStart = ta.selectionEnd = s + 4;
      }
    });
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', _initDockerEditors);
} else {
  _initDockerEditors();
}
