import { useState } from 'react';

const API_URL = (import.meta.env.VITE_API_URL || 'http://localhost:8000').replace(/\/$/, '');

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [dragActive, setDragActive] = useState(false);

  const handleFile = async (selectedFile) => {
    if (!selectedFile) return;

    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
    setResult(null);
    setError('');
    setLoading(true);

    const formData = new FormData();
    formData.append('file', selectedFile);

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
      setError('Unable to get prediction. Please ensure the backend is running on port 8000.');
    } finally {
      setLoading(false);
    }
  };

  const handleInput = (event) => {
    handleFile(event.target.files?.[0]);
  };

  const handleDrop = (event) => {
    event.preventDefault();
    setDragActive(false);
    handleFile(event.dataTransfer.files?.[0]);
  };

  const displayLabel = result?.label === 'flood' ? 'Flood detected' : 'No flood detected';

  return (
    <div className="page-shell">
      <div className="app-card">
        <header className="hero-section">
          <div>
            <p className="eyebrow">Flood Detection Assistant</p>
            <h1>Upload an image and classify it in seconds.</h1>
            <p className="hero-text">
              This interface sends your image to the backend model and returns a clear flood prediction result.
            </p>
          </div>
          <div className="status-pill">Live • AI inference</div>
        </header>

        <div className="content-grid">
          <section
            className={`upload-card ${dragActive ? 'drag-active' : ''}`}
            onDragOver={(event) => {
              event.preventDefault();
              setDragActive(true);
            }}
            onDragLeave={() => setDragActive(false)}
            onDrop={handleDrop}
          >
            <input id="image-upload" type="file" accept="image/*" onChange={handleInput} />
            <label htmlFor="image-upload" className="drop-zone">
              <span className="drop-icon">⬆</span>
              <strong>Drop your image here</strong>
              <span>or click to browse</span>
            </label>
            <p className="hint">Supported formats: JPG, JPEG, PNG, WEBP</p>
            {file && <p className="file-name">Selected file: {file.name}</p>}
          </section>

          <section className="preview-card">
            {preview ? (
              <img src={preview} alt="Uploaded preview" />
            ) : (
              <div className="placeholder">
                <p>Your uploaded image will appear here.</p>
              </div>
            )}
          </section>
        </div>

        <section className="result-card">
          {loading && <div className="loading">Analyzing image…</div>}
          {error && <div className="error-box">{error}</div>}
          {result && (
            <>
              <div className="result-top">
                <span className={`badge ${result.label === 'flood' ? 'danger' : 'safe'}`}>{displayLabel}</span>
                <span className="confidence">Confidence: {result.confidence}</span>
              </div>
              <h2>Classification result</h2>
              <p>{result.message}</p>
              <div className="meta-row">Model mode: {result.model_type}</div>
              {result.model_type === 'heuristic' && (
                <div className="meta-row">Tip: place a trained model in the models folder to switch from fallback mode to real inference.</div>
              )}
            </>
          )}
          {!loading && !result && !error && (
            <div className="empty-state">Upload an image to see the classification result here.</div>
          )}
        </section>
      </div>
    </div>
  );
}

export default App;
