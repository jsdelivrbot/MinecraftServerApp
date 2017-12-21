// an alternative is axios
import axios from 'axios';

// so many dependency issues trying to use fetch. dns, ngram, tap, fs...
// import fetch from 'fetch';

//todo: Look into spread operations.
export function turnServerOn(url=''){
    url += '/api/server_controller/turn_on';
    return (
        axios.put(url)
        .then( (response) => {
            if (response.status_code === 200){
                return true
            }
            else{
                console.error('Error when turn on server', response);
                return false
            }
        })
        .catch( (err) => {
            console.error('Error with fetch request turnOnServer()', err)
        })
    )
}

export function turnServerOff(url=''){
    url += '/api/server_controller/turn_off';
    return (
        axios.put(url)
        .then( (response) => {
            if (response.status_code === '200'){
                return true
            }
            else{
                console.error('Error when turning on server', response)
                return false
            }
        })
        .catch( (err) => {
            console.error('Error with fetch request turnOffServer()', err)
        })
    )
}
