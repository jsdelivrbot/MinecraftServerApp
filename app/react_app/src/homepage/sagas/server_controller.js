import { call, put, takeLatest } from 'redux-saga/effects';
import { turnServerOn, turnServerOff } from '../http_requests/server_controller';

import { serverOn, serverOff, serverErrored, serverPending } from '../actions/server_controller';
import { MC_SERVER_ON, MC_SERVER_OFF, MC_SERVER_PENDING, MC_SERVER_ERRORED } from '../actions/server_controller';


export const TURN_ON_MC_SERVER = 'TURN_ON_MC_SERVER_SAGAS';
export const TURN_OFF_MC_SERVER = 'TURN_OFF_MC_SERVER_SAGAS';

// todo: need to rename to better names...
export function* turnOnServerSagas(){
    try {
        yield put({type: MC_SERVER_PENDING, payload: true});
        yield call(turnServerOn);
        yield put({type: MC_SERVER_ON, payload: true});
        yield put({type: MC_SERVER_ERRORED, payload: false});

    } catch (error) {
        console.error('Sagas error with turning on server', error);
        yield put({type: MC_SERVER_ERRORED, payload: true});

    } finally {
        yield put({type: MC_SERVER_PENDING, payload: false});
    }
}

export function* turnOffServerSagas(){
    try {
        yield put({type: MC_SERVER_PENDING, payload: true});
        yield call(turnServerOff);
        yield put({type: MC_SERVER_ON, payload: false});
        yield put({type: MC_SERVER_ERRORED, payload: false});

    } catch (error) {
        console.error('Sagas error with turning on server', error);
        yield put({type: MC_SERVER_ERRORED, payload: true});

    } finally {
        yield put({type: MC_SERVER_PENDING, payload: false});
    }
}

// saga watcher
export function* watchServerController(){
    yield takeLatest(TURN_ON_MC_SERVER, turnOnServerSagas)
    yield takeLatest(TURN_OFF_MC_SERVER, turnOffServerSagas)
}