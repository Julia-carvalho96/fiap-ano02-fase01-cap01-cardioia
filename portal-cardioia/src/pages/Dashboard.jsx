import { useEffect, useState } from "react";
import StatCard from "../components/StatCard";
import { fetchPatients } from "../services/api";
import styles from "../styles/Portal.module.css";

export default function Dashboard() {
  const [patients, setPatients] = useState([]);
  const [error, setError] = useState("");
  const appointments = JSON.parse(localStorage.getItem("cardioia_appointments") || "[]");

  useEffect(() => {
    fetchPatients().then(setPatients).catch((reason) => setError(reason.message));
  }, []);

  const priorities = patients.filter((patient) => patient.status === "Prioridade").length;

  return (
    <>
      <header className={styles.pageHeader}>
        <div><span>Visão geral</span><h2>Dashboard</h2></div>
        <p>Indicadores simulados da rotina cardiológica.</p>
      </header>
      {error && <p className={styles.error} role="alert">{error}</p>}
      <section className={styles.statsGrid}>
        <StatCard label="Pacientes" value={patients.length} detail="Cadastros simulados" />
        <StatCard label="Consultas" value={appointments.length} detail="Agendamentos locais" />
        <StatCard label="Prioridades" value={priorities} detail="Marcadores demonstrativos" />
      </section>
      <section className={styles.contentCard}>
        <h3>Próximas etapas do portal</h3>
        <p>
          Este front não usa prontuários reais nem back-end. Ele demonstra Context API,
          Hooks, rotas protegidas, consumo de JSON e controle de estado.
        </p>
      </section>
    </>
  );
}
