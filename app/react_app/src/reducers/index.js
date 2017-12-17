import { combineReducers } from 'redux';
import { serverStatusReducers } from '../homepage/reducers/index';


const rootReducer = combineReducers({
    serverStatus: serverStatusReducers
});

export default rootReducer;