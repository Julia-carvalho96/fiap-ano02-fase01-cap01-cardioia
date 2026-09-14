import "@testing-library/jest-dom/vitest";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { MemoryRouter } from "react-router-dom";
import App from "./App";
import { AuthProvider } from "./contexts/AuthContext";

function renderPortal(route = "/") {
  return render(
    <MemoryRouter initialEntries={[route]}>
      <AuthProvider>
        <App />
      </AuthProvider>
    </MemoryRouter>,
  );
}

describe("CardioIA Portal", () => {
  beforeEach(() => {
    localStorage.clear();
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => [
          { id: 1, name: "Paciente Teste", age: 50, status: "Estável", lastVisit: "01/09/2026" },
        ],
      }),
    );
  });

  it("protege as rotas e permite login com credenciais simuladas", async () => {
    renderPortal("/");
    expect(await screen.findByText("Entrar no CardioIA")).toBeInTheDocument();

    fireEvent.click(screen.getByRole("button", { name: "Entrar" }));

    expect(await screen.findByRole("heading", { name: "Dashboard" })).toBeInTheDocument();
    await waitFor(() => expect(screen.getByText("1")).toBeInTheDocument());
    expect(localStorage.getItem("cardioia_fake_jwt")).toBeTruthy();
  });

  it("rejeita credenciais diferentes das credenciais demonstrativas", async () => {
    renderPortal("/login");
    fireEvent.change(screen.getByLabelText("E-mail"), {
      target: { value: "invalido@exemplo.com" },
    });
    fireEvent.click(screen.getByRole("button", { name: "Entrar" }));
    expect(await screen.findByRole("alert")).toHaveTextContent(
      "E-mail ou senha de demonstração inválidos.",
    );
  });
});
