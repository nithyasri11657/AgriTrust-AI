function Dashboard({ setPage }) {
  const goToDisease = () => {
    setPage("disease");
  };

  const goToSensors = () => {
    document.getElementById("sensor-section")?.scrollIntoView({
      behavior: "smooth",
    });
  };

  const goToAI = () => {
  document.getElementById("recommendation-section")?.scrollIntoView({
    behavior: "smooth",
  });
};

  return (
    <main className="dashboard-page">

      {/* HERO */}
      <section className="hero-section">
        <div className="hero-content">
          <span className="eyebrow">🌱 SMART FARMING TECHNOLOGY</span>

          <h1>
            Grow Smarter.
            <br />
            <span>Farm Better.</span>
          </h1>

          <p>
            AgriTrust AI combines artificial intelligence and smart agriculture
            technology to help farmers monitor crops, detect diseases, and make
            better farming decisions.
          </p>

          <div className="hero-buttons">
            <button className="primary-button" onClick={goToDisease}>
              🌱 Start Crop Analysis →
            </button>

            <button className="secondary-button" onClick={goToSensors}>
              📊 View Farm Insights
            </button>
          </div>
        </div>

        <div className="hero-visual">
          <div className="plant-circle">🌱</div>

          <div className="floating-card ai-card">
            🔬
            <div>
              <strong>AI Detection</strong>
              <small>Ready to analyze</small>
            </div>
          </div>

          <div className="floating-card sensor-card">
            🌡️
            <div>
              <strong>Farm Monitor</strong>
              <small>Systems active</small>
            </div>
          </div>
        </div>
      </section>

      {/* SENSOR OVERVIEW */}
      <section id="sensor-section" className="dashboard-section">
        <div className="section-heading">
          <div>
            <span className="eyebrow">FARM OVERVIEW</span>
            <h2>Smart insights for your crops</h2>
          </div>

          <span className="status-badge">● All systems operational</span>
        </div>

        <div className="sensor-grid">

          <div className="sensor-card">
            <span className="sensor-icon">🌡️</span>
            <span>Temperature</span>
            <strong>28.5°C</strong>
            <small>Optimal range</small>
          </div>

          <div className="sensor-card">
            <span className="sensor-icon">💧</span>
            <span>Humidity</span>
            <strong>65%</strong>
            <small>Healthy level</small>
          </div>

          <div className="sensor-card">
            <span className="sensor-icon">🌱</span>
            <span>Soil Moisture</span>
            <strong>42%</strong>
            <small>Moderate moisture</small>
          </div>

          <div className="sensor-card">
            <span className="sensor-icon">🧪</span>
            <span>Soil pH</span>
            <strong>6.5</strong>
            <small>Suitable for crops</small>
          </div>

        </div>
      </section>

      {/* MAIN FEATURES */}
      <section className="feature-grid">

        <div className="feature-card">
          <div className="feature-icon">🔬</div>

          <span className="eyebrow">AI POWERED</span>

          <h2>Plant Disease Detection</h2>

          <p>
            Upload a plant leaf image and let our trained AI model identify
            possible crop diseases.
          </p>

          <button className="primary-button" onClick={goToDisease}>
            Analyze Plant →
          </button>
        </div>

        <div className="feature-card">
          <div className="feature-icon">📡</div>

          <span className="eyebrow">LIVE MONITORING</span>

          <h2>Farm Sensor Insights</h2>

          <p>
            Monitor environmental and soil conditions to understand your
            farm's current health.
          </p>

          <button className="primary-button" onClick={goToSensors}>
            View Sensors →
          </button>
        </div>

      </section>

      {/* AI SECTION */}
      <section id="ai-section" className="ai-banner">

        <div className="feature-icon dark">🤖</div>

        <div>
          <span className="eyebrow light">AI FARM ASSISTANT</span>

          <h2>Intelligent recommendations for your farm</h2>

          <p>
            AgriTrust AI can use crop health and environmental information
            to support smarter agricultural decisions.
          </p>
        </div>

        <button className="light-button" onClick={goToAI}>
          Explore AI →
        </button>

      </section>

      {/* TECHNOLOGY */}
      <section className="technology-section">

        <div>
          <span className="eyebrow">POWERED BY AI</span>

          <h2>Technology built for modern agriculture</h2>
        </div>

        <div className="technology-grid">

          <div>
            🤖
            <strong>AI</strong>
            <small>Plant disease analysis</small>
          </div>

          <div>
            📡
            <strong>IoT</strong>
            <small>Farm sensor monitoring</small>
          </div>

          <div>
            📊
            <strong>Analytics</strong>
            <small>Actionable farm insights</small>
          </div>

        </div>

      </section>

      {/* AI RECOMMENDATIONS */}
      <section id="recommendation-section" className="recommendation-section">

        <span className="eyebrow">AI FARM ASSISTANT</span>

        <h2>Smart recommendations</h2>

        <div className="recommendation-grid">

          <div className="recommendation-card">
            💧
            <h3>Irrigation</h3>
            <p>
              Current soil moisture is 42%. Monitor moisture levels regularly.
            </p>
          </div>

          <div className="recommendation-card">
            🌱
            <h3>Crop Health</h3>
            <p>
              Use Disease Detection to analyze suspicious leaf symptoms.
            </p>
          </div>

          <div className="recommendation-card">
            🧪
            <h3>Soil Condition</h3>
            <p>
              Current soil pH is 6.5 and is marked as suitable for crops.
            </p>
          </div>

        </div>

      </section>

    </main>
  );
}

export default Dashboard;