var modalVisible = true

  
function Card(props) {
	
  function selected(){
	  $.ajax({
	  type: "POST",
	  url: props.url,
	  data: {'pk':props.attraction.pk, 'name': props.attraction.name ,'csrfmiddlewaretoken': props.csrf},
	  dataType: "json",
	  success: function(response){
		// 배열이 아니면 에러 출력
		console.assert(Array.isArray(response), {errorMsg: "response is not an Array of Attraction"});

		response.forEach(function(attraction){
			// name이나 latitude가 누락되면 에러 출력
			console.assert(attraction.hasOwnProperty('name'), attraction)
			console.assert(attraction.hasOwnProperty('latitude'), attraction)

			placeMarkerAndPanTo(attraction);
		});
	  }
	});
  }
  return (
    <div className="w3-card w3-round-large w3-animate-left">
		<img src={props.attraction.img_src} alt="title" style={{width:"100%"}} className="w3-round-large"/>
		<h4>{props.attraction.name}</h4>
		<div>
		  <div className="w3-col" style={{width:'3%',
		  backgroundColor:'#ff6666',
		  color:"#ff0000"}}>.</div>
		  <div className="w3-col" style={{width:'5%',
		  backgroundColor:'#ff9966',
		  color:'#ffcc66'}}>.</div>
		  <div className="w3-col" style={{width:'20%',
		  backgroundColor:'#fff0b3',
		  color:'#ffdb4d'}}>★</div>
		  <div className="w3-col" style={{width:'32%',
		  backgroundColor:'#ffcc66',
		  color:'#fff0b3'}}>★</div>
		  <div className="w3-col" style={{width:'40%',
		  backgroundColor:'#ffdb4d',
		  color:'#ff9900'}}>avg : 4.5</div>
		</div>
		<span className="w3-round-xxlarge w3-tag w3-blue"> tag_name </span>	
		<button onClick={selected} className="w3-margin w3-tag w3-round-large w3-blue"> SELECT </button>
    </div>
    );
}