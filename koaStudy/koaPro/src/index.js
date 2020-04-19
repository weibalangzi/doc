// const koa = require('koa');
import koa from 'koa';
const path = require('path');
const router = require('./routes/routes');
const helmet = require('koa-helmet');
const koaStatic = require('koa-static');
import koaBody from 'koa-body';
import jsonUtil from 'koa-json';
import cors from '@koa/cors';
import compose from 'koa-compose';

const app = new koa();

const middleware = compose([
    koaBody(),
    koaStatic(path.join(__dirname, '../public')),
    cors(),
    jsonUtil({pretty: false, param: 'pretty'}),
    helmet()
])

app.use(middleware);
app.use(router());

app.listen(4000, res=>{
    console.log('server is running at localhost:3000')
})