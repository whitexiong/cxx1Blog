(function($) {
  'use strict';

  $(function() {
    var $fullText = $('.admin-fullText');
    $('#admin-fullscreen').on('click', function() {
      $.AMUI.fullscreen.toggle();
    });

    $(document).on($.AMUI.fullscreen.raw.fullscreenchange, function() {
      $fullText.text($.AMUI.fullscreen.isFullscreen ? '退出全屏' : '开启全屏');
    });
  });



  // $("site-navigation")


$(function(){
        //判断是否是手机
        var mobile_flag = isMobile();
        if(mobile_flag){
            alert(1)
        }else{
          alert(2)
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

})(jQuery);
