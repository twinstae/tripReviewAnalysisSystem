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
		console.log(response)
		response.forEach(function(attraction){
			// name이나 latitude가 누락되면 에러 출력
			console.assert(attraction.fields.hasOwnProperty('name'), attraction)
			console.assert(attraction.fields.hasOwnProperty('latitude'), attraction)
			var pk = attraction.pk;
			const cardWindow = document.getElementById('card-window');
			var c = cardWindow.children;
			var isid = false;
			var i;
			for (i = 0; i < c.length; i++) {
				if (c[i].id == pk){
					isid = true;
				}
			}
			if (isid != true){
				makeCard(attraction)
				placeMarker(attraction);
			}

		});
	  }
	});
  }
  return (
	<div style={{width:"200px", maxHeight:"350px"}}>
		<div className="w3-round-large w3-white w3-card">
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
			<span className="w3-round-xxlarge w3-tag w3-blue w3-margin-small w3-small"> tag_name </span>	
			<br />
			<button onClick={selected} className="w3-margin-small w3-tag w3-round-large w3-blue"> SELECT </button>			
		</div>
	</div>
	
    );
}