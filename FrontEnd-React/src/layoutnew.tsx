import React, { ReactNode } from 'react';
import NavbarNew from './components/NavbarNew/NavbarNew';

interface LayoutProps {
    children: ReactNode;
}

const LayoutNew: React.FC<LayoutProps> = ({ children }) => {
    return (
        <div>
           <NavbarNew/>
            <main>
                {children}
            </main>
           
        </div>
    );
};

export default LayoutNew;
