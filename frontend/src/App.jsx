import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import DiseaseDetection from "./pages/DiseaseDetection";
import "./App.css";

function App() {
  const [page, setPage] = useState("dashboard");

  return (
    <div className="app">
      {/* Navigation */}
      <header className="navbar">
        <div className="brand" onClick={() => setPage("dashboard")}>
          <div className="brand-icon">🌱</div>

          <div>
            <div className="brand-name">AgriTrust AI</div>
            <div className="brand-tagline">Smart Agriculture Platform</div>
          </div>
        </div>

        <nav className="nav-links">
          <button
            className={page === "dashboard" ? "nav-button active" : "nav-button"}
            onClick={() => setPage("dashboard")}
          >
            Dashboard
          </button>

          <button
            className={page === "disease" ? "nav-button active" : "nav-button"}
            onClick={() => setPage("disease")}
          >
            Disease Detection
          </button>
        </nav>

        <div className="nav-status">
          <span className="status-dot"></span>
          AI System Online
        </div>
      </header>

      {/* Main content */}
      <main className="main-content">
        {page === "dashboard" && <Dashboard setPage={setPage} />}
        {page === "disease" && <DiseaseDetection />}
      </main>

      {/* Footer */}
      <footer className="footer">
        <div>
          <strong>🌱 AgriTrust AI</strong>
          <span> — Intelligent technology for smarter farming</span>
        </div>

        <div className="footer-right">
          AI-powered • Smart Agriculture
        </div>
      </footer>
    </div>
  );
}

export default App;