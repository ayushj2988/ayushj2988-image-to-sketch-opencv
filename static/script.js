console.log("script.js loaded");
const uploadBox = document.getElementById("uploadBox");
const input = document.getElementById("imageInput");
const preview = document.getElementById("previewImg");
const result = document.getElementById("resultImg");
const statusText = document.getElementById("statusText");
const convertBtn = document.getElementById("convertBtn");

// Open file picker
uploadBox.addEventListener("click", () => {
  input.click();
});

// Show preview
input.addEventListener("change", () => {
  const file = input.files[0];
  if (!file) return;

  preview.src = URL.createObjectURL(file);
  preview.classList.remove("hidden");
  statusText.textContent = "Image selected.";
});

// Send to Flask
convertBtn.addEventListener("click", async () => {
  if (!input.files[0]) {
    statusText.textContent = "Please upload an image first.";
    return;
  }

  statusText.textContent = "Processing...";
  convertBtn.disabled = true;

  const formData = new FormData();
  formData.append("image", input.files[0]);

  try {
    const res = await fetch("/sketch", {
      method: "POST",
      body: formData
    });

    if (!res.ok) throw new Error("Server error");

    const blob = await res.blob();
    result.src = URL.createObjectURL(blob);
    result.classList.remove("hidden");
    statusText.textContent = "Done!";
  } catch (err) {
    console.error(err);
    statusText.textContent = "Error: Conversion failed";
  } finally {
    convertBtn.disabled = false;
  }
});
