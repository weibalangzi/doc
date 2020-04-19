
const combineRouters = require('koa-combine-routers');

const aRoutes = require('./aRouter');
const bRoutes = require('./bRouter');

module.exports = combineRouters(
    aRoutes,
    bRoutes,
)

