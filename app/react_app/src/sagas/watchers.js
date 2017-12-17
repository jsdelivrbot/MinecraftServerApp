import { all } from 'redux-saga/effects';
import { watchServerController } from '../homepage/sagas/server_controller';

export default function* rootSaga(){
    yield all([
        watchServerController()
    ])
}
