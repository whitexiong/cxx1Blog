/**
 * 用于markdown的解析
 */

var testEditormdView        //文章解析
var testCommentMarkdown //评论解析
// var windowsWidth = 0
// var userAgentInfo = navigator.userAgent;  
// var Agents = new Array("Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod");  
// var agentinfo = null;  
//   
//  for (var i = 0; i < Agents.length; i++) {  
//        if (userAgentInfo.indexOf(Agents[i]) > 0) { agentinfo = userAgentInfo; break; }  
//    }  
//    if(agentinfo){
//          windowsWidth = $(window).width()
//         $('.hentry').width(windowsWidth) //跳转markdown的宽度
//    }else{
//
//
//         windowsWidth = $(window).width() * (61/100);
//         $('.hentry').width(windowsWidth) //跳转markdown的宽度
//    } 


$(function(){
        //判断是否是手机
        var mobile_flag = isMobile();
        if(mobile_flag){
            //手机端就隐藏电脑端的导航
            $("#site-navigation").css("display", "none")
            $("#moble-nav").css("display", "block")
        }else{
        }
    })




function isMobile() {
            var userAgentInfo = navigator.userAgent;

            var mobileAgents = [ "Android", "iPhone", "SymbianOS", "Windows Phone", "iPad","iPod"];

            var mobile_flag = false;

            //根据userAgent判断是否是手机
            for (var v = 0; v < mobileAgents.length; v++) {
                if (userAgentInfo.indexOf(mobileAgents[v]) > 0) {
                    mobile_flag = true;
                    break;
                }
            }
             var screen_width = window.screen.width;
             var screen_height = window.screen.height;

             //根据屏幕分辨率判断是否是手机
             if(screen_width < 500 && screen_height < 800){
                 mobile_flag = true;
             }

             return mobile_flag;
        }



testEditormdView = editormd.markdownToHTML("test-editormd-view", {
                    htmlDecode      : true,  // you can filter tags decode
                    emoji           : true,
                    taskList        : true,
                    tex             : true,  // 默认不解析
                    flowChart       : true,  // 默认不解析
                    sequenceDiagram : true,  // 默认不解析
                    tocm : true,
                });


testCommentMarkdown = editormd.markdownToHTML("testCommentMarkdown", {
                    htmlDecode      : true,  // you can filter tags decode
                    emoji           : true,
                    taskList        : true,
                    tex             : true,  // 默认不解析
                    flowChart       : true,  // 默认不解析
                    sequenceDiagram : true,  // 默认不解析
                    tocm : true,
                });



