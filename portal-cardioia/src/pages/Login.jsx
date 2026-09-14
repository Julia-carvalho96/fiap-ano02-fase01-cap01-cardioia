import { useState } from "react";
import { Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import styles from "../styles/Portal.module.css";

export default function Login() {
  const { isAuthenticated, login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState("cardioia@fiap.com");
  const [password, setPassword] = useState("aura2026");
  const [error, setError] = useState("");

  if (isAuthenticated) return <Navigate to="/" replace />;

  function handleSubmit(event) {
    event.preventDefault();
    const result = login(email, password);
    if (!result.success) return setError(result.message);
    navigate("/");
  }

  return (
    <main className={styles.loginPage}>
      <section className={styles.loginCard}>
        <span className={styles.badge}>Protótipo acadêmico</span>
        <h1>Entrar no CardioIA</h1>
        <p>Use as credenciais de demonstração já preenchidas.</p>
        <form onSubmit={handleSubmit}>
          <label>
            E-mail
            <input value={email} onChange={(event) => setEmail(event.target.value)} type="email" />
          </label>
          <label>
            Senha
            <input value={password} onChange={(event) => setPassword(event.target.value)} type="password" />
          </label>
          {error && <p className={styles.error} role="alert">{error}</p>}
          <button className={styles.primaryButton} type="submit">Entrar</button>
        </form>
        <small>JWT fictício armazenado apenas no localStorage.</small>
      </section>
    </main>
  );
}
