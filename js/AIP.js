function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
    }
	function showtime() {
    var aip = ["2019-12-4","2020-1-2","2020-1-30","2020-2-27","2020-3-26","2020-4-23","2020-5-21","2020-6-18","2020-7-16","2020-8-13","2020-9-10","2020-10-08","2020-11-05","2020-12-03","2020-12-31"];
    var cycle = "err";
    var nowdate = new Date();
    var year = nowdate.getFullYear(),
        month = nowdate.getMonth() + 1,
        date = nowdate.getDate(),
        day = nowdate.getDay();
    for(var i = 0;i<aip.length;i++){
        //i = 3;
       // console.log("aaa");
        var nowaip = new Date(aip[i]);
        var baip = new Date(aip[i-1]);
        if(nowdate>baip&&nowdate<nowaip){
            if(i<9){
                cycle="200"+(i-1);
            }else{
                cycle="20"+(i-1);
            }
        }
      //  cycle = nowdate>baip;
    }
    return year + "年" + month + "月" + date + "日"+"当前应生效航行资料周期："+cycle;
}