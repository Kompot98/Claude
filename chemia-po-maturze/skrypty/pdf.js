// Drukuje wydanie/chemia-po-maturze.html do PDF przez Chromium (Playwright). Użycie: node skrypty/pdf.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const wyd = path.join(__dirname, '..', 'wydanie');
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.join(wyd, 'chemia-po-maturze.html'), { waitUntil: 'load' });
  await p.pdf({ path: path.join(wyd, 'chemia-po-maturze.pdf'), format: 'A4', margin: { top: '18mm', bottom: '18mm', left: '18mm', right: '18mm' }, printBackground: true });
  await b.close();
  console.log('pdf ok');
})();
