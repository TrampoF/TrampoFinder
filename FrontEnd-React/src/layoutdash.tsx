import React, { ReactNode } from 'react';
import MainNavBar from "./components/MainNavBar"

interface LayoutProps {
    children: ReactNode;
}

const LayoutDash: React.FC<LayoutProps> = ({ children }) => {
    return (
        <div>
            <MainNavBar />
            <main>
                {children}
            </main>
        </div>
    );
};

export default LayoutDash;

