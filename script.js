// part 1)making the slider in html change default no according to the user 
const sliders = [
    "programming",
    "problemSolving",
    "analyticalThinking",
    "mathematics",
    "creativity",
    "communication",
    "designInterest",
    "technicalInterest",
    "teamwork",
    "attentionToDetail"
];
// for making the default no that is displaying change with the user input number 
sliders.forEach(function (sliderName) {
    const slider = document.getElementById(sliderName);
    const value = document.getElementById(sliderName + "Value");
    slider.addEventListener("input", function () {
        value.textContent = slider.value;
    });
});

// part 2)making the button function properly 
const form = document.getElementById("careerForm");
const result = document.getElementById("result");


form.addEventListener("submit", async function (event) {
    // Stop the page from refreshing
    event.preventDefault();

    // Collecting  user input
    const userData = {
        "Programming": Number(document.getElementById("programming").value),
        "Problem Solving": Number(document.getElementById("problemSolving").value),
        "Analytical Thinking": Number(document.getElementById("analyticalThinking").value),
        "Mathematics": Number(document.getElementById("mathematics").value),
        "Creativity": Number(document.getElementById("creativity").value),
        "Communication": Number(document.getElementById("communication").value),
        "Design Interest": Number(document.getElementById("designInterest").value),
        "Technical Interest": Number(document.getElementById("technicalInterest").value),
        "Teamwork": Number(document.getElementById("teamwork").value),
        "Attention to Detail": Number(document.getElementById("attentionToDetail").value)
    };

    // Send data to Flask
    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        // convert python data into json format
        body: JSON.stringify(userData)
    });

    // Receive response from Flask
    const data = await response.json();

    // Display result
 let probabilityHTML = "";


for (const career in data.probabilities) {
    const probability = data.probabilities[career];

    probabilityHTML += `
        <div class="career-row">

            <div class="career-info">
                <span>${career}</span>
                <span>${probability}%</span>
            </div>

            <div class="progress-bar">
                <div class="progress-fill"
                     style="width: ${probability}%">
                </div>
            </div>
        </div>
    `;
}
result.innerHTML = `
    <div class="result-card">
        <p class="result-label">
            YOUR RECOMMENDED CAREER
        </p>
        <h2>${data.career}</h2>

        <p class="result-score">
            Based on your skills and interests
        </p>

        <div class="probability-list">
            <h3>Career Match</h3>
            ${probabilityHTML}
        </div>
    </div>
`;
});
