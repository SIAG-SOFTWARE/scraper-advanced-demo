export async function scrapeURL(url) {
  const res = await fetch("http://localhost:8000/scrape/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url }),
  });

  return res.json();
}
