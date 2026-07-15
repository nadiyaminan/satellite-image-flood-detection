import { useState } from 'react';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleUpload = async (event) => {
    const selected = event.target.files?.[0];
    if (!selected) return;

    setFile(selected);
    setPreview(URL.createObjectURL(selected));
    setResult(null);
    setError('');
    setLoading(true);

    const formData = new FormData();
    formData.append('file', selected);

    try {
      const response = await fetch(`${API_URL}/predict`, {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error('Prediction failed');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError('Unable to get prediction. Make sure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <section className="hero-card">
        <div className="hero-copy">
          <p className="eyebrow">AI Flood Detection</p>
          <h1>Detect flood risk from satellite-style imagery in seconds.</h1>
          <p className="hero-text">
            Upload an image to run inference using your trained model or the built-in fallback engine.
          </p>
          <label className="upload-button">
            <input type="file" accept="image/*" onChange={handleUpload} />
            Choose image
          </label>
        </div>

        <div className="preview-panel">
          {preview ? (
            <img src={preview} alt="Uploaded preview" />
          ) : (
            <div className="empty-state">No image selected yet</div>
          )}
        </div>
      </section>

      <section className="result-card">
        {loading && <p>Running inference...</p>}
        {error && <p className="error">{error}</p>}
        {result && (
          <>
            <h2>Prediction result</h2>
            <div className="pill-row">
              <span className={`pill ${result.label === 'flood' ? 'danger' : 'safe'}`}>{result.label}</span>
              <span className="pill neutral">Confidence: {result.confidence}</span>
            </div>
            <p>{result.message}</p>
            <p className="meta">Model mode: {result.model_type}</p>
          </>
        )}
      </section>
    </div>
  );
}

export default App;
