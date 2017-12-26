import React, { Component } from 'react';
import { connect } from 'react-redux';
import LinearProgress from 'material-ui/LinearProgress';
import Snackbar from 'material-ui/Snackbar';

//todo: Have shareable component for Server card status
import { Card, CardActions, CardHeader, CardTitle } from 'material-ui/Card';
import Toggle from 'material-ui/Toggle';
import { TURN_ON_MC_SERVER, TURN_OFF_MC_SERVER, IS_SERVER_ON } from '../sagas/server_controller';
// import { WorldMap } from './world_map';

const cardStyle = {
    width: "100%",
};

class Homepage extends Component {
    constructor(props){
        super(props);
        this.onMinecraftServerToggle = this.onMinecraftServerToggle.bind(this);
        this.getServerStatusIcon = this.getServerStatusIcon.bind(this);
        this.getServerPendingMessage = this.getServerPendingMessage.bind(this);
        this.toggleStyle = {
            trackStyle: {color: 'red'}
        };
        this.state = {
          pending: true,
        };
    }

    componentDidMount(){
        this.props.isServerOn();
        this.setState({
            pending: false
        })
    }

    onMinecraftServerToggle(){
        if (this.props.serverStatus.serverPending){
            return;
        } else if (!this.props.serverStatus.serverOn){
            this.props.turnOnServer();
        } else if (this.props.serverStatus.serverOn){
            this.props.turnOffServer();
        }
    }

    getServerStatusIcon(serverStatus){
        if (serverStatus.serverOn){
            return 'On'
        } else if (serverStatus.serverPending){
            return "Pending..."
        } else {
            return 'Off'
        }
    }

    getServerPendingMessage(){
        return (
            <LinearProgress mode="indeterminate" />
        );
    }

    render(){
        return (
            // todo: need to move this div to something like a body component for other components
            <div style={{width:'96vw', marginLeft: '2vw', marginTop: '10px'}}>
                <Card style={cardStyle}>
                    <CardHeader
                        title="Minecraft Server Status Panel"
                        titleStyle={{fontSize: '18px'}}
                    />
                    <CardActions
                        style={{padding:'8px 16px 8px 16px'}}
                    >
                        // todo: need to update check mark for when server is on... or change it out right. Looks kindof ugly.
                        <div>
                            Server Status: {this.getServerStatusIcon(this.props.serverStatus)}
                        </div>
                        <Toggle
                            label="Turn On Server"
                            onToggle={this.onMinecraftServerToggle}
                            trackSwitchedStyle={this.toggleStyle.trackStyle}
                            toggled={this.props.serverStatus.serverOn}
                            labelPosition='left'
                            labelStyle={{width: 'fit-content', marginRight: '10px'}}
                            iconStyle={{marginTop: '1px'}}
                        />
                    </CardActions>
                </Card>
                <Snackbar
                    open={this.state.pending}
                    message={this.getServerPendingMessage()}
                    autoHideDuration={30000}
                    bodyStyle={{
                        backgroundColor: '#0097a724',
                        padding: "25px 25px 25px 25px"
                    }}
                />
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        serverStatus: state.serverStatus
    }
};

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        turnOnServer: () => {
            dispatch({type: TURN_ON_MC_SERVER})
        },
        turnOffServer: () => {
            dispatch({type: TURN_OFF_MC_SERVER})
        },
        isServerOn: () => {
            dispatch({type: IS_SERVER_ON})
        }

    }
};

export default connect(mapStateToProps, mapDispatchToProps)(Homepage);
