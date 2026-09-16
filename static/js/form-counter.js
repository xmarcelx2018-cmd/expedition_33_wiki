const titleInput = document.querySelector("#wiki-title");
const contentInput = document.querySelector("#wiki-content");

function addCharacterCounter(input, limit) {
    if (!input) {
        return;
    }

    const counter = document.createElement("small");
    counter.classList.add("character-counter");

    input.insertAdjacentElement("afterend", counter);

    function updateCounter() {
        const count = input.value.length;

        if (count >= limit) {
            counter.textContent = `${count} / ${limit} — Character limit reached`;
            counter.classList.add("limit-reached");
        } else {
            counter.textContent = `${count} / ${limit} characters`;
            counter.classList.remove("limit-reached");
        }
    }

    input.addEventListener("input", updateCounter);
    updateCounter();
}

addCharacterCounter(titleInput, 50);
addCharacterCounter(contentInput, 3000);