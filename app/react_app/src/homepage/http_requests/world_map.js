import axios from 'axios';

export function getWorldMap(){
    axios.get('/api/get_world_map')
    .then( (response) => {
        if (response.status === 200){
            return response.text
        } else {
            console.error('Failed to get world map', response.text);
            return false
        }

    }).catch( (err) => {
        console.error('Unable to get world map...', err);
        return false
    })
}

export function refreshWorldMap(){
    axios.post('/api/create_world_map')
    .then( (response) => {
        if (response.status === 200){
            return response.text
        } else {
            console.error('Failed to create world map', response.text);
            return false
        }

    }).catch( (err) => {
        console.error('Create world map errored...', err);
        return false
    })
}
