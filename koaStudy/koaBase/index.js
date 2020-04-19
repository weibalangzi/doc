const Koa = require('koa');
const Router = require('koa-router');
const KoaBody = require('koa-body');
const Cors = require('@koa/cors')
const app = new Koa();
const router = new Router();

router.prefix('/api');

router.post('/user', ctx => {
    let {body, header} = ctx.request;
    
    ctx.body = {
        code: 200,
        data: body,
        msg: '上传成功',
    };

    if(!body.email || !body.name){
        ctx.body = {
            code: '404',
            msg: 'name或者email不能为空'
        }
    }

    if(header.role !== 'admin'){
        ctx.body = {
            code: '401',
            msg: 'unauthorized post'
        }
    }
})


app.use(KoaBody())
app.use(Cors())

app.use(router.routes())
.use(router.allowedMethods())

app.listen(4000, ()=>{
    console.log('server is running at http://localhost:4000')
});