import React, { ReactNode } from 'react';
import styles from './Form.module.css';

interface FormProps {
    children: ReactNode;
}

const Form: React.FC<FormProps> = ({ children }) => {
    return (
        <section className={styles.form}>
            <div className={styles.container}>
                {children}
            </div>
        </section>
    );
};

export default Form;
