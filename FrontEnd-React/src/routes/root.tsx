import {createBrowserRouter} from "react-router-dom";
import Home from "../pages/Home/Home.tsx";
import About from "../pages/About/About.tsx";
import Cadastro from "../pages/Cadastro/Cadastro.tsx";


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
    }
])

export default router