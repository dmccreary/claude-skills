const { test, expect } = require('@playwright/test');

const fixtureUrl =
  process.env.PRONUNCIATION_FIXTURE_URL ||
  'http://127.0.0.1:8765/skills/book-media-generator/tests/fixtures/pronunciation-controls/';

for (const viewport of [
  { name: 'desktop', width: 1280, height: 900 },
  { name: 'mobile', width: 390, height: 844 },
]) {
  test(`native pronunciation control remains usable at ${viewport.name} width`, async ({ page }) => {
    await page.setViewportSize(viewport);
    const pageErrors = [];
    page.on('pageerror', (error) => pageErrors.push(error.message));
    await page.goto(fixtureUrl);

    const audio = page.locator('audio');
    const status = page.getByRole('status');
    await expect(audio).toBeVisible();
    await expect(audio).toHaveAttribute('controls', '');
    await expect(audio).toHaveAttribute('aria-label', 'Pronunciation of Bryophytes');
    await expect(status).toHaveText('Ready');

    await audio.evaluate((element) => element.dispatchEvent(new Event('play')));
    await expect(status).toHaveText('Playing pronunciation');
    await audio.evaluate((element) => element.dispatchEvent(new Event('pause')));
    await expect(status).toHaveText('Paused');
    await audio.evaluate((element) => element.dispatchEvent(new Event('error')));
    await expect(status).toHaveText('Pronunciation unavailable');

    const overflow = await page.locator('html').evaluate((element) =>
      element.scrollWidth > window.innerWidth + 1
    );
    expect(overflow).toBe(false);
    expect(pageErrors).toEqual([]);
  });
}
