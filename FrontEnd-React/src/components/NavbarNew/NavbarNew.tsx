import styles from './NavbarNew.module.css';


const NavbarNew: React.FC = () => {
    return (
        <nav className={styles.nav}>
            <div className={styles.imagem}>
              <a href='/'>
                <img src="/images/trampofinder.svg" alt="Logo" className={styles.logo} />
                </a>
              
            </div>
        </nav>
    );
};

export default NavbarNew;
