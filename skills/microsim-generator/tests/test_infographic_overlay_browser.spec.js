const { test, expect } = require('@playwright/test');

const fixtureUrl =
  process.env.INFOGRAPHIC_OVERLAY_FIXTURE_URL ||
  'http://127.0.0.1:8765/skills/microsim-generator/tests/fixtures/callout-overlay/';

for (const viewport of [
  { name: 'desktop', width: 1280, height: 900 },
  { name: 'mobile', width: 390, height: 844 },
]) {
  test(`callout controls remain stable at ${viewport.name} width`, async ({ page }) => {
    await page.setViewportSize(viewport);
    const pageErrors = [];
    page.on('pageerror', (error) => pageErrors.push(error.message));

    await page.goto(fixtureUrl);
    const overlay = page.frameLocator('#overlay');
    await expect(overlay.locator('#sim-title')).toHaveText(
      'Callout Overlay Contract Fixture'
    );
    await expect(overlay.locator('.label-row')).toHaveCount(2);

    const controls = overlay.locator('#controls');
    const initialTop = await controls.evaluate((element) =>
      element.getBoundingClientRect().top
    );

    await overlay.locator('.label-row[data-id="short"]').hover();
    await expect(overlay.locator('#infobox-label')).toHaveText('Short callout');
    const shortTop = await controls.evaluate((element) =>
      element.getBoundingClientRect().top
    );

    await overlay.locator('.label-row[data-id="long"]').hover();
    await expect(overlay.locator('#infobox-label')).toHaveText('Long callout');
    const longTop = await controls.evaluate((element) =>
      element.getBoundingClientRect().top
    );

    expect(Math.abs(shortTop - initialTop)).toBeLessThan(0.5);
    expect(Math.abs(longTop - initialTop)).toBeLessThan(0.5);

    const overflow = await overlay.locator('html').evaluate((element) => ({
      horizontal: element.scrollWidth > window.innerWidth + 1,
      vertical: element.scrollHeight > window.innerHeight + 1,
    }));
    expect(overflow).toEqual({ horizontal: false, vertical: false });
    expect(pageErrors).toEqual([]);
  });
}
