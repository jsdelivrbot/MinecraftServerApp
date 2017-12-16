import React, { Component } from 'react';
//todo: Move navbar to a shared component
import AppBar from 'material-ui/AppBar';

export class Homepage extends Component{
    render(){
        return (
            <AppBar
                title="Minecraft Server Homepage"
                iconClassNameRight='muidocs-icon-navigation-expand-more' />
        )
    }
}