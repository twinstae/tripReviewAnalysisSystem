var modalVisible = true

function Card(props) {
  return (
    <div className="w3-quarter w3-card" id={props.attraction.pk}>
      <h3>Hello, {props.attraction.name}</h3>
      <span className="w3-round-xxlarge w3-tag" style = {{
         backgroundColor:'#fff0b3',
        color:'#ff9900'
        }}> 3.5</span>
      <span className="w3-round-xxlarge w3-tag w3-color"> tag_name </span>
    </div>
    );
}

ReactDOM.render(<Card attraction = {{
          name: "taehee",
          pk:3
        }}/>, document.getElementById('taehee'));