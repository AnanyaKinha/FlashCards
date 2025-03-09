async function loadTopics() {
    const res = await fetch("/topics");
    const data = await res.json();
    const select = document.getElementById("topicSelect");
    select.innerHTML = data.topics.map(topic => `<option value="${topic}">${topic}</option>`).join("");
}

async function loadQuestion() {
    const topic = document.getElementById("topicSelect").value;
    const res = await fetch(`/question?topic=${topic}`);
    const data = await res.json();
    if (data.error) {
        alert(data.error);
        return;
    }
    document.getElementById("questionText").innerText = data.question;
    document.getElementById("flashcard").style.display = "block";
    document.getElementById("correctAnswer").style.display = "none";
}

async function revealAnswer() {
    const topic = document.getElementById("topicSelect").value;
    const question = document.getElementById("questionText").innerText;
    const res = await fetch("/answer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, question })
    });
    const data = await res.json();
    if (data.error) {
        alert(data.error);
        return;
    }
    document.getElementById("correctAnswer").innerText = "Answer: " + data.answer;
    document.getElementById("correctAnswer").style.display = "block";
}

window.onload = loadTopics;
