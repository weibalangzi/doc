const Koa = require('Koa');
const Router = require('koa-router');
const app = new Koa();
const home = new Router();
home.get('/', (ctx) => {
    ctx.body = 'hhahaha';
});
const router = new Router();
router.use('/', home.routes(), home.allowedMethods());
app.use(router.routes()).use(router.allowedMethods());
app.listen(3001, () => {
    console.log('server is running');
});
//# sourceMappingURL=app.js.map