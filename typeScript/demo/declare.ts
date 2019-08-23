
/**
 * 声明语句
 * 当使用第三方库时，我们需要引用它的声明文件，才能获得对应的代码补全、接口提示等功能
 */

// example
// 以前在js里面使用jq时，经常要用到$或者JQuery来获取dom元素或者做一些其它操作，
// 但是在ts里面，是无法识别

// 在ts里面，需要声明一下
declare var jQuery: (selector: string) => any;

// declare var 并没有真的定义一个变量，只是定义了全局变量 jQuery 的类型，仅仅会用于编译时的检查，在编译结果中会被删除

jQuery('#foo');


/**
 * 声明文件
 * 通常我们会把声明语句放到一个单独的文件（jQuery.d.ts）中，这就是声明文件
 * 声明文件必需以 .d.ts 为后缀
 * ts 会解析项目中所有的 *.ts 文件，当然也包含以 .d.ts 结尾的文件。所以当我们将 jQuery.d.ts 放到项目中时，其他所有 *.ts 文件就都可以获得 jQuery 的类型定义了
 * 假如仍然无法解析，那么可以检查下 tsconfig.json 中的 files、include 和 exclude 配置，确保其包含了 jQuery.d.ts 文件
 */

 // 最好是使用 @types 统一管理第三方库的声明文件
 //  npm install @types/jquery --save-dev




