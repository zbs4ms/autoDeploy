/**
 * Created by wang on 15/6/12.
 * 消息分发器，作用于各个页面模块之间信息传递分发。
 * 每个模块定义并注册自己的事件到分发器，同时也注册自己需要订阅的消息。消息分发器会再接收到
 * 消息事件之后将其分发至对应的页面组件中。
 */

//params 必须是一个数组
function EventDispatcher (){
    this._eventMap={};//结构{'eventName':[fn1,fn2]}
    this.regEvent=function(name,fn){
        this._eventMap[name]!=null?this._eventMap[name].push(fn):this._eventMap[name]=[fn];
    };
    //params 必须是一个数组
    this.broadcast=function(eventName,params){
        var fun=this._eventMap[eventName];
        for(var i=0;i<fun.length;i++){
            fun[i].apply(this, params);
        }
    };
};

var  Bus=new EventDispatcher();//消息总线
var  App = angular.module("App", []);
App.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('((');
    $interpolateProvider.endSymbol('))');
});