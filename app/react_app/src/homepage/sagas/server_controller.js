import { call, put, takeLatest } from 'redux-saga/effects';
import { turnOnServer, turnOffServer } from '../http_requests/server_controller'

import { serverOn, serverOff, serverErrored, serverPending } from '../actions/server_controller';

export const TURN_ON_MC_SERVER = 'TURN_ON_MC_SERVER_SAGAS';
export const TURN_OFF_MC_SERVER = 'TURN_OFF_MC_SERVER_SAGAS';

// todo: need to rename to better names...
export function* turnOnServerSagas(){
    try {
        yield put(serverPending, true)
        let turnOnRequest = yield call(serverOn)
        console.log('Turning on server... ', turnOnRequest)

    } catch (error) {
        console.error('Sagas error with turning on server', error)

    } finally {
        yield call(serverPending, false)
    }
}

export function* turnOffServerSagas(){
    try {
        yield call(serverOff, true)
        let turnOffRequest = yield call(serverOff)

    } catch (error) {
        console.error('Sagas error with turning on server', error)
        yield put()

    } finally {
        yield call(serverPending, false)
    }
}

// saga watcher
export function* watchServerController(){
    yield takeLatest(TURN_ON_MC_SERVER, turnOnServerSagas)
    yield takeLatest(TURN_OFF_MC_SERVER, turnOffServerSagas)
}