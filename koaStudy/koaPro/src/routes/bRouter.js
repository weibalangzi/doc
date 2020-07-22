

const koaRouter = require('koa-router');
const bRoutes = require('../api/b');

const router = new koaRouter();

router.get('/b', bRoutes.b);

module.exports = router;