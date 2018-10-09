## 关于本次移动端ui框架选型评估报告
### elementUI
#### elementUI作为一套PC端的组件库，经常配合vue使用，也是和vue契合度较高的一套组件，但鉴于本次选型的是移动端ui组件，所以暂时不考虑elementui。
### vux
#### vux作为一套专为vue量身定做的移动端ui组件，现在市面上也有越来越多的公司在使用vue+vux+vuex+vue-router的技术栈。
#### >>>>简介
#### vux是基于weUI和vue开发的一套移动端ui组件库，但组件的多样化又高于weUI，且延续了weUI的设计风格，配合vue-loader可以实现按需加载组件。
#### >>>>主题切换
#### 可以配合vue-loader的less-theme插件，覆盖原来的主题配置列表https://github.com/airyland/vux/blob/v2/src/styles/variable.less，所以需要事先有一整套的设计风格，然后手动去修改配置，然后覆盖，这一点相对于其他ui组件来说比较麻烦。
#### >>>>国际化
#### 国际化的问题也可以配合vue-loader使用vux-i18n
```javascript
{
  name: 'i18n',
  vuxStaticReplace: false,
  staticReplace: false,
  extractToFiles: 'src/locales/components.yml',
  localeList: ['en', 'zh-CN']
}
```
