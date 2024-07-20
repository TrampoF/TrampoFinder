import { useState, ChangeEvent, FormEvent } from 'react';
import TextField from '@mui/material/TextField';
import Layout from '../../layout';
import styles from './Cadastro.module.css';


interface FormData {
  nome: string;
  sobrenome: string;
  email: string;
  senha: string;
  confirmarSenha: string;
}

export default function Cadastro() {
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

    // Verificação de senha e confirmação de senha
    if (formData.senha !== formData.confirmarSenha) {
      alert('As senhas não coincidem.');
      return;
    }
    console.log(formData);
  };

  return (
    <Layout>
      <div className={styles.container}>
        <div>
          <h1 className={styles.title}>Cadastro</h1>
        </div>

        <form onSubmit={handleSubmit}>
          <div className={styles.form}>
          <span>
            <p>Nome*</p>
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
            <p>Sobrenome*</p>
            <TextField
              required
              name="sobrenome"
              value={formData.sobrenome}
              onChange={handleChange}
              id="filled-required"
              variant="filled"
              className={styles.teste}
              size="small"
              error={formSubmitted && formData.sobrenome.trim() === ''}
              helperText={formSubmitted && formData.sobrenome.trim() === '' && 'Campo obrigatório'}
            />
          </span>
          <span>
            <p>Email*</p>
            <TextField
              required
              name="email"
              value={formData.email}
              onChange={handleChange}
              id="filled-required"
              variant="filled"
              className={styles.teste}
              size="small"
              error={formSubmitted && formData.email.trim() === ''}
              helperText={formSubmitted && formData.email.trim() === '' && 'Campo obrigatório'}
            />
          </span>
          <span>
            <p>Senha*</p>
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
          <span>
            <p>Confirmar senha*</p>
            <TextField
              required
              name="confirmarSenha"
              value={formData.confirmarSenha}
              onChange={handleChange}
              id="filled-password-input"
              type="password"
              autoComplete="new-password"
              variant="filled"
              className={styles.teste}
              size="small"
              error={formSubmitted && formData.confirmarSenha.trim() === ''}
              helperText={formSubmitted && formData.confirmarSenha.trim() === '' && 'Campo obrigatório'}
            />
          </span>
          </div>
          <button type="submit" className={styles.button}>
              Cadastrar
            </button>
        </form>
      </div>
    </Layout>
  );
}
