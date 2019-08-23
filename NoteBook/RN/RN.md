### 添加底部Tab
当前项目中使用的是createBottomTabNavigator方法,里面包裹需要作为Tab的模块，直接设置文字和图标，这样倒是挺方便的。

这里面用到了View和Image两个组件，就类似于html里面的div和img吧，感觉差不多。

```javascript
import {createBottomTabNavigator, createStackNavigator} from 'react-navigation';

const MainPage = createBottomTabNavigator({
        Tab1: {
            screen: MainTab1,
            navigationOptions: () => ({
                tabBarLabel: 'tab1',
                tabBarIcon: ({tintColor, focused}) => (
                    <View style={[{alignItems: 'flex-end'}]}>
                        <Image
                            source={focused ? TabIconChecked1 : TabIcon1}
                            style={styles.tabIcon}
                        >
                        </Image>
                    </View>
                ),
            }),
        },
    )
}
```

### 页面的跳转

在以前使用react的时候，页面的跳转涉及到路由的配置，会有个一个react-router配合使用，但是在react-native中，直接使用了一个createStackNavigator方法，里面包含所有的页面，每个页面有一个对应的名称。

```javascript
import Splash from "./src/pages/mine/Splash";
const App = createStackNavigator(
    {
        SplashPager: {screen: Splash},
        MainPager: {screen: MainPage},
        FirstComeInPager: {screen: FirstComeIn},
        walletDetailPager: {screen: walletDetail},
        walletListPager:{screen: walletList},
        reNamePager:{screen: reName},
    }
)    
```

### 关于输入框

原来做PC端的时候都是直接event.target.value拿到输入框的值，但是在RN中好像不能这么做（试了几次吧）,RN中有一个TextInput组件，该组件可以绑定一个方法onChangeText，入参直接就是当前输入框的值。

```javascript
<TextInput
    placeholder={"手机号(选填)"}
    style={styles.textInput}
    underlineColorAndroid={"transparent"}
    onChangeText={(text) => this.setState({phoneNum: text})}
/>
```
### 点击设备上的返回键

需要引入react-native中的一个方法，用来监听设备的返回事件。

注意监听的事件在组件卸载的时候需要被移除（我也不知道为了啥）


```javascript
import { BackHandler } from 'react-native'


componentWillMount() {
    BackHandler.addEventListener('hardwareBackPress', this.onBackAndroid);
    this.onGetCoinType()
}

componentWillUnmount() {
    this.getContactUrlEmitter.remove();
    BackHandler.removeEventListener('hardwareBackPress', this.onBackAndroid);
}

onBackAndroid = () => {
    this.props.navigation.goBack();
    return true;
};
```

### ScrollView和FlatList如何选择

二者都是滚动视图类的组件，从性能上来说，FlatList更好一点，但是ScrollView使用起来更简单。

注意ScrollView必须要有一个确定的高度才能正常工作，且ScrollView内部的其他响应者尚无法阻止ScrollView本身成为响应者（类似于事件冒泡吧）,ScrollView会一次性渲染所有子元素（如果子元素很多的话。。。）。

FlatList会惰性渲染子元素，只在它们将要出现在屏幕中时开始渲染，所以子元素如果不是特别少，还是使用FlatList表较好。

### TouchableOpacity的使用

手机app上经常看见这样的效果，用手点击页面上某一部分的手，该部分会出现渐隐的效果，react-native中可以使用TouchableOpacity包裹该部分，设置相应样式，即可实现这种效果。

`TouchableHighlight`好像与之有类似的效果，没有深究，并不知道区别在哪里。

### SectionList组件

分组列表组件，本次项目中有个联系人列表的模块,当前使用的是FlatList组件，但是如果有需求按姓名手写字母进行分组，可能需要用到这个组件。

```javascript
<SectionList
  renderItem={({ item, index, section }) => <Text key={index}>{item}</Text>}
  renderSectionHeader={({ section: { title } }) => (
    <Text style={{ fontWeight: "bold" }}>{title}</Text>
  )}
  sections={[
    { title: "Title1", data: ["item1", "item2"] },
    { title: "Title2", data: ["item3", "item4"] },
    { title: "Title3", data: ["item5", "item6"] }
  ]}
  keyExtractor={(item, index) => item + index}
/>
```

### formData对象

本来以为不会再碰到formData这玩意了，想不到，又给遇上了，这东西传递少量的数据还行，如果上千上万条数据拼接起来，简直就是灾难。

```javascript
    let formData = new FormData();
    this.state.device_token = await Android.getDeviceId();
    this.state.first_start_at = await Android.getFirstStartTimestamp();
    formData.append('device_token', this.state.device_token);
    formData.append('first_start_at', parseInt(this.state.first_start_at));
    formData.append('offset', listNum);
    let url = Host + '/api/msg/list';
    HTTPUtil.post(url, formData).then((json) => {
        if(json.retcode==1){
            this.state.LastPage=json.data.lastPage;
            this.setState({messageList:json.data.list,indicatorShow:false,IfLoading:false});
        } else {
            this.setState({messageList:[],indicatorShow:false,IfLoading:false},()=>{
                Toast.info("网络异常",1)
            });
        }
    }, () => {
        Toast.fail('请求失败',1)
        this.setState({messageList:[],indicatorShow:false,IfLoading:false});
    })
```
***

### ActivityIndicator

名字这么长，就是一个loading，坑爹！

### Dimensions(获取设备的屏幕宽高)

```javascript
screenWidth: Dimensions.get('window').width,   //屏幕宽度
screenHeight: Dimensions.get('window').height, //屏幕高度
```

### PixelRatio(获取设备的像素密度)

```javascript
pixelRatio: PixelRatio.get(), //像素密度
```

### StackActions

StackActions对象包含了生成特定actions的方法,支持Reset、Replace、Push、Pop、PopToTop。

当前项目用到了Reset，reset清楚整个导航状态，并且用若干个actions来替代。

目前暂时不太明白具体作用有哪些，怎么看都像是切换路由的效果，可是为什么不直接切换路由，非得搞得这么复杂？

```javascript
const resetAction = StackActions.reset({
    index: 2,
    actions: [
        NavigationActions.navigate({
            routeName: 'MainPager', 
            params: {
                coinType: await DeviceStorage.get('currentCoinType'),
            }
        }),
        NavigationActions.navigate({routeName: 'walletListPager'}),
        NavigationActions.navigate({
            routeName: 'walletDetailPager',
            params: {item: this.props.navigation.getParam('walletData', null)},
        }),
    ],
});            const resetAction = StackActions.reset({
    index: 2,
    actions: [
        NavigationActions.navigate({
            routeName: 'MainPager', 
            params: {
                coinType: await DeviceStorage.get('currentCoinType'),
            }
        }),
        NavigationActions.navigate({routeName: 'walletListPager'}),
        NavigationActions.navigate({
            routeName: 'walletDetailPager',
            params: {item: this.props.navigation.getParam('walletData', null)},
        }),
    ],
});
```

### NavigationActions

NavigationActions.Navigate(导航到其它路由)
NavigationActions.Back(返回上一个状态)
NavigationActions.SetParams(向给定的路由设置参数)
NavigationActions.init(如果状态未定义，用来初始化第一个状态)

### AsyncStorage

网上找到的相关资料是这样描述的：一个简单的、异步的、持久化的以键值对形式进行数据存储的存储系统。

然而其实就是原来的LocalStorage，好像说是要替换LocalStorage,不得不再说一次，前端的东西更新的真特么快，劳资快学不动了有木有？？？

AsyncStorage包含多个方法，就只说几个常用的吧。

相较于LocalStorage，特点就是每一个方法都有回调函数，返回一个Promise对象。

```javascript
// 设置键值对
setItem(key:string,value:string,callback)
// 根据键获取值
getItem(key:string,value:string,callback)
// 根据键移除值
removeItem(key:string,value:string,callback)
```

### SQLite

对于存放数据量小且简易的数据我们可以通过AsyncStorage来存储，但对于数据结构复杂、数据量大的数据，我们可以使用移动开发中常用的SQLite来处理。 

SQLite是一种轻型的数据库，多用于移动端开发，在原生应用开发中比较常见。

SQLite应该是存储在设备中的吧，PC党表示没用过，LocalStorage是存储在浏览器中的，SQLite应该是就是存储在设备中的吧，嗯，应该是的。

```javascript
import SQLiteStorage from 'react-native-sqlite-storage';

SQLiteStorage.DEBUG(true);
var database_name = "test.db";//数据库文件
var database_version = "1.0";//版本号
var database_displayname = "MySQLite";
var database_size = -1;
var db;

export let SQLiteUtil = {
    //打开或者创建数据库
    open:function (){
        db = SQLiteStorage.openDatabase(
            database_name,
            database_version,
            database_displayname,
            database_size,
            ()=>{
                this._successCB('open');
            },
            (err)=>{
                this._errorCB('open',err);
            });
        return db;
    }
}
```

***

### DeviceEventEmitter(发送和接收事件)

最重要的一点就是在组件卸载的时候记得移除事件监听。
```javascript
// 发送消息
DeviceEventEmitter.emit('left', '发送了个通知');
// 接收消息
this.deEmitter = DeviceEventEmitter.addListener('left', (a) => {
    alert('收到通知：' + a);
});
// 移除监听
componentWillUnmount() {
    this.deEmitter.remove();
}
```

### Clipboard（读写剪贴板的内容）

这个就没什么好说的了，我也没用过。
```javascript
// 写入剪贴板内容
Clipboard.setString()
// 读取剪贴板内容
Clipboard.getString() 
```

### Platfrom（检测当前运行平台的相关信息）

说白了就是查看当前设备是android还是ios,是哪个版本之类的。

```javascript
import { Platform } from "react-native"
// 返回ios或者android
deviceType = Platform.OS
// 查看设备版本
deviceLevel = Platform.Version
```

***

### WebView（创建一个原生的WebView）

WebView可以创建一个原生的WebView，用于访问外部的网页，也可以在里面直接嵌套html代码。

```javascript
import { WebView } from 'react-native';
class MyWeb extends Component {
  render() {
    return (
      <WebView
        source={{uri: 'https://github.com/facebook/react-native'}}
        style={{marginTop: 20}}
      />
    );
  }
}

// 或者直接嵌套html代码
import { WebView } from 'react-native';
 class MyInlineWeb extends Component {
  render() {
    return (
      <WebView
        originWhitelist={['*']}
        source={{ html: '<h1>Hello world</h1>' }}
      />
    );
  }
}
```

### StyleSheet

StyleSheet提供了一种类似css样式表的抽象，好官方的样子，其实就是将css样式转换为当前系统能够是别的样子。

```javascript
const styles = StyleSheet.create({
    container: {
        backgroundColor: '#ffffff',
        position: 'relative',
        height: theme.screenHeight,
        width: theme.screenWidth,
        flex: 1,
    },
});
```

### RefreshControl

喜闻乐见的下拉刷新，此刻内心应该有一万只小绵羊奔腾而过，以前不知道被坑过多少次了。

RefreshControl可以用在ScrollView或者FlatList内部，为其添加下拉刷新的功能。

当ScrollView处于竖直方向的起点位置（scrollY: 0），此时下拉会触发一个onRefresh事件。

refreshing是一个受控属性， 所以必须在onRefresh函数中设置为true，否则loading指示器会立即停止。

```javascript
refreshControl={
    <RefreshControl
        refreshing={this.state.refreshing}
        onRefresh={this.onRefresh}
        tintColor={theme.themeColor}
        colors={[theme.themeColor]}
    />
}>

onRefresh = () => {
    // this.setState({});
    this.setState({refreshing: true,isForce:true},()=>{
        // this.getWallets();
        this.walletChange(this.state.currentWallet);
    });
};
```

