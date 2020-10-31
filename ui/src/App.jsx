import './App.css';
import React, {Component} from "react"

export default class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      email: null
    }
  }

  handleChange = (e) => {
    this.setState({email: e.target.value})
  }

  sendForm = (e) => {
    e.preventDefault()
    let formData = new FormData();
    formData.append("email", this.state.email)

    const url = "http://localhost:5000/submit";

    const config = {
      headers: {
        "content-type": "multipart/form-data"
      }
    };

    // console.log(formData);

    // Envoi au serveur
    axios
      .post(url, formData, config)
      .then(res => console.log(res))
      .catch(err => console.log(err));

  }

  render(){
    return (
      <div className="App">
        <form>
          <label for="email">Enter your email:</label>
          <input type="email" placeholder="Your email" id="email" onChange={e => this.handleChange(e)} required/>
          <input type="submit" onClick={e => this.sendForm(e)}/>
        </form>
      </div>
    );
  }
}

