import { useState } from "react";
import { scrapeURL } from "./api";

export default function ScraperUI() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleScrape() {
    setLoading(true);
    const data = await scrapeURL(url);
    setResult(data);
    setLoading(false);
  }

  return (
    <div style={{ margin: "40px", fontFamily: "sans-serif" }}>
      <h1 style={{ color: "#00AEEF" }}>🕷️ SIAG Advanced Scraper Demo</h1>

      <input
        type="text"
        placeholder="Enter website URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: "350px", padding: "8px" }}
      />

      <button
        onClick={handleScrape}
        style={{ marginLeft: "10px", padding: "10px" }}
      >
        Scrape
      </button>

      {loading && <p>⏳ Scraping…</p>}

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Results:</h3>
          <pre>{JSON.stringify(result.items, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
