

const koaRouter = require('koa-router');
const aRoutes = require('../api/a');

const router = new koaRouter();

router.get('/a', aRoutes.a);

module.exports = router;