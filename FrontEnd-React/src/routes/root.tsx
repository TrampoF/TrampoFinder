import {createBrowserRouter} from "react-router-dom";
import Home from "../pages/Home/Home.tsx";
import About from "../pages/About/About.tsx";
import Cadastro from "../pages/Cadastro/Cadastro.tsx";
import Login from "../pages/Login/Login.tsx";


const router = createBrowserRouter([
    {
        path: "/",
        element: <Home/>
    },
    {
        path: "/about",
        element: <About/>
    },
    {
        path: "/cadastro",
        element: <Cadastro/>
        
    },
    {
        path: "/login",
        element: <Login/>
        
    }
])

export default router