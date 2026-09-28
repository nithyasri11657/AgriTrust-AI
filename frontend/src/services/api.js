const API_URL = "http://127.0.0.1:8000";

export async function predictDisease(imageFile) {
  const formData = new FormData();
  formData.append("file", imageFile);

  const response = await fetch(`${API_URL}/disease/predict`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Disease detection failed");
  }

  return await response.json();
}

export async function sendSensorData(sensorData) {
  const response = await fetch(`${API_URL}/sensor/data`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(sensorData),
  });

  if (!response.ok) {
    throw new Error("Sensor data submission failed");
  }

  return await response.json();
}