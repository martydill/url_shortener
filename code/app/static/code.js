var ReactCSSTransitionGroup = React.addons.CSSTransitionGroup;

var UrlAddedBox = React.createClass({
  render: function() {
    return (
      <ReactCSSTransitionGroup transitionName="fade-in" transitionAppear={true}>
        <h1>URL Created at <a href={this.props.link}>{this.props.link}</a></h1>
      </ReactCSSTransitionGroup>
    );
  }
});

var AddUrlBox = React.createClass({

  getInitialState: function() {
    return { value: '', showUrlAdded: false };
  },

  handleChange: function(event) {
    this.setState({value: event.target.value});
  },

  handleClick: function(event) {
    var me = this;
    var url = this.state.value;
    $.ajax({
      type: 'POST',
      url: '/urls',
      data: {url: url}
    })
    .done(function(data) {
      me.props.link = '/' + data.short_url;
      me.props.id = data.id;
      me.setState({showUrlAdded: true});
      me.setState({value: ''});
    })
    .fail(function(jqXhr) {
      console.log('failed to register');
    });
  },

  handleKeyDown: function(e) {
    if (e.keyCode == 13) {
      this.handleClick(e)
    }
  },

  render: function() {
    var value = this.state.value;

    return (
      <ReactCSSTransitionGroup transitionName="fade-in" transitionAppear={true}>
      <div className="add-url-box text-center">
        <input className="large-input" type="text" placeholder="Enter your URL here" value={value} onKeyDown={this.handleKeyDown} onChange={this.handleChange}></input>
      </div>
      <div className="text-center">
        <button type="submit" onClick={this.handleClick}>Shorten My URL!</button>
      </div>
      { this.state.showUrlAdded ? <UrlAddedBox link={this.props.link} /> : null }
      </ReactCSSTransitionGroup>
    );
  }
});

React.render(
  <div>
    <AddUrlBox/>
  </div>,
  document.getElementById('content')
);
