"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Koa = require('Koa');
const Router = require('koa-router');
const app = new Koa();
const home = new Router();
const page = new Router();
home.get('/', (ctx) => {
    ctx.body = 'hhahaha';
});
page.get('/404', (ctx) => {
    ctx.body = `<h1>404</h1>`;
});
const router = new Router();
router.use('/', home.routes(), home.allowedMethods());
router.use('/page', page.routes(), home.allowedMethods());
app.use(router.routes()).use(router.allowedMethods());
app.listen(3001, () => {
    console.log('server is running');
});
//# sourceMappingURL=router.js.map