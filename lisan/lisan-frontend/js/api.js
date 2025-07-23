const BASE_URL = "http://127.0.0.1:8000"; // Change this if deployed

export async function postData(endpoint, data, isFormData = false) {
  try {
    const res = await fetch(`${BASE_URL}${endpoint}`, {
      method: "POST",
      headers: isFormData ? {} : { "Content-Type": "application/json" },
      body: isFormData ? data : JSON.stringify(data),
    });

    return await res.json();
  } catch (error) {
    console.error("API Error:", error);
    alert("Something went wrong. Check console.");
  }
}
