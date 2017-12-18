export const MC_SERVER_ON = 'MC_SERVER_ON';
export const MC_SERVER_OFF = 'MC_SERVER_OFF';
export const MC_SERVER_PENDING = 'MC_SERVER_PENDING';
export const MC_SERVER_ERRORED = 'MC_SERVER_ERRORED';

export function serverOn(){
    return {
        type: MC_SERVER_ON,
        payload: true
    }
}

export function serverOff(){
    return {
        type: MC_SERVER_OFF,
        payload: false
    }
}

export function serverErrored(bool=true){
    return {
        type: MC_SERVER_ERRORED,
        payload: bool
    }
}

export function serverPending(bool=true){
    console.log('server pending is... ', bool)
    return {
        type: MC_SERVER_PENDING,
        payload: bool
    }
}
