import React, {useState} from "react";
import Layout from "../../layout";
import styles from './Home.module.css';

const Home: React.FC = () => {
    return (
        
        <Layout>
            <section className={styles.container}>
            <div className={styles.img}>
            <img src="/images/home.svg" alt="Logo" width={520} className={styles.img} />
            </div>
            <div className={styles.text}>
                <p>Conecte - se as vagas mais atuais do mercado! </p>
            
            </div>
            </section>
        </Layout>
    );
};

export default Home;