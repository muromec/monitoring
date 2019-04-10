Monitoring
==========

This repo contains an idea of monitoring system for brewing machine.

Contents
========

Contents outline:

* `app.py` -- Binds to port :5555 as HTTP server with websocket support;
* `mock_client.py` -- websocket client that provider server with measurement results;
* `templates/index.html` -- entry point to HTML app;
* `static/main.js` -- frontend app that connects to main server and shows measurements results;
* `static/styles.css` -- styles for frontend app.


API
===

Server exports two API endpoints:

- /socket -- websocket endpoint that would stread data provided by inlet;
- /inlet -- websocket endpoint that accepts data from brewing machine.

Server essintially works as a proxy, but has an ability to save data later user as well.


Dependencies
============

Server-side code uses python module aiohttp. Frontend code is essitially self-contained, but could require some kind of polyfill for dead browsers.

Although assignment welcomed the use of frameworks, like react, angular or vue, I have decided to skip that part, as page doesn't really need any framework to function. I could provide finished test assignments that higlight my skills with react.js if requested.

How to run
==========

type `make run` (on Linux), open URL written in console.

type `make mock_client` to see updating numbers in browser.
