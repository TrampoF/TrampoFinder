import React from "react";
import Layout from "../../layout";
import styles from './Home.module.css';
import { Link } from "react-router-dom";

const Home: React.FC = () => {
    return (
        <Layout>
            <section className={styles.container}>
                <div className={styles.img}>
                    <img src="/images/home.svg" alt="Logo" width={520} className={styles.img} />
                </div>
                <div className={styles.text}>
                    <p>Conecte-se às vagas mais atuais do mercado!</p>
                </div>
                <div>
                    <a href="/app" className={`${styles.link} ${styles.callToAction}`}>
                        Comece já!
                    </a>
                </div>
            </section>
        </Layout>
    );
};

export default Home;
