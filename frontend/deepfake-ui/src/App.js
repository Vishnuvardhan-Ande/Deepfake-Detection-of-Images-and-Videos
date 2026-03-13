import React, { useState, useEffect, useRef } from "react";
import Webcam from "react-webcam";
import "./App.css";

function App() {

  // -------- Agent Core States --------
  const [agentState, setAgentState] = useState("Idle");
  const [agentOnline, setAgentOnline] = useState(false);
  const [reasoningSteps, setReasoningSteps] = useState([]);
  const [history, setHistory] = useState([]);

  // -------- Media & Result --------
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // -------- Modes --------
  const [webcamMode, setWebcamMode] = useState(false);
  const [autoScan, setAutoScan] = useState(false);

  const webcamRef = useRef(null);

  // -------- Health Check --------
  useEffect(() => {
    const checkHealth = async () => {
      try {
        const res = await fetch("http://localhost:8000/health");
        const data = await res.json();
        if (data.status === "online") setAgentOnline(true);
      } catch {
        setAgentOnline(false);
      }
    };

    checkHealth();
    const interval = setInterval(checkHealth, 5000);
    return () => clearInterval(interval);
  }, []);

  // -------- Agent Analysis Flow --------
  const runAgentFlow = async (formData) => {
    setLoading(true);
    setReasoningSteps([]);
    setAgentState("Scanning");

    setTimeout(() => {
      setAgentState("Analyzing");
      setReasoningSteps(prev => [...prev, "Extracting deep visual features"]);
    }, 500);

    setTimeout(() => {
      setAgentState("Evaluating Risk");
      setReasoningSteps(prev => [...prev, "Computing fake probability score"]);
    }, 1000);

    setTimeout(() => {
      setAgentState("Generating Explanation");
      setReasoningSteps(prev => [...prev, "Activating Grad-CAM heatmap"]);
    }, 1500);

    try {
      const response = await fetch("http://localhost:8000/analyze-image", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      setResult(data);
      setAgentState("Final Decision");

      // Update memory (last 5)
      setHistory(prev => {
        const updated = [data, ...prev];
        return updated.slice(0, 5);
      });

      // Autonomous Alert
      if (data.risk_level === "High Risk" && data.confidence > 0.9) {
        setAgentState("Alert Triggered");
        alert("⚠ HIGH RISK DEEPFAKE DETECTED!");
      }

    } catch {
      setAgentState("Error");
    }

    setLoading(false);
  };

  // -------- File Handling --------
  const handleFile = (selectedFile) => {
    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
  };

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    runAgentFlow(formData);
  };

  // -------- Webcam Capture --------
  const captureWebcam = async () => {
    const imageSrc = webcamRef.current.getScreenshot();
    const blob = await fetch(imageSrc).then(res => res.blob());
    const formData = new FormData();
    formData.append("file", blob, "webcam.jpg");
    runAgentFlow(formData);
  };

  // -------- Auto Scan Mode --------
  useEffect(() => {
    if (!autoScan) return;

    const interval = setInterval(() => {
      if (webcamRef.current) {
        captureWebcam();
      }
    }, 5000);

    return () => clearInterval(interval);
  }, [autoScan]);

  return (
    <div className="main-container">

      {/* Sidebar */}
      <aside className="sidebar">
        <h2>DeepVision Agent</h2>

        <div className={`status ${agentOnline ? "online" : "offline"}`}>
          <span className="dot" />
          {agentOnline ? "Agent Online" : "Agent Offline"}
        </div>

        <p className="state-display">
          <strong>State:</strong> {agentState}
        </p>

        <button onClick={() => setWebcamMode(false)}>Upload Mode</button>
        <button onClick={() => setWebcamMode(true)}>Webcam Mode</button>

        {webcamMode && (
          <button onClick={() => setAutoScan(!autoScan)}>
            {autoScan ? "Stop Auto Scan" : "Start Auto Scan"}
          </button>
        )}
      </aside>

      {/* Main Content */}
      <main className="content">

        <header className="header">
          <h1>Autonomous Deepfake Detection Agent</h1>
        </header>

        {/* interaction area */}
        <section className="interaction-section">
          {!webcamMode ? (
            <>
              <div className="upload-box">
                {preview ? (
                  <img src={preview} alt="preview" />
                ) : (
                  <p>Select an image to analyze</p>
                )}
                <label htmlFor="fileInput" className="file-label">
                  Choose File
                </label>
                <input
                  id="fileInput"
                  type="file"
                  onChange={(e) => handleFile(e.target.files[0])}
                />
              </div>

              <button
                className="analyze-btn"
                onClick={handleUpload}
                disabled={loading}
                aria-busy={loading}
              >
                Analyze Image
              </button>
            </>
          ) : (
            <>
              <Webcam
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                width="400"
              />
              <button
                className="analyze-btn"
                onClick={captureWebcam}
                disabled={loading}
                aria-busy={loading}
              >
                Capture & Analyze
              </button>
            </>
          )}
        </section>

        {loading && <div className="loader" />}

        {result && (
          <div className="result-panel">
            <h2>Prediction: {result.prediction}</h2>
            <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
            <p className="risk">{result.risk_level}</p>
            <p>{result.explanation}</p>
          </div>
        )}

        <div className="bottom-panels">
          {/* Reasoning Panel */}
          <div className="reasoning-panel">
            <h3>Agent Reasoning</h3>
            {reasoningSteps.map((step, index) => (
              <p key={index}>➜ {step}</p>
            ))}
          </div>

          {/* Memory Panel */}
          <div className="memory-panel">
            <h3>Recent Analyses</h3>
            {history.map((item, index) => (
              <p key={index}>
                {item.prediction} - {(item.confidence * 100).toFixed(2)}%
              </p>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;