import { useState, ChangeEvent, FormEvent } from 'react';
import TextField from '@mui/material/TextField';
import LayoutNew from '../../layoutnew';
import styles from './Login.module.css';


interface FormData {
  nome: string;
  sobrenome: string;
  email: string;
  senha: string;
  confirmarSenha: string;
}

export default function Login() {
  const [formData, setFormData] = useState<FormData>({
    nome: '',
    sobrenome: '',
    email: '',
    senha: '',
    confirmarSenha: ''
  });
  const [formSubmitted, setFormSubmitted] = useState(false);

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setFormSubmitted(true);

    if (formData.senha !== formData.confirmarSenha) {
      alert('As senhas não coincidem.');
      return;
    }


    console.log(formData);
  };

  return (
    <LayoutNew>
      <div className={styles.container}>
        <div className={styles.imagem}>
          <img src="/images/trampofinder.svg" alt="Logo" className={styles.logo} />
        </div>
        <form onSubmit={handleSubmit}>
          <div className={styles.form}>
            <span>
              <p>Email</p>
              <TextField
                required
                name="nome"
                value={formData.nome}
                onChange={handleChange}
                id="filled-required"
                variant="filled"
                className={styles.teste}
                size="small"
                error={formSubmitted && formData.nome.trim() === ''}
                helperText={formSubmitted && formData.nome.trim() === '' && 'Campo obrigatório'}
              />
            </span>
            <span>
              <p>Senha</p>
              <TextField
                required
                name="senha"
                value={formData.senha}
                onChange={handleChange}
                id="filled-password-input"
                type="password"
                autoComplete="new-password"
                variant="filled"
                className={styles.teste}
                size="small"
                error={formSubmitted && formData.senha.trim() === ''}
                helperText={formSubmitted && formData.senha.trim() === '' && 'Campo obrigatório'}
              />
            </span>
          </div>
          <div className={styles.buttonContainer}>
          <button type="submit" className={styles.button}>
          Cadastrar
        </button>
        </div>
        </form>
      </div>
    </LayoutNew>
  );
}
