/**
 * Controls the visualizations for the polyrhythms. PULSE is defined as the underlying beat (every 2nd beat in a 3:2),
 * while COUNTERPULSE is the secondary beat (every 3rd beat in a 3:2). PULSE <= COUNTERPULSE
 */

// Uncomment the following to easily test CSS
// visualize()
document.querySelector("#submit_button").addEventListener("click", e => {
    const [counterpulse, pulse] = collectInputs()
    console.log(`Pulse: ${pulse}, Counterpulse: ${counterpulse}`)
    clearGrid()
    visualize(pulse, counterpulse)
    startPolyrhythm(pulse, counterpulse)
})

function visualize(pulse, counterpulse) {
    createGrid(pulse, counterpulse)
    colorGrid(counterpulse)
}

/** Returns a list with two INTEGER values, where arr[0] is the COUNTERPULSE and arr[1] is the PULSE.
 * PULSE is defined as having the smaller value i.e. PULSE hits on 
 * every beat 1 while SUBDIVISION hits on the offbeats
 */
function collectInputs() {
    const inputs = document.querySelectorAll("#form input")
    let counterpulse = parseInt(inputs[0].value)
    let pulse = parseInt(inputs[1].value)
    if (counterpulse < pulse) {
        const temp = counterpulse
        counterpulse = pulse
        pulse = temp
    }
    return [counterpulse, pulse]
}

/** Creates a WIDTH x HEIGHT grid of div.box elements. Returns VOID */
function createGrid(width, height) {
    const grid = document.querySelector(".grid")
    for (let i = 0; i < height; i += 1) {
        const row = document.createElement("div")
        row.classList.add("row")
        for (let j = 0; j < width; j += 1) {
            const box = document.createElement("div")
            box.classList.add("box")
            box.innerText = j + 1
            row.appendChild(box);
        }
        grid.appendChild(row)
    }
}

/** Clears every row from GRID. Returns VOID */
function clearGrid() {
    const grid = document.querySelector(".grid")
    grid.innerHTML = ''
}

/** Adds the CSS class SUBDIV to every .box that lands on a subdiv */
function colorGrid(counterpulse) {
    let beat = 0;
    document.querySelectorAll(".box").forEach(box => {
        if (beat == counterpulse) {
            box.classList.add("subdiv")
            beat = 0
        }
        beat += 1
        console.log(box, beat)
    })
}

/** Starts the polyrhythm count that cycles at BMP beats per minute */
async function startPolyrhythm(pulse, counterpulse) {
    let bpm = getBPM()
    let boxCounter = 0
    await colorBox(pulse, counterpulse, boxCounter, bpm)
}

/** Apply the .beat class to the box at index BOXCOUNTER */
async function colorBox(pulse, counterpulse, boxCounter, bpm) {
    setTimeout(() => (console.log("hi")), BPMtoBPMS(bpm))
}

/** Fetches the BPM from the DOM */
function getBPM() {
    // FIXME
    return 60
}

/** Converts Beats per Minute to Beats per Miliseconds */
function BPMtoBPMS(bpm) {
    return bpm / 60 * 1000
}