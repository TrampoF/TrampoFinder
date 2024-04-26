// Navbar.tsx
import { Link } from 'react-router-dom';
import React, { useState } from 'react';
import styles from './Navbar.module.css';
import { GiHamburgerMenu } from 'react-icons/gi';

const Navbar: React.FC = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    return (
        <nav className={styles.nav}>
            <div className={styles.imagem}>
              <a href='/'>
                <img src="/images/trampofinder.svg" alt="Logo" className={styles.logo} />
                </a>
              
            </div>
            <div className={styles.navend}>
                <div className={styles.menuIcon} onClick={toggleMenu}>
                    <GiHamburgerMenu />
                    <div className={`${styles.menuItems} ${isMenuOpen ? styles.open : ''}`}>
                        <a href="/login" className={styles.link}>Login</a>
                        <a href="/cadastro" className={styles.link}>Cadastro</a>
                    </div>
                </div>
                <div className={styles.linksDesktop}>
                    <a href="/login" className={styles.link}>Login</a>
                    <a href="/cadastro" className={styles.link}>Cadastro</a>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
