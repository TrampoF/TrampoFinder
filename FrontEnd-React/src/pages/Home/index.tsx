import {api} from "../../api/config";
import React, {useState} from "react";

const Home: React.FC = () => {
    const [users, setUsers] = useState<string>('')
    api.get("").then(res => {
        console.log(res)
        setUsers(res.data)
    }).catch(err => {
        console.log(err)
    })
    return (
        <div>
            <h1>Home</h1>
            <p>{users}</p>
        </div>
    );
};

export default Home;