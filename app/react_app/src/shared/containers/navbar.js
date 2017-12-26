import React, { Component } from 'react';
import AppBar from 'material-ui/AppBar';

const appBarStyling = {
    width: '100vw !important'
}

export class NavBar extends Component{
    render(){
        return (
            <AppBar
                    title="Minecraft Server Homepage"
                    iconClassNameRight='muidocs-icon-navigation-expand-more'
                    style={appBarStyling}
            />
        )
    }
}