(function () {
  'use strict';

  function setStatus(container, message) {
    const status = container.querySelector('[role="status"]');
    if (status) status.textContent = message;
  }

  function initialize(container) {
    const audio = container.querySelector('audio[controls]');
    if (!audio) {
      setStatus(container, 'Audio control unavailable');
      return;
    }

    audio.addEventListener('loadstart', function () {
      setStatus(container, 'Loading pronunciation');
    });
    audio.addEventListener('canplay', function () {
      setStatus(container, 'Ready');
    });
    audio.addEventListener('play', function () {
      setStatus(container, 'Playing pronunciation');
    });
    audio.addEventListener('pause', function () {
      if (!audio.ended) setStatus(container, 'Paused');
    });
    audio.addEventListener('ended', function () {
      setStatus(container, 'Pronunciation complete');
    });
    audio.addEventListener('error', function () {
      setStatus(container, 'Pronunciation unavailable');
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-pronunciation]').forEach(initialize);
  });
}());
