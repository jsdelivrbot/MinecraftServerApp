import React, { Component } from 'react';
import { Card, CardHeader, CardText, CardMedia, CardTitle, RaisedButton } from 'material-ui';
import { getWorldMap, refreshWorldMap } from "../http_requests/world_map";
import _ from 'lodash';
import world_map from '../../../images/world_map.png'


const cardStyle = {
    width: "100%",
    marginTop: "10px",
};

export class WorldMap extends Component{
    constructor(props){
        super(props);
        // this.world_map = (`
        //     <div
        //     class="tile"
        //     style="width:250px; height:250px; position:absolute; top:0px; left: 0px; background=url('big.png')"
        //     >
        //     </div>
        // `)
        this.css_source = "../assets/static/css/tiles.css";
        this.map_tiles;
    }

    forceUpdate(){}

    componentDidMount(){
        // comment: test
        // this.world_map = (`
        //     <div
        //     class="tile"
        //     style="width:250px; height:250px; position:absolute; top:0px; left: 0px; background=url('../assets/static/images/tile.0.0.png')"
        //     >
        //     </div>
        // `)

        this.forceUpdate();

        // need to render images...
        // this.map_tiles = getWorldMap();
        // if (this.map_tiles && this.map_tiles.length > 0){
        //     this.setWorldMap()
        // }
    }

    // setWorldMap(){
    //     let css_link = '';  // add css links
    //     this.world_map = _.reduce(this.map_tiles.sort(), (accum, tile_url) => {
    //         tile = `
    //             <div
    //                 class="tile"
    //                 style="width:10px; height:10px; position:absolute; top:0px; left: 0px; background=url(${tile_url})"
    //             >
    //             </div>
    //         `;
    //
    //         return accum += tile
    //     }, css_link)
    //
    // }
    //
    // refreshWorldMap(){
    //
    // }

    render(){
        return (
            <Card style={cardStyle}>
                <CardHeader
                    title="World Map"
                    titleStyle={{fontSize: '18px'}}
                />
                <CardMedia>
                  <img src={world_map} alt='No Image Found.'/>
                </CardMedia>
            </Card>
        )
    }
}
