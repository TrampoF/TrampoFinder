import {createBrowserRouter} from "react-router-dom";
import About from "../pages/About";
import Home from "../pages/Home";
import Dashboard from "../pages/Dashboard";
import Register from "../pages/Register";
import Login from "../pages/Login";
import RecoverAccount from "../pages/RecoverAccount";
import ChangePassword from "../pages/ChangePassword";
import Cadastro from "../pages/Cadastro/Cadastro.tsx";



const router = createBrowserRouter([
    {
        path: "",
        element: <Home/>
    },
    {
        path: "/app",
        element: <Dashboard/>
    },
    {
        path: "/about",
        element: <About/>
    },
    {

        path: "/register",
        element: <Register/>
    },
    {
        path: "/login",
        element: <Login/>
    },
    {
        path: "/recover",
        element: <RecoverAccount/>
    },
    {
        path: "/recover/changePassword",
        element: <ChangePassword/>
    },
    {

        path: "/cadastro",
        element: <Cadastro/>

    }
])

export default router