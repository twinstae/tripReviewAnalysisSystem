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
  
  var negSample = props.attraction.review_sample.neg;
  var posSample = props.attraction.review_sample.pos;
  
  const star = props.attraction.star_info;
  console.log(star);
  if (star != null){
	var star_1 = star[1].toString()+"%";
	const star_2 = star[2].toString()+"%";
	const star_3 = star[3].toString()+"%";
	const star_4 = star[4].toString()+"%";
	var string_4 = "★"
	const value_5 = 100-star[1]-star[2]-star[3]-star[4];
	const star_5 = value_5.toString()+"%";
	var string_5 = "avg:" + props.attraction.star_info.avg.toString();
	if (value_5 < 30){
		string_4 = string_5;
		string_5 = "★";
	  }
	console.log(star_5);
	
	return (
		<div className="w3-round-large w3-white w3-card w3-dropdown-hover w3-center"  style={{width:"200px", maxHeight:"350px"}}>
			<img src={props.attraction.img_src} alt="title" style={{width:"100%"}} className="w3-round-large"/>
			<h4>{props.attraction.name}</h4>
			<div>
				<div className="w3-col" style={{width: star_1,
				backgroundColor:'#ff6666',
				color:"#ff0000"}}>.</div>
				<div className="w3-col" style={{width: star_2,
				backgroundColor:'#ff9966',
				color:'#ffcc66'}}>.</div>
				<div className="w3-col" style={{width: star_3,
				backgroundColor:'#fff0b3',
				color:'#ffdb4d'}}>★</div>
				<div className="w3-col" style={{width: star_4,
				backgroundColor:'#ffcc66',
				color:'#fff0b3'}}>{string_4}</div>
				<div className="w3-col" style={{width: star_5,
				backgroundColor:'#ffdb4d',
				color:'#ff9900'}}>{string_5}</div>
			</div>
			<span className="w3-round-xxlarge w3-tag w3-blue w3-margin-small w3-small"> tag_name </span>	
			<br />
			<button onClick={selected} className="w3-margin-small w3-tag w3-round-large w3-blue"> SELECT </button>			
			<div className="w3-dropdown-content" style = {{top: "-5px",
left: "125%", width:"300px"}}>
			<span className="w3-round-xxlarge w3-tag w3-margin-small w3-small" style={{backgroundColor:'#ffdb4d',
				color:'#ff9900'}}>Most Positive</span>
			{posSample.map((sentence, i) => {
				return (<p> {sentence} </p>)
			})}
			<span className="w3-round-xxlarge w3-tag w3-margin-small w3-small w3-red">Most Negative</span>
			{negSample.map((sentence, i) => {
				return (<p> {sentence} </p>)
			})}
			</div>
		</div>
		
		);
  } else {
	return null
  }
}