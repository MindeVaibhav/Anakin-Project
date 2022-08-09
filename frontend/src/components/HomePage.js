import React, { Component } from 'react';
import RoomJoinPage from './RoomJoinPage';
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from 'react-router-dom';

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
                <Routes>
                    <Route exact path='/'><p>This is base route</p></Route>
                    {/* <Route path='sign_in' Component={RoomJoinPage}></Route> */}
                </Routes>
            </Router>
        )
    }
}