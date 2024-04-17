import React from 'react';
import styles from './Navbar.module.css';

const Navbar: React.FC = () => {
    return (
        <nav className={styles.nav}>
            <div className={styles.imagem}>
                <img src="/images/trampofinder.svg" alt="Logo" width={210} className={styles.logo} />
            </div>
            <div className={styles.navend}>
                <a href="/login" className={styles.link}>Login</a>
                <a href="/cadastro" className={styles.link}>Cadastro</a>
            </div>
        </nav>
    );
};

export default Navbar;
