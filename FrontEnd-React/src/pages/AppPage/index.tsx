import React from "react";
import LayoutDash from "../../layoutdash";
import styles from './AppPage.module.css';

const AppPage: React.FC = () => {
    return (
        <LayoutDash>
            <section className="">
                <div className={styles.container}>
                    <div className="">
                        <img src="/images/home.svg" alt="Logo" width={300} className={styles.img} />
                    </div>
                    <div className="">
                        <h1 className={styles.titulo}>Cadastre um aplicativo pra ficar por dentro das mais novas oportunidades!</h1>
                    </div>
                    <div className={styles.container_heading}>
                        <h1 className={styles.heading}>Aplicativos disponíveis:</h1>
                    </div>
                    <div className={styles.container_card}>
                        <div className={styles.card}>
                            <div className={styles.flex}>
                                <img src="/images/home.svg" alt="Logo" width={75} className={styles.img} />
                                <h1>Telegram</h1>
                            </div>
                            <p>Aplicativo de mensagem instantâneas</p>
                            <button>Cadastrar</button>
                        </div>
                        <div className={styles.card}>
                            <div className={styles.flex}>
                                <img src="/images/home.svg" alt="Logo" width={75} className={styles.img} />
                                <h1>Linkedin</h1>
                            </div>
                            <p>Aplicativo de portal de vagas e rede social</p>
                            <button>Cadastrar</button>
                        </div>
                    </div>
                </div>
            
            </section>
        </LayoutDash>
    );
};

export default AppPage;
