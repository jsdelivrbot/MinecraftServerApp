import axios from 'axios';

// so many dependency issues trying to use fetch. dns, ngram, tap, fs...
// import fetch from 'fetch';

//todo: Look into spread operations.
export function turnServerOn(url=''){
    url += '/api/server_controller/turn_on';
    return (
        axios.put(url)
        .then( (response) => {
            if (response.status === 200){
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
            if (response.status === 200){
                return true
            }
            else{
                console.error('Error when turning on server', response);
            }
        })
        .catch( (err) => {
            console.error('Error with fetch request turnOffServer()', err);
        })
    )
}

export function isServerOn(url=''){
    url += '/api/server_controller/is_on';
    return (
        axios.get(url)
            .then( (response) => {
                if (response.status === 200){
                    return (response.data === 'True')
                } else {
                    console.error('Error when checking if server was on.');
                }
            })
            .catch( (err) => {
                console.error('Error when request isServerOn()', err);
            })
    )
}
