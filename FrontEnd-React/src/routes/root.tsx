import {createBrowserRouter} from "react-router-dom";
import About from "../pages/About";
import Home from "../pages/Home";
import LandingPage from "../pages/LandingPage";
import Register from "../pages/Register";
import Login from "../pages/Login";
import RecoverAccount from "../pages/RecoverAccount";
import ChangePassword from "../pages/ChangePassword";

const router = createBrowserRouter([
    {
        path: "",
        element: <LandingPage/>
    },
    {
        path: "/app",
        element: <Home/>
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
    }
])

export default router