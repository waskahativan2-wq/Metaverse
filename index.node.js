const http = require('node:http');
const fs = require('node:fs/promises');
const path = require('node:path');

const docsDir = path.join(__dirname, 'docs');
const landingPagePath = path.join(docsDir, 'index.html');

const contentTypes = new Map([
  ['.css', 'text/css; charset=utf-8'],
  ['.html', 'text/html; charset=utf-8'],
  ['.ico', 'image/x-icon'],
  ['.jpeg', 'image/jpeg'],
  ['.jpg', 'image/jpeg'],
  ['.js', 'text/javascript; charset=utf-8'],
  ['.json', 'application/json; charset=utf-8'],
  ['.md', 'text/markdown; charset=utf-8'],
  ['.png', 'image/png'],
  ['.svg', 'image/svg+xml'],
  ['.txt', 'text/plain; charset=utf-8'],
  ['.webp', 'image/webp'],
]);

function generatedLandingPage() {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Metaverse Launch Records</title>
  <style>
    :root { color-scheme: dark; }
    body {
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: linear-gradient(180deg, #081222, #111827 60%, #0f172a);
      color: #e5eefb;
    }
    main {
      max-width: 52rem;
      margin: 0 auto;
      padding: 4rem 1.5rem;
    }
    a { color: #8bd3ff; }
    .card {
      background: rgba(15, 23, 42, 0.78);
      border: 1px solid rgba(148, 163, 184, 0.25);
      border-radius: 1rem;
      padding: 1.5rem;
    }
  </style>
</head>
<body>
  <main>
    <div class="card">
      <p>Metaverse</p>
      <h1>Documented launch package for the OSIS concept</h1>
      <p>This repository currently presents governance, policy, and release evidence materials for a metaverse launch concept. Add <code>docs/index.html</code> for a customized GitHub Pages landing page.</p>
      <p><a href="/docs/records-policy.html">Open the records policy</a></p>
    </div>
  </main>
</body>
</html>`;
}

function getContentType(filePath) {
  return contentTypes.get(path.extname(filePath).toLowerCase()) || 'application/octet-stream';
}

async function fileExists(filePath) {
  try {
    const stat = await fs.stat(filePath);
    return stat.isFile();
  } catch {
    return false;
  }
}

function safeDocsPath(relativePath) {
  const normalizedPath = relativePath.replace(/^\/+/, '');
  const resolvedPath = path.resolve(docsDir, normalizedPath);
  const docsRoot = `${docsDir}${path.sep}`;

  if (resolvedPath !== docsDir && !resolvedPath.startsWith(docsRoot)) {
    return null;
  }

  return resolvedPath;
}

async function sendBuffer(res, statusCode, body, contentType) {
  res.writeHead(statusCode, {
    'Content-Length': Buffer.byteLength(body),
    'Content-Type': contentType,
    'X-Content-Type-Options': 'nosniff',
  });
  res.end(body);
}

async function serveLandingPage(req, res) {
  if (await fileExists(landingPagePath)) {
    const body = await fs.readFile(landingPagePath);
    res.writeHead(200, {
      'Content-Length': body.length,
      'Content-Type': 'text/html; charset=utf-8',
      'X-Content-Type-Options': 'nosniff',
    });
    res.end(req.method === 'HEAD' ? undefined : body);
    return;
  }

  const body = generatedLandingPage();
  await sendBuffer(res, 200, req.method === 'HEAD' ? '' : body, 'text/html; charset=utf-8');
}

async function serveStaticFile(req, res, filePath) {
  if (!(await fileExists(filePath))) {
    await sendBuffer(res, 404, req.method === 'HEAD' ? '' : 'Not Found\n', 'text/plain; charset=utf-8');
    return;
  }

  const body = await fs.readFile(filePath);
  res.writeHead(200, {
    'Content-Length': body.length,
    'Content-Type': getContentType(filePath),
    'X-Content-Type-Options': 'nosniff',
  });
  res.end(req.method === 'HEAD' ? undefined : body);
}

async function requestHandler(req, res) {
  if (!['GET', 'HEAD'].includes(req.method)) {
    const body = req.method === 'HEAD' ? '' : 'Method Not Allowed\n';
    res.writeHead(405, {
      Allow: 'GET, HEAD',
      'Content-Length': String(Buffer.byteLength(body)),
      'Content-Type': 'text/plain; charset=utf-8',
      'X-Content-Type-Options': 'nosniff',
    });
    res.end(req.method === 'HEAD' ? undefined : body);
    return;
  }

  const requestTarget = req.url || '/';
  const rawRequestPath = requestTarget.split('?')[0].split('#')[0];
  if (/%(?:2f|5c)/i.test(rawRequestPath)) {
    await sendBuffer(res, 404, req.method === 'HEAD' ? '' : 'Not Found\n', 'text/plain; charset=utf-8');
    return;
  }

  let pathname;
  try {
    const rawPathname = new URL(requestTarget, 'http://localhost').pathname;
    pathname = decodeURIComponent(rawPathname);
  } catch {
    await sendBuffer(res, 400, req.method === 'HEAD' ? '' : 'Bad Request\n', 'text/plain; charset=utf-8');
    return;
  }

  if (pathname === '/' || pathname === '/index.html' || pathname === '/docs' || pathname === '/docs/') {
    await serveLandingPage(req, res);
    return;
  }

  const relativePath = pathname.startsWith('/docs/')
    ? pathname.slice('/docs/'.length)
    : pathname.slice(1);

  const resolvedPath = safeDocsPath(relativePath);
  if (!resolvedPath) {
    await sendBuffer(res, 404, req.method === 'HEAD' ? '' : 'Not Found\n', 'text/plain; charset=utf-8');
    return;
  }

  await serveStaticFile(req, res, resolvedPath);
}

function startServer({
  host = process.env.HOST || '0.0.0.0',
  port = Number.parseInt(process.env.PORT || '3000', 10),
} = {}) {
  const server = http.createServer((req, res) => {
    requestHandler(req, res).catch((error) => {
      res.writeHead(500, {
        'Content-Type': 'text/plain; charset=utf-8',
        'X-Content-Type-Options': 'nosniff',
      });
      res.end('Internal Server Error\n');
      console.error(error);
    });
  });

  return new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(port, host, () => {
      server.off('error', reject);
      resolve(server);
    });
  });
}

if (require.main === module) {
  startServer()
    .then((server) => {
      const address = server.address();
      const activeHost = typeof address === 'object' && address ? address.address : '0.0.0.0';
      const activePort = typeof address === 'object' && address ? address.port : process.env.PORT || '3000';
      console.log(`Metaverse landing server listening on http://${activeHost}:${activePort}`);
    })
    .catch((error) => {
      console.error(error);
      process.exitCode = 1;
    });
}

module.exports = {
  requestHandler,
  startServer,
};
