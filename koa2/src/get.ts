import { createContext } from "vm"

const Koa = require('Koa')
const Router = require('koa-router')

const app = new Koa()

const home = new Router()
const page = new Router()

home.get('/', (ctx:any) => {
    let url = ctx.url
    let request = ctx.request
    let rep_body = {
        req_url: url,
        req_query: request.query,
        req_query_string:request.querystring
    }
    ctx.body = rep_body
})

page.get('/404', (ctx:any) => {
    ctx.body = `<h1>404</h1>`
})


const router = new Router()

router.use('/', home.routes(), home.allowedMethods())
router.use('/page', page.routes(), home.allowedMethods())

app.use(router.routes()).use(router.allowedMethods())

app.listen(3001, ()=>{
    console.log('server is running')
})