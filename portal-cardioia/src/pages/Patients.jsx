import { useEffect, useState } from "react";
import { fetchPatients } from "../services/api";
import styles from "../styles/Portal.module.css";

export default function Patients() {
  const [patients, setPatients] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchPatients()
      .then(setPatients)
      .catch((reason) => setError(reason.message))
      .finally(() => setLoading(false));
  }, []);

  const filtered = patients.filter((patient) =>
    patient.name.toLowerCase().includes(query.toLowerCase()),
  );

  return (
    <>
      <header className={styles.pageHeader}>
        <div><span>Base simulada</span><h2>Pacientes</h2></div>
        <p>Nenhum registro representa uma pessoa real.</p>
      </header>
      <section className={styles.contentCard}>
        <label className={styles.searchLabel}>
          Buscar paciente
          <input value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Digite um nome" />
        </label>
        {loading && <p>Carregando...</p>}
        {error && <p className={styles.error} role="alert">{error}</p>}
        <div className={styles.patientGrid}>
          {filtered.map((patient) => (
            <article className={styles.patientCard} key={patient.id}>
              <div className={styles.avatar}>{patient.name.charAt(0)}</div>
              <div>
                <h3>{patient.name}</h3>
                <p>{patient.age} anos • {patient.status}</p>
                <small>Última consulta: {patient.lastVisit}</small>
              </div>
            </article>
          ))}
        </div>
      </section>
    </>
  );
}
