import { useState } from "react";

function DiseaseDetection() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];

    if (!selectedFile) {
      return;
    }

    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
    setResult(null);
    setError("");
  };

  const detectDisease = async () => {
    if (!file) {
      setError("Please select a plant leaf image first.");
      return;
    }

    setLoading(true);
    setResult(null);
    setError("");

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(
        "http://127.0.0.1:8000/disease/predict",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        throw new Error("Disease detection request failed.");
      }

      const data = await response.json();

      setResult(data);
    } catch (err) {
      console.error(err);
      setError(
        "Unable to connect to the AI server. Please make sure the backend is running."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="disease-page">

      {/* Hero */}
      <section className="disease-hero">
        <div className="disease-hero-content">

          <div className="disease-badge">
            🌿 AI POWERED AGRICULTURE
          </div>

          <h1>
            Plant Disease
            <span> Detection</span>
          </h1>

          <p>
            Upload a clear image of a plant leaf and let our trained
            AI model identify possible crop diseases.
          </p>

          <div className="disease-trust">
            <span>✓</span>
            Powered by EfficientNet-B0
          </div>

        </div>

        <div className="disease-hero-icon">
          🌱
        </div>
      </section>


      {/* Main Detection Area */}
      <section className="disease-workspace">

        {/* Upload Card */}
        <div className="upload-card">

          <div className="section-mini-label">
            IMAGE ANALYSIS
          </div>

          <h2>Upload Plant Leaf</h2>

          <p className="upload-description">
            Select a JPG or PNG image of a plant leaf for AI analysis.
          </p>

          <label className="upload-box">

            {preview ? (
              <img
                src={preview}
                alt="Selected plant leaf"
                className="leaf-preview"
              />
            ) : (
              <>
                <div className="upload-icon">
                  📷
                </div>

                <strong>
                  Choose a leaf image
                </strong>

                <span>
                  JPG or PNG • Clear leaf images work best
                </span>
              </>
            )}

            <input
              type="file"
              accept="image/jpeg,image/png,image/jpg"
              onChange={handleFileChange}
            />

          </label>

          {file && (
            <div className="selected-file">
              <span>📄</span>
              <div>
                <strong>{file.name}</strong>
                <small>
                  Image ready for AI analysis
                </small>
              </div>
            </div>
          )}

          <button
            className="analyze-button"
            onClick={detectDisease}
            disabled={!file || loading}
          >
            {loading ? (
              <>
                <span className="spinner"></span>
                Analyzing Leaf...
              </>
            ) : (
              <>
                🔬 Analyze Leaf
              </>
            )}
          </button>

          {error && (
            <div className="disease-error">
              ⚠️ {error}
            </div>
          )}

        </div>


        {/* Result Card */}
        <div className="result-card">

          <div className="section-mini-label">
            AI DIAGNOSIS
          </div>

          <h2>Detection Result</h2>

          {!result && !loading && (
            <div className="empty-result">

              <div className="empty-result-icon">
                🤖
              </div>

              <h3>Ready to analyze</h3>

              <p>
                Upload a plant leaf image and click
                <strong> Analyze Leaf </strong>
                to receive an AI prediction.
              </p>

            </div>
          )}

          {loading && (
            <div className="empty-result">

              <div className="ai-loading-icon">
                🔬
              </div>

              <h3>AI is analyzing...</h3>

              <p>
                Your image is being processed by the trained
                disease detection model.
              </p>

            </div>
          )}

          {result && (
            <div className="prediction-result">

              <div className="prediction-icon">
                🌿
              </div>

              <span className="prediction-label">
                DETECTED CONDITION
              </span>

              <h3>
                {result.disease}
              </h3>

              <div className="confidence-section">

                <div className="confidence-header">
                  <span>AI Confidence</span>

                  <strong>
                    {result.confidence}%
                  </strong>
                </div>

                <div className="confidence-bar">
                  <div
                    className="confidence-fill"
                    style={{
                      width: `${Math.min(
                        Number(result.confidence),
                        100
                      )}%`,
                    }}
                  ></div>
                </div>

              </div>

              <div className="prediction-message">
                ✓ {result.message}
              </div>

              <div className="prediction-note">
                <strong>AI Model:</strong> EfficientNet-B0
                <br />
                <strong>Classes:</strong> 38 plant disease categories
              </div>

            </div>
          )}

        </div>

      </section>


      {/* Information Cards */}
      <section className="disease-info-grid">

        <div className="disease-info-card">
          <div>🤖</div>
          <h3>AI Powered</h3>
          <p>
            Uses your trained EfficientNet-B0 model
            for plant disease classification.
          </p>
        </div>

        <div className="disease-info-card">
          <div>🌱</div>
          <h3>38 Categories</h3>
          <p>
            The model was trained to recognize
            38 plant health categories.
          </p>
        </div>

        <div className="disease-info-card">
          <div>⚡</div>
          <h3>Fast Analysis</h3>
          <p>
            Upload an image and receive the prediction
            directly from your local AI backend.
          </p>
        </div>

      </section>

    </main>
  );
}

export default DiseaseDetection;