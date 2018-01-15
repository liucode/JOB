$("#mypay").click(function(){
	 var paytext = $("#paytext").val();
   	 $.post("../getpay/",{'paytext':paytext}, function(ret){ 
   		 	$("#containermain").html(ret);
   		 	
   		 	
       })
       	
})