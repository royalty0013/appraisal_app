$(document).ready(function(){

   $("input[name='optionsRadios']").click(function() {

   	if ($("#optionsRadios1").is(":checked")) {
   		$("#intro").slideDown();
     } else {
     	$("#intro").slideUp();
     }
   });
 });
$(document).ready(function() {
		$("#dropdown").change(function() {
			var Regions = $(this).val();
			if (Regions == "Regions") {
				$(".Goal-Info").show();
			} else if (Regions == "FCT Central") {
				$(".Goal-Info").show();
			} else if (Regions == "FCT South") {
				$(".Goal-Info").show();
    		} else if (Regions == "Head Office") {
      			$(".Goal-Info").show();
    		} else if (Regions == "FCT West"){
          $(".Goal-Info").show();
        } else if (Regions == "Kogi") {
      			$(".Goal-Info").show();
      		} else if (Regions == "FCT East"){
            $(".Goal-Info").show();
          }else if (Regions == "Nasarawa") {
      			$(".Goal-Info").show();
      		} else if (Regions == "Niger") {
      			$(".Goal-Info").show();	
    		} else if(Regions == "FCT North") {
      			$(".Goal-Info").show();
      		} else {
      		  $(".Goal-Info").hide();
   		 	}
   			});
	});